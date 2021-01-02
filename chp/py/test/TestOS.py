# 方法1：使用os.listdir
import os
def f1():
    for filename in os.listdir(r'c:\\'):
        print(filename)

#方法2：使用glob模块，可以设置文件过滤
import glob
def f2():
    for filename in glob.glob(r'c:\\'):
        print(filename)

#方法3：通过os.path.walk递归遍历，可以访问子文件夹
import os.path
def processDirectory(args, dirname, filenames):
    print('Directory', dirname)
    for filename in filenames:
        print(' File', filename)

def f3():
    os.path.walk(r'c:\\windows', processDirectory, None)


def main():
    f1()
    print("-"*10)
    f2()
    print("-"*10)
    f3()


if __name__ == '__main__':
    main()