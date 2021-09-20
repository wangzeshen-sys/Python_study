"""
注:字符串使用双引号标识
"""
import sys
import os
import json
import requests
import re
import time
import random
import datetime


class CheckSandboxDictMD5(object):
    """
    检测字典在controller是否生效
    """
    def __init__(self, url_path, dcs_api_sandbox_url_list):
        """
        init
        """
        self.url_path = url_path
        self.dcs_api_sandbox_url_list = dcs_api_sandbox_url_list
    
    def push_to_hi(self, msg):
        """
        hi 提示
        """
        url = "http://apiin.im.baidu.com/api/msg/groupmsgsend?access_token=def220613392b82cf0ba985d2f047b7e9"
        body = {
            "message": {
                "header": {
                    "toid": [4395985]
                },
                "body": [
                    {
                        "content": msg,
                        "type": "TEXT"
                    },
                    {
                        "atuserids": ["v_wangzeshen"],
                        "atall": False,
                        "type": "AT"
                    }
                ]
            }
        }
        jsondata = json.dumps(body)
        res = requests.post(url=url, data=jsondata)
        
    def send_request_post(self, ip_port):
        """
        向沙盒实例发请求，获取响应
        """
        dcs_url = ip_port + self.url_path
        response = requests.post(url=dcs_url)
        if int(response.status_code) != 200:
            msg = "instance url send failed"
            self.push_to_hi(msg)
            return
        return response

    def get_instance_md5(self):
        """
        获取沙盒实例的md5，只取一个实例上的MD5
        """ 
        i = random.randint(0, len(self.dcs_api_sandbox_url_list)-1)
        ip_port = self.dcs_api_sandbox_url_list[i]
        response = self.send_request_post(ip_port)
        resp = response.json()
        if "sample_dict_data" not in resp:
            msg = "instance not found sample_dict_data"
            self.push_to_hi(msg)
            return
        else:
            instance_md5_list = []
            for instance_md5 in resp["data"].values():
                instance_md5_list.append(instance_md5)
            return instance_md5_list

    def getOriginalDictMD5(self):
        """
        获取原始词典的md5
        """
        # 获取原始词典的md5
        t = os.popen('md5sum /home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data.tar.gz')
        originalMd5 = t.read().split()[0]
        # 为空的可能性极小
        if originalMd5 == "":
            msg = "originalMd5 is empty"
            self.push_to_hi(msg)
            return
        msg = "get original dict md5 success"
        print(msg)
        return originalMd5

    def getSandboxMisMd5(self):
        """
        获取沙盒mis平台的md5,大约需要40分钟左右，
        """
        start_time = time.time()
        # 设置超时
        timeout = 60 * 60
        sandbox_mis_md5 = ""
        while time.time() - start_time < timeout:
            get_sandbox_mis_md5_url = 'http://mis.baidu.com:8080/api/GetInstances?data_name=duer_exp_didp_sandbox'
            response = requests.get(get_sandbox_mis_md5_url)
            if int(response.status_code) != 200:
                msg = "get_sandbox_mis_md5_url send failed"
                print(msg)
            resp = response.json()
            if 'md5' not in resp:
                msg = "sandbox mis not found md5"
                print(msg)
            # 只获取最新的，最新的在第一位
            sandbox_mis_md5 = resp["data"][0]["md5"]
            if sandbox_mis_md5 == "":
                msg = "sandbox mis md5 is empty"
                print(msg)
            else:
                break
            # 延时
            time.sleep(30)
        if sandbox_mis_md5 == "":
            msg = "sandbox mis md5 is empty"
            self.push_to_hi("timeout:3600s not get sandbox_mis_md5")
            return
        msg = "get sandbox mis platform md5 success"
        print(msg)
        return sandbox_mis_md5
    
    def original_sandbox_diff(self):
        """
        比较原始词典和沙盒mis平台的md5
        """
        originalMd5 = self.getOriginalDictMD5()
        sandbox_mis_md5 = self.getSandboxMisMd5()
        if originalMd5 != sandbox_mis_md5:
            msg = "originalMd5 is not equal to sandbox_mis_md5"
            self.push_msg_to_hi(msg)
            print(msg)
        else:
            msg = "originalMd5 is equal to sandbox_mis_md5"
            self.push_msg_to_hi(msg)
            print(msg)


    def instanceMd5_sandbox_diff(self):
        """
        沙盒实例的md5 与 沙盒mis平台的md5 比较
        """
        sandbox_mis_md5 = self.getSandboxMisMd5()
        instance_md5_list = self.get_instance_md5()
        # 查找是否存在与沙盒mis平台相同的MD5
        for instance_md5 in instance_md5_list:
            if instance_md5 == sandbox_mis_md5:
                msg = "instance_md5 is equal to sandbox_mis_md5"
                self.push_to_hi(msg)
                print("over")
                return
        msg = "instance_md5 not found"
        self.push_to_hi(msg)
        return

    def run(self):
        # 检查 原始md5 与沙盒mis平台对比
        self.original_sandbox_diff()
        # 检查 沙盒实例md5 与沙盒mis平台对比
        self.instanceMd5_sandbox_diff()

class GetHosts(object):
    """
    解析 bns 
    为什么不用 get_instance_by_service bns -ip
    """
    def getHosts(self, bns):
        host = []
        dcs_sandbox_url_list = []
        with os.popen("get_instance_by_service -a %s" % bns) as fd:
            results = fd.readlines()
            for item in results:
                items = item.split(' ')
                if len(items) < 5 or items[4] != '0':
                    continue
                host.append({
                    "host": items[0],
                    "ip": items[1],
                    "port": items[3]
                })
        for url in host:
            dcs_sandbox_url_list.append("http://" + url["host"] + ":" + url["port"])
        # print dcs_sandbox_url_list
        return dcs_sandbox_url_list

if __name__ == '__main__':
    bns_sandbox = "group.dumi-dcs-controller-sandbox.dumi.all"
    url_path = "/api/sample/info?type=file"
    dcs_api_sandbox_url_list = GetHosts().getHosts(bns_sandbox)
    test_dcs_api = CheckSandboxDictMD5(url_path, dcs_api_sandbox_url_list)
    test_dcs_api.run()