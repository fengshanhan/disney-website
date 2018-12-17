from app.db.user_base import VisitorCommand

visitorCommand=VisitorCommand()

class Visitor():
    # 注册
    def register(self,username, password, confirm):  # 返回1可注册，返回0不可注册
        if password == confirm:
            id="1"
            tel="1"
            wallet="1"
            isvip='1'
            wallet='1'
            if visitorCommand.insertVisitor(id, username, tel, isvip, wallet, password) == 1:
                print("注册成功")
                return 1
            else:
                print("wrong")
                return 0
        else:
            print("注册失败")
            return 0

    # 登陆
    def login(self,username, password):
        if visitorCommand.readVisitor(username, password) == 1:
            print("登陆成功")
            return 1
        else:
            print("登陆失败")
            return 0