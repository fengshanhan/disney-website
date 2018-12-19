from app.db.user_base import VisitorCommand
from app.db.user_base import AdministratorCommand

visitorCommand=VisitorCommand()
administratorCommand=AdministratorCommand()

class Visitor():
    # 注册
    def register(self,id,username, password, confirm):  # 返回1可注册，返回0不可注册
        if password == confirm:
            tel="null"
            wallet=0
            isvip='1'
            print('>>>>>>')
            print(id)
            print(username)
            print(tel)
            print(isvip)
            print(wallet)
            print(password)
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


class Administrator():
    # 登陆
    def login(self,username, password):
        if administratorCommand.readAdministrator(username, password) == 1:
            print("登陆成功")
            return 1
        elif administratorCommand.readAdministrator(username, password) == 2:
            print("登陆成功")
            return 2
        elif administratorCommand.readAdministrator(username, password) == 3:
            print("登陆成功")
            return 3
        elif administratorCommand.readAdministrator(username, password) == 4:
            print("登陆成功")
            return 4
        else:
            print("登陆失败")
            return 0