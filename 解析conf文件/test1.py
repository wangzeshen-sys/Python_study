import configparser

#  获取ConfigParser
conf = configparser.ConfigParser()
# print(type(conf))

# 读取配置，
conf.read("myconf.conf")

# 获取文件中所有sections （部门）
sections = conf.sections()
# print(sections) # 是list

#获取某个section下的所有选项或value，等价于 option = conf.options('logoninfo')
option = conf.options("logoninfo")
# option = conf.options(conf.sections()[0])
# print(option)
# 根据某个sections 下的某个key 获取对应的value
value = conf.get('logoninfo', 'addr')
print(value)