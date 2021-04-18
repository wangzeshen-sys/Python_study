import time
import os
import random
import sys
import json
import re

print("==========time包使用==========")
timestamp = time.time()
print("时间戳:", timestamp)
localtime = time.ctime()
print("本地时间:", localtime)
localtime = time.localtime(time.time())
print("本地时间：", localtime)
localtime = time.asctime(time.localtime(time.time()))
print("本地时间:", localtime)

print("格式化日期")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("通过时间戳获取时分秒")
print(time.asctime(time.localtime(321656)))

print("==========json包使用==========")
str_data = {
    'no': 1,
    'name':'Runoob',
    'url': 'http://www.baidu.com'
}
json_str = json.dumps(str_data)
print("python原始数据:", repr(str_data))
print("JSON对象:", json_str)

orig_str_data = json.loads(json_str)
print("解析JSON对象:", orig_str_data)

print("读取json文件")
with open('test_json.json', 'r') as fp:
    json_str_fp = json.load(fp)
print(json_str_fp)

# 将json文件写入文件对象
with open('test_json1.json', 'w') as fp:
    json.dump(json_str_fp, fp)

print("==========os包使用==========")
# 创建目录
os.mkdir('./test1')
# 查看当前路径
print(os.getcwd())
# 改变当前的工作路径
os.chdir('/home/wzs/Desktop/python_up/Python_study/')
print(os.getcwd())

