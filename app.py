from flask import Flask
from flask import render_template, redirect, url_for, request
from app.db.user_db import Visitor
from app.db.ticket_db import TicketCommand
from app.db.user_base import VisitorCommand
from app.db.hotel_db import HotelCommand
from app.db.room_db import RoomCommand
from app.db.activity_db import ActivityCommand
from app.data import user_info

app = Flask(__name__)
#user=user_info() #全局记录下当前登陆用户的信息
ticketno=0

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
        global no
        no=no+1
        if visitor.register(no,name,password,confirm) == 1:
            return redirect(url_for('login'))
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
        user_info.User.user_name=request.form.get('name')
        name=request.form.get('name')
        password=request.form.get('password')
        if visitor.login(name,password) == 1:
            #可以登陆
            # 获取当前的用户ID
            # 这里需要从数据库中读取name为当前name的vno，然后存储到user_info中
            no = visitorCommand.read_for_no(name)
            user_info.User.user_no = no
            return redirect(url_for('map'))
        else:
            return "不能登陆"

@app.route('/map.html',methods=['GET','POST'])
def map():
    return render_template('map.html')

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
        normalprice = ticketCommand.readTicket('0')  # 0 is normal ticket
        vipprice = ticketCommand.readTicket('1')  # 1 is vip ticket
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
                v=str(vno)
                if ticketCommand.insertTicket(tno, v, b, normalprice, normaltime1, normaltime2, b, b) == 1:
                    #print(vno+"成功后买了普通票号"+ticketno)
                    normalsuccess+=1
                else:
                    print("买normal票过程中出现异常,系统只存储之前买的票")
                     #一旦出现一个失败就都失败，这里还有一个问题就是怎么rollback？
        if vipnumber!=0:
            #print("买了VIP票数" + vipnumber)
            for i in range((vipnumber)):
                ticketno = ticketno + 1  # 实现了票号的自增长
                print(vno)
                print(">>>>>>")
                print(ticketno)
                a='1'
                b='0'
                if ticketCommand.insertTicket(ticketno, vno, a, vipprice, viptime1, viptime2, b, b) == 1:
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
        print(hotel[0])
        print(hotel[0][0])
        print(hotel[0][4])
        return render_template('hotel.html',hotel=hotel)
    else:
        pass

@app.route('/room1/<hotelname>',methods=['GET','POST'])
def room1(hotelname):
    if request.method == 'GET': #获取当前房间信息
        #return "your lrllrlr is %s"%hotelname
        print("hotelname>>>")
        print(hotelname)
        roomcommand=RoomCommand()
        roommessage=roomcommand.readRoom(hotelname)
        print("roommessage")
        print(roommessage)
        return render_template('/room1.html',roommessage=roommessage)
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
        activity=activitycommand.readActivity_ww(activityname)
        comments=activitycommand.readComment(activityname)
        return render_template('/ww_activity.html', activity=activity,comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
