#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class VisitorCommand():
    #插入游客，和注册相对应
    def insertVisitor(self,id,name,tel,isVIP,wallet,password):
        #open database
        db=pymysql.connect("localhost","root","rewq66505441-","dbwebsite")
        cursor=db.cursor()
        sql="""INSERT INTO VISITOR (VNO,VNAME,TELNO,ISVIP,WALLET,PSW) VALUES ('%s','%s','%s','%s','%d','%s')"""%(id,name,tel,isVIP,wallet,password)
        #print("插入"+name+id)
        try:
            cursor.execute(sql)
            print("插入成功")
            db.commit()
            return 1
        except:
            print("不能插入")
            db.rollback()

        cursor.close()

    #查询，和登陆相对应
    def readVisitor(self,name,password):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql="""SELECT * FROM VISITOR WHERE VNAME= '%s' and PSW= '%s'"""%(name,password)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            n=cursor.rownumber
            print("rownumber>>>>>")
            print(n)
            if n == 0:
                return 0
            return 1
        except:
            import traceback
            print("呜呜呜呜呜呜呜呜呜呜呜")
            traceback.print_exc()

        cursor.close()

    #查询表内总的用户数
    def readVisitorNum(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM VISITOR"""
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            n=cursor.rownumber
        except:
            import traceback
            print("呜呜呜呜呜呜呜呜呜呜呜")
            traceback.print_exc()
        cursor.close()
        return n

    #查询，和获取当前用户账号相对应
    def read_for_no(self,vname):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT VNO FROM VISITOR WHERE VNAME= '%s'""" %vname
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                no=result[0]
                return no
        except:
            import traceback
            traceback.print_exc()

        cursor.close()


class AdministratorCommand():
    #查询，和登陆相对应
    def readAdministrator(self,name,password):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql="""SELECT * FROM ADMINISTRATOR WHERE adNo= '%s' and psw= '%s'"""%(name,password)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for result in results:
                dpt=result[2]
                print(dpt)
            if dpt == 'Disney Land':
                return 1
            elif dpt == 'Activity':
                return 2
            elif dpt == 'Hotel':
                return 3
            if dpt == 'Transport':
                return 4
            n=cursor.rownumber
            print("rownumber>>>>>")
            print(n)
            if n == 0:
                return 0
        except:
            import traceback
            print("呜呜呜呜呜呜呜呜呜呜呜")
            traceback.print_exc()

        cursor.close()



