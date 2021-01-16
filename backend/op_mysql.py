import pymysql

import datetime
import time
import copy


class OPMYSQL():
    def __init__(self):

        # 初始化连接对象
        # 打开数据库连接
        self.db = pymysql.connect("localhost", "root", "123456", "xb_ops")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def insertTask(self, dataDict):
        if dataDict:
            try:
                keyname = ""
                value = ""
                dateTime = dataDict.pop("dateTime")
                beginTime = time.mktime(time.strptime(
                    dateTime[0].split(".")[0], "%Y-%m-%dT%H:%M:%S"))
                endTime = time.mktime(time.strptime(
                    dateTime[1].split(".")[0], "%Y-%m-%dT%H:%M:%S"))
                for k, v in dataDict.items():
                    keyname += k+","
                    value += "\""+v+"\""+","
                keyname = keyname.rstrip(",")
                value = value.rstrip(",")
                insertSql = "insert into todolist(%s,begintime,endtime) values(%s,%s,%s)" % (
                    keyname, value, beginTime, endTime)
                print(insertSql)
                self.cursor.execute(insertSql)
                self.db.commit()
                return "sucess"
            except Exception as e:
                print("error")
                return "failed"
            finally:
                self.db.close()

        if not dataDict:
            self.db.close()
            return "null form"

    def selectTask(self, status):
        if status:
            try:
                selectSql = "select * from todolist where status=%s;" % (
                    status)
                print(selectSql)
                self.cursor.execute(selectSql)
                data = self.cursor.fetchall()
                descSql = "desc todolist;"
                self.cursor.execute(descSql)
                structure = self.cursor.fetchall()
                col_list = [i[0] for i in structure]
                length = len(col_list)
                new_list = []
                for one in data:
                    one_dict = {}
                    for i in range(length):
                        one_dict.update({col_list[i]: one[i]})
                    copy_dict = copy.copy(one_dict)
                    new_list.append(copy_dict)
                return new_list

            except Exception as e:
                pass
            finally:
                pass

        if not status:
            self.db.close()
            return "null level"

    def pre2Doing(self):
        nowstrap = int(time.time())

        try:
            selectSql = "select id from todolist where begintime<=%s and status=1;" % (
                nowstrap)
            self.cursor.execute(selectSql)
            data = self.cursor.fetchall()

            for one in data:
                updateSql = "update todolist set status=2 where id=%s;" % (
                    one[0])
                self.cursor.execute(updateSql)
                self.db.commit()
        except Exception as e:
            print(e)
        finally:
            self.db.close()

    def doing2Done(self, taskID):
        if taskID:
            try:
                updateSql = "update todolist set status=3 where id=%s;" % (
                    taskID)
                self.cursor.execute(updateSql)
                self.db.commit()
            except Exception as e:
                print(e)
            finally:
                self.db.close()
