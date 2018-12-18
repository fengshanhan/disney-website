#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class RoomCommand():
    #读出当前酒店的房间信息（hname,rno,isEmpty,rprice）,根据rprice分类   对Room table的操作
    def readRoom(self,hname):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        isempty='1'
        print(hname)
        print(isempty)
        sql = """SELECT COUNT(*),RPRICE FROM ROOM WHERE HNAME='%s'AND ISEMPTY='%s' GROUP BY RPRICE""" %(hname,isempty)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                emptynumber=result[1]
                rprice=result[0]
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results