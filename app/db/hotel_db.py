#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class HotelCommand():
    #读取hotel信息传回界面
    def readHotel(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql="""SELECT * FROM HOTEL"""
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for result in results:
                hname=result[0]
                haddr=result[1]
                rnum=result[2]
                htele=result[3]
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results

    #更改或增加hotel信息
    def modifyHotel(self,hname,haddr,rNum,htele):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM HOTEL WHERE hname = '%s'"""%(hname)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO Hotel(HNAME,HADDR,RNUM,HTELE) VALUES ('%s','%s','%d','%s')"""%(hname,haddr,int(rNum),htele)
                cursor.execute(sql)
            else:
                sql = """UPDATE HOTEL SET HADDR='%s',RNUM='%d',HTELE='%s' WHERE HNAME='%s'""" % (haddr,int(rNum),htele,hname)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results