from core import auth
from core import student
from core import manager
def entry_point():
    print('欢迎进入学生选课')
    auth.login()
    print(student.Student)
    print(manager.Manager)



if __name__ == '__main__':
    entry_point()