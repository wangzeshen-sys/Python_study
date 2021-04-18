os.access(path, mode) 检验权限模式 除windows系统
os.chdir(path) 改变当前工作目录
os.chmod(path, mode) 更改权限
os.getcwd() 返回当前工作目录
os.link(src, dst) 创建硬链接，名为参数dst， 指向参数src
os.listdir(path) 返回指定路径下所有文件及文件夹的列表
os.makedirs(path[,mode]) 递归文件创建函数
os.mkdir(path[,mode]) 创建文件夹 默认权限0777
os.popen(command[,mode[,bufsize]]) 执行Linux命令
os.popen(cmd).read().split() 返回一个列表
os.remove(path) 删除路径为path的文件
os.removedirs(path) 递归删除目录
os.rename(src, dst) 重命名 从src 到dst
os.renames(old, new) 递归地对目录进行更名，也可以对文件进行更名
os.rmdir(path) 删除path指定的空目录，如果目录非空，则抛出一个OSError异常


============================================================
os.path()模块 获取文件属性

os.path.abspath(path) 返回绝对路径
os.path.basename(path) 返回文件名
os.path.commonprofix(list) 返回list(多个路径)中，所有path共有的最长的路径
os.path.dirname(path)返回文件路径
os.path.exists(path) 路径存在则返回True,路径损坏返回False
os.path.getsize(path) 返回文件大小，如果文件不存在就返回错误
os.path.isfile(path) 判断路径是否为文件
os.path.isdir(path)	判断路径是否为目录
os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组























