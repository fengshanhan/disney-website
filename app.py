from flask import Flask
from flask import render_template, redirect, url_for, request
from app.db.user_db import Visitor
from app.db.user_db import Administrator
from app.db.ticket_db import TicketCommand
from app.db.user_base import VisitorCommand
from app.db.user_base import AdministratorCommand
from app.db.hotel_db import HotelCommand
from app.db.room_db import RoomCommand
from app.db.activity_db import ActivityCommand
from app.data import user_info
from app.db.administrator_db import administratoInfo
from app.db.bus_db import BusCommand
from app.db.stop_db import StopCommand

app = Flask(__name__)
#user=user_info() #全局记录下当前登陆用户的信息
ticketno=0

#my information 登录后跳转到自己的信息页面



#注册时实现ID自增长
@app.route('/register.html',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        name=request.form.get('name')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        visitor=Visitor()
        visitorcommand=VisitorCommand()
        no=visitorcommand.readVisitorNum()#每次register都执行
        num=no+1
        print(num)
        print(name)
        print(password)
        print(confirm)
        if visitor.register(num,name,password,confirm) == 1:
            return render_template("my.html")
        else:
            return "不能注册"
    else:
        return "wrong"

@app.route('/',methods=['GET','POST'])
@app.route('/login.html',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        visitor=Visitor()
        visitorCommand=VisitorCommand()
        user_info.User.user_name=request.form.get('name') #记录下当前用户名,用户名唯一！！！
        name=request.form.get('name')
        password=request.form.get('password')
        if visitor.login(name,password) == 1:
            #可以登陆
            # 获取当前的用户ID
            # 这里需要从数据库中读取name为当前name的vno，然后存储到user_info中
            num = visitorCommand.read_for_no(name)
            user_info.User.user_no = num #记录下当前登陆用户号
            return redirect(url_for('bus '))
        else:
            return "不能登陆"

@app.route('/bus.html',methods=['GET','POST'])
def map():
    return render_template('bus.html')

@app.route('/ticket.html',methods=['GET','POST'])
def ticket():
    #每次进入买票页面的时候就要从系统获取当前的票号，则新加的票号为+1
    ticketCommand=TicketCommand()
    global ticketno
    ticketnoo=ticketCommand.read_ticketnum()
    ticketno=int(ticketnoo)
    if request.method == 'GET': #显示票价信息
        ticketCommand=TicketCommand()
        normalprice=ticketCommand.readTicket('0') #0 is normal ticket
        vipprice=ticketCommand.readTicket('1') #1 is vip ticket
        return render_template('ticket.html',normalprice=normalprice,vipprice=vipprice)
    elif request.method == 'POST': #提交购买信息,需要提交到ticket表中
        print("post")
        ticketCommand = TicketCommand()
        normalprice = str(ticketCommand.readTicket('0'))  # 0 is normal ticket
        vipprice = str(ticketCommand.readTicket('1'))  # 1 is vip ticket
        vno=user_info.User.user_no #是当前用户在买票哦
        print(vno)
        normalnumber=request.form.get('normalnumber')
        normalnumber=int(normalnumber)
        normaltime1=request.form.get('normaltime1')
        normaltime2=request.form.get('normaltime2')
        print("normalnumber>>>>>>>>>")
        print(normalnumber)
        print(normaltime1)
        print(normaltime2)
        viptime1 = request.form.get('viptime1')
        viptime2 = request.form.get('viptime2')
        vipnumber=request.form.get('vipnumber')
        vipnumber=int(vipnumber)

        normalsuccess=0
        vipsuccess=0
        if normalnumber!=0:
            #print("买了普通票数"+normalnumber)
            for i in range((normalnumber)):
                a='1'
                b='0'
                ticketno=ticketno+1 #实现了票号的自增长
                tno=str(ticketno)
                v=vno
                if ticketCommand.insertTicket(tno, v, b, normalprice, normaltime1, normaltime2, b) == 1:
                    #print(vno+"成功后买了普通票号"+ticketno)
                    normalsuccess+=1
                else:
                    print("买normal票过程中出现异常,系统只存储之前买的票")
                     #一旦出现一个失败就都失败，这里还有一个问题就是怎么rollback？
        if vipnumber!=0:
            #print("买了VIP票数" + vipnumber)
            for i in range((vipnumber)):
                ticketno = ticketno + 1  # 实现了票号的自增长
                tno=str(ticketno)
                print(vno)
                print(">>>>>>")
                print(ticketno)
                a='1'
                b='0'
                if ticketCommand.insertTicket(tno, vno, a, vipprice, viptime1, viptime2, b) == 1:
                    #print(vno + "成功后买了VIP票号" + ticketno)
                    vipsuccess+=1
                else:
                    print("买VIP票过程中出现异常,系统只存储之前买的票")# 一旦出现一个失败就都失败，这里还有一个问题就是怎么rollback？
        print("///////")
        print(vipsuccess)
        print(vipnumber)
        print(normalsuccess)
        print(normalnumber)
        if vipsuccess == vipnumber:
            if normalsuccess == normalnumber:
                return render_template('map.html')
            else:
                return render_template('ticket.html')
        else:
            #print("vipsuccess"+vipsuccess)
            #print("normalsuccess"+normalsuccess)
            return render_template('ticket.html')

@app.route('/hotel.html',methods=['GET','POST'])
def hotel():
    if request.method == 'GET': #显示hotel信息
        hotelcommand=HotelCommand()
        hotel=hotelcommand.readHotel()
        print(hotel)
        #print(hotel[0])
        #print(hotel[0][0])
        #print(hotel[0][4])
        return render_template('hotel.html',hotel=hotel)
    else:
        pass

@app.route('/room1/<hotelname>.html',methods=['GET','POST'])
def room1(hotelname):
    if request.method == 'GET': #获取当前房间信息
        #return "your lrllrlr is %s"%hotelname
        print("hotelname>>>")
        print(hotelname)
        roomcommand=RoomCommand()
        roommessage=roomcommand.readRoom(hotelname)
        print("roommessage")
        print(roommessage)
        return render_template('/room1.html',roommessage=roommessage,hotelname=hotelname)
    elif request.method == 'POST':
        #预定房间##参考订票
        pass

@app.route('/activity.html',methods=['GET','POST'])
def activity():
    if request.method == 'GET': #显示activity信息
        activitycommand=ActivityCommand()
        activities=activitycommand.readActivity()
        print(activities)
        print(activities[0])
        print(activities[0][0])
        print(activities[0][4])
        return render_template('activity.html',activities=activities)
    else:
        pass

@app.route('/ww_activity/<activityname>.html',methods=['GET','POST'])
def activity_ww(activityname):
    if request.method == 'GET':
        activitycommand=ActivityCommand()
        activity=activitycommand.readActivity_ww(activityname)#获取当前活动的名称，内容，最大容纳量
        comments=activitycommand.readComment(activityname)#获取当前活动的所有评论
        return render_template('/ww_activity.html', activity=activity,comments=comments)


#######################################################
################## administrator ######################
#######################################################

@app.route('/login_administrator.html',methods=['GET','POST'])
def login_administrator():
    if request.method == 'GET':
        return render_template("login_administrator.html")
    else:
        administrator=Administrator()
        administratorCommand=AdministratorCommand()
        name=request.form.get('name')
        password=request.form.get('password')
        if administrator.login(name,password) == 1:
            return redirect(url_for('administrator_chief'))
        elif administrator.login(name,password) == 2:
            return redirect(url_for('administrator_activity'))
        if administrator.login(name,password) == 3:
            return redirect(url_for('administrator_hotel'))
        if administrator.login(name,password) == 4:
            return redirect(url_for('administrator_transport'))
        else:
            return "不能登陆"


@app.route('/my_activity.html',methods=['GET','POST'])
def my_activity():
    if request.method == 'GET':
        vno = user_info.User.user_no
        activityCommand = ActivityCommand()
        Activity = activityCommand.readActivityBook(vno)
        return render_template("my_activity.html",activitys=Activity)


@app.route('/administrator_activity.html',methods=['GET','POST'])
def administrator_activity():
    if request.method == 'GET':
        activityCommand = ActivityCommand()
        Activity= activityCommand.readActivity()
        return render_template('administrator_activity.html', Activity=Activity)
    else:
        activityCommand = ActivityCommand()
        print("收到了POST!")
        print(request.form.get('aname_delete'))
        if (request.form.get('aname_delete') is None):  #修改或增加activity
            print("修改activity")
            aname=request.form.get('aname')
            description = request.form.get('description')
            tnum = request.form.get('tnum')
            vip = request.form.get('vip')
            aLength = request.form.get('aLength')
            stime = request.form.get('stime')
            etime = request.form.get('etime')
            if activityCommand.modifyActivity(aname,description,tnum,vip,aLength,stime,etime) == 1:
                   return redirect(url_for('administrator_activity'))
            else:
                   return "失败"
        else:       #删除
            print("删除")
            aname = request.form.get('aname_delete')
            if activityCommand.deleteActivity(aname)==1:
                return redirect(url_for('administrator_activity'))
            else:
                return "失败"



@app.route('/administrator_chief.html',methods=['GET','POST'])
def administrator_chief():
    if request.method == 'GET':
        administrationCommand = administratoInfo()
        administration = administrationCommand.readAdministrator()
        return render_template('administrator_chief.html', administration=administration)
    else:
        administration = administratoInfo()
        adNo=request.form.get('adNo')
        password = request.form.get('password')
        dept = request.form.get('dept')
        if administration.modifyAdministrator(adNo,password,dept) == 1:
            return redirect(url_for('administrator_chief'))
        else:
            return "失败"


@app.route('/administrator_hotel.html',methods=['GET','POST'])
def administrator_hotel():
    if request.method == 'GET':
        hotelcommand = HotelCommand()
        hotel = hotelcommand.readHotel()
        roomcommand = RoomCommand()
        room = roomcommand.readRoom_admi()
        print(";;;;;;;;;;;")
        return render_template('administrator_hotel.html', Hotel=hotel,Room=room)
    else:
        if (request.form.get('rno') != None):
            #修改的hotel
            print(";;;;;")
            hotelCommand = HotelCommand()
            hname=request.form.get('hname')
            haddr = request.form.get('haddr')
            rNum = request.form.get('rNum')
            htele = request.form.get('htele')
            if hotelCommand.modifyHotel(hname,haddr,rNum,htele) == 1:
                return redirect(url_for('administrator_hotel'))
            else:
                return "失败"
        else:                                      #修改的Room
            roomCommand =RoomCommand()
            print("...........")
            hname = request.form.get('hname')
            rno = request.form.get('rno')
            rprice = request.form.get('rprice')
            if roomCommand.modifyRoom(hname,rno,rprice) == 1:
                return redirect(url_for('administrator_hotel'))
            else:
                return "失败"


@app.route('/administrator_transport.html',methods=['GET','POST'])
def administrator_transport():
    if request.method == 'GET':
        busCommand = BusCommand()
        bus = busCommand.readHotel()
        stopCommand = StopCommand()
        stop = stopCommand.readHotel()
        return render_template('administrator_transport.html', Bus=bus,Stop=stop)
    else:
        if (request.form.get('stid') == None):      #修改的hotel
            busCommand = BusCommand()
            bno=request.form.get('bno')
            bStart = request.form.get('bStart')
            bEnd = request.form.get('bEnd')
            sdes = request.form.get('sdes')
            edes = request.form.get('edes')
            Total_seat = request.form.get('Total_seat')
            if busCommand.modifyBus(bno,bStart,bEnd,sdes,edes,Total_seat) == 1:
                return redirect(url_for('administrator_transport'))
            else:
                return "失败"
        else:                                      #修改的Room
            stopCommand =StopCommand()
            stid = request.form.get('stid')
            bno = request.form.get('bno')
            stName = request.form.get('stName')
            time1 = request.form.get('time1')
            time2 = request.form.get('time2')
            time3 = request.form.get('time3')
            time4 = request.form.get('time4')
            if stopCommand.modifyStop(stid,bno,stName,time1,time2,time3,time4) == 1:
                return redirect(url_for('administrator_transport'))
            else:
                return "失败"

if __name__ == '__main__':
    app.run(debug=True)
