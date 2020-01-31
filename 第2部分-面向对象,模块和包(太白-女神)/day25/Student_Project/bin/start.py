import sys
lst = __file__.split('/')
base_path  = '/'.join(lst[:-2])
sys.path.append(base_path)   # python解释器相关
from core import main

if __name__ == '__main__':
    main.entry_point()


# 启动的是一个文件
# 这个文件通过你启动 导入其他文件
# 所有导入的文件和你启动的文件是一个程序
# 由一个python解释器来解释

# 所有的文件都加载到一块内存空间中
# 一些解释器中的全局变量 应该是这个程序共享的






