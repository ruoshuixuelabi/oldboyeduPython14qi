from django.test import TestCase
from app02.models import Student
# Create your tests here.

# 测试model


class StudentTest(TestCase):
    
    def setUp(self):
        Student.objects.create(name='签到哥', age=18)

    def test_student_create(self):
        obj = Student.objects.get(name='签到哥')
        self.assertEqual(obj.age, 18)


class HomeTest(TestCase):

    def test_home_page_renders_home_template(self):
        """测试index视图"""
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '箭头函数.html')  # 判断使用的模板文件
