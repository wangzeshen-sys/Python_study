import unittest
from register import register   # 导入被测试的代码

class TestRegister(unittest.TestCase):
    """注册接口测试用例类"""
    
    def setUp(self):
        # 每条用例执行之前都会执行
        print("用例{}开始执行--".format(self))

    def tearDown(self):
        # 每条用例执行之后都会执行
        print("用例{}执行结束--".format(self))

    @classmethod	# 指明这是个类方法以类为维度去执行的
    def setUpClass(cls):
        # 整个测试用例类中的用例执行之前，会先执行此方法
        print("-----setup---class-----")

    @classmethod
    def tearDownClass(cls):
        # 整个测试用例类中的用例执行完之后，会执行此方法
        print("-----teardown---class-----")

    def test_register_success(self):
        """注册成功"""
        data = ("mikitest", "miki123", "miki123")   # 测试数据
        expected = {"code": 1, "msg": "注册成功！"}   # 预期结果
        result = register(*data)    # 把测试数据传到被测的代码，接收实际结果
        self.assertEqual(expected, result)  # 断言，预期和实际是否一致，一致即用例通过

    def test_username_isnull(self):
        """注册失败-用户名为空"""
        data = ("", "miki123", "miki123")
        expected = {"code": 0, "msg": "所有参数不能为空！"}
        result = register(*data)
        self.assertEqual(expected, result)


# 如果直接运行这个文件，需要使用unittest中的main函数来执行测试用例
if __name__ == '__main__':
    unittest.main()