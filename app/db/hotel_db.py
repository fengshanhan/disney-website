#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class HotelCommand():
    #读取hotel信息传回界面
    def readHotel(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
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
