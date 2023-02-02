import pymysql
import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'http://192.168.0.10:8100/view/T2/'
url2 = 'http://192.168.0.16:1111/index.php?m=user&f=login'
url3 = 'http://39.108.195.58:1111/index.php?m=user&f=login'
jenkins_url = "http://192.168.0.10:8100/view/T2/"

# 数据库配置
mysql0_zf = ('139.9.193.57', 3306, 'tester', 'test!@#2019')
mysql0 = ('139.9.193.57', 3307, 'tester', 'test!@#2019')
mysql1 = ('81.71.46.125', 3306, 'tester', 'test!@#2019')
mysql2 = ('81.71.46.125', 3306, 'tester', 'test!@#2019')
mysql3 = ('106.55.234.253', 3306, 'tester', 'test!@#2019')
mysql4 = ('159.75.200.7', 3306, 'tester', 'test!@#2019')
mysql5 = ('81.71.38.17', 3307, 'tester', 'test!@#2019')
mysql6 = ('81.71.39.122', 3306, 'tester', 'test!@#2019')
mysql7 = ('81.71.46.124', 3306, 'tester', 'test!@#2019')
mysql_nw1 = ('192.168.0.21', 3307, 'tester', 'test!@#2019')
mysql_nw2 = ('192.168.0.22', 3307, 'tester', 'test!@#2019')
mysql_nw3 = ('192.168.0.23', 3307, 'tester', 'test!@#2019')
mysqlefun999 = ('162.62.175.195', 3306, 'tester', 'test!@#2019')
mysqlefun10000 = ('162.62.175.195', 3307, 'tester', 'test!@#2019')
mysqlZongFu = ('43.131.66.43', 20006, 'dev', 'wjkjdev@2016')

# 高图测试服周循环初始化失败后，手动执行这脚
goat_c_i = "http://139.9.193.57/crons/run/CarnivalWeek.php?CLEAR=1"

# 服务器地址
address = {'address_goat': "http://139.9.193.57:800",
           'address_t1': "http://192.168.0.12:800",
           'address_t2': "http://81.71.46.125:8",
           'address_t3': "http://106.55.234.253:8",
           'address_t4': "http://159.75.200.7:800",
           'address_t5': "http://81.71.38.17:800",
           'address_t6': "http://81.71.39.122:800",
           'address_t7': "http://81.71.46.124:8",
           'address_nw1': "http://192.168.0.21:8",
           'address_nw2': "http://192.168.0.22:8",
           'address_nw3': "http://192.168.0.23:8",
           'address_efun999': "http://162.62.175.195:8001",
           'address_efun9999': "http://162.62.175.195:8002",
           'address_efun10000': "http://162.62.175.195:8003"}

# 魔眼刷新脚本
refreshe_eye = "/crons/run/VisionEye/VisionEye.php"

# 购买脚本
address_buy = "http://192.168.0.12:8009/tests/battle.php?s="
parameter_buy = "&recc="

# 全球赛事脚本
global_match = "/crons/run/Carnival/ContestReward.php"

# 清缓存脚本
clean_data_log = "/crons/run/Log/CreateLogTable.php"
clean_data = "/crons/run/ClearMemcache.php"
clean_config = "/crons/install/TableCache.php"


def message_nw():
    print("1.开副本\n\t12.关副本 13.重置所有副本 14.重置指定章节 15.完成副本到x章 16.降低副本野怪难度"
          "\n2.走testC 21.完成章节任务  22.走UI2.0  23.走UI3.0(不分奇偶) 24.走章节testD "
          "\n21.完成所有章节任务 212.完成当前章节任务"
          "\n3.市政厅等级 up↑↑↑ \n\t31.修改金币 32.修改资源 33.重置脚本执行时间（满体力)"
          "\n\t34.我要变强[美女养成、神兽养成、英雄兑换、已有英雄满级、艾拉斯之心、科技、魔法书变强]"
          "\n\t35.添加聊天头像框"
          "\n4.联盟等级 up↑↑↑ \n\t41.修改魔眼配置 42.刷新魔眼状态 43.联盟建筑立即完成 "
          "\n\t44.修改捐献值 45.修改联盟角色 46.修改入盟时间"
          "\n5.查道具id 51.添加道具 52.清空道具"
          "\n6.查士兵 61.加士兵 62.清除士兵 63.添加全等级全士兵 "
          "\n64.修改开服时间"
          "\n65.一键当国王"
          "\n7.pid查uid \n\t71.查vip前xx玩家 72.NickName查信息 73.NickName查UserName"
          "\n9.美女约会cd 91.酒馆-冒险家cd 92.酒馆-事件cd"
          "\n10:删除指定指引"
          "\n888:充值礼包 999：全球赛事排行奖励\n"
          "00：清所有缓存\t(输入'q'返回)\n")


def Build_message():
    ServerId = input("\n服务器：\n2:T2   3:T3   4:T4   5:T5   6:T6\n"
                     "21:内网1\t22：内网2\t23：内网3\n"
                     "0:高图测试服\t7:T2特殊服(T2-2)\n"
                     "8:efun测试服修改分服\n"
                     "efun:999、9999、10000\n"
                     "总服(查玩家信息):00\n12580:查线上数据库对应群组\n\n请输入选择：")
    if ServerId == "00":
        fun = input("总服\n1.通过Useid查玩家信息\n2.通过NickName查玩家信息\n(输入'q'返回)\n请输入:")
        print()
        if fun == "1":
            search = search_player(mysqlZongFu, ServerId, 0)
            search.serch_ZF_Message_By_Useid()
        elif fun == "2":
            search = search_player(mysqlZongFu, ServerId, 0)
            search.serch_ZF_Message_By_NickName()
        else:
            print("请重新选择")
            Build_message()

    elif ServerId == '12580':
        SearchGroup()
        Build_message()

    elif ServerId == "8":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        fun = input("efun分服切换:1.通过efunId查UseId    2.通过UseId修改分服号 "
                    "\n'999':999服账号重定向  '99999':9999服账号重定向\n '10000':10000服账号重定向  :")
        if fun == "1":
            search = efun(mysqlefun999, ServerId, 0)
            search.efunid_search_useid()
        elif fun == "2":
            change = efun(mysqlefun999, ServerId, 0)
            change.useid_change_serverId()
        elif fun == "999" or fun == "9999":
            exchange = efun(mysqlefun999, ServerId, 0)
            exchange.efun_exchange_useid()
        elif fun == "10000":
            exchange = efun(mysqlefun10000, ServerId, 0)
            exchange.efun_exchange_useid()

        elif fun == "3":
            try:
                jenkins_clean_data()
            except Exception:
                print("调用jenkins 失败")
                print("请重新选择")
                Build_message()

        else:
            print("请重新选择")
            Build_message()

    elif ServerId == "":
        print("请重新选择")
        Build_message()
    elif ServerId == "1":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        fun = input(
            "\n新大陆\n版本更新：\n1.更全部(不包括 T1, T5, T6, T2-2)\n2.更T2\t3.更T3\t4.更T4\t5.更T5\t7.更T2特殊服\n21.31.41.51.71.删除当前最大版本\n请选择：")
        print()
        Version_update = version_update(fun)
        Version_update.update_all()

    elif ServerId == "9":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        select_function()

    else:
        Serverid = input("分服：")
        if Serverid == "":
            Build_message()
        else:
            print()
            S = Select_Server(ServerId, Serverid)
            S.Select_server()


# efun测试服改服务器号serverId
class efun:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def efun_exchange_useid(self):
        try:
            serverid = input("分服号：")
            exchange_A = input("你的useid:")
            if exchange_A == "q" or exchange_A == "Q":
                Build_message()
            else:
                exchange_B = input("想要重定向的useid:")
                if exchange_B == "q" or exchange_B == "Q":
                    Build_message()
                else:
                    # 临时容器
                    exchange_C = '99999'
                    # print("\n执行之前：")
                    # SQL_before__search_data = \
                    #     "SELECT NickName, PlayerId,TotalServiceId " \
                    #     "FROM `server%s`.`tb_player` " \
                    #     "WHERE TotalServiceId = '%s' OR TotalServiceId = '%s' ;" % (serverid, exchange_A, exchange_B)
                    # B = Build_DB(self.mysql, SQL_before__search_data)
                    # B.Connection_DB()
                    # B.execuse_one_SQL_exch()
                    # print()

                    SQL_exchange = [
                        "UPDATE `server%s`.`tb_player` SET TotalServiceId = %s WHERE TotalServiceId = %s;" % (
                        serverid, exchange_C, exchange_A),
                        "UPDATE `server%s`.`tb_player` SET TotalServiceId = %s WHERE TotalServiceId = %s;" % (
                        serverid, exchange_A, exchange_B),
                        "UPDATE `server%s`.`tb_player` SET TotalServiceId = %s WHERE TotalServiceId = %s;" % (
                        serverid, exchange_B, exchange_C)
                    ]

                    B = Build_DB(self.mysql, SQL_exchange)
                    B.Connection_DB()
                    B.execuse_more_SQL()

                    # print("\n执行之后：")
                    # SQL_after_search_data = \
                    #     "SELECT NickName, PlayerId,TotalServiceId " \
                    #     "FROM `server%s`.`tb_player` " \
                    #     "WHERE TotalServiceId = '%s' OR TotalServiceId = '%s' ;" % (serverid, exchange_A, exchange_B)
                    #
                    # B = Build_DB(self.mysql, SQL_after_search_data)
                    # B.Connection_DB()
                    # B.execuse_one_SQL_exch()
                    # B.close_DB()

                    try:
                        jenkins_clean_data()
                    except Exception:
                        pass

                    Build_message()


        except Exception:
            print("账号重定向失败")
            Build_message()

    def efunid_search_useid(self):
        try:
            EfunId = input("请输入EfunId：")
            if EfunId == "q" or EfunId == "Q":
                Build_message()
            else:
                print("\n正在查询....")
                sql_efunid_search_useid = "SELECT UserId FROM `global`.`tb_user_efun` WHERE EfunId = %s;" % (EfunId)
                B = Build_DB(self.mysql, sql_efunid_search_useid)
                B.Connection_DB()
                B.execuse_useid_SQL()
                B.close_DB()
                print()
                Build_message()

        except Exception:
            print("查询失败，请联系King")
            print()
            Build_message()

    def useid_change_serverId(self):
        try:
            useId = input("请输入useId：")
            if useId == "q" or useId == "Q":
                Build_message()
            else:
                serverId = input("请输入想要去的分服Id：")
                if serverId == "q" or serverId == "Q":
                    Build_message()
                else:
                    print("\n正在修改...")
                    sql_useid_change_serverId = "UPDATE `global`.tb_user SET ServerId = %s WHERE UserId = %s;" % (
                        serverId, useId)
                    sql_search_serverId = "SELECT ServerId FROM `global`.`tb_user` WHERE UserId = %s;" % (useId)
                    B = Build_DB(self.mysql, sql_useid_change_serverId)
                    B.Connection_DB()
                    B.execuse_one_SQL()
                    B.close_DB()

                    print("\nuseId：%s" % useId)
                    B = Build_DB(self.mysql, sql_search_serverId)
                    B.Connection_DB()
                    B.efun_search_serverid_sql()
                    B.close_DB()
                    print("请到Jenkins清一下数据缓存！！！\n")

                    try:
                        jenkins_clean_data()
                    except Exception:
                        pass

                    Build_message()

        except Exception:
            print("efun分服修改失败，请联系King")
            print()
            Build_message()


class version_update:
    def __init__(self, fun):
        self.fun = fun

    def update_all(self):
        try:
            # SQL_del_max_version = "DELETE A FROM `global`.`tb_data_version` AS A, (SELECT MAX(VersionID) AS MaxId FROM `global`.`tb_data_version`) AS B WHERE A.VersionID = B.MaxId;"
            SQL_del_max_version = "DELETE FROM `global`.`tb_data_version` WHERE VersionID IN (SELECT MID FROM (SELECT MAX(VersionID) as MID FROM `global`.`tb_data_version`) as v);"

            # T2
            if self.fun == "21":
                B = Build_DB(mysql2, SQL_del_max_version)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("删除 MAX-版本 成功")
            elif self.fun == "31":
                B = Build_DB(mysql3, SQL_del_max_version)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("删除 MAX-版本 成功")
            elif self.fun == "41":
                B = Build_DB(mysql4, SQL_del_max_version)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("删除 MAX-版本 成功")
            elif self.fun == "51":
                B = Build_DB(mysql5, SQL_del_max_version)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("删除 MAX-版本 成功")
            elif self.fun == "71":
                B = Build_DB(mysql7, SQL_del_max_version)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("删除 MAX-版本 成功")

            else:
                version_number = input("请输入版本号(输入'q'返回)：")
                if version_number == "q" or version_number == "Q":
                    Build_message()
                else:
                    print("\n版本号为：" + version_number)
                    first_enter = input("第一次确认(输入'q'返回)")
                    if first_enter == "q" or first_enter == "Q":
                        Build_message()
                    else:
                        print("\n版本号为：" + version_number)
                        secend_enter = input("第二次确认，(输入'q'返回)")
                        if secend_enter == "q" or secend_enter == "Q":
                            Build_message()
                        else:
                            now_time = int(time.time())
                            print(now_time)

                            SQL_1 = "REPLACE INTO `global`.`tb_data_version`(VersionID, VersionDescription, CreateTime) VALUES (%s, %s, %s);" % (
                                version_number, version_number, now_time)

                            SQL_2 = "UPDATE `global`.`tb_data_server` SET Version = %s,VersionUpdateTime = %s WHERE 1;" % (
                                version_number, now_time)

                            # T2
                            if self.fun == "1" or self.fun == "2":
                                try:
                                    B = Build_DB(mysql2, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql2, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://81.71.46.125/crons/run/ClearMemcache.php")
                                    # print(result.text)
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T2 pass")
                                except Exception:
                                    print("T2 更新失败")

                            # T3
                            if self.fun == "1" or self.fun == "3":
                                try:
                                    B = Build_DB(mysql3, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql3, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://106.55.234.253/crons/run/ClearMemcache.php")
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T3 pass")
                                except Exception:
                                    print("T3 更新失败")

                                # T4
                            if self.fun == "1" or self.fun == "4":
                                try:
                                    B = Build_DB(mysql4, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql4, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://159.75.200.7:8000/crons/run/ClearMemcache.php")
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T4 pass")
                                except Exception:
                                    print("T4 更新失败")

                                # T6
                            if self.fun == "1" or self.fun == "6":
                                try:
                                    B = Build_DB(mysql6, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql6, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://81.71.39.122:8000/crons/run/ClearMemcache.php")
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T6 pass")
                                except Exception:
                                    print("T6 更新失败")

                            # 内网1、内网2、内网3
                            if self.fun == "1" or self.fun == "nw1":
                                try:
                                    # 内网1
                                    B = Build_DB(mysql_nw1, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql_nw1, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    # result = requests.get("http://192.168.0.21/crons/run/ClearMemcache.php")
                                    # print(result.text)
                                    # ok = "更新其它总服机器"
                                    # if result.text[0] in ok:
                                    #     print("内网1 pass")
                                    try:
                                        jenkins_clean_data_nw1()
                                    except Exception:
                                        pass
                                    print("内网1 pass")
                                    print("请到Jenkins清一下数据缓存！！！\n")
                                except Exception:
                                    print("内网1  更新失败")

                            if self.fun == "1" or self.fun == "nw2":
                                try:
                                    # 内网2
                                    B = Build_DB(mysql_nw2, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql_nw2, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    #     result = requests.get("http://192.168.0.22/crons/run/ClearMemcache.php")
                                    #     print(result.text)
                                    #     ok = "更新其它总服机器"
                                    #     if result.text[0] in ok:
                                    #         print("内网2 pass")
                                    try:
                                        jenkins_clean_data_nw2()
                                    except Exception:
                                        pass
                                    print("内网2 pass")
                                    print("请到Jenkins清一下数据缓存！！！\n")
                                except Exception:
                                    print("内网2  更新失败")

                            if self.fun == "1" or self.fun == "nw3":
                                try:
                                    # 内网3
                                    B = Build_DB(mysql_nw3, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql_nw3, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    # result = requests.get("http://192.168.0.23/crons/run/ClearMemcache.php")
                                    # print(result.text)
                                    # ok = "更新其它总服机器"
                                    # if result.text[0] in ok:
                                    #     print("内网3 pass")
                                    try:
                                        jenkins_clean_data_nw3()
                                    except Exception:
                                        pass
                                    print("内网3 pass")
                                    print("请到Jenkins清一下数据缓存！！！\n")
                                except Exception:
                                    print("内网  更新失败")

                                # T1
                            if self.fun == "01":
                                try:
                                    B = Build_DB(mysql1, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql1, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://192.168.0.12:8000//crons/run/ClearMemcache.php")
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T1 pass")
                                except Exception:
                                    print("T1 更新失败")

                                # T5
                                if self.fun == "5":
                                    try:
                                        B = Build_DB(mysql5, SQL_1)
                                        B.Connection_DB()
                                        B.execuse_one_SQL()
                                        B = Build_DB(mysql5, SQL_2)
                                        B.Connection_DB()
                                        B.execuse_one_SQL()
                                        B.close_DB()
                                        result = requests.get("http://112.74.172.133:8000/crons/run/ClearMemcache.php")
                                        ok = "更新其它总服机器"
                                        if result.text[0] in ok:
                                            print("T5 pass")
                                    except Exception:
                                        print("T5 更新失败")

                                # T2特殊服
                            if self.fun == "7":
                                try:
                                    B = Build_DB(mysql7, SQL_1)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B = Build_DB(mysql7, SQL_2)
                                    B.Connection_DB()
                                    B.execuse_one_SQL()
                                    B.close_DB()
                                    result = requests.get("http://81.71.46.124/crons/run/ClearMemcache.php")
                                    # print(result.text)
                                    ok = "更新其它总服机器"
                                    if result.text[0] in ok:
                                        print("T2特殊服 pass")
                                except Exception:
                                    print("T2特殊服 更新失败")
            print("更新结束~")
            Build_message()
        except Exception:
            print("更新失败，请联系管理员")
            Build_message()


class Select_Server:
    def __init__(self, ServerId, Serverid):
        self.ServerId = ServerId
        self.Serverid = Serverid

    def Select_server(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        if self.ServerId == "q" or self.Serverid == "q" or self.ServerId == "Q" or self.Serverid == "Q":
            Build_message()

        # T2
        elif self.ServerId == "2":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql2, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql2, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.update_player_gold()

            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql2, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql2, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql2, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                # 修改开服时间
                up_core = update_core(mysql2, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql2, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql2, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql2, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql2, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName(账号)
                search = search_player(mysql2, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                # 通过活动id查活动信息
                oc = OpenCenter(mysql2, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                # 通过活动名查活动信息
                oc = OpenCenter(mysql2, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                # 强开活动
                oc = OpenCenter(mysql2, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                # 美女约会刷新cd
                M = girl(mysql2, self.ServerId, self.Serverid)
                M.girl_DateCD()
            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql2, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()
            elif fun == "92":
                # 酒馆事件刷新cd
                R = risk(mysql2, self.ServerId, self.Serverid)
                R.risk_update_EventFreshTime()

            elif fun == "10":
                Guide = guide(mysql2, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()


        # 内网1
        elif self.ServerId == "21":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql_nw1, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql_nw1, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.update_player_gold()

            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql_nw1, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql_nw1, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql_nw1, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                # 修改开服时间
                up_core = update_core(mysql_nw1, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql_nw1, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql_nw1, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql_nw1, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql_nw1, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName(账号)
                search = search_player(mysql_nw1, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                # 通过活动id查活动信息
                oc = OpenCenter(mysql_nw1, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                # 通过活动名查活动信息
                oc = OpenCenter(mysql_nw1, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                # 强开活动
                oc = OpenCenter(mysql_nw1, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                # 美女约会刷新cd
                M = girl(mysql_nw1, self.ServerId, self.Serverid)
                M.girl_DateCD()
            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql_nw1, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()
            elif fun == "92":
                # 酒馆事件刷新cd
                R = risk(mysql_nw1, self.ServerId, self.Serverid)
                R.risk_update_EventFreshTime()

            elif fun == "10":
                Guide = guide(mysql_nw1, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()


        # 内网2
        elif self.ServerId == "22":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql_nw2, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql_nw2, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.update_player_gold()

            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql_nw2, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql_nw2, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql_nw2, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                # 修改开服时间
                up_core = update_core(mysql_nw2, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql_nw2, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql_nw2, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql_nw2, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql_nw2, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName(账号)
                search = search_player(mysql_nw2, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                # 通过活动id查活动信息
                oc = OpenCenter(mysql_nw2, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                # 通过活动名查活动信息
                oc = OpenCenter(mysql_nw2, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                # 强开活动
                oc = OpenCenter(mysql_nw2, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                # 美女约会刷新cd
                M = girl(mysql_nw2, self.ServerId, self.Serverid)
                M.girl_DateCD()
            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql_nw2, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()
            elif fun == "92":
                # 酒馆事件刷新cd
                R = risk(mysql_nw2, self.ServerId, self.Serverid)
                R.risk_update_EventFreshTime()

            elif fun == "10":
                Guide = guide(mysql_nw2, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # 内网3
        elif self.ServerId == "23":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql_nw3, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql_nw3, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.update_player_gold()

            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql_nw3, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql_nw3, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql_nw3, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                # 修改开服时间
                up_core = update_core(mysql_nw3, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql_nw3, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql_nw3, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql_nw3, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql_nw3, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName(账号)
                search = search_player(mysql_nw3, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                # 通过活动id查活动信息
                oc = OpenCenter(mysql_nw3, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                # 通过活动名查活动信息
                oc = OpenCenter(mysql_nw3, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                # 强开活动
                oc = OpenCenter(mysql_nw3, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                # 美女约会刷新cd
                M = girl(mysql_nw3, self.ServerId, self.Serverid)
                M.girl_DateCD()
            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql_nw3, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()
            elif fun == "92":
                # 酒馆事件刷新cd
                R = risk(mysql_nw3, self.ServerId, self.Serverid)
                R.risk_update_EventFreshTime()

            elif fun == "10":
                Guide = guide(mysql_nw3, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()


        # T1
        elif self.ServerId == "01":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql1, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql1, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.update_player_gold()

            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql1, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql1, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql1, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql1, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql1, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql1, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql1, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql1, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName(账号)
                search = search_player(mysql1, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql1, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql1, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql1, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                # 美女约会刷新cd
                M = girl(mysql1, self.ServerId, self.Serverid)
                M.girl_DateCD()
            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql1, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()
            elif fun == "92":
                # 酒馆事件刷新cd
                R = risk(mysql1, self.ServerId, self.Serverid)
                R.risk_update_EventFreshTime()

            elif fun == "10":
                Guide = guide(mysql1, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # T3
        elif self.ServerId == "3":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql3, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql3, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql3, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql3, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql3, self.ServerId,
                                      self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql3, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql3, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql3, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql3, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql3, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql3, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql3, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql3, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql3, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql3, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysql3, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        # T4
        elif self.ServerId == "4":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql4, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql4, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql4, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql4, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql4, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql4, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql4, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql4, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql4, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql4, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql4, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "91":
                # 酒馆冒险家刷新cd
                R = risk(mysql4, self.ServerId, self.Serverid)
                R.risk_update_RecruitTime()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "8":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql4, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "10":
                Guide = guide(mysql4, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # T5
        elif self.ServerId == "5":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql5, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql5, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql5, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql5, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql5, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql5, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql5, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql5, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql5, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql5, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql5, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql5, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql5, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql5, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysql5, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # T6
        elif self.ServerId == "6":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql6, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql6, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql6, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql6, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql6, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql6, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql6, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql6, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql6, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql6, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql6, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql6, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql6, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql6, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "999":
                C = Clean(self.ServerId, self.Serverid)
                C.global_match()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysql6, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # 0 goat
        elif self.ServerId == "0":
            message_nw()
            print("000:周循环初始化")
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql0, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql0, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql0, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql0, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql0, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql0, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql0, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql0, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql0, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql0, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql0, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "8":
                oc = OpenCenter(mysql0, self.ServerId, self.Serverid)
                oc.search_avtivity_by_id()

            elif fun == "81":
                oc = OpenCenter(mysql0, self.ServerId, self.Serverid)
                oc.search_avtivity_by_note()

            elif fun == "82":
                oc = OpenCenter(mysql0, self.ServerId, self.Serverid)
                oc.open_activity()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysql0, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "000":
                goat_Cycle_initialization()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # T2特殊服
        elif self.ServerId == "7":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysql7, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysql7, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysql7, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_eye()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysql7, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysql7, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysql7, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysql7, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysql7, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysql7, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysql7, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysql7, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysql7, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_log()
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # efun999、9999
        elif self.ServerId == "999" or self.ServerId == "9999":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysqlefun999, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysqlefun999, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysqlefun999, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                # C = Clean(self.ServerId, self.Serverid)
                # C.Clean_eye()
                print("没有权限，找运维执行  /crons/run/VisionEye/VisionEye.php")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysqlefun999, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysqlefun999, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysqlefun999, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysqlefun999, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysqlefun999, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysqlefun999, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysqlefun999, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysqlefun999, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysqlefun999, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

        # efun10000
        elif self.ServerId == "10000":
            message_nw()
            fun = input("请选择：")
            if fun == "q" or fun == "Q" or fun == "0":
                Build_message()

            elif fun == "1":
                # 开副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.open_FB()
            elif fun == "12":
                # 关副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.close_FB()
            elif fun == "13":
                # 重置所有副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.reset_all_FB()
            elif fun == "14":
                # 重置指定副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.reset_some_FB()
            elif fun == "15":
                # 完成xx副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.add_FB()
            elif fun == "16":
                # 完成xx副本
                FB = instance_FB(mysqlefun10000, self.ServerId, self.Serverid)
                FB.reduce_the_difficulty_FB()

            elif fun == "2":
                # 开TestC
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.open_TestC()
            elif fun == "21":
                # 完成所有章节任务
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.finish_all_task()
            elif fun == "212":
                # 完成当前章节任务
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.finish_current_task()
            elif fun == "22":
                # 开ui2.0
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.open_Ui2()
            elif fun == "23":
                # 无论奇偶，都走UI3.0
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.open_Ui3()
            elif fun == "24":
                # testD
                testC = new_testC(mysqlefun10000, self.ServerId, self.Serverid)
                testC.open_TestD()

            elif fun == "3":
                # 修改市政厅等级
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.update_city()

            elif fun == "31":
                # 修改金币数值
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.update_player_gold()
            elif fun == "32":
                # 修改资源数值
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.update_player_resource()
            elif fun == "33":
                # 设脚本执行时间为0（满体力）
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.clear_attribute()
            elif fun == "34":
                # 一键变强[英雄、艾拉斯之心、科技、魔法书]
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.be_stronger()
            elif fun == "35":
                # 添加聊天头像框
                player = player_date(mysqlefun10000, self.ServerId, self.Serverid)
                player.add_player_Avatarframe()

            elif fun == "4":
                # 修改联盟等级
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.update_union()
            elif fun == "41":
                # 修改魔眼保护时间配置
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.set_visionEye()
            elif fun == "42":
                # C = Clean(self.ServerId, self.Serverid)
                # C.Clean_eye()
                print("没有权限，找运维执行  /crons/run/VisionEye/VisionEye.php")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            elif fun == "43":
                # 联盟建筑完成状态
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.finish_UnionBuilding_state()
            elif fun == "44":
                # 修改联盟贡献
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.update_Contribution()
            elif fun == "45":
                # 修改联盟角色
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.update_union_role()
            elif fun == "46":
                # 修改入盟时间
                union = union_date(mysqlefun10000, self.ServerId, self.Serverid)
                union.update_union_player_Creattime()

            elif fun == "5":
                # 查询道具Id
                Item = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Item.serch_Item()
            elif fun == "51":
                # 插入道具
                Item = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Item.insert_Item()
            elif fun == "52":
                # 清空玩家道具
                Item = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Item.clear_Item()
            elif fun == "6":
                # 查询士兵
                Solder = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Solder.serch_Solder()
            elif fun == "61":
                # 插入士兵
                Solder = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Solder.insert_solder()
            elif fun == "62":
                # 清空玩家士兵
                Solder = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Solder.clear_Solder()
            elif fun == "63":
                # 插入全士兵
                Solder = item_or_solder(mysqlefun10000, self.ServerId, self.Serverid)
                Solder.insert_all_solder()

            elif fun == "64":
                up_core = update_core(mysqlefun10000, self.ServerId, self.Serverid)
                up_core.up_core()

            elif fun == "65":
                # 一键当国王
                up_city_job = update_city_job(mysqlefun10000, self.ServerId, self.Serverid)
                up_city_job.up_city_job()

            elif fun == "7":
                # 查询usdId
                search = search_player(mysqlefun10000, self.ServerId, self.Serverid)
                search.serch_useId_by_pid()

            elif fun == "71":
                # 查询vip高级玩家信息
                search = search_player(mysqlefun10000, self.ServerId, self.Serverid)
                search.serch_VIP_Player()

            elif fun == "72":
                # 通过玩家NickName查玩家信息
                search = search_player(mysqlefun10000, self.ServerId, self.Serverid)
                search.serch_Player_by_Nickname()

            elif fun == "73":
                # 通过玩家NickName查账号UserName
                search = search_player(mysqlefun10000, self.ServerId, self.Serverid)
                search.serch_UserName_by_NickName()

            elif fun == "888":
                buy = buy_Rechaerge(self.ServerId, self.Serverid)
                buy.buy_recharge()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            elif fun == "9":
                Guide = guide(mysqlefun10000, self.ServerId, self.Serverid)
                # 删除指定指引
                Guide.delete_player_guide()

            elif fun == "00":
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                C.Clean_config()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                print("请重新输入：")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()


class risk:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def risk_update_EventFreshTime(self):
        # 酒馆事件刷新时间
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("酒馆时间刷新时间修改\t(输入'q'返回)")
            EventFreshTime = input("约会CD（s）：")
            if EventFreshTime == "q" or EventFreshTime == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_risk_update_EventFreshTime = "UPDATE `serverconfig%s`.`tb_config_public` SET ConfigValue = JSON_SET(ConfigValue, '$.EventFreshTime', %s) WHERE ConfigKey = 'Risk';" % ()
                B = Build_DB(self.mysql, SQL_risk_update_EventFreshTime)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_config()
                print("酒馆-事件刷新时间已修改为", EventFreshTime, "秒")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("酒馆冒险家刷新CD失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def risk_update_RecruitTime(self):
        # 酒馆冒险家刷新时间
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("酒馆冒险家刷新时间修改\t(输入'q'返回)")
            RecruitTime = input("约会CD（s）：")
            if RecruitTime == "q" or RecruitTime == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_risk_update_RecruitTime = "UPDATE `serverconfig%s`.`tb_config_public` " \
                                              "SET ConfigValue = JSON_SET(ConfigValue, '$.RecruitTime', %s) " \
                                              "WHERE ConfigKey = 'Risk';" \
                                              % (self.Serverid, RecruitTime)
                B = Build_DB(self.mysql, SQL_risk_update_RecruitTime)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_config()
                print("酒馆-冒险家刷新时间已修改为", RecruitTime, "秒")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("酒馆冒险家刷新时间失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


class girl:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def girl_DateCD(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("美女约会刷新时间修改\t(输入'q'返回)")
            DateCD = input("约会CD（s）：")
            if DateCD == "q" or DateCD == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_update_girl_DateCD = "UPDATE `serverconfig%s`.`tb_config_girl_totality` " \
                                         "SET `Value` = '%s' " \
                                         "WHERE `Key` = \"DateCD\";" \
                                         % (self.Serverid, DateCD)
                B = Build_DB(self.mysql, SQL_update_girl_DateCD)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_config()
                print("美女约会刷新时间已修改为", DateCD, "秒")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("修改美女约会刷新时间失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


class OpenCenter:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def search_avtivity_by_id(self):
        id = input("请输入活动Id：")
        if id == "Q" or id == "q":
            Build_message()
        SQL_search_activity = "SELECT Id, OpenHallLevel, OpenType, OpenDate, IsNew, Note " \
                              "FROM `serverconfig%s`.`tb_config_carnival_center` " \
                              "WHERE Id = '%s';" % (self.Serverid, id)

        B = Build_DB(self.mysql, SQL_search_activity)
        B.Connection_DB()
        B.execuse_one_SQL()
        B.close_DB()

        S = Select_Server(self.ServerId, self.Serverid)
        S.Select_server()

    def search_avtivity_by_note(self):
        note = input("请输入活动名：")
        if note == "Q" or note == "q":
            Build_message()
        SQL_search_activity = "SELECT Id, OpenHallLevel, OpenType, OpenDate, IsNew, Note " \
                              "FROM `serverconfig%s`.`tb_config_carnival_center` " \
                              "WHERE Note REGEXP '%s';" % (self.Serverid, note)

        B = Build_DB(self.mysql, SQL_search_activity)
        B.Connection_DB()
        B.execuse_one_SQL()
        B.close_DB()

        S = Select_Server(self.ServerId, self.Serverid)
        S.Select_server()

    def open_activity(self):
        try:
            print("强开活动：")
            id = input("请输入活动Id：")
            if id == "Q" or id == "q":
                Build_message()

            print("`格式：20210521 00:00`")
            opentime = input("输入开启日期：   ")
            if opentime == "Q" or opentime == "q":
                Build_message()
            timeArray = time.strptime(opentime, "%Y%m%d %H:%M")
            timeStamp0 = int(time.mktime(timeArray)) + 28800
            print(timeStamp0)


            SQL_open_activity = "UPDATE `serverconfig%s`.`tb_config_carnival_center` " \
                                "SET OpenDate = '%s', IsNew = '1'  " \
                                "WHERE Id = '%s';" % (self.Serverid, timeStamp0, id)

            B = Build_DB(self.mysql, SQL_open_activity)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        except Exception:
            print("开启失败，是不是输入格式有误？")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()








class guide:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def delete_player_guide(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("删除指定指引\t(输入'q'返回)")
            del_guide = input("指引编号：")
            if del_guide == "q" or del_guide == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                del_pid = input("playerId：")
                if del_pid == "q" or del_pid == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_delete_player_guide = "DELETE FROM `server%s`.`tb_player_guide` WHERE GuideId = %s  AND PlayerId = %s ;" \
                                              % (self.Serverid, del_guide, del_pid)
                B = Build_DB(self.mysql, SQL_delete_player_guide)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("玩家", del_pid, "的指引：", del_guide, "已删除")
                print()
                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("指引删除失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


# 查玩家信息
class search_player:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    # 总服
    def serch_ZF_Message_By_Useid(self):
        try:
            Useid = input("(输入'q'返回)\nUseid:")
            if Useid == "q" or Useid == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                serch_message_by_useid = "SELECT UserId, NickName, UserName, ServerId " \
                                         "FROM `global`.`tb_user` WHERE UserId REGEXP '%s';" % (
                                             Useid)
                B = Build_DB(self.mysql, serch_message_by_useid)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("UserId, NickName, UserName, ServerId")
                print()
                Build_message()

        except Exception:
            print()
            print("查询失败,请联系管理员~\n")
            Build_message()

    # 总服
    def serch_ZF_Message_By_NickName(self):
        try:
            # print(self.mysql)
            NickName = input("(输入'q'返回)\nNickName:")
            if NickName == "q" or NickName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                serch_message_by_NickName = "SELECT UserId, NickName, UserName, ServerId, Channel " \
                                            "FROM `global`.`tb_user` WHERE NickName REGEXP '%s';" % NickName
                B = Build_DB(self.mysql, serch_message_by_NickName)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("UserId, NickName, ServerName, UserName, ServerId, Channel")
                print()
                Build_message()
        except Exception:
            print()
            print("查询失败,请联系管理员~\n")
            Build_message()

    # 非总服
    def serch_UserName_by_NickName(self):
        try:
            print("通过NickName查UserName (输入'q'返回)")
            NickName = input("NickName:")
            if NickName == "q" or NickName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                serch_username = "SELECT NickName, UserName FROM `global`.`tb_user` " \
                                 "WHERE NickName REGEXP '%s';" % NickName
                B = Build_DB(self.mysql, serch_username)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("NickName  UserName")
                print()
                Build_message()
        except Exception:
            print()
            print("查询失败,原因分析：1.请确认对应的数据库号 2.数据库连不上了,不妨试试？ 若多次尝试失败后请联系管理员~~\n")
            Build_message()

        # pid查uid
        def serch_useId_by_pid(self):
            try:
                print("通过pid查useid(输入'q'返回)")
                # if self.ServerId == '3' and self.Serverid == '1':
                #     self.Serverid = ''
                playerId = input("playerId:")
                if playerId == "q" or playerId == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    serch_useid = "SELECT TotalServiceId FROM server%s.`tb_player` WHERE PlayerId = %s;" \
                                  % (self.Serverid, playerId)
                    B = Build_DB(self.mysql, serch_useid)
                    B.Connection_DB()
                    B.execuse_useid_SQL()
                    B.close_DB()
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
            except Exception:
                print()
                print("查询失败,原因分析：1.请确认对应的数据库号 2.数据库连不上了,不妨试试？ 若多次尝试失败后请联系管理员~~\n")
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

    # NickName查信息
    def serch_Player_by_Nickname(self):
        try:
            print("通过NickName查玩家信息(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            solder_NickName = input("NickName:")
            if solder_NickName == "q" or solder_NickName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                serch_message = "SELECT NickName, PlayerId, TotalServiceId, HallLevel, VIPLevel " \
                                "FROM `server%s`.`tb_player`" \
                                " WHERE NickName REGEXP '%s';" \
                                % (self.Serverid, solder_NickName)
                B = Build_DB(self.mysql, serch_message)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print("  NickName   PId    UseId  等级 VIP等级")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("查询失败,原因分析：1.请确认对应的数据库号 2.数据库连不上了,不妨试试？ 若多次尝试失败后请联系管理员~~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    # 查vip前xx玩家
    def serch_VIP_Player(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            serch_player = "SELECT NickName, PlayerId, TotalServiceId, HallLevel, VIPLevel " \
                           "FROM `server%s`.`tb_player` " \
                           "ORDER BY VIPLevel DESC LIMIT 15;" \
                           % (self.Serverid)
            B = Build_DB(self.mysql, serch_player)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            print("NickName  PId  UseId 等级  VIP等级")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("查询失败,原因分析：1.请确认对应的数据库号 2.数据库连不上了,不妨试试？ 若多次尝试失败后请联系管理员~~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def serch_useId_by_pid(self):
        try:
            print("通过pid查useid(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            playerId = input("playerId:")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                serch_useid = "SELECT TotalServiceId FROM server%s.`tb_player` WHERE PlayerId = %s;" \
                              % (self.Serverid, playerId)
                B = Build_DB(self.mysql, serch_useid)
                B.Connection_DB()
                B.execuse_useid_SQL()
                B.close_DB()
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("查询失败,原因分析：1.请确认对应的数据库号 2.数据库连不上了,不妨试试？ 若多次尝试失败后请联系管理员~~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


# 道具
class item_or_solder:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def serch_Item(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("查询道具(输入'q'返回)")
            item_name = input("道具名:")
            if item_name == "q" or item_name == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_serch_item = "SELECT ItemId, Note FROM `serverconfig%s`.`tb_config_item` WHERE Note REGEXP '%s';" \
                                 % (self.Serverid, item_name)
                B = Build_DB(self.mysql, SQL_serch_item)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("查询道具失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def serch_Solder(self):
        try:
            print("查询士兵类型、等级(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            solder_name = input("士兵名:")
            if solder_name == "q" or solder_name == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_serch_solder = "SELECT `SoldierType`, `SoldierLevel`, `Note` " \
                                   "FROM `serverconfig%s`.`tb_config_soldier` WHERE Note REGEXP '%s';" \
                                   % (self.Serverid, solder_name)
                B = Build_DB(self.mysql, SQL_serch_solder)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("查询士兵失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def insert_Item(self):
        try:
            print("插入道具(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            item_id = input("道具Id：")
            if item_id == "q" or item_id == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                number = input("道具数量：")
                if number == "q" or number == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    playerId = input("请输入你的playerId：")
                    if playerId == "q" or playerId == "Q":
                        S = Select_Server(self.ServerId, self.Serverid)
                        S.Select_server()
                    else:
                        lastplayerId = playerId[-1]
                        SQL_insert_Item = [
                            "DELETE FROM `server%s`.`tb_player_item%s` WHERE PlayerId = %s AND ItemId = %s " % (
                                self.Serverid, lastplayerId, playerId, item_id),

                            "INSERT INTO " \
                            "`server%s`.`tb_player_item%s`" \
                            "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                            "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                            "FROM `serverconfig%s`.`tb_config_item` " \
                            "WHERE ItemId = %s;" % (
                                self.Serverid, lastplayerId, playerId, number, self.Serverid, item_id)
                        ]
                B = Build_DB(self.mysql, SQL_insert_Item)
                B.Connection_DB()
                B.execuse_more_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(playerId, "已添加道具")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("添加道具失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def insert_solder(self):
        try:
            print("添加、修改士兵数量(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            soldierType = input("士兵类型：")
            if soldierType == "q" or soldierType == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                soldierLevel = input("士兵等级：")
                if soldierLevel == "q" or soldierLevel == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    number = input("士兵数量：")
                    if number == "q" or number == "Q":
                        S = Select_Server(self.ServerId, self.Serverid)
                        S.Select_server()
                    else:
                        playerId = input("请输入你的playerId：")
                        if playerId == "q" or playerId == "Q":
                            S = Select_Server(self.ServerId, self.Serverid)
                            S.Select_server()
                        else:
                            lastplayerId = playerId[-1]
                            SQL_insert_solder = [
                                "DELETE FROM `server%s`.`tb_player_soldier%s` WHERE PlayerId = %s AND soldierType = %s AND soldierLevel = %s" \
                                % (self.Serverid, lastplayerId, playerId, soldierType, soldierLevel),

                                "INSERT INTO `server%s`.`tb_player_soldier%s`(`PlayerId`, `SoldierType`, `SoldierLevel`, `Number`, `CreateTime`, `UpdateTime`) " \
                                "SELECT %s, soldierType, soldierLevel, %s, 0, 0 " \
                                "FROM `serverconfig%s`.`tb_config_soldier`" \
                                " WHERE  SoldierType = %s AND SoldierLevel = %s;" \
                                % (self.Serverid, lastplayerId, playerId, number, self.Serverid, soldierType,
                                   soldierLevel)
                            ]
                B = Build_DB(self.mysql, SQL_insert_solder)
                B.Connection_DB()
                B.execuse_more_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(playerId, "已添加士兵")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("添加士兵失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def insert_all_solder(self):
        try:
            print("添加全等级士兵(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            number = input("士兵数量：")
            if number == "q" or number == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                playerId = input("请输入你的playerId：")
                if playerId == "q" or playerId == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    lastplayerId = playerId[-1]
                    SQL_insert_all_solder = "REPLACE INTO `server%s`.`tb_player_soldier%s`" \
                                            "(`PlayerId` , `SoldierType` , `SoldierLevel` , `Number`)" \
                                            "SELECT %s, `SoldierType`, `SoldierLevel`,%s " \
                                            "FROM serverconfig%s.`tb_config_soldier` " \
                                            "where `Load` !=0 AND `SoldierType` NOT IN (19,37) ;" \
                                            % (self.Serverid, lastplayerId, playerId, number, self.Serverid)
            B = Build_DB(self.mysql, SQL_insert_all_solder)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            print(playerId, "全等级士兵已添加")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("添加全士兵失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def clear_Item(self):
        try:
            print("清空所有道具(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            playerId = input("请输入你的playerId：")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                lastplayerId = playerId[-1]
                SQl_delete_item = "DELETE FROM `server%s`.`tb_player_item%s` WHERE PlayerId = %s;" \
                                  % (self.Serverid, lastplayerId, playerId)
                B = Build_DB(self.mysql, SQl_delete_item)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(playerId, "道具已清空")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("清除道具失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def clear_Solder(self):
        try:
            print("清空所有士兵(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            playerId = input("(输入'q'返回)\n请输入你的playerId：")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                lastplayerId = playerId[-1]

                SQl_delete_soldier = "DELETE FROM `server%s`.`tb_player_soldier%s` WHERE PlayerId = %s;" \
                                     % (self.Serverid, lastplayerId, playerId)
                B = Build_DB(self.mysql, SQl_delete_soldier)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(playerId, "士兵已清空")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("清除士兵失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


class update_Opentime:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def update_opentime(self):
        print("`格式：20210521 00:00`")
        try:
            opentime = input("开始开服时间：   ")
            if opentime == "Q" or opentime == "q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            timeArray = time.strptime(opentime, "%Y%m%d %H:%M")
            timeStamp0 = int(time.mktime(timeArray)) + 28800
            print(timeStamp0)
        except:
            print("时间格式写错了\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        try:
            SQL_update_opentime = "UPDATE `serverconfig%s`.`tb_config_core` " \
                                  "SET CoreValue = '%s' " \
                                  "WHERE CoreKey = 'OpenTime';" %(self.Serverid, opentime)
            B = Build_DB(self.mysql, SQL_update_opentime)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            print("开服时间修改成功~")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        except Exception:
            print("修改开服时间失败，请联系管理员~")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()






# 士兵
# 联盟相关
class union_date:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def update_union_player_Creattime(self):
        try:
            print("修改入盟时间（'q'返回）")
            CreateTime = input("!!!GMT+8,记得减个8h!!!\n入盟时间格式：20210521 20:20  :")
            if CreateTime == "q" or CreateTime == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            print("进来了。。。改时间")
            timeArray = time.strptime(CreateTime, "%Y%m%d %H:%M")
            timeStamp = int(time.mktime(timeArray))
            print(timeStamp)
            UnionName = input("UnionName:")
            if UnionName == "q" or UnionName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL = "UPDATE `server%s`.tb_player_union SET CreateTime = %s " \
                      "WHERE  UnionId " \
                      "IN (SELECT UnionId FROM `server%s`.`tb_sys_union` WHERE UnionName REGEXP '%s');" \
                      % (self.Serverid, timeStamp, self.Serverid, UnionName)
                B = Build_DB(self.mysql, SQL)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print("入盟时间修改成功")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("入盟时间修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def update_union_role(self):
        try:
            print("修改联盟角色(输入'q'返回)")
            UnionName = input("请输入联盟名称：")
            if UnionName == "q" or UnionName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                PlayerId = input("PlayerId:")
                if PlayerId == "q" or PlayerId == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    UnionRole = input("UnionRole（1-5）角色等级:")
                    if UnionRole == "q" or UnionRole == "Q":
                        S = Select_Server(self.ServerId, self.Serverid)
                        S.Select_server()
                    else:
                        SQL_update_union_role = "UPDATE `server%s`.tb_player_union SET UnionRole = %s " \
                                                "WHERE PlayerId = %s AND UnionId IN " \
                                                "(SELECT UnionId FROM `server%s`.`tb_sys_union` " \
                                                "WHERE UnionName REGEXP '%s');" \
                                                % (self.Serverid, UnionRole, PlayerId, self.Serverid, UnionName)
                B = Build_DB(self.mysql, SQL_update_union_role)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print("联盟角色修改成功")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("联盟角色修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def update_union(self):
        try:
            print("修改联盟等级(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            UnionName = input("请输入联盟名称：")
            if UnionName == "q" or UnionName == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                UnionLevel = input("等级：")
                if UnionLevel == "q" or UnionLevel == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_update_union = [
                        "UPDATE server%s.`tb_sys_union` SET UnionLevel = '%s' WHERE UnionName REGEXP '%s';" \
                        % (self.Serverid, UnionLevel, UnionName),

                        "UPDATE server%s.tb_sys_union_data " \
                        "SET Food = 20000000000,Wood = 20000000000,Crystal = 20000000000,Gem = 20000000000 " \
                        "WHERE UnionId " \
                        "IN (SELECT UnionId FROM server%s.tb_sys_union WHERE UnionName REGEXP '%s')" \
                        % (self.Serverid, self.Serverid, UnionName)
                    ]
                    B = Build_DB(self.mysql, SQL_update_union)
                    B.Connection_DB()
                    B.execuse_more_SQL()
                    B.close_DB()

                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print("联盟等级修改成功")
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
        except Exception:
            print()
            print("联盟等级修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def set_visionEye(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("修改魔眼保护时间(输入'q'返回)")
            eyeProtectTime = input("\n魔眼保护时间（s）：")
            if eyeProtectTime == "q" or eyeProtectTime == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_set_VisionEye = "UPDATE  `serverconfig%s`.`tb_config_public` " \
                                    "SET ConfigValue = '{\"Number\":{\"1\":1,\"2\":1,\"3\":1,\"4\":1,\"5\":1,\"6\":2,\"7\":2,\"8\":2,\"9\":2,\"10\":2,\"11\":3,\"12\":3,\"13\":3,\"14\":3,\"15\":3,\"16\":3,\"17\":3,\"18\":3,\"19\":3,\"20\":3,\"21\":3,\"22\":3,\"23\":3,\"24\":3,\"25\":3,\"26\":3,\"27\":3,\"28\":3,\"29\":3,\"30\":3},\"ProtectTime\":28800,\"GuardTime\":%s,\"WarVisionUnionLevel\":3,\"RankRecover\":0.00125,\"RankHeroExp\":1,\"MaxHeroExpTime\":8,\"HeroExpRewardTime\":3600,\"UnionManorRank\":0.4,\"UnionManorMaxRank\":15000000}' " \
                                    "WHERE ConfigKey REGEXP  'VisionEye';" \
                                    % (self.Serverid, eyeProtectTime)
                B = Build_DB(self.mysql, SQL_set_VisionEye)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_config()
                print("魔眼保护时间已修改")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("魔眼保护时间修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def finish_UnionBuilding_state(self):
        try:
            print("立即建完 联盟建筑(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            Union_Name = input("请输入联盟的名称：")
            if Union_Name == "q" or Union_Name == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_finish_UnionBuilding_state = "UPDATE server%s.`tb_sys_visioneye_manor` " \
                                                 "SET State = 1 " \
                                                 "WHERE UnionId = ANY(SELECT UnionId FROM server%s.tb_sys_union WHERE UnionName REGEXP '%s')" \
                                                 % (self.Serverid, self.Serverid, Union_Name)
                print()
                B = Build_DB(self.mysql, SQL_finish_UnionBuilding_state)
                print(SQL_finish_UnionBuilding_state)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(Union_Name, "联盟建筑状态已修改")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("联盟建筑状态修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def update_Contribution(self):
        try:
            print("修改联盟捐献(输入'q'返回)")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            # print("4.进来了 ")
            PlayerId = input("请输入你的 PlayerId ： ")
            if PlayerId == "q" or PlayerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                Contribution = input("联盟贡献值： ")
                if Contribution == "q" or Contribution == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_update_Contribution = "UPDATE `server%s`.`tb_player_union_attribute` SET Contribution = %s WHERE PlayerId = %s ;" \
                                              % (self.Serverid, Contribution, PlayerId)
                B = Build_DB(self.mysql, SQL_update_Contribution)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(PlayerId, "联盟贡献修改成功")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("玩家捐献值修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


# 玩家数据
class player_date:
    def __init__(self, myqsl, ServerId, Serverid):
        self.mysql = myqsl
        self.ServerId = ServerId
        self.Serverid = Serverid

    def update_city(self):

        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("升级市政厅等级(输入'q'返回)")
            PlayerId = input("请输入你的 PlayerId ： ")
            if PlayerId == "q" or PlayerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                HallLevel = input("市政厅等级 HallLevel ： ")
                # print("Serverid:" + self.Serverid)
                if HallLevel == "q" or HallLevel == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    # print("进入SQL")
                    if self.Serverid == "1" or self.Serverid == "":
                        self.last_pid = PlayerId[-1]
                    else:
                        self.last_pid = ""
                        # print("非1服， last_pid =" + self.last_pid)

                    SQL_update_city = [
                        "UPDATE server%s.tb_player " \
                        "SET HallLevel = %s " \
                        "WHERE PlayerId = %s;" % (self.Serverid, HallLevel, PlayerId),

                        "UPDATE server%s.tb_player_build%s " \
                        "SET BuildLevel = %s " \
                        "WHERE PlayerId = %s and BuildType < 100;" % (
                            self.Serverid, self.last_pid, HallLevel, PlayerId),

                        "UPDATE `server%s`.`tb_player_resource` " \
                        "SET Food = 20000000000,Wood = 20000000000,Crystal = 20000000000,Gem = 20000000000,Gold = 20000000000 " \
                        "WHERE PlayerId =  %s;" % (self.Serverid, PlayerId)
                    ]
                    B = Build_DB(self.mysql, SQL_update_city)
                    B.Connection_DB()
                    B.execuse_more_SQL()
                    B.close_DB()
                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print(PlayerId, "等级修改成功")
                    print()

                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
        except Exception:
            print()
            print("等级修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def update_player_gold(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("修改金币(输入'q'返回)")
            playerId = input("请输入playerId：")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                gold = input("请输入金币数量：")
                if gold == "q" or gold == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_update_gold = "UPDATE server%s.tb_player_resource SET Gold = %s WHERE PlayerId = %s;" \
                                      % (self.Serverid, gold, playerId)
                    B = Build_DB(self.mysql, SQL_update_gold)
                    B.Connection_DB()
                    B.execuse_one_SQL()
                    B.close_DB()

                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print(playerId, "金币修改成功")
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
        except Exception:
            print()
            print("金币修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def update_player_resource(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("修改资源(输入'q'返回)")
            playerId = input("请输入playerId：")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                resource = input("请输入资源数量：")
                if resource == "q" or resource == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_update_resouce = "UPDATE server%s.tb_player_resource " \
                                         "SET Food = %s, Wood = %s, Crystal = %s, Gem= %s, SafeFood = %s," \
                                         "SafeWood = %s,SafeCrystal = %s,SafeGem = %s WHERE PlayerId = %s;" \
                                         % (self.Serverid, resource, resource, resource, resource, resource, resource,
                                            resource, resource, playerId)
                    B = Build_DB(self.mysql, SQL_update_resouce)
                    B.Connection_DB()
                    B.execuse_one_SQL()
                    B.close_DB()

                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print(playerId, "资源数量已修改")
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
        except Exception:
            print()
            print("资源修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def add_player_Avatarframe(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("添加聊天头像框功能：(输入'q'返回)")
            playerId = input("请输入playerId：")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_add_player_Avatarframe = \
                    "UPDATE `server%s`.`tb_player_photo_frame` " \
                    "SET `FrameIds` = '{\"Chat\": [2, 32, 30, 28, 26, 24, 22, 20, 17, 15, 13, 11, 9, 7, 6, 4], \"Head\": [1, 33, 31, 29, 27, 25, 23, 21, 19, 18, 16, 14, 12, 10, 8, 5, 3]}' " \
                    "WHERE `playerId` = %s" % (self.Serverid, playerId)
                B = Build_DB(self.mysql, SQL_add_player_Avatarframe)
                B.Connection_DB()
                B.execuse_one_SQL()
                B.close_DB()

                C = Clean(self.ServerId, self.Serverid)
                C.Clean_data()
                print(playerId, "已添加头像框")
                print()
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
        except Exception:
            print()
            print("添加头像框失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def clear_attribute(self):
        try:
            if self.ServerId == '0':
                SQL_clear_attribute = "UPDATE `global`.`tb_config_execute` SET LastTime = 0;"
                B = Build_DB(mysql0_zf, SQL_clear_attribute)
                B.Connection_DB()
                B.execuse_one_SQL()
                # B.close_DB()

                SQL_clear_attribute = [
                    "UPDATE `server%s`.`tb_player_attribute` SET PhysicalUSETime = 0, "
                    "ManaUSETime = 0, EnergyUSETime = 0, ExpendTime = 0 WHERE 1;" % self.Serverid,

                    "UPDATE `server90051`.`tb_player_attribute` SET PhysicalUSETime = 0, "
                    "ManaUSETime = 0, EnergyUSETime = 0, ExpendTime = 0 WHERE 1;",

                    "UPDATE `server%s`.`tb_player_attribute_time` SET `GlobalChatTime` = 0 WHERE  1;" % self.Serverid,

                    "UPDATE `server90051`.`tb_player_attribute_time` SET `GlobalChatTime` = 0 WHERE  1;",

                    "UPDATE  serverconfig%s.`tb_config_execute` SET  LastTime = 0 WHERE 1;" % self.Serverid,

                    "UPDATE  serverconfig90051.`tb_config_execute` SET  LastTime = 0 WHERE 1;"
                ]
                B = Build_DB(self.mysql, SQL_clear_attribute)
                B.Connection_DB()
                B.execuse_more_SQL()
                B.close_DB()

            else:
                # if self.ServerId == '3' and self.Serverid == '1':
                #     self.Serverid = ''
                SQL_clear_attribute = [
                    "UPDATE `global`.`tb_config_execute` SET LastTime = 0;",

                    "UPDATE `server%s`.`tb_player_attribute` SET PhysicalUSETime = 0, "
                    "ManaUSETime = 0, EnergyUSETime = 0, ExpendTime = 0 WHERE 1;" % self.Serverid,

                    "UPDATE `server90051`.`tb_player_attribute` SET PhysicalUSETime = 0, "
                    "ManaUSETime = 0, EnergyUSETime = 0, ExpendTime = 0 WHERE 1;",

                    "UPDATE `server%s`.`tb_player_attribute_time` SET `GlobalChatTime` = 0 WHERE  1;" % self.Serverid,

                    "UPDATE `server90051`.`tb_player_attribute_time` SET `GlobalChatTime` = 0 WHERE  1;",

                    "UPDATE  serverconfig%s.`tb_config_execute` SET  LastTime = 0 WHERE 1;" % self.Serverid,

                    "UPDATE  serverconfig90051.`tb_config_execute` SET  LastTime = 0 WHERE 1;"
                ]
                B = Build_DB(self.mysql, SQL_clear_attribute)
                B.Connection_DB()
                B.execuse_more_SQL()
                B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            C.Clean_config()
            print("脚本最后执行时间已设为0\n体力已经拉满")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("重置脚本执行时间失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    # 增加英雄
    def add_hero(self):
        print("增加英雄")
        PlayerId = input("请输入请输入你的 PlayerId ：")
        last_pid = PlayerId[-1]
        for i in 5:
            a = i + 1

    # 英雄变强
    def be_stronger(self):
        try:
            print("一键变强[美女养成礼包、神兽养成大礼包、英雄兑换大礼包、英雄装备大礼包、领主套装大礼包]  (输入'q'返回\t技术支持：培老板）")
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            PlayerId = input("请输入你的 PlayerId ： ")
            if PlayerId == "q" or PlayerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                # if self.Serverid == "1" or self.Serverid == "":
                #     lastplayerId = PlayerId[-1]
                # else:
                #     lastplayerId = ""
                lastplayerId = PlayerId[-1]

                SQL_be_stronger = [
                    # 市政厅30级
                    "UPDATE server%s.tb_player " \
                    "SET HallLevel = %s " \
                    "WHERE PlayerId = %s;" % (self.Serverid, 30, PlayerId),

                    "UPDATE server%s.tb_player_build%s " \
                    "SET BuildLevel = %s " \
                    "WHERE PlayerId = %s and BuildType < 100;" % (self.Serverid, lastplayerId, 30, PlayerId),

                    "UPDATE `server%s`.`tb_player_resource` " \
                    "SET Food = 20000000000,Wood = 20000000000,Crystal = 20000000000,Gem = 20000000000,Gold = 20000000000 " \
                    "WHERE PlayerId =  %s;" % (self.Serverid, PlayerId),

                    "UPDATE `server%s`.`tb_player_monstersiege` SET `State` = 4 WHERE PlayerId = %s;"
                    % (self.Serverid, PlayerId),

                    # 英雄招募道具
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80101),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80102),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80103),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80122),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80123),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80124),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42001),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42002),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42003),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42004),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42005),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42006),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42007),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42008),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42009),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42010),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42011),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42012),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42013),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42014),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 42015),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72931),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 73056),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72868),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72724),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72625),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72332),

                    # 插道具
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 8000, self.Serverid, 72650),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80011),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80012),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80013),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80014),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80015),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80016,),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80017),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80018),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80019),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 80020),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 100, self.Serverid, 90001),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 88888, self.Serverid, 20029),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 9000, self.Serverid, 72674),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 2000, self.Serverid, 72674),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 2000, self.Serverid, 72675),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 2000, self.Serverid, 72676),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 2000, self.Serverid, 72677),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 72745),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 1000, self.Serverid, 72812),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 99999, self.Serverid, 72558),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 50000, self.Serverid, 72913),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 800000, self.Serverid, 30091),

                    # 稀有兵种
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20038),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20039),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20040),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20041),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20042),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20043),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20044),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20045),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20046),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20047),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20048),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20049),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20050),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20051),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20052),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20053),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 5000, self.Serverid, 20054),

                    # 万能宝典
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 999999, self.Serverid, 72149),

                    # 万能符文
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 999999, self.Serverid, 72165),

                    # 神兽碎片
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 90000, self.Serverid, 44001),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 90000, self.Serverid, 44002),

                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 90000, self.Serverid, 44003),

                    # 神兽经验
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 90000, self.Serverid, 44010),

                    # 神兽技能经验
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 90000, self.Serverid, 44015),

                    # 英雄技能随机包
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 80000, self.Serverid, 72813),

                    # 灵魂石
                    "REPLACE INTO " \
                    "`server%s`.`tb_player_item%s`" \
                    "(`PlayerId`, `ItemId`, `ItemType`,  `Number`, `Index`,`CreateTime`, `UpdateTime`, `DataVersion`) " \
                    "SELECT %s, ItemId,ItemType, %s, `Index`,0, 0, 0 " \
                    "FROM `serverconfig%s`.`tb_config_item` " \
                    "WHERE ItemId = %s;" % (
                        self.Serverid, lastplayerId, PlayerId, 80000, self.Serverid, 10214),

                    # 全英雄9品质 + 30级 + 满特长点
                    "update `server%s`.`tb_player_hero` " \
                    "set `HeroStar` = 9, `HeroLevel` = 30, `SpecialPoint` = 30 " \
                    "WHERE `PlayerId` =%s;" % (self.Serverid, PlayerId),

                    # 全符文添加符文等级20级
                    "replace INTO `server%s`.`tb_player_hero_rune` ("
                    "PlayerId, HeroId, RuneType, RuneLevel, Item, UpdateTime) " \
                    "select PlayerId, HeroId, RuneType, RuneLevel, Item, 1532991659 " \
                    "FROM `server%s`.`tb_player_hero` a " \
                    "JOIN `serverconfig%s`.tb_config_rune on PlayerId = %s and RuneLevel = 20;" \
                    % (self.Serverid, self.Serverid, self.Serverid, PlayerId),

                    # 全英雄适性50级
                    "update `server%s`.`tb_player_hero` set `ResLevel` = 50, `ErodeLevel` = 50 WHERE `PlayerId` = %s;" \
                    % (self.Serverid, PlayerId),

                    # 英雄技能全8级
                    "update `server%s`.`tb_player_hero_skill` set `SkillLevel` = 8 WHERE `PlayerId` = %s;" \
                    % (self.Serverid, PlayerId),

                    # 英雄等级满级
                    "update `server%s`.`tb_player_hero` set `HeroLevel` = 40 WHERE `PlayerId` = %s;" \
                    % (self.Serverid, PlayerId),

                    "DELETE FROM `server%s`.`tb_player_item%s` "
                    "WHERE PlayerId = %s AND ItemId IN (72713,80019,80020,90010,90012);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    "INSERT INTO `server%s`.`tb_player_item%s` ("
                    "`PlayerId`, `ItemId`, `ItemType`, `Number`, `Index`) VALUES (%s, 72713, 80, 52000, 2999);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    "INSERT INTO `server%s`.`tb_player_item%s` ("
                    "`PlayerId`, `ItemId`, `ItemType`, `Number`, `Index`) VALUES (%s, 80019, 34, 52000, 1206);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    "INSERT INTO `server%s`.`tb_player_item%s` ("
                    "`PlayerId`, `ItemId`, `ItemType`, `Number`, `Index`) VALUES (%s, 80020, 34, 52000, 1207);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    "INSERT INTO `server%s`.`tb_player_item%s` ("
                    "`PlayerId`, `ItemId`, `ItemType`, `Number`, `Index`) VALUES (%s, 90010, 49,52000, 2395);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    "INSERT INTO `server%s`.`tb_player_item%s` ("
                    "`PlayerId`, `ItemId`, `ItemType`, `Number`, `Index`) VALUES (%s, 90012, 2, 52000, 1567);" % (
                        self.Serverid, lastplayerId, PlayerId),

                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    # 艾拉斯之心全属性满
                    "UPDATE `server%s`.`tb_player_ailas` " \
                    "SET `Level` = 60, `PhysicsAttack` = 60000, `PhysicsDefense` = 60000, `MagicAttack` = 60000," \
                    " `MagicDefense` = 60000, `Prestige` = 200, `Res` = 200, `Erode` = 250 " \
                    "WHERE `PlayerId` = %s;" % (self.Serverid, PlayerId),

                    # 艾拉斯之魂 强化
                    "replace into `server%s`.`tb_player_ailas_soldier_strong` ("
                    "PlayerId, `SoldierType`, `StrongLevel`, `SoldierPhysicsAttack`, `SoldierMagicAttack`, " \
                    "`SoldierPhysicsDefense`, `SoldierMagicDefense`, `SoldierHP`, `SoldierHurt`, `Index`, " \
                    "`CreateTime`, `UpdateTime`) " \
                    "SELECT %s,  `SoldierType`, 30, `SoldierPhysicsAttack`, `SoldierMagicAttack`, " \
                    "`SoldierPhysicsDefense`, `SoldierMagicDefense`, `SoldierHP`, `SoldierHurt`, 0, 1499082046, 1499082046 " \
                    "FROM serverconfig%s.`tb_config_ailas_soldier_strong`;" % (self.Serverid, PlayerId, self.Serverid),

                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    # 魔法师升级
                    "REPLACE INTO `server%s`.`tb_player_magic_study` ("
                    "`PlayerId`, `MagicId`, `MagicLevel`, `MagicClass`, " \
                    "`MagicType`, `ForcePoint`, `Item`, `UpdateTime`) " \
                    "SELECT %s, `MagicId`, 5, `MagicClass`, `MagicType`, `ForcePoint`, `Item`, 1509321633 " \
                    "FROM `serverconfig%s`.`tb_config_magic_book`;" % (
                        self.Serverid, PlayerId, self.Serverid),

                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    # 科技全满
                    "replace into `server%s`.`tb_player_science%s`("
                    "PlayerId, ScienceId, ScienceClass, ScienceType, State, isHelp, CreateTime, FinishTime, TotalTime) "
                    "SELECT %s, ScienceId, ScienceClass, ScienceType, 1, 1, 1499082046, 1499082046, 1499082046 "
                    "FROM serverconfig%s.`tb_config_science`;" % (
                        self.Serverid, lastplayerId, PlayerId, self.Serverid),

                    "UPDATE `server%s`.`tb_player_girl` SET LoveValue = 3000, Star = 10 WHERE PlayerId = %s;"
                    % (self.Serverid, PlayerId)
                ]
            B = Build_DB(self.mysql, SQL_be_stronger)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            print()
            print(
                "PlayerId：" + PlayerId + "     请重新登录~ 请重新登录~\n[艾拉斯之心已变强]\t[研究院科技已变强]"
                                         "\t[魔法书已变强]\n[未拥有的英雄、神兽可直接进行兑换]"
                                         "\n[背包是个好东西，请查收养成礼包]"
                                         "\n[英雄变强]"
                                         "\n请重登后,手动升一级英雄!\n手动升一级英雄!!\n手动升一级英雄!!!"
                                         "\n（用到特长：需tb_player_hero_specialty,选一条数据ExclusiveType改2）")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("一键变强失败,自己变强啦~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


# 开testC
class new_testC:
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def cut_testD_task(self):
        print("开始删除章节活动组....")
        try:
            if self.ServerId == "3" and self.Serverid == "1":
                self.Serverid = ""
            start1 = time.time()
            SQL_pass_task = "DELETE FROM `serverconfig%s`.`tb_config_task_group` WHERE 1 ;" % self.Serverid
            B = Build_DB(self.mysql, SQL_pass_task)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("章节任务组已清除,请重新创号~")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        except Exception:
            print()
            print("执行失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def add_testD_task(self):
        print("开始恢复章节活动组....")
        try:
            if self.ServerId == "3" and self.Serverid == "1":
                self.Serverid = ""
            start1 = time.time()
            SQL_add_task = [
                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (1,1,'{\"Item\": {\"20010\": 1, \"30009\": 5, \"30017\": 5, \"30041\": 5}}','第0章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (2,2,'{\"Item\": {\"30009\": 10, \"30088\": 5}, \"Soldier\": {\"1\": {\"1\": 600}, \"2\": {\"1\": 1000}}}','第1章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (3,3,'{\"Equip\": {\"1\": 1, \"11\": 1, \"21\": 1, \"31\": 1}}','第2章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (4,4,'{\"Item\": {\"30017\": 10, \"40001\": 80}, \"Soldier\": {\"3\": {\"1\": 500}, \"6\": {\"1\": 300}}}','第3章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (5,5,'{\"Item\": {\"30033\": 10, \"42007\": 5, \"44006\": 30}, \"Soldier\": {\"5\": {\"2\": 900}}}','第4章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (6,6,'{\"Item\": {\"30009\": 20, \"30017\": 20, \"30041\": 20}, \"Soldier\": {\"3\": {\"2\": 500}}}','第5章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (7,7,'{\"Item\": {\"10014\": 1, \"10034\": 3, \"30088\": 10, \"90004\": 1}}','第6章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (8,8,'{\"Item\": {\"10212\": 1000, \"20036\": 1, \"44005\": 1, \"86001\": 250}}','第7章基础配置');" % self.Serverid
            ]
            B = Build_DB(self.mysql, SQL_add_task)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()
            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("章节任务组已恢复,请重新创号~")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        except Exception:
            print()
            print("执行失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def finish_current_task(self):
        try:
            print("仅完成当前章节所有任务....")
            start1 = time.time()
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            playerId = input("playerId:")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            SQL_finish_current_task = \
                "UPDATE `server%s`.`tb_player_task` SET State = 2 WHERE PlayerId = %s;" % (self.Serverid, playerId)

            B = Build_DB(self.mysql, SQL_finish_current_task)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            end1 = time.time()
            print("SQL耗时:" + str(end1 - start1))

            start2 = time.time()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            end2 = time.time()
            print("清配置耗时:" + str(end2 - start2))
            print("当前章节任务已完成,请前往领取奖励~")
            print()

            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("章节任务进度修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def finish_all_task(self):
        try:
            print("完成所有章节任务....")
            start1 = time.time()
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            playerId = input("playerId:")
            if playerId == "q" or playerId == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()

            SQL_finish_all_task = [
                "UPDATE `server%s`.`tb_player_task` SET `State` =3 WHERE `PlayerId` = %s ;" % (self.Serverid, playerId),
                "UPDATE `server%s`.`tb_player_task_group_reward` SET `State` =1  WHERE `PlayerId` = %s ;" % (
                    self.Serverid, playerId)
            ]

            B = Build_DB(self.mysql, SQL_finish_all_task)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()
            end1 = time.time()
            print("SQL耗时:" + str(end1 - start1))

            start2 = time.time()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            end2 = time.time()
            print("清配置耗时:" + str(end2 - start2))
            print("章节任务已完成,请前往领取奖励~")
            print()

            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("章节任务进度修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def open_TestC(self):
        try:
            print("正在配置testC环境....")
            start1 = time.time()
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_open_testC = [
                # 取消章节任务
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.OpenServerId', \"\") "
                "WHERE ConfigKey = 'task';" % self.Serverid,

                # 删除章节任务组
                "DELETE FROM `serverconfig%s`.`tb_config_task_group` WHERE 1 ;" % self.Serverid,

                # 取消mission3
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.\"2\"', '1-10000','$.\"3\"', '') "
                "WHERE ConfigKey = 'ServerMission';" % self.Serverid,

                # testC
                "UPDATE `serverconfig%s`.`tb_config_public` " \
                "SET ConfigValue = '{\"Where\":{\"2\":{\"ServerId\":[\"1-10000\"]," \
                "\"Channel\":[1,2,3,4,5,6,7,12000,11111,11112,11115,11122,11131,11132,11135,11136]}}," \
                "\"LimitServerId\":0,\"LimitTime\":0,\"TestC\":1}'" \
                "WHERE ConfigKey = 'switchversion';" % self.Serverid
            ]

            B = Build_DB(self.mysql, SQL_open_testC)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()
            end1 = time.time()
            print("SQL耗时:" + str(end1 - start1))

            start2 = time.time()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            end2 = time.time()
            print("清配置耗时:" + str(end2 - start2))
            print("testC已开,请重新创号~")
            print()

            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("testC开启失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def open_Ui3(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_open_ui30 = [
                # 取消章节任务
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.OpenServerId', \"\") "
                "WHERE ConfigKey = 'task';" % self.Serverid,

                # 删除章节任务组
                "DELETE FROM `serverconfig%s`.`tb_config_task_group` WHERE 1 ;" % self.Serverid,

                # 取消mission3
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.\"2\"', '1-10000','$.\"3\"', '') "
                "WHERE ConfigKey = 'ServerMission';" % self.Serverid,

                # ui3.0
                "UPDATE `serverconfig%s`.`tb_config_public` " \
                "SET ConfigValue = '{\"Where\":{\"3\":{\"ServerId\":[\"1-10000\"]," \
                "\"Channel\":[1,2,3,4,5,6,7,12000,11111,11112,11115,11122,11131,11132,11135,11136]}}," \
                "\"LimitServerId\":0,\"LimitTime\":0,\"TestC\":1}'" \
                "WHERE ConfigKey = 'switchversion';" % self.Serverid
            ]

            B = Build_DB(self.mysql, SQL_open_ui30)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("UI3.0  已开,请重新创号~")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("操作失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def open_Ui2(self):
        try:
            if self.ServerId == '3' and self.Serverid == '1':
                self.Serverid = ''
            SQL_open_ui20 = [
                # 取消章节任务
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.OpenServerId', \"\") "
                "WHERE ConfigKey = 'task';" % self.Serverid,

                # 删除章节任务组
                "DELETE FROM `serverconfig%s`.`tb_config_task_group` WHERE 1 ;" % self.Serverid,

                # 取消mission3
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.\"2\"', '1-10000','$.\"3\"', '') "
                "WHERE ConfigKey = 'ServerMission';" % self.Serverid,

                "UPDATE `serverconfig%s`.`tb_config_public` " \
                "SET ConfigValue = '{\"Where\":{\"2\":{\"ServerId\":[\"1-10000\"]," \
                "\"Channel\":[1,2,3,4,5,6,7,12000,11111,11112,11115,11122,11131,11132,11135,11136]}}," \
                "\"LimitServerId\":0,\"LimitTime\":0,\"TestC\":0}'" \
                "WHERE ConfigKey = 'switchversion';" % self.Serverid
            ]

            B = Build_DB(self.mysql, SQL_open_ui20)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("UI2.0  已开,请重新创号~")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("操作失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def open_TestD(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_open_testD = [
                # 添加章节任务组配置
                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (1,1,'{\"Item\": {\"20010\": 1, \"30009\": 5, \"30017\": 5, \"30041\": 5}}','第0章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (2,2,'{\"Item\": {\"30009\": 10, \"30088\": 5}, \"Soldier\": {\"1\": {\"1\": 600}, \"2\": {\"1\": 1000}}}','第1章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (3,3,'{\"Equip\": {\"1\": 1, \"11\": 1, \"21\": 1, \"31\": 1}}','第2章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (4,4,'{\"Item\": {\"30017\": 10, \"40001\": 80}, \"Soldier\": {\"3\": {\"1\": 500}, \"6\": {\"1\": 300}}}','第3章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (5,5,'{\"Item\": {\"30033\": 10, \"42007\": 5, \"44006\": 30}, \"Soldier\": {\"5\": {\"2\": 900}}}','第4章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (6,6,'{\"Item\": {\"30009\": 20, \"30017\": 20, \"30041\": 20}, \"Soldier\": {\"3\": {\"2\": 500}}}','第5章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (7,7,'{\"Item\": {\"10014\": 1, \"10034\": 3, \"30088\": 10, \"90004\": 1}}','第6章基础配置');" % self.Serverid,

                "REPLACE INTO `serverconfig%s`.`tb_config_task_group` (`Id`,`Group`,`Reward`,`Note`) "
                "VALUES (8,8,'{\"Item\": {\"10212\": 1000, \"20036\": 1, \"44005\": 1, \"86001\": 250}}','第7章基础配置');" % self.Serverid,

                # 开启章节任务
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.OpenServerId', \"1-10000\") "
                "WHERE ConfigKey = 'task';" % self.Serverid,

                # 走mission3
                "UPDATE `serverconfig%s`.`tb_config_public` "
                "SET ConfigValue = JSON_SET(ConfigValue, '$.\"2\"', '','$.\"3\"', '1-10000') "
                "WHERE ConfigKey = 'ServerMission';" % self.Serverid,

                # tesC前提

                "UPDATE `serverconfig%s`.`tb_config_public` " \
                "SET ConfigValue = '{\"Where\":{\"2\":{\"ServerId\":[\"1-10000\"]," \
                "\"Channel\":[1,2,3,4,5,6,7,12000,11111,11112,11115,11122,11131,11132,11135,11136]}}," \
                "\"LimitServerId\":0,\"LimitTime\":0,\"TestC\":1}'" \
                "WHERE ConfigKey = 'switchversion';" % self.Serverid
            ]

            B = Build_DB(self.mysql, SQL_open_testD)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("章节(testD)  已开,请重新创号~")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("操作失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()



class update_city_job:
    #任命国王
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def up_city_job(self):
        print("\t一键当国王")
        try:
            pid = input("请输入playerid:")
            SQL_get_unionid = "SELECT UnionId FROM `server%s`.`tb_player_union` WHERE PlayerId = %s;" % (self.Serverid, pid)

            B = Build_DB(self.mysql, SQL_get_unionid)
            B.Connection_DB()
            unionid = B.execuse_return_SQL_()
            # print("联盟id:", unionid)

        except:
            print("联盟id查询失败")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        try:
            last_weekday = input("（时间格式：'20210521 00:00`）\n请输入上周六/日的任一时间:")
            timeArray = time.strptime(last_weekday, "%Y%m%d %H:%M")
            timeStamp0 = int(time.mktime(timeArray))
            print(timeStamp0)

        except:
            print()
            print("输入时间格式错误~\n")
            try:
                last_weekday = input("（时间格式：'20210521 00:00`）\n请输入上周六/日的任一时间:")
                timeArray = time.strptime(last_weekday, "%Y%m%d %H:%M")
                timeStamp0 = int(time.mktime(timeArray))
                print(timeStamp0)
            except:
                print()
                print("输入时间格式错误~\n")
                try:
                    last_weekday = input("（时间格式：'20210521 00:00`）\n请输入上周六/日的任一时间:")
                    timeArray = time.strptime(last_weekday, "%Y%m%d %H:%M")
                    timeStamp0 = int(time.mktime(timeArray))
                    print(timeStamp0)
                except:
                    print()
                    print("输入时间格式错误~\n")



        try:
            SQL_up_job = [
                # 删除分城守卫
                "DELETE  FROM server%s.tb_sys_city_monster;" % self.Serverid,

               # 修改圣城和三分城的保护状态，xxx=时间戳(要当前时间的上周六/日任意时间)   yyy=盟主的playid   zzz=联盟id
                "UPDATE server%s.tb_sys_city " \
                "SET State = '2', WinTime = '%s',BattleTime='%s',RewardTime = '%s',PlayerId = '%s',UnionId = '%s' " \
                "WHERE tb_sys_city.CityId in(1,2,3,4);" \
                % (self.Serverid, timeStamp0, timeStamp0, timeStamp0, pid, unionid),

                # 删除国王技能使用cd
                "DELETE FROM server%s.tb_sys_city_skill;" % self.Serverid,

                # 任命盟主为国王职位
                "UPDATE server%s.tb_sys_city_job " \
                "SET PlayerId = '%s',UnionId='%s',CreateTime='%s' " \
                "WHERE tb_sys_city_job.JobId = 16;" \
                % (self.Serverid, pid, unionid, timeStamp0)
            ]

            # 上面sql执行完后，要清数据缓存和总服缓存（go服务）
            B = Build_DB(self.mysql, SQL_up_job)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()

            print("一键当国王执行完成,请重新登陆~~\n一键当国王执行完成,请重新登陆~~\n一键当国王执行完成,请重新登陆~~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        except:
            print("一键当国王失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


class update_core:
    #修改开服时间
    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def up_core(self):
        print("\n\t修改开服时间")
        try:
            core_time = input("\t格式：'20210521 00:00`\n请输入想要修改的开服时间:")
            timeArray = time.strptime(core_time, "%Y%m%d %H:%M")
            timeStamp0 = int(time.mktime(timeArray))
            print(timeStamp0)
        except:
            print("时间格式输入错误,请重试!")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_update_core = "UPDATE `serverconfig%s`.`tb_config_core` SET CoreValue =%s  WHERE CoreKey = 'OpenTime';" \
                             % (self.Serverid, timeStamp0)

            B = Build_DB(self.mysql, SQL_update_core)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("开服时间已修改")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("开服时间修改失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

# 副本（命运之门）
class instance_FB:

    def __init__(self, mysql, ServerId, Serverid):
        self.mysql = mysql
        self.ServerId = ServerId
        self.Serverid = Serverid

    def reduce_the_difficulty_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_open_FuBen = "UPDATE `serverconfig%s`.`tb_config_instance_guard_troop` SET SoldierLevel = 1, SoldierNumber = 1;" % self.Serverid

            B = Build_DB(self.mysql, SQL_open_FuBen)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("副本难度已降低,野怪数量为1,等级为1")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("副本开启失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def open_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_open_FuBen = "UPDATE `serverconfig%s`.`tb_config_carnival_center_open_server` " \
                             "SET OpenServer = '1-10000'  " \
                             "WHERE Id = 903;" % self.Serverid

            B = Build_DB(self.mysql, SQL_open_FuBen)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()

            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("副本已开")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("副本开启失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def close_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            SQL_close_FuBen = "UPDATE `serverconfig%s`.`tb_config_carnival_center_open_server` " \
                              "SET OpenServer = '999999'  " \
                              "WHERE Id = 903;" % self.Serverid

            B = Build_DB(self.mysql, SQL_close_FuBen)
            B.Connection_DB()
            B.execuse_one_SQL()
            B.close_DB()
            C = Clean(self.ServerId, self.Serverid)
            C.Clean_config()
            print("副本已关闭")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("副本关闭失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def reset_all_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("重置所有副本\t(输入'q'返回)")
            del_pid = input("playerId：")
            if del_pid == "q" or del_pid == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                SQL_del_all_FB = [
                    "DELETE FROM `server%s`.`tb_player_instance` WHERE PlayerId = %s;" % (self.Serverid, del_pid),
                    "DELETE FROM `server%s`.`tb_player_instance_chamber_reward` WHERE PlayerId = %s;" % (
                        self.Serverid, del_pid),
                    "DELETE FROM `server%s`.`tb_player_instance_data` WHERE PlayerId = %s;" % (self.Serverid, del_pid),
                    "DELETE FROM `server%s`.`tb_player_instance_event_reward` WHERE PlayerId = %s;" % (
                        self.Serverid, del_pid),
                    "DELETE FROM `server%s`.`tb_player_instance_plot_reward` WHERE PlayerId = %s;" % (
                        self.Serverid, del_pid),
                    "DELETE FROM `server%s`.`tb_player_instance_other_reward` WHERE PlayerId = %s;" % (
                        self.Serverid, del_pid)
                ]
            B = Build_DB(self.mysql, SQL_del_all_FB)
            B.Connection_DB()
            B.execuse_more_SQL()
            B.close_DB()
            C = Clean(self.ServerId, self.Serverid)
            C.Clean_data()
            print(del_pid, "副本已重置全部章节")
            print()
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()
        except Exception:
            print()
            print("重置副本失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def reset_some_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("重置副本指定章节\t(输入'q'返回)")
            del_pid = input("playerId：")
            if del_pid == "q" or del_pid == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                choose = input("删除章节：")
                if choose == "q" or choose == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    SQL_del_some_FB = [
                        "DELETE FROM `server%s`.`tb_player_instance` "
                        "WHERE PlayerId = %s AND InstanceId = %s;" % (self.Serverid, del_pid, choose),
                        "DELETE FROM `server%s`.`tb_player_instance_chamber_reward` "
                        "WHERE PlayerId = %s AND InstanceId = %s;" % (self.Serverid, del_pid, choose),
                        "DELETE FROM `server%s`.`tb_player_instance_data` "
                        "WHERE PlayerId = %s AND InstanceId = %s;" % (self.Serverid, del_pid, choose),
                        "DELETE FROM `server%s`.`tb_player_instance_event_reward` "
                        "WHERE PlayerId = %s AND InstanceId =  %s;" % (self.Serverid, del_pid, choose),
                        "DELETE FROM `server%s`.`tb_player_instance_plot_reward` "
                        "WHERE PlayerId = %s AND InstanceId = %s;" % (self.Serverid, del_pid, choose),
                        "DELETE FROM `server%s`.`tb_player_instance_other_reward` "
                        "WHERE PlayerId = %s AND InstanceId = %s;" % (self.Serverid, del_pid, choose)
                    ]
                    B = Build_DB(self.mysql, SQL_del_some_FB)
                    B.Connection_DB()
                    B.execuse_more_SQL()
                    B.close_DB()
                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print(del_pid, "第", choose, "章副本已重置")
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
        except Exception:
            print()
            print("重置章节失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()

    def add_FB(self):
        try:
            # if self.ServerId == '3' and self.Serverid == '1':
            #     self.Serverid = ''
            print("完成到副本x章\t(输入'q'返回)")
            add_pid = input("playerId：")
            if add_pid == "q" or add_pid == "Q":
                S = Select_Server(self.ServerId, self.Serverid)
                S.Select_server()
            else:
                add_time = int(input("章节："))
                if add_time == "q" or add_time == "Q":
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()
                else:
                    # SQL_del__all_FB = "DELETE FROM `server%s`.`tb_player_instance` WHERE PlayerId = %s;" \
                    #                   % (self.Serverid, add_pid)
                    # B = Build_DB(self.mysql, SQL_del__all_FB)
                    # B.Connection_DB()
                    # B.execuse_one_SQL()
                    # B.close_DB()

                    SQL_All_FB = []
                    for x in range(add_time):
                        add_times = x + 1
                        SQL_add_FB = "REPLACE INTO " \
                                     "`server%s`.`tb_player_instance` (PlayerId, InstanceId, InstanceProgress, InstanceState, " \
                                     "CurrentState, EnterTime, QuitTime, FinishTime, CreateTime, UpdateTime) " \
                                     "VALUES " \
                                     "(%s, %s, 100, 1, 1, 1620180000, 1620180000, 1620180000, 1620180000, 1620180000)" \
                                     % (self.Serverid, add_pid, add_times)
                        SQL_All_FB.append(SQL_add_FB)
                        # print(SQL_All_FB)
                    B = Build_DB(self.mysql, SQL_All_FB)
                    B.Connection_DB()
                    B.execuse_more_SQL()
                    B.close_DB()
                    C = Clean(self.ServerId, self.Serverid)
                    C.Clean_data()
                    print(add_pid, "已完成到第", add_time, "章节")
                    print("请重登两次游戏~，请重登两次游戏~ ~ ~")
                    print()
                    S = Select_Server(self.ServerId, self.Serverid)
                    S.Select_server()

        except Exception:
            print()
            print("完成章节失败,请联系管理员~\n")
            S = Select_Server(self.ServerId, self.Serverid)
            S.Select_server()


def SearchServer():
    ServerName = input("想查哪个服？")
    if ServerName == "Q" or ServerName == "q":
        Build_message()
    else:
        try:
            SQL_search_server = "SELECT ServerId,ServerName FROM `global`.`tb_data_server` WHERE ServerName REGEXP '%s';" % (
                ServerName)
            # 连接database
            cDB = pymysql.connect(host='43.131.66.43', port=20006, user='dev', password='wjkjdev@2016')
            # 得到一个可以执行SQL语句的光标对象
            cursor = cDB.cursor()
            cursor.execute(SQL_search_server)
            # print(data)
            result = cursor.fetchall()
            print("ServerId", "ServerName")
            for data in result:
                ServerId = data[0]
                ServerName = data[1]
                print("  ", ServerId, "\t  ", ServerName)
        except:
            print("连不上总服")


def SearchGroup():
    ServerName = input("想查哪个服？")
    if ServerName == "Q" or ServerName == "q":
        Build_message()
    else:
        try:
            SQL_search_server = "SELECT ServerId,ServerName FROM `global`.`tb_data_server` WHERE ServerName REGEXP '%s';" % (
                ServerName)
            # 连接database
            cDB = pymysql.connect(host='43.131.66.43', port=20006, user='dev', password='wjkjdev@2016')
            # 得到一个可以执行SQL语句的光标对象
            cursor = cDB.cursor()
            cursor.execute(SQL_search_server)
            # print(data)
        except:
            print("连不上总服")

        result = cursor.fetchall()
        # print("ServerId", "ServerName")
        for data in result:
            ServerId = data[0]
            servername = data[1]
            # print("  ", ServerId, "\t  ", LastName)

        # print("  ", ServerId, "\t  ", servername)
        LastName = str(ServerId)
        global  GroupName
        if ServerName[0] == "M" or ServerName[0] == "m":
            GroupName = '100' + LastName
        elif ServerName[0] == "K" or ServerName[0] == "k":
            if len('200' + LastName) == 6:
                GroupName = '200' + LastName
            else:
                GroupName = '2000' + LastName
        else:
            FirstName = ''
            GroupName = LastName

        print("数据库号:", GroupName)

        Sql_search_group = "SELECT * FROM `server%s`.`tb_option_public`;" % (GroupName)
        cDB.commit()
        cursor.close()
        cDB.close()

        try:
            # efun正式服（群组1）
            cDB = pymysql.connect(host='43.131.66.43', port=20117, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群1")
            Build_message()
        except:
            # print("不在群1")
            pass

        try:
            # 群组2-1
            cDB = pymysql.connect(host='43.131.66.43', port=20217, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组2-1")
            Build_message()
        except:
            # print("不在群组2-1")
            pass

        try:
            # 群组2-2
            cDB = pymysql.connect(host='43.131.66.43', port=20227, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组2-2")
            Build_message()
        except:
            # print("不在群组2-2")
            pass

        try:
            # 群组3-1
            cDB = pymysql.connect(host='43.131.66.43', port=20317, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组3-1")
        except:
            # print("不在群组3-1")
            pass

        try:
            # 群组3-2
            cDB = pymysql.connect(host='43.131.66.43', port=20327, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组3-2")
            Build_message()
        except:
            # print("不在群组3-2")
            pass

        try:
            # 群组4-1
            cDB = pymysql.connect(host='43.131.66.43', port=20417, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组4-1")
            Build_message()
        except:
            # print("不在群组4-1")
            pass

        try:
            # 群组4-2
            cDB = pymysql.connect(host='43.131.66.43', port=20427, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组4-2")
            Build_message()
        except:
            # print("不在群组4-2")
            pass

        try:
            # 群组998
            cDB = pymysql.connect(host='159.138.4.50', port=3307, user='dev', password='wjkjdev@2016')
            cursor = cDB.cursor()
            cursor.execute(Sql_search_group)
            cDB.commit()
            cursor.close()
            cDB.close()
            print("在群组998")
            Build_message()
        except:
            # print("不在群组4-2")
            pass

class Build_DB:
    def __init__(self, mysql, Sql):
        self.host = mysql[0]
        self.port = mysql[1]
        self.user = mysql[2]
        self.password = mysql[3]
        self.Sql = Sql

    def Connection_DB(self):
        self.start_time = time.time()
        try:
            self.cDB = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
            )
            self.cursor = self.cDB.cursor()
        except Exception:
            print("连接数据库失败")

    def execuse_more_SQL(self):
        try:
            for sql in self.Sql:
                print(sql)
                # print(self.cursor.execute(sql))
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                for data in result:
                    print(data)
        except Exception:
            print("执行SQL失败")

    def execuse_one_SQL(self):
        # print("execuse_one_SQL 进来了")
        try:
            print(self.Sql, "\n")
            self.cursor.execute(self.Sql)
            # print("执行结果完成。")
            result = self.cursor.fetchall()
            for data in result:
                print(data)
        except Exception:
            print("执行SQL失败")

    def execuse_return_SQL_(self):
        # print("execuse_one_SQL 进来了")
        try:
            print(self.Sql, "\n")
            self.cursor.execute(self.Sql)
            result = self.cursor.fetchall()
            for data in result:
                return data[0]
        except Exception:
            print("执行SQL失败")

    def execuse_one_SQL_exch(self):
        # print("execuse_one_SQL 进来了")
        try:
            print(self.Sql)
            self.cursor.execute(self.Sql)
            result = self.cursor.fetchall()
            for data in result:
                print("NicaName:", data[0], "playerid:", data[1], "useid", data[2])
        except Exception:
            print("执行SQL失败")

    #   查efun分服Id
    def efun_search_serverid_sql(self):
        try:
            # print(self.Sql)
            self.cursor.execute(self.Sql)
            result = self.cursor.fetchone()
            for data in result:
                print("当前分服Id: " + str(data))
        except Exception:
            print("执行SQL失败")

    # 查UserId
    def execuse_useid_SQL(self):
        try:
            print(self.Sql)
            self.cursor.execute(self.Sql)
            result = self.cursor.fetchone()
            for data in result:
                print("UseId: " + str(data))
        except Exception:
            print("执行SQL失败")

    # 查UserName
    def execuse_UserName_SQL(self):
        try:
            print(self.Sql)
            self.cursor.execute(self.Sql)
            result = self.cursor.fetchone()
            for data in result:
                print("账号 " + str(data))
        except Exception:
            pass

    def close_DB(self):
        try:
            self.cDB.commit()
            self.cursor.close()
            self.cDB.close()
            end_time = time.time()
            print("数据库耗时：" + str(end_time - self.start_time))
        except Exception:
            pass


# 充值
class buy_Rechaerge:
    def __init__(self, ServerId, Serverid):
        self.ServerId = ServerId
        self.Serverid = Serverid

    def buy_recharge(self):
        start_time = time.time()
        try:
            if self.ServerId == "01":
                s = "t1"
                recc = self.Serverid
                # print("T1不支持充值\n")
                # S = Select_Server(self.ServerId, self.Serverid)
                # S.Select_server()
            elif self.ServerId == "0":
                s = "goat3307"
                recc = self.Serverid
            elif self.ServerId == "7":
                s = "t22"
                recc = self.Serverid
            elif self.ServerId == "999":
                s = "999"
                recc = "999"
            elif self.ServerId == "9999":
                s = "999"
                recc = "9999"
            elif self.ServerId == "10000":
                s = "999"
                recc = "10000"
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                s = "t" + self.ServerId
                recc = self.Serverid

            Buy = address_buy + s + parameter_buy + recc
            requests.get(Buy)
            print(Buy)
            end_time = time.time()
            print("购买成功~\t耗时：" + str(end_time - start_time))
        except Exception:
            print("购买失败，请联系管理员~\n")
        S = Select_Server(self.ServerId, self.Serverid)
        S.Select_server()


# 高图测试服周循环初始化失败后，手动执行这脚本
def goat_Cycle_initialization():
    print(goat_c_i)
    result = requests.get(goat_c_i)
    print("高图测试服周循环初始化~")
    # print(result.text)


# 清缓存
class Clean:
    def __init__(self, ServerId, Serverid):
        self.ServerId = ServerId
        self.Serverid = Serverid

    # 全球赛事奖励
    def global_match(self):
        start_time = time.time()
        try:
            if self.ServerId == "0":
                a = address["address_goat"] + self.Serverid
            elif self.ServerId == "7":
                a = address["address_t7"] + self.Serverid

            elif self.ServerId == "999":
                a = address["address_efun999"]
            elif self.ServerId == "9999":
                a = address["address_efun9999"]
            elif self.ServerId == "10000":
                a = address["address_efun10000"]
            elif self.ServerId == "01":
                a = address["address_t" + self.ServerId[-1]] + self.Serverid
            elif self.ServerId == "21" or self.ServerId == "22" or self.ServerId == "23":
                a = address["address_nw" + self.ServerId[-1]] + self.Serverid
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                a = address["address_t" + self.ServerId] + self.Serverid
            math_php = a + global_match
            print(math_php)
            result = requests.get(math_php)
            end_time = time.time()
            # print(result.text + "py耗时：" + str(end_time - start_time))
            ok = "每1小时判断是否发送全球邮件排名奖励"
            if result.text[0] in ok:
                print("全球邮件排名奖励执行成功\t耗时：" + str(end_time - start_time) + "\n")
            else:
                print("全球邮件排名奖励执行失败！！！！！！！\t耗时：" + str(end_time - start_time) + "\n")
        except Exception:
            print("全球邮件排名奖励执行失败\n")

    # 刷新魔眼状态
    def Clean_eye(self):
        start_time = time.time()
        try:
            if self.ServerId == "0":
                a = address["address_goat"] + self.Serverid
            elif self.ServerId == "7":
                a = address["address_t7"] + self.Serverid

            elif self.ServerId == "999":
                a = address["address_efun999"]
            elif self.ServerId == "9999":
                a = address["address_efun9999"]
            elif self.ServerId == "10000":
                a = address["address_efun10000"]
            elif self.ServerId == "01":
                a = address["address_t" + self.ServerId[-1]] + self.Serverid
            elif self.ServerId == "21" or self.ServerId == "22" or self.ServerId == "23":
                a = address["address_nw" + self.ServerId[-1]] + self.Serverid
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                a = address["address_t" + self.ServerId] + self.Serverid
            r_refreshe_eye = a + refreshe_eye
            print(r_refreshe_eye)
            result = requests.get(r_refreshe_eye)
            end_time = time.time()
            # print(result.text + "py耗时：" + str(end_time - start_time))
            ok = "每10分钟检测魔眼状态"
            if result.text[0] in ok:
                print("魔眼刷新成功\t耗时：" + str(end_time - start_time) + "\n")
            else:
                print("魔眼刷新失败！！！！！！！\t耗时：" + str(end_time - start_time) + "\n")

        except Exception:
            print("魔眼状态刷新失败\n")

    # 清数据缓存
    def Clean_data(self):
        start_time = time.time()
        try:
            if self.ServerId == "0":
                a = address["address_goat"] + self.Serverid
                b = address["address_goat"] + self.Serverid
                c_clean_data = b[:-5] + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                # c_clean_data = b[:-3] + "951" + clean_data
                # print(c_clean_data)
                # result = requests.get(c_clean_data)

            elif self.ServerId == "01":
                a = address["address_t" + self.ServerId[-1]] + self.Serverid
                b = address["address_t" + self.ServerId[-1]]
                c_clean_data = b[:-1] + "00" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                c_clean_data = b[:-2] + "951" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)

            elif self.ServerId == "4" or self.ServerId == "6":
                a = address["address_t" + self.ServerId] + self.Serverid
                b = address["address_t" + self.ServerId]

                c_clean_data = b[:-1] + "00" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                c_clean_data = b[:-2] + "951" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)

            elif self.ServerId == "21" or self.ServerId == "22" or self.ServerId == "23":
                a = address["address_nw" + self.ServerId[1:]] + self.Serverid
                b = address["address_nw" + self.ServerId[1:]]

                c_clean_data = b[:-2] + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                # c_clean_data = b + "951" + clean_data
                # print(c_clean_data)
                # result = requests.get(c_clean_data)


            elif self.ServerId == "5":
                a = address["address_t" + self.ServerId] + self.Serverid
                b = address["address_t" + self.ServerId]
                c_clean_data = b[:-4] + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)

            elif self.ServerId == "7":
                a = address["address_t7"] + self.Serverid
                b = address["address_t" + self.ServerId]
                c_clean_data = b[:-2] + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                c_clean_data = b + "951" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)

            elif self.ServerId == "999":
                a = address["address_efun999"]
            elif self.ServerId == "9999":
                a = address["address_efun9999"]
            elif self.ServerId == "10000":
                a = address["address_efun10000"]
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                a = address["address_t" + self.ServerId] + self.Serverid
                # b = address["address_t" + self.ServerId] + "0"
                b = address["address_t" + self.ServerId]
                c_clean_data = b[:-2] + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)
                c_clean_data = b + "951" + clean_data
                print(c_clean_data)
                result = requests.get(c_clean_data)

            c_clean_data = a + clean_data
            print(c_clean_data)
            result = requests.get(c_clean_data)

            end_time = time.time()
            # print(result.text + "耗时：" + str(end_time - start_time) + "\n")
            ok = "每日5时清空一下Memcache数据"
            if result.text[0] in ok:
                print("清除数据缓存成功\t耗时：" + str(end_time - start_time) + "\n")
            else:
                print("清除数据缓存失败\t耗时：" + str(end_time - start_time) + "\n")
        except Exception:
            print("清数据缓存失败\n")

    # 清失败日志log
    def Clean_log(self):
        start_time = time.time()
        try:
            if self.ServerId == "0":
                a = address["address_goat"] + self.Serverid
            elif self.ServerId == "7":
                a = address["address_t7"] + self.Serverid
            elif self.ServerId == "999":
                a = address["address_efun999"]
            elif self.ServerId == "9999":
                a = address["address_efun9999"]
            elif self.ServerId == "10000":
                a = address["address_efun10000"]
            elif self.ServerId == "01":
                a = address["address_t" + self.ServerId[-1]] + self.Serverid
            elif self.ServerId == "21" or self.ServerId == "22" or self.ServerId == "23":
                a = address["address_nw" + self.ServerId[-1]] + self.Serverid
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                a = address["address_t" + self.ServerId] + self.Serverid
            c_clean_data_log = a + clean_data_log
            print("清日志缓存：", c_clean_data_log)
            result = requests.get(c_clean_data_log)
            end_time = time.time()
        except Exception:
            print("清日志缓存失败\n")

    # 清配置缓存
    def Clean_config(self):
        start_time = time.time()
        try:
            if self.ServerId == "0":
                a = address["address_goat"] + self.Serverid
                b = address["address_goat"]
                # print(a)
                # print(b[:-4])
                c_clean_config = b[:-4] + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)

            elif self.ServerId == "01":
                a = address["address_t" + self.ServerId[-1]] + self.Serverid
                b = address["address_t" + self.ServerId[-1]]
                c_clean_config = b[:-1] + "00" + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)
                c_clean_config = b[:-2] + "951" + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)

            elif self.ServerId == "21" or self.ServerId == "22" or self.ServerId == "23":
                a = address["address_nw" + self.ServerId[1:]] + self.Serverid
                b = address["address_nw" + self.ServerId[1:]]

                c_clean_config = b[:-2] + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)
                # c_clean_config = b + "951" +clean_config
                # print(c_clean_config)
                # result = requests.get(c_clean_config)


            elif self.ServerId == "4" or self.ServerId == "6":
                a = address["address_t" + self.ServerId] + self.Serverid
                b = address["address_t" + self.ServerId]
                c_clean_config = b[:-1] + "00" + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)
                c_clean_config = b[:-2] + "951" + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)


            elif self.ServerId == "5":
                a = address["address_t" + self.ServerId] + self.Serverid
                b = address["address_t" + self.ServerId]
                # print(a)
                # print(b[:-4])
                c_clean_config = b[:-4] + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)
            elif self.ServerId == "7":
                a = address["address_t7"] + self.Serverid
                b = address["address_t" + self.ServerId]
                c_clean_config = b[:-2] + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)

            elif self.ServerId == "999":
                a = address["address_efun999"]
            elif self.ServerId == "9999":
                a = address["address_efun9999"]
            elif self.ServerId == "10000":
                a = address["address_efun10000"]
            else:
                if self.ServerId == "3" and self.Serverid == "":
                    self.Serverid = "1"
                a = address["address_t" + self.ServerId] + self.Serverid
                b = address["address_t" + self.ServerId]
                c_clean_config = b[:-2] + clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)
                c_clean_config = b + "951" +clean_config
                print(c_clean_config)
                result = requests.get(c_clean_config)

            c_clean_config = a + clean_config
            print(c_clean_config)
            result = requests.get(c_clean_config)
            end_time = time.time()
            # print(result.text + "\t耗时：" + str(end_time - start_time) + "\n")
            ok = "更新结束"
            if result.text in ok:
                print("清除配置缓存成功\t耗时：" + str(end_time - start_time) + "\n")
            else:
                print("清除配置缓存失败\t耗时：" + str(end_time - start_time) + "\n")
        except Exception:
            print("清配置缓存失败\n")


# selenium
def jenkins_clean_data():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("j_username").send_keys('yeyongning')
    driver.find_element_by_name("j_password").send_keys("allyyn067")
    driver.find_element_by_id("yui-gen1-button").click()
    driver.find_element_by_link_text("EFUN测试服").click()
    driver.find_element_by_xpath(
        "//a[@href='job/test-servermanage-EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/']").click()
    driver.find_element_by_xpath(
        "//a[@href='/view/EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D/job/test-servermanage-EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/build?delay=0sec']").click()
    driver.find_element_by_xpath("//body[@id='jenkins']").send_keys(Keys.F5)
    Build_message()

def jenkins_clean_data_nw1():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("j_username").send_keys('yeyongning')
    driver.find_element_by_name("j_password").send_keys("allyyn067")
    driver.find_element_by_id("yui-gen1-button").click()
    driver.find_element_by_link_text("内网测试机1").click()
    driver.find_element_by_xpath(
        "//a[@href='job/test-servermanage-local1-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/']").click()
    driver.find_element_by_xpath(
        "//a[@href='/view/%E5%86%85%E7%BD%91%E6%B5%8B%E8%AF%95%E6%9C%BA1/job/test-servermanage-local1-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/build?delay=0sec']").click()
    driver.find_element_by_xpath("//body[@id='jenkins']").send_keys(Keys.F5)

def jenkins_clean_data_nw2():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("j_username").send_keys('yeyongning')
    driver.find_element_by_name("j_password").send_keys("allyyn067")
    driver.find_element_by_id("yui-gen1-button").click()
    driver.find_element_by_link_text("内网测试机2").click()
    driver.find_element_by_xpath(
        "//a[@href='job/test-servermanage-local2-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/']").click()
    driver.find_element_by_xpath(
        "//a[@href='/view/%E5%86%85%E7%BD%91%E6%B5%8B%E8%AF%95%E6%9C%BA2/job/test-servermanage-local2-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/build?delay=0sec']").click()
    driver.find_element_by_xpath("//body[@id='jenkins']").send_keys(Keys.F5)

def jenkins_clean_data_nw3():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("j_username").send_keys('yeyongning')
    driver.find_element_by_name("j_password").send_keys("allyyn067")
    driver.find_element_by_id("yui-gen1-button").click()
    driver.find_element_by_link_text("内网测试机3").click()
    driver.find_element_by_xpath(
        "//a[@href='job/test-servermanage-local3-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/']").click()
    driver.find_element_by_xpath(
        "//a[@href='/view/%E5%86%85%E7%BD%91%E6%B5%8B%E8%AF%95%E6%9C%BA3/job/test-servermanage-local3-%E6%B8%85%E7%90%86%E7%8E%A9%E5%AE%B6%E6%95%B0%E6%8D%AE%E7%BC%93%E5%AD%98-%E5%BC%BA%E5%88%B6%E6%A8%A1%E5%BC%8F/build?delay=0sec']").click()
    driver.find_element_by_xpath("//body[@id='jenkins']").send_keys(Keys.F5)

def select_function():
    print()
    fun = input(
        "1：提bug  12：查需求  13：查内网bug单\n14.查分服多应数据库号\t15.查群组\n11：查看外网bug\n21更T2 1服  22更T2全服  31、32、41、42...\n9999、10000拉数据\n请选择:")
    if fun == "0" or fun == "q" or fun == "Q":
        Build_message()

    elif fun == '999' or fun == '9999' or fun == '10000':
        key = input("key:")
        print()
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId1(fun, key, driver)
        S.select_server()

        Build_message()

    elif fun == '1':
        # 提bug
        driver = webdriver.Chrome()
        driver.get(url2)
        driver.maximize_window()
        driver.find_element_by_id("account").send_keys('yeyongning')
        driver.find_element_by_name("password").send_keys("@123456")
        driver.find_element_by_id("submit").click()

        C = changDao(driver)
        C.putBug()

        Build_message()

    elif fun == '11':
        # 查看外网bug

        driver = webdriver.Chrome()
        driver.get(url3)
        driver.maximize_window()
        driver.find_element_by_id("account").send_keys('yeyongning')
        driver.find_element_by_name("password").send_keys("@123456")
        driver.find_element_by_id("submit").click()

        C = changDao(driver)
        C.search_Waiwang_Bug()

        Build_message()

    elif fun == '12':
        # 查任务

        driver = webdriver.Chrome()
        driver.get(url2)
        driver.maximize_window()
        driver.find_element_by_id("account").send_keys('yeyongning')
        driver.find_element_by_name("password").send_keys("@123456")
        driver.find_element_by_id("submit").click()

        C = changDao(driver)
        C.search_task()

        Build_message()

    elif fun == '13':
        # 查bug

        driver = webdriver.Chrome()
        driver.get(url2)
        driver.maximize_window()
        driver.find_element_by_id("account").send_keys('yeyongning')
        driver.find_element_by_name("password").send_keys("@123456")
        driver.find_element_by_id("submit").click()

        C = changDao(driver)
        C.search_Bug()

        Build_message()

    elif fun == '14':
        # 查分服号
        SearchServer()
        Build_message()

    elif fun == '15':
        # 查看在哪个群组
        SearchGroup()
        Build_message()


    elif fun == '21':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()


    elif fun == '22':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()

    elif fun == '31':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()

    elif fun == '32':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

    elif fun == '41':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()

    elif fun == '42':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()

    elif fun == '51':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()

    elif fun == '52':
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('yeyongning')
        driver.find_element_by_name("j_password").send_keys("allyyn067")
        driver.find_element_by_id("yui-gen1-button").click()

        S = select_ServerId2(fun, driver)
        S.select_server()

        Build_message()
    else:
        select_function()


# 禅道
class changDao():
    def __init__(self, driver):
        self.driver = driver

    def putBug(self):
        sleep(0.3)
        self.driver.find_element_by_link_text('测试').click()
        sleep(0.3)
        self.driver.find_elements_by_link_text('Bug')[1].click()
        sleep(0.3)

        self.driver.find_element_by_link_text("提Bug").click()

        # 选择项目
        self.driver.find_element_by_xpath("//a[@class='chosen-single chosen-default']").click()
        sleep(0.3)
        self.driver.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']").click()
        # sleep(0.15)
        sleep(0.3)

        Build_message()

        # self.driver.find_element_by_xpath(
        #     "//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']//li[@class='active-result']").click()
        # self.driver.find_element_by_xpath("//input[@id='title']").click()

    def search_task(self):
        sleep(0.3)
        self.driver.find_elements_by_xpath("//div[@class='tile-amount']//a")[0].click()

        Build_message()

    def search_Bug(self):
        sleep(1)
        self.driver.find_element_by_xpath("//a[@href='/index.php?m=my&f=bug']").click()

        Build_message()

    def search_Waiwang_Bug(self):
        sleep(0.3)
        self.driver.find_element_by_xpath("//a[@href='/index.php?m=my&f=bug']").click()

        Build_message()


# Jenkens
class select_ServerId1():
    def __init__(self, fun, key, driver):
        self.fun = fun
        self.key = key
        self.driver = driver

    def select_server(self):
        if self.fun == '9999':
            # 选择 efun测试服
            self.driver.find_element_by_link_text("EFUN测试服").click()
            # 进入9999
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-servermanage-EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D-%E6%95%B0%E6%8D%AE%E6%8B%89%E5%8F%96-9999%E6%9C%8D/']").click()
            self.driver.find_element_by_link_text("Build with Parameters").click()
            sleep(0.3)
            self.driver.find_element_by_xpath("//input[@name='value']").send_keys(self.key)
            sleep(0.3)
            self.driver.find_element_by_id("yui-gen1-button").click()

            Build_message()

        elif self.fun == '999':
            # 选择 efun测试服
            self.driver.find_element_by_link_text("EFUN测试服").click()
            # 进入999
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-servermanage-EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D-%E6%95%B0%E6%8D%AE%E6%8B%89%E5%8F%96-999%E6%9C%8D/']").click()
            self.driver.find_element_by_link_text("Build with Parameters").click()
            sleep(0.3)
            self.driver.find_element_by_xpath("//input[@name='value']").send_keys(self.key)
            sleep(0.3)
            self.driver.find_element_by_id("yui-gen1-button").click()

            Build_message()

        elif self.fun == '10000':
            # 选择 efun测试服
            self.driver.find_element_by_link_text("EFUN测试服").click()
            # 进入10000
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-servermanage-EFUN%E6%B5%8B%E8%AF%95%E6%9C%8D-%E6%95%B0%E6%8D%AE%E6%8B%89%E5%8F%96-10000%E6%9C%8D/']").click()
            self.driver.find_element_by_link_text("Build with Parameters").click()
            sleep(0.3)
            self.driver.find_element_by_xpath("//input[@name='value']").send_keys(self.key)
            sleep(0.3)
            self.driver.find_element_by_id("yui-gen1-button").click()

            Build_message()


class select_ServerId2():
    def __init__(self, fun, driver):
        self.fun = fun
        self.driver = driver

    def select_server(self):
        if self.fun == '21':
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T2-%E6%9B%B4%E6%96%B01%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '22':
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T2-%E6%9B%B4%E6%96%B0%E6%89%80%E6%9C%89%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '31':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T3/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T3-%E6%9B%B4%E6%96%B01%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '32':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T3/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T3-%E6%9B%B4%E6%96%B0%E6%89%80%E6%9C%89%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '41':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T4/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T4-%E6%9B%B4%E6%96%B01%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '42':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T4/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T4-%E6%9B%B4%E6%96%B0%E6%89%80%E6%9C%89%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '51':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T5/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T5-%E6%9B%B4%E6%96%B01%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()

        elif self.fun == '52':
            self.driver.find_element_by_xpath(
                "//a[@href='/view/T5/']").click()
            self.driver.find_element_by_xpath(
                "//a[@href='job/test-config-T5-%E6%9B%B4%E6%96%B0%E6%89%80%E6%9C%89%E6%9C%8D-%E7%AD%96%E5%88%92%E9%85%8D%E7%BD%AE/']").click()
            # sleep()
            self.driver.find_element_by_link_text("立即构建").click()

            Build_message()


if __name__ == "__main__":

    i = time.time()
    # print(i)