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


class CheckOnlineDictMD5(object):
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
        向线上实例发请求
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
        获取线上实例的md5，取到全部的MD5
        线上每一个实例对应一个MD5_list
        ip_port 的格式为 （"http://" + url["host"] + ":" + url["port"]）
        不影响定位问题
        """ 
        all_online_dict_md5 = {}
        for ip_port in self.dcs_api_sandbox_url_list:
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
            all_online_dict_md5[ip_port] = instance_md5_list
        return all_online_dict_md5

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

    def getOnlineMisMd5(self):
        """
        获取线上mis平台的md5,大约需要40分钟左右，
        """
        start_time = time.time()
        # 设置超时
        online_mis_md5 = ""
        timeout = 60 * 60
        while time.time() - start_time < timeout:
            get_online_mis_md5_url = 'http://mis.baidu.com:8080/api/GetInstances?data_name=duer_exp_didp'
            response = requests.get(get_online_mis_md5_url)
            if int(response.status_code) != 200:
                msg = "get_online_mis_md5_url send failed"
                print(msg)
            resp = response.json()
            if 'md5' not in resp:
                msg = "online mis not found md5"
                print(msg)
            # 只获取最新的，最新的在第一位
            online_mis_md5 = resp["data"][0]["md5"]
            if online_mis_md5 == "":
                msg = "online mis md5 is empty"
                print(msg)
            else:
                break
            # 延时
            time.sleep(30)
        if online_mis_md5 == "":
            msg = "sandbox mis md5 is empty"
            self.push_to_hi("timeout:3600s not get sandbox_mis_md5")
            return
        msg = "get sandbox mis platform md5 success"
        print(msg)
        return online_mis_md5
    
    def original_online_diff(self):
        """
        比较原始词典和沙盒mis平台的md5
        """
        originalMd5 = self.getOriginalDictMD5()
        online_mis_md5 = self.getOnlineMisMd5()
        if originalMd5 != online_mis_md5:
            msg = "originalMd5 is not equal to sandbox_mis_md5"
            self.push_msg_to_hi(msg)
            print(msg)
        else:
            msg = "originalMd5 is equal to online_mis_md5"
            self.push_msg_to_hi(msg)
            print(msg)


    def instanceMd5_online_diff(self):
        """
        线上实例的md5 与 线上mis平台的md5 比较
        """
        online_mis_md5 = self.getOnlineMisMd5()
        all_online_dict_md5 = self.get_instance_md5()
        # 查找是否存在与沙盒mis平台相同的MD5
        for key in all_online_dict_md5.keys():
            if online_mis_md5 in all_online_dict_md5[key]:
                pass
            else:
                msg = key + "is not MD5 equal to online_mis_md5"
                self.push_to_hi(msg)

    def run(self):
        # 检查 原始md5 与 线上mis平台对比
        self.original_online_diff()
        # 检查 线上实例md5 与 线上 mis平台对比
        self.instanceMd5_online_diff()

class GetHosts(object):
    """
    解析 bns 
    为什么不用 get_instance_by_service bns -ip
    """
    def getHosts(self, bns):
        host = []
        dcs_online_url_list = []
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
            dcs_online_url_list.append("http://" + url["host"] + ":" + url["port"])
        print(dcs_online_url_list)
        return dcs_online_url_list

if __name__ == '__main__':
    bns_online = ""
    url_path = ""
    dcs_api_online_url_list = GetHosts().getHosts(bns_online)
    test_dcs_api = CheckOnlineDictMD5(url_path, dcs_api_online_url_list)
    test_dcs_api.run()