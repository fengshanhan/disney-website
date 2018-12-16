#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class VisitorCommand():
    #插入游客，和注册相对应
    def insertVisitor(self,id,name,tel,isVIP,wallet,password):
        #open database
        db=pymysql.connect("localhost","root","rewq66505441-","database")
        cursor=db.cursor()
        #暂时把ID设置为1，之后要实现递增
        sql="""INSERT INTO VISITOR(VNO,VNAME,TELNO,ISVIP,WALLET,PWS) VALUES ('%s','%s','%s','%s','%s','%s')"""%(id,name,tel,isVIP,wallet,password)
        print("插入"+name+id)
        try:
            cursor.execute(sql)
            print("插入成功")
            db.commit()
            return 1
        except:
            print("不能插入")
            db.rollback()

        db.close()

    #查询，和登陆相对应
    def readVisitor(self,name,password):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT * FROM VISITOR WHERE VNAME= '%s' and PSW= '%s"""%(name,password)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            n=cursor.rownumber
            if n == 0:
                return 0
        except:
            import traceback
            traceback.print_exc()

        db.close()
        return 1


