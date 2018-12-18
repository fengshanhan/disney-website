#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class BusCommand():
    #读取Bus信息传回界面
    def readBus(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM BUS"""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results

    #更改或增加bus信息
    def modifyBus(self,bno,bStart,bEnd,sDest,eDest,totalSeat):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM BUS WHERE bno = '%s'"""%(bno)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO BUS(bno,bStart,bEnd,sDest,eDest,totalSeat) VALUES ('%s','%s','%s','%s','%s','%d')"""%(bno,bStart,bEnd,sDest,eDest,int(totalSeat))
                cursor.execute(sql)
            else:
                sql = """UPDATE BUS SET bStart='%s',bEnd='%s',sDest='%s',eDest='%s',totalSeat='%d' WHERE bno='%s'""" % (bStart,bEnd,sDest,eDest,int(totalSeat),bno)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results