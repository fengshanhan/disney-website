#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:chenhong time:2018-12-14

import pymysql

def data(a):

  con=pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="test", charset="utf8")
  rel = con.cursor()
  rel.execute('select * from '+a)
  val = rel.fetchall()
  a=len(val)





  con.close();
  rel.close();
  return  val


if __name__ == '__main__':

    a=data("type");
    print(a)
