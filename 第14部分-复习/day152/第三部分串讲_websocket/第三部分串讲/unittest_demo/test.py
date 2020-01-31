# -*- coding: utf-8 -*-
# __author__ = "maple"

import unittest
from demo1 import MyClass


class MyClassTest(unittest.TestCase):
    def setUp(self):
        """
        测试之前做的准备工作
        :return:
        """
        self.calc = MyClass(170, 55)

    def tearDown(self):
        """测试之后做的收尾工作"""
        pass

    def test_add(self):
        ret = self.calc.add()
        self.assertEqual(ret, 225)

    def test_sub(self):
        ret = self.calc.sub()  # 得到你代码的结果
        self.assertEqual(ret, 115)  # 判断你代码运行的结果和期望结果是否一致


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(MyClassTest('test_add'))
    suite.addTest(MyClassTest('test_sub'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
