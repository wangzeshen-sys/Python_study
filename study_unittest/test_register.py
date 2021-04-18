import unittest
from register import register

class TestRegister(unittest.TestCase):
    """
    注册接口测用例类
    """
    def test_register_success(self):
        """
        注册成功
        """
        data = ("mikitest", "miki123", "miki123")
        expected = {"code": 1, "msg":"注册成功"}
        result = register(*data)
        self.assertEqual(expected, result)

    def test_username_isnull(self):
        """
        注册失败-用户名为空
        """
        data = ("", "miki123", "miki123")
        expected = {"code": 0, "msg":"所有参数不能为空"}
        result = register(*data)
        self.assertEqual(expected, result)
    
    def test_username_lt6(self):
        """
        注册失败-用户名大于18位
        """
        data = ("mikitestmikitestmikitest", "miki123", "miki123")
        expected = {"code": 0, "msg":"用户名和密码必须在6-18位之间！"}
        result = register(*data)
        self.assertEqual(expected, result)

    def test_pwd1_not_pwd2(self):
        """
        注册失败-两次密码不一致
        """
        data = ("miki123", "test123", "test321")
        expected = {"code": 0, "msg":"两次密码输入不一致！"}
        result = register(*data)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()