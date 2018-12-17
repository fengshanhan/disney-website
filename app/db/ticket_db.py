#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class TicketCommand():

    #查询，显示票价
    def readTicket(self,ttype):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT TPRICE FROM TICKET WHERE TTYPE= '%s'"""%(ttype)
        try:
            cursor.execute(sql)
            results=cursor.fetchone()
            price=results[0]
            print(price)
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return price

    #插入，买票时用到
    def insertTicket(self,tno,vno,ttype,tprice,tEdate,tSdate,isRe,isCh):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()

        sql= """INSERT INTO TICKET(TNO,VNO,TTYPE,TPRICE,TEDATE,TSDATE,ISRE,ISCH)
           VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"""%(tno,vno,ttype,tprice,tEdate,tSdate,isRe,isCh)
        try:
            cursor.execute(sql)
            #print(vno+"购买票号"+tno)
            print("yes")
            db.commit()
            return 1
        except:
            #print(vno+"不能购买票号"+tno)
            print("vno+>>>>>>>")
            print(vno)
            print("tno>>>>>")
            print(tno)
            print("no")
            db.rollback()

        cursor.close()

    #查询当前票号
    def read_ticketnum(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()

        sql="""SELECT * FROM TICKET"""
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for result in results:
                number=result[0]
            return number
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return number


