参考资料   https://www.cnblogs.com/miki-peng/p/12501341.html

1 test fixture ：setUp（前置条件），tearDown（后置条件），用于初始化测试用例、清理释放资源
2 test case ：测试用例，以继承unittest.TestCase实现用例的继承，在UnitTest中，测试用例都通过test识别，所以在每个用例的命名上，必须要带上test，否则就不会识别
3 test suite ：测试套件，即测试用例集，list = (case1,case2…)
4 test runner ：运行器，通过runner调用suite执行测试
5 test report：生成测试报告

常用断言

1   assertEqual(arg1, arg2, msg=None)	验证arg1=arg2，不等则fail
2	assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
3	assertTrue(expr, msg=None)	验证expr是true，如果为false，则fail
4	assertFalse(expr,msg=None)	验证expr是false，如果为true，则fail
5	assertIs(arg1, arg2, msg=None)	验证arg1、arg2是同一个对象，不是则fail
6	assertIsNot(arg1, arg2, msg=None)	验证arg1、arg2不是同一个对象，是则fail
7	assertIsNone(expr, msg=None)	验证expr是None，不是则fail
8	assertIsNotNone(expr, msg=None)	验证expr不是None，是则fail

case 执行顺序
unittest 框架默认加载测试用例的顺序是根据 ASCII 码的顺序，数字与字母的顺序为： 0~9,A~Z,a~z 。



UnitTest.skip用法
在case中，如果需要忽略某些用例或者特定条件下不执行的用例，那么就可以使用skip
skip 是通过装饰器执行，无条件执行跳过操作，有一个参数，传入的内容会在控制台显示
如果使用 skipIf 将会有条件的执行跳过操作



