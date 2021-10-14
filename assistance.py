# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/5/2 9:12
"""
from selenium import webdriver
import time
import pymysql
from datetime import datetime
import threading
from selenium.webdriver.common.keys import Keys
import requests
import json


class Assistance:
    def __init__(self, account_id, is_hold):
        self.account_id = account_id
        self.is_hold = is_hold
        self.login_url = "http://0di.cc:88/#/login"
        self.executable_path = r"E:\Google\Chrome\Application\chromedriver.exe"

    def set_options(self, from_which):
        browser = webdriver.Chrome(self.executable_path)
        browser.get(self.login_url)
        time.sleep(3)
        connect = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="assistance", charset="utf8")
        cursor = connect.cursor()
        # 防止注入
        sql = "select * from accounts where id=%s"
        cursor.execute(sql, [self.account_id])
        res = cursor.fetchone()
        if res is not None:
            username = res[1]
            password = res[2]
            browser.find_element_by_xpath('//*[@id="input-11"]').send_keys(username)
            browser.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
            browser.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[2]/button/span').click()
            time.sleep(3)
            # 选中球队
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/header/div/div/div/div[2]/div/a[1]').click()
            time.sleep(3)
            # 重置解绑
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[4]/button[3]/span').click()
            time.sleep(3)
            # 确定解绑
            browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/button[2]/span').click()
            time.sleep(5)
            # 选中QQ
            browser.find_element_by_xpath(
                '//*[@id="app"]/div/div/main/div/div/div/div/header/div/div/div/div[2]/div/a[2]'
            ).click()
            time.sleep(3)
            # 删除QQ
            js = 'document.getElementsByClassName(''"v-icon notranslate v-icon--link fa fa-trash-alt theme--dark red--text"'')[0].click()'
            browser.execute_script(js)
            time.sleep(3)
            # 确定删除
            browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/button[2]/span').click()
            time.sleep(3)
            delete_sql = "delete from accounts where id=%s"
            cursor.execute(delete_sql, [self.account_id])
            connect.commit()
            browser.quit()
        else:
            browser.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div/button/span').click()
            time.sleep(3)
            # 时间戳命名
            now_time = datetime.now().strftime("%Y-%m-%d-%H-%M").replace('-', '')
            now_time = now_time + str(from_which)
            username = 'pku' + now_time
            password = 'pku2017113120'
            browser.find_element_by_xpath('//*[@id="input-11"]').send_keys(username)
            browser.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
            browser.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[2]/button').click()
            time.sleep(5)
            # 点击购买
            browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/a[4]/span/i').click()
            time.sleep(1)
            # 选择类型
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div/div/div/div/div[7]/div/div/div').click()
            time.sleep(1)
            # 购买
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div/div/div/div/div[8]/button').click()
            time.sleep(5)
            # 点击管理
            browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/a[3]/span/i').click()
            time.sleep(1)
            # 点击QQ
            browser.find_element_by_xpath(
                '//*[@id="app"]/div/div/main/div/div/div/div/header/div/div/div/div[2]/div/a[2]').click()
            time.sleep(1)
            # 点击+号
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[1]/div/div/button/span/i').click()
            time.sleep(1)
            # 输入账号
            browser.find_element_by_xpath('//*[@id="input-199"]').send_keys(self.account_id)
            time.sleep(1)
            # 点击确定
            browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[4]/button').click()
            time.sleep(1)
            insert_sql = "insert into accounts values (%s, %s, %s)"
            cursor.execute(insert_sql, [self.account_id, username, password])
            connect.commit()
            print(username)
            # 点击球队
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/header/div/div/div/div[2]/div/a[1]').click()
            time.sleep(1)
            # 绑定游戏
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div/button/span').click()
            time.sleep(1)
            # 游戏账号
            browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div/div/div/div/div[1]/form/div[1]/div/div/div[1]/div[1]/div[1]').click()
            time.sleep(1)
            # 选中账号
            browser.find_element_by_xpath('//*[@id="list-271"]/div').click()
            time.sleep(1)
            # 游戏分组
            browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[2]/div/div/div[1]/div[1]').click()
            time.sleep(1)
            # 选中分组
            browser.find_element_by_xpath('//*[@id="list-278"]/div[2]').click()
            time.sleep(1)
            # 游戏分区
            browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]').click()
            time.sleep(1)
            # 选中分区
            browser.find_element_by_xpath('//*[@id="list-285"]/div[12]').click()
            time.sleep(1)
            # 绑定
            browser.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div/div/div/div/div/div[2]/button').click()
            time.sleep(1)
            # 挂机设置
            browser.find_element_by_xpath('//*[@id="app"]/div[5]/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[4]/a').click()
            time.sleep(1)
            # 综合设置
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/button').click()
            time.sleep(1)
            # 伤病球员打针
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/button')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/label').click()
            time.sleep(1)
            # 滚动到能显示出
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/label')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            # 签高级星探
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[5]/div/div[1]/label').click()
            time.sleep(1)
            # 星探回收
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[6]/div/div[1]/label').click()
            time.sleep(1)
            # 兑换底薪卡
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[8]/div/div[1]/label').click()
            time.sleep(1)
            # 卡级设置
            if self.is_hold == 1:
                browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[9]/div/div[1]/label').click()
                time.sleep(1)
            # 商城设置
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[3]/button').click()
            time.sleep(1)
            # 滚动到能显示的位置
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[3]/button')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # VIP商店
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div/div/label').click()
            time.sleep(1)
            # 球星钱包
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/label').click()
            time.sleep(1)
            # 体育广场
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[8]/button').click()
            time.sleep(1)
            # 滚动到能显示的位置
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[8]/button')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # 启用
            browser.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div/div/div[8]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/label').click()
            time.sleep(1)
            # 强化宝石
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[8]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/label').click()
            time.sleep(1)
            # 滚动到合适位置
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[8]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/label')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # 赞助商
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[8]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div[1]/label').click()
            time.sleep(1)
            # 梦幻征程
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/button').click()
            time.sleep(1)
            game_list1 = [3, 4, 5, 6, 8]
            for i in game_list1:
                if i == 1:
                    xpath_former = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/button'
                else:
                    xpath_former = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/div/div/div/div/div/div/div/div/div/div[{}]/div/div/div[1]/div/div[1]/label'.format(i-1)
                xpath = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/div/div/div/div/div/div/div/div/div/div[{}]/div/div/div[1]/div/div[1]/label'.format(i)
                target = browser.find_element_by_xpath(xpath_former)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                browser.find_element_by_xpath(xpath).click()
                time.sleep(1)
                if i == 3:
                    xpath_temp = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div[4]/div/div/label'
                    browser.find_element_by_xpath(xpath_temp).click()
                    time.sleep(1)
                elif i == 6:
                    xpath_temp = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/div/div/div/div/div/div/div/div/div/div[6]/div/div/div[2]/div[2]/div[3]/div/div/label'
                    browser.find_element_by_xpath(xpath_temp).click()
                    time.sleep(1)
                elif i == 8:
                    xpath_temp = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[10]/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[2]/div[2]/div/div/label'
                    browser.find_element_by_xpath(xpath_temp).click()
                    time.sleep(1)
                else:
                    time.sleep(1)
            # 各种比赛
            # 第一个特别处理
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/button').click()
            time.sleep(1)
            game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 20, 21, 25]
            for i in game_list:
                if i == 1:
                    xpath_former = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/button'
                elif i == 20:
                    xpath_former = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/div/div/div/div/div/div/div/div/div/div/div/div/div[{}]/div/div[1]/label'.format(i-2)
                else:
                    xpath_former = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/div/div/div/div/div/div/div/div/div/div/div/div/div[{}]/div/div[1]/label'.format(i-1)
                xpath = '//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/div/div/div/div/div/div/div/div/div/div/div/div/div[{}]/div/div[1]/label'.format(i)
                target = browser.find_element_by_xpath(xpath_former)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                browser.find_element_by_xpath(xpath).click()
                time.sleep(1)
                if i == 16:
                    # 天梯最大次数
                    for j in range(0, 13):
                        browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[11]/div/div/div/div/div/div/div/div/div/div/div/div/div[17]/div/div[3]/div/i').click()
                        time.sleep(1)
            # 比赛设置
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[12]/button').click()
            time.sleep(1)
            # 战术克制
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[12]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/label').click()
            time.sleep(1)
            # 节日活动
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/button').click()
            time.sleep(1)
            # 滚动到合适位置
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/button')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # 喝红茶
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/label').click()
            time.sleep(1)
            # 领取每日宝珠
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/label').click()
            time.sleep(1)
            # 经理培训班
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/label').click()
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/label').click()
            time.sleep(1)
            # 码头捕鱼
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div/label').click()
            time.sleep(1)
            # 挑战吉兽
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[4]/div/div[1]/div/div/label').click()
            time.sleep(1)
            # 滚动到合适位置
            target = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[7]/div/div[1]/div/div[1]/label')
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # 合成礼盒
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[13]/div/div/div/div/div/div/div/div/div/div[7]/div/div[2]/div/div[1]/label').click()
            time.sleep(1)
            # 保存
            browser.find_element_by_xpath('//*[@id="app"]/div/div/header/div/button[2]/span/i').click()
            time.sleep(5)
            # 挂机
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div/label').click()
            time.sleep(1)
            # 点击QQ
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/header/div/div/div/div[2]/div/a[2]').click()
            time.sleep(2)
            # 登录
            browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div/div/div[1]/div/div/div/div[1]/table/tbody/tr/td[4]/button[1]/span').click()
            time.sleep(250)
            browser.quit()


def run(id_list, keep_level, from_which):
    for i in id_list:
        ass = Assistance(i, keep_level)
        ass.set_options(from_which)


if __name__ == "__main__":
    QID_list1 = ["3552479476", "2329145264", "289054887"]
    QID_list2 = ["3428272172", "1843611610", "2713648022"]
    QID_list3 = ["3393348468", "1148099884", "2136827672"]
    QID_list4 = ["3307964506", "3564683815", "1753044001"]
    QID_list5 = ["3036619233", "3560567145", "1752307607"]
    QID_list6 = []
    threads = [threading.Thread(target=run, args=(QID_list1, 0, 1)),
               threading.Thread(target=run, args=(QID_list2, 0, 2)),
               threading.Thread(target=run, args=(QID_list3, 0, 3)),
               threading.Thread(target=run, args=(QID_list4, 0, 4)),
               threading.Thread(target=run, args=(QID_list5, 0, 5)),
               threading.Thread(target=run, args=(QID_list6, 1, 6))]
    for thread in threads:
        thread.start()
    # 试账号密码
    # for i in range(20210511155653, 20210511170540):
    #     para = {
    #         "account": str(i),
    #         "password": str(i)
    #     }
    #     url = "http://0di.cc:88/api/user/login"
    #     response = requests.post(url, data=para)
    #     response_data = json.loads(response.text)
    #     if response_data["msg"] == "用户名或者密码错误！":
    #         print(i, response_data["msg"])
    #         continue
    #     else:
    #         print(i, response_data["msg"])
    #         break
