# coding:utf-8
import unittest
from common.start import start_app
from time import sleep
from  appium import webdriver
from pages.service_page import Marriage,Cause,Emotion,Fleeting
import time


class Test_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = start_app()
        cls.marriage = Marriage(cls.driver)
        cls.cause = Cause(cls.driver)
        cls.emotion = Emotion(cls.driver)
        cls.fleeting = Fleeting(cls.driver)

    def test_01(self):
        '''测试提问功能点：服务-婚姻爱情-综合-咨询-提问-元宝支付'''
        time.sleep(10)
        self.marriage.step_01()

    def test_02(self):
        '''测试举报功能点'''
        self.marriage.step_02()

    def test_03(self):
        '''好评-马上提问-元宝支付'''
        self.marriage.step_03()

    def test_04(self):
        '''已答数-马上提问-元宝支付'''
        self.marriage.step_04()

    def test_05(self):
        '''婚姻爱情--综合-马上提问-元宝支付'''
        self.cause.step_05()

    def test_06(self):
        '''测试举报功能点'''
        self.cause.step_06()

    def test_07(self):
        '''好评-马上提问-元宝支付'''
        self.cause.step_07()

    def test_08(self):
        '''已答数-马上提问-元宝支付'''
        self.cause.step_08()

    def test_09(self):
        '''婚姻爱情--综合-马上提问-元宝支付'''
        self.emotion.step_09()

    def test_10(self):
        '''测试举报功能点'''
        self.emotion.step_10()

    def test_11(self):
        '''好评-马上提问-元宝支付'''
        self.emotion.step_11()

    def test_12(self):
        '''已答数-马上提问-元宝支付'''
        self.emotion.step_12()

    def test_13(self):
        '''已答数-马上提问-元宝支付'''
        self.fleeting.step_13()

    def test_14(self):
        '''测试举报功能点'''
        self.fleeting.step_14()

    def test_15(self):
        '''好评-马上提问-元宝支付'''
        self.fleeting.step_15()

    def test_16(self):
        '''已答数-马上提问-元宝支付'''
        self.fleeting.step_16()

    def test_17(self):
        '''测试-星座占卜页面功能点'''
        self.fleeting.step_17()

    def test_18(self):
        '''测试塔罗牌页面功能点'''
        self.fleeting.step_18()

    def test_19(self):
        '''测试八字算命页面功能点'''
        self.fleeting.step_19()

    def test_20(self):
        '''测试手相面相页面功能点'''
        self.fleeting.step_20()

    def test_21(self):
        '''测试周公解梦页面功能点'''
        self.fleeting.step_21()

    def test_22(self):
        '''测试起名页面功能点'''
        self.fleeting.step_22()

    def test_23(self):
        '''测试祈福转运页面功能点'''
        self.fleeting.step_23()

    def test_24(self):
        '''测试属相婚配页面功能点'''
        self.fleeting.step_24()

    def test_25(self):
        '''测试黄历择日页面功能点'''
        self.fleeting.step_25()

    def test_26(self):
        '''测试八字风水页面功能点'''
        self.fleeting.step_26()

    def test_27(self):
        '''聊天-互动-已读'''
        self.fleeting.step_27()

    def test_28(self):
        '''我的-我的主页-更换昵称'''
        self.fleeting.step_28()

    def test_29(self):
        '''我的-编辑资料-更换姓别'''
        self.fleeting.step_29()

    def test_30(self):
        '''我的-编辑资料-更换感情状态'''
        self.fleeting.step_30()

    def test_31(self):
        '''我的-编辑资料-更换感情状态'''
        self.fleeting.step_31()


if __name__ == "__main__":
    unittest.main()

