# -*- encoding:utf-8 -*-
import time
from common.base import BaseApp

'''我的页面元素抓取'''


class Ming(BaseApp):
    '''我的'''
    def step_01(self):
        '''更换头像'''
        loc1 = {"name": "点击我的", "by": "id", "value": "com.mmc.linghit:id/home_main_tab_mine"}
        loc2 = {"name": "点击>", "by": "id", "value": "com.mmc.linghit:id/me_user_go_detail"}
        loc3 = {"name": "点击编辑", "by": "id", "value": "com.mmc.linghit:id/uc_user_edit"}
        loc4 = {"name": "点击头像", "by": "text", "value": "头像"}
        loc5 = {"name": "点击修改", "by": "text", "value": "修改"}
        loc6 = {"name": "点击相册", "by": "text", "value": "相册"}
        loc7 = {"name": "点击对勾", "by": "id", "value": "com.mmc.linghit:id/check"}
        loc8 = {"name": "点击已完成", "by": "text", "value": "已完成"}
        loc9 = {"name": "点击对勾", "by": "id", "value": "com.mmc.linghit:id/menu_crop"}
        loc10 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}

        self.click(loc1)
        self.click(loc2)
        self.click(loc3)

    def step_02(self):
        '''更换昵称'''
        pass
        # loc4 = {"name": "点击昵称", "by": "id", "value": "ccom.mmc.linghit:id/nickname_layout"}
        # loc5 = {"name": "点击输入框", "by": "id", "value": "com.mmc.linghit:id/edit"}
        # loc6 = {"name": "点击保存", "by": "id", "value": "com.mmc.linghit:id/login_topbar_right_save"}
        #
        # self.click(loc4)
        # self.clear(loc5)
        # self.send_text(loc5, "斑马")
        # self.click(loc6)
        # print(self.is_toast_in("修改成功"))

    def step_03(self):
        '''更换性别'''
        loc4 = {"name": "点击性别", "by": "id", "value": "com.mmc.linghit:id/sex_layout"}
        loc5 = {"name": "选择男", "by": "text", "value": "男"}
        self.click(loc4)
        self.click(loc5)

    def step_04(self):
        '''更换出生年月'''

        loc4 = {"name": "点击出生年月", "by": "id", "value": "com.mmc.linghit:id/birthday_layout"}
        loc5 = {"name": "点击确定", "by": "text", "value": "确定"}
        self.click(loc4)
        self.click(loc5)

    def step_05(self):
        '''感觉状态'''
        loc4 = {"name": "点击感情状态", "by": "id", "value": "com.mmc.linghit:id/marital_status_layout"}
        loc5 = {"name": "点击已婚", "by": "text", "value": "已婚"}
        self.click(loc4)
        self.click(loc5)

    def step_06(self):
        '''工作状态'''
        loc4 = {"name": "点击工作状态", "by": "id", "value": "com.mmc.linghit:id/working_status_layout"}
        loc5 = {"name": "点击学生", "by": "text", "value": "学生"}
        self.click(loc4)
        self.click(loc5)


class Order(BaseApp):

    def step_01(self):
        '''咨询室'''
        loc1 = {"name": "点击我的", "by": "id", "value": "com.mmc.linghit:id/home_main_tab_mine"}
        loc2 = {"name": "点击咨询室", "by": "id", "value": "com.mmc.linghit:id/consult"}
        loc3 = {"name": "点击查看消息", "by": "id", "value": "com.mmc.linghit:id/order_operate"}
        loc4 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}
        loc5 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)

    def step_02(self):
        '''闪测'''
        loc1 = {"name": "点击闪测", "by": "id", "value": "com.mmc.linghit:id/fast"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}

        self.click(loc1)
        self.click(loc2)

    def step_03(self):
        '''普通问题'''
        loc1 = {"name": "点击普通问题", "by": "id", "value": "com.mmc.linghit:id/question"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)

    def step_04(self):
        '''旁听'''
        loc1 = {"name": "点击旁听", "by": "id", "value": "com.mmc.linghit:id/eavesdrop"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)

    def step_05(self):
        '''查看更多'''
        loc1 = {"name": "点击查看更多", "by": "id", "value": "com.mmc.linghit:id/more"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.linghit:id/topbar_item_left_back"}
        self.click(loc1)
        self.click(loc2)