#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class Administration():
    #读取administrator信息传回界面
    def readAdministrator(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql="""SELECT * FROM ADMINISTRATION"""
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results


    #更改或增加administrator信息
    def modifyAdministrator(self,adNo,psw,dept):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM ADMINISTRATION WHERE adNo = '%s'"""%(adNo)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO ADMINISTRATION(ADNO,psw,DEPT) VALUES ('%s','%s','%s')"""%(adNo,psw,dept)
                cursor.execute(sql)
            else:
                sql = """UPDATE ADMINISTRATION SET psw='%s',DEPT='%s' WHERE ADNO='%s'""" % (psw,dept,adNo)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results
