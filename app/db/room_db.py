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

    #更改或增加Room信息
    def modifyRoom(self,hname,rno,rprice):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """SELECT * FROM ROOM WHERE hname = '%s' and rno = '%s'"""%(hname,rno)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO ROOM(HNAME,RNO,RPRICE) VALUES ('%s','%s','%d')"""%(hname,rno,int(rprice))
                cursor.execute(sql)
            else:
                sql = """UPDATE ROOM SET RPRICE='%d' WHERE hname = '%s' and rno = '%s'""" % (int(rprice),hname,rno)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results