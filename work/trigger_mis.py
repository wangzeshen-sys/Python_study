# coding=utf-8

"""
注: 请使用双引号表示字符串
"""

import os
import sys
import requests
import json
import time


class triggerMis:

    def __init__(self, command):
        self.route = command

    def push_to_hi(self, msg):
        url = "http://apiin.im.baidu.com/api/msg/groupmsgsend?access_token=d6ef1108a804e21d4b6d715fc0398d641"
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

    def del_expdidp_dict(self):
        """
        删除 expdidp_dict
        """
        os.chdir("/home/disk6/v_wangzeshen/oss_exp_didp_workspace")
        os.system("rm -rf expdidp_dict")
        cmd = "cd /home/disk6/v_wangzeshen/oss_exp_didp_workspace && rm -rf expdidp_dict"
        os.popen(cmd)

    def trigger_mis_run(self):
        """
        开始
        """
        self.del_expdidp_dict()

        if self.route == "sandbox":
            self.trigger_sandbox_mis()
        elif self.route == "online":
            self.trigger_online_mis()
        else:
            msg = "not found route"
            self.push_to_hi(msg)
            return

    def file_check(self):
        """
        校验文件
        """
        # 判断 expdidp_dict 是否存在
        expdidp_dict_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict")
        if expdidp_dict_file == False:
            msg = "expdidp_dict not found"
            self.push_to_hi(msg)
            return
        # 判断 expdidp_dict 是否为空
        expdidp_dict_list = os.listdir(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict")
        if len(expdidp_dict_list) == 0:
            msg = "expdidp_dict  is empty"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data 是否存在
        exp_didp_data_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data")
        if exp_didp_data_file == False:
            msg = "exp_didp_data not found"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data 是否为空
        exp_didp_data_list = os.listdir(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data")
        if len(exp_didp_data_list) == 0:
            msg = "exp_didp_data is empty"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data.tar.gz 是否存在
        exp_didp_data_tar_gz_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data.tar.gz")
        if exp_didp_data_tar_gz_file == False:
            msg = "exp_didp_data.tar.gz not found"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data.tar.gz 是否为空
        exp_didp_data_tar_gz_size = os.path.getsize(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data.tar.gz")
        if exp_didp_data_tar_gz_size == 0:
            msg = "exp_didp_data.tar.gz is empty"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data.tar.gz.md5是否存在
        exp_didp_data_tar_gz_md5_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data.tar.gz.md5")
        if exp_didp_data_tar_gz_md5_file == False:
            msg = "exp_didp_data.tar.gz.md5 not found"
            self.push_to_hi(msg)
            return
        # 判断 exp_didp_data.tar.gz.md5 是否为空
        exp_didp_data_tar_gz_md5_size = os.path.getsize(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data.tar.gz.md5")
        if exp_didp_data_tar_gz_md5_size == 0:
            msg = "exp_didp_data.tar.gz.md5 is empty"
            self.push_to_hi(msg)
            return
        # 判断data 是否存在
        data_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data")
        if data_file == False:
            msg = "data not found"
            self.push_to_hi(msg)
            return
        # 判断 data 是否为空
        data_list = os.listdir(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data")
        if len(data_list) == 0:
            msg = "data is empty"
            self.push_to_hi(msg)
            return
        # 判断 indexSet 是否存在
        indexSet_file = os.path.exists(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/indexSet")
        if indexSet_file == False:
            msg = "indexSet not found"
            self.push_to_hi(msg)
            return
        # 判断 indexSet 是为空
        indexSet_size = os.path.getsize(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/indexSet")
        if indexSet_size == 0:
            msg = "indexSet is empty"
            self.push_to_hi(msg)
            return

    def get_dict_file(self):
        """
        获取存在的词典文件list
        """
        indexSet_file_list = os.popen(
            "cat /home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/indexSet").read().split()
        # 找出词典的文件名
        dict_file_list = []
        for file_name in indexSet_file_list:
            dict_file_list.append(file_name)
        # 判断词典文件是否存在
        if len(dict_file_list) == 0:
            msg = "not found dict file"
            self.push_to_hi(msg)
            return
        # 判断词典是否为空
        for dict_file in dict_file_list:
            dict_file_dir = os.path.join(
                "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data", dict_file)
            dict_file_size = os.path.getsize(dict_file_dir)
            if dict_file_size == 0:
                msg = dict_file_dir + "is empty"
                self.push_to_hi(msg)
                return

    def dict_check(self):
        """
        校验词典内容
        """
        self.get_dict_file()
        os.chdir(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data")
        # 获取词典文件的list
        dict_file_list = os.listdir(
            "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data")
        # 构造 词典所在路径
        dict_dir = "/home/disk6/v_wangzeshen/oss_exp_didp_workspace/expdidp_dict/exp_didp_data/data"

        for mis_dict_file in dict_file_list:
            # 拼接路径
            dict_data_dir = os.path.join(dict_dir, mis_dict_file)
            with open(dict_data_dir, "r") as fp:
                mis_dict_data = json.load(fp)
            # 检验词典的key是否相同
            dict_key_list = []
            for key in mis_dict_data.keys():
                dict_key_list.append(key)
            new_dict_key_set = set(dict_key_list)
            if len(dict_key_list) != len(new_dict_key_set):
                msg = dict_data_dir + "有相同的key"
                self.push_to_hi(msg)
                return
            # 校验词典的value类型是否符合预期 目前只对每一个value做了第一层的格式校验
            for key in mis_dict_data.keys():
                key_value_type = isinstance(mis_dict_data[key], dict)
                if key_value_type == False:
                    msg = mis_dict_data[key] + "is no dict"
                    self.push_to_hi(msg)
                    return
                lastModifyTime_type = isinstance(
                    mis_dict_data[key]["lastModifyTime"], int)
                if lastModifyTime_type == False:
                    msg = "lastModifyTime_type no int"
                    self.push_to_hi(msg)
                    return
                expDidpId_type = isinstance(
                    mis_dict_data[key]["expDidpId"], str)
                if expDidpId_type == False:
                    msg = "expDidpId_type no str"
                    self.push_to_hi(msg)
                    return
                supportAppidList_type = isinstance(
                    mis_dict_data[key]["supportAppidList"], list)
                if supportAppidList_type == False:
                    msg = "supportAppidList_type no list"
                    self.push_to_hi(msg)
                    return
                else:
                    # 存在 supportAppidList 为空值的情况
                    if len(mis_dict_data[key]["supportAppidList"]) == 0:
                        pass
                    # supportAppidList 不为空值的情况
                    else:
                        # list 中每一个 元素
                        for item in mis_dict_data[key]["supportAppidList"]:
                            item_type = isinstance(item, dict)
                            if item_type == False:
                                msg = "item_type is not dict"
                                self.push_to_hi(msg)
                                return
                            else:
                                # list中每一个dict中 key-->value 的 assert
                                for k in item.keys():
                                    item_va_type = isinstance(item[k], str)
                                    if item_va_type == False:
                                        msg = item[k] + "is not str"
                                        self.push_to_hi(msg)
                                        return

                supportDeviceType_type = isinstance(
                    mis_dict_data[key]["supportDeviceType"], str)
                if supportDeviceType_type == False:
                    msg = "supportDeviceType_type no str"
                    self.push_to_hi(msg)
                    return
                clientConf_type = isinstance(
                    mis_dict_data[key]["clientConf"], dict)
                if clientConf_type == False:
                    msg = "supportDeviceType_type no dict"
                    self.push_to_hi(msg)
                    return

    def trigger_sandbox_mis(self):
        """
        触发沙盒mis
        """
        os.chdir("/home/disk6/v_wangzeshen/oss_exp_didp_workspace")
        status = os.system(
            "tool/hadoop/bin/hadoop fs -D hadoop.job.ugi='dumi_qa,duer-qa' -D fs.default.name=afs://pegasus.afs.baidu.com:9902 -get /user/dumi/duer/dumi_oss/expdidp_dict .")
        if status == 0:
            msg = "hadoop get dict success"
            self.push_to_hi(msg)
        else:
            msg = "hadoop get dict failed"
            self.push_to_hi(msg)
            return
        # 校验文件
        print("check file")
        self.file_check()
        print("check dict")
        # 校验词典格式
        self.dict_check()
        # 触发
        os.chdir("/home/disk6/v_wangzeshen/oss_exp_didp_workspace")
        fp = os.popen(
            "sh mis_tool.sh -m duer_exp_didp_sandbox -f expdidp_dict/exp_didp_data.tar.gz").read().split()
        if "Successfully" in fp:
            msg = "trigger sandbox mis success"
            self.push_to_hi(msg)
        else:
            msg = "trigger sandbox mis failed"
            self.push_to_hi(msg)
            return

    def trigger_online_mis(self):
        """
        触发线上mis
        """
        os.chdir("/home/disk6/v_wangzeshen/oss_exp_didp_workspace")

        """
        在触发的沙盒的时候已经执行过下面的命令了，
        """
        # status = os.system("tool/hadoop/bin/hadoop fs -D hadoop.job.ugi='dumi_qa,duer-qa' -D fs.default.name=afs://pegasus.afs.baidu.com:9902 -get /user/dumi/duer/dumi_oss/expdidp_dict .")
        # if status == 0:
        #     msg = "hadoop get dict success"
        #     self.push_to_hi(msg)
        #     print msg
        # else:
        #     mas = "hadoop get dict failed"
        #     self.push_to_hi(msg)
        #     sys.exit(0)

        with os.popen("sh mis_tool.sh -m duer_exp_didp  -f  expdidp_dict/exp_didp_data.tar.gz") as fp:
            if "Successfully" in fp.read().split():
                msg = "trigger online mis success"
                self.push_to_hi(msg)
            else:
                msg = "trigger online mis failed"
                self.push_to_hi(msg)
                return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        command = sys.argv[1]
        trimis = triggerMis(command)
        trimis.trigger_mis_run()
    else:
        sys.exit(1)
