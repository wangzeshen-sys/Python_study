
import unittest


class Demo01(unittest.TestCase):

    # 类的初始化
    @classmethod
    def setUpClass(cls):
        print('class')

    # 类的资源释放
    @classmethod
    def tearDownClass(cls):
        print('tclass')

    # 初始化
    def setUp(self):
        print('setUp')

    # 释放资源
    def tearDown(self):
        print('tearDown')

    # 测试用例
    def test_a(self):
        self.assertEqual(1, 1)

    def test_b(self):
        self.assertNotEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
