import os, re,shutil

# path = r'G:\CZBK-黑ma-JAVA EE 49期基础班+就业班\01-JavaSE知识(学习27天)'
def move(path):
    for name in os.listdir(path):
        path1 = os.path.join(path,name)
        if os.path.isdir(path1):
            for name in os.listdir(path1):
                path2 = os.path.join(path1,name)
                if os.path.isdir(path2):
                    for name in os.listdir(path2):
                        path3 = os.path.join(path2,name)
                        for name in os.listdir(path3):
                            file_path = os.path.join(path3,name)
                            if os.path.isfile(file_path):
                                shutil.move(file_path,path1)



# move(path)

path = r'G:\CZBK-黑ma-JAVA EE 49期基础班+就业班\08-Spring框架(学习4天)\Spring_day04_SSH整合\spring-day04\视频'

for name in os.listdir(path):
    new_name = 'day4-'+name.replace('__rec','')

    file_path = os.path.join(path,name)
    if os.path.isfile(file_path):
        os.rename(file_path,os.path.join(path,new_name))
