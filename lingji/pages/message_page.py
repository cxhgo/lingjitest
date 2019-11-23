# -*- encoding:utf-8 -*-
import time
from common.base import BaseApp

'''消息页面元素抓取'''


class House(BaseApp):
    '''小管家'''
    def step_01(self):
        loc1 = {"name": "点击消息", "by": "text", "value": "消息"}
        loc2 = {"name": "点击灵机小管家", "by": "text", "value": "灵机小管家"}
        loc3 = {"name": "点击立即查看", "by": "text", "value": "立即查看"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)


class Coupon(BaseApp):
    '''优惠卷'''
    def step_01(self):
        loc1 = {"name": "点击消息", "by": "text", "value": "消息"}
        loc2 = {"name": "点击灵机优惠劵", "by": "text", "value": "灵机优惠劵"}
        self.click(loc1)
        time.sleep(3)
        self.click(loc2)


class Interactive(BaseApp):
    def step_01(self):
        loc1 = {"name": "点击消息", "by": "text", "value": "消息"}
        loc2 = {"name": "点击互动", "by": "text", "value": "互动"}
        loc3 = {"name": "点击已读", "by": "text", "value": "已读"}
        loc4 = {"name": "点击确定", "by": "text", "value": "确定"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
