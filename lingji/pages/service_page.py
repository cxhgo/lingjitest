# -*- encoding:utf-8 -*-
import time
from common.base import BaseApp

'''服务页面元素抓取'''


class Marriage(BaseApp):

    def step_01(self):
        '''婚姻爱情--综合-马上提问-元宝支付'''
        loc1 = {"name": "点击服务", "by": "id", "value": "com.mmc.linghit.internal:id/home_main_tab_ask"}
        loc2 = {"name": "点击婚姻爱情", "by": "text", "value": "婚姻爱情"}
        loc3 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc4 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc5 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc6 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)
        self.click(loc3)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc4)
        time.sleep(3)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)

    def step_02(self):
        '''测试举报功能点'''
        loc1 = {"name": "点击私聊", "by": "id", "value": "com.mmc.linghit.internal:id/consult"}
        loc2 = {"name": "点击...", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_right_more"}
        loc3 = {"name": "点击举报", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc4 = {"name": "输入内容", "by": "id", "value": "com.mmc.linghit.internal:id/reason"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.linghit.internal:id/reason_commit"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.click(loc3)
        self.send_text(loc4,u"骚扰到我了呢")
        self.click(loc5)
        self.click(loc6)

    def step_03(self):
        '''好评-马上提问-元宝支付'''
        loc1 = {"name": "点击好评", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)

    def step_04(self):
        '''已答数-马上提问-元宝支付'''
        loc1 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        time.sleep(2)
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)


class Cause(BaseApp):
    '''事业财运--综合-马上提问-元宝支付'''
    def step_05(self):
        '''事业财运--综合-马上提问-元宝支付'''
        loc3 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc4 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc5 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc6 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(5)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/name")[1].click()
        self.click(loc3)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc4)
        time.sleep(3)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)

    def step_06(self):
        '''测试举报功能点'''
        loc1 = {"name": "点击私聊", "by": "id", "value": "com.mmc.linghit.internal:id/consult"}
        loc2 = {"name": "点击...", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_right_more"}
        loc3 = {"name": "点击举报", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc4 = {"name": "输入内容", "by": "id", "value": "com.mmc.linghit.internal:id/reason"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.linghit.internal:id/reason_commit"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.click(loc3)
        self.send_text(loc4,"骚扰到我了呢")
        self.click(loc5)
        self.click(loc6)

    def step_07(self):
        '''好评-马上提问-元宝支付'''
        loc1 = {"name": "点击好评", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)

    def step_08(self):
        '''已答数-马上提问-元宝支付'''
        loc1 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        time.sleep(2)
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)


class Emotion(BaseApp):
    '''恋爱情感--综合-马上提问-元宝支付'''
    def step_09(self):
        '''事业爱情--综合-马上提问-元宝支付'''
        loc3 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc4 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc5 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc6 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(5)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/name")[1].click()
        self.click(loc3)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc4)
        time.sleep(3)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)

    def step_10(self):
        '''测试举报功能点'''
        loc1 = {"name": "点击私聊", "by": "id", "value": "com.mmc.linghit.internal:id/consult"}
        loc2 = {"name": "点击...", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_right_more"}
        loc3 = {"name": "点击举报", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc4 = {"name": "输入内容", "by": "id", "value": "com.mmc.linghit.internal:id/reason"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.linghit.internal:id/reason_commit"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.click(loc3)
        self.send_text(loc4,"骚扰到我了呢")
        self.click(loc5)
        self.click(loc6)

    def step_11(self):
        '''好评-马上提问-元宝支付'''
        loc1 = {"name": "点击好评", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)

    def step_12(self):
        '''已答数-马上提问-元宝支付'''
        loc1 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        time.sleep(2)
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)


class Fleeting(BaseApp):
    '''流年运势--综合-马上提问-元宝支付'''
    def step_13(self):
        '''流年运势--综合-马上提问-元宝支付'''
        loc3 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc4 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc5 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc6 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(5)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/name")[3].click()
        self.click(loc3)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc4)
        time.sleep(3)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)

    def step_14(self):
        '''测试举报功能点'''
        loc1 = {"name": "点击私聊", "by": "id", "value": "com.mmc.linghit.internal:id/consult"}
        loc2 = {"name": "点击...", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_right_more"}
        loc3 = {"name": "点击举报", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc4 = {"name": "输入内容", "by": "id", "value": "com.mmc.linghit.internal:id/reason"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.linghit.internal:id/reason_commit"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.click(loc3)
        self.send_text(loc4,"骚扰到我了呢")
        self.click(loc5)
        self.click(loc6)

    def step_15(self):
        '''好评-马上提问-元宝支付'''
        loc1 = {"name": "点击好评", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)

    def step_16(self):
        '''已答数-马上提问-元宝支付页面功能点'''
        loc1 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/title"}
        loc2 = {"name": "点击老师", "by": "id", "value": "com.mmc.linghit.internal:id/avatar"}
        loc3 = {"name": "点击马上提问", "by": "id", "value": "com.mmc.linghit.internal:id/ask_question_now"}
        loc4 = {"name": "输入元宝", "by": "id", "value": "com.mmc.linghit.internal:id/pay_title"}
        loc5 = {"name": "点击确认支付", "by": "id", "value": "com.mmc.linghit.internal:id/pay_confirm"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc7 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc8 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        self.click(loc3)
        time.sleep(2)
        self.driver.find_elements_by_id("com.mmc.linghit.internal:id/pay_radio")[2].click()
        time.sleep(2)
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)

    def step_17(self):
        '''测试-星座占卜页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "星座占卜"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_18(self):
        '''测试塔罗牌页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "塔罗牌"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_19(self):
        '''测试八字算命页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "八字算命"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_20(self):
        '''测试手相面相页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "手相面相"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_21(self):
        '''测试周公解梦页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "周公解梦"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_22(self):
        '''测试起名页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "起名"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_23(self):
        '''测试祈福转运页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "祈福转运"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_24(self):
        '''测试属相婚配页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "属相婚配"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_25(self):
        '''测试黄历择日页面功能点'''
        loc1 = {"name": "点击已答数", "by": "text", "value": "黄历择日"}
        loc2 = {"name": "点击已答数", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_26(self):
        '''测试八字风水页面功能点'''
        loc1 = {"name": "点击八字风水", "by": "text", "value": "八字风水"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(3)
        self.click(loc1)
        time.sleep(2)
        self.click(loc2)

    def step_27(self):
        '''聊天-互动-已读'''
        loc1 = {"name": "点击聊天", "by": "id", "value": "com.mmc.linghit.internal:id/home_main_tab_message"}
        loc2 = {"name": "点击聊天", "by": "text", "value": "互动"}
        loc3 = {"name": "点击聊天", "by": "id", "value": "com.mmc.linghit.internal:id/message_topbar_item_right_all_read"}
        loc4 = {"name": "点击聊天", "by": "id", "value": "com.mmc.linghit.internal:id/confirm"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)

    def step_28(self):
        '''我的-我的主页-更换昵称'''
        loc1 = {"name": "点击我的", "by": "id", "value": "com.mmc.linghit.internal:id/home_main_tab_mine"}
        loc2 = {"name": "点击>", "by": "id", "value": "com.mmc.linghit.internal:id/me_user_go_detail"}
        loc3 = {"name": "点击编辑", "by": "id", "value": "com.mmc.linghit.internal:id/uc_user_edit"}
        loc4 = {"name": "点击昵称", "by": "id", "value": "com.mmc.linghit.internal:id/nickname_layout"}
        loc5 = {"name": "点击*", "by": "id", "value": "com.mmc.linghit.internal:id/clear"}
        loc6 = {"name": "输入昵称", "by": "id", "value": "com.mmc.linghit.internal:id/edit"}
        loc7 = {"name": "点击保存", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        time.sleep(2)
        self.click(loc1)
        time.sleep(2)
        self.swipe_down()
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)
        self.send_text(loc6, "格格")
        self.click(loc7)

    def step_29(self):
        '''我的-编辑资料-更换姓别'''
        loc1 = {"name": "点击性别", "by": "id", "value": "com.mmc.linghit.internal:id/sex_layout"}
        loc2 = {"name": "点击女", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)

    def step_30(self):
        '''我的-编辑资料-更换感情状态'''
        loc1 = {"name": "点击性别", "by": "id", "value": "com.mmc.linghit.internal:id/marital_status_layout"}
        loc2 = {"name": "点击已婚", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)

    def step_31(self):
        '''我的-编辑资料-更换感情状态'''
        loc1 = {"name": "点击性别", "by": "id", "value": "com.mmc.linghit.internal:id/working_status_layout"}
        loc2 = {"name": "点击学生", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc3 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        loc4 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit.internal:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)