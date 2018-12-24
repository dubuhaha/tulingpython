# 获取文件夹大小

import os
def getdirpath(dirpath):
    total = 0
    # 获取所有文件
    allname = os.listdir(dirpath)
    for name in allname:
        # 拼接成完整路径
        fullpath = os.path.join(dirpath, name)
        # 判断是否是文件
        if os.path.isfile(fullpath):
            # 获取文件大小
            total += os.path.getsize(fullpath)
        # 判断是否是文件夹（目录）
        elif os.path.isdir(fullpath):
            total += getdirpath(fullpath)
    # 返回大小
    return total

size = getdirpath('C:\\Users\\liujinghui\\丘比特笔记')
print(size)