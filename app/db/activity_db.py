#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class ActivityCommand():
    #读取activity信息传回界面
    def readActivity(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT * FROM ACTIVITY"""
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results