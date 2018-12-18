#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class Administration():
    #读取administrator信息传回界面
    def readAdministrator(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT * FROM AADMINISTRATION"""
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
    def modifyAdministrator(self,adNo,password,dept):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """SELECT * FROM ACTIVITY WHERE adNo = '%s'"""%(adNo)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO ACTIVITY(ADNO,PASSWORD,DEPT) VALUES ('%s','%s','%s','%s')"""%(adNo,password,dept)
                cursor.execute(sql)
            else:
                sql = """UPDATE ACTIVITY SET PASSWORD='%s',DEPT='%s' WHERE ADNO='%s'""" % (password,dept,adNo)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results
