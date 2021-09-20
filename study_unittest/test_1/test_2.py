
import unittest
 
class Demo03(unittest.TestCase):
    #初始化
    def setUp(self):
        print('setUp')
 
    #释放资源
    def tearDown(self):
        print('tearDown')
 
    #测试用例
    #无条件执行跳过操作
    @unittest.skip('不需要运行该条用例')
    def test_a(self):
        print('1')
 
    def test_b(self):
        print('2')
 
    # 有条件执行跳过操作
    @unittest.skipIf(1 < 2, '如果if条件是true就跳过')
    def test_c(self):
        print('3')
 
    def test_d(self):
        print('4')
 
    @unittest.skipUnless(1 > 2, '如果unless条件是false就跳过')
    def test_e(self):
        print('5') 
 
if __name__=='__main__':
    unittest.main()