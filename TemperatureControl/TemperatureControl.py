# coding=UTF-8 
import time;

#获取时间

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


class vicecontroler:

    ControlerCount=0

    def __init__(self,room,used_energy,used_pay,used_time):
        self.room=room          #房间号
        self.used_energy=0    #度为单位
        self.used_pay=0        #角为单位
        self.used_time=0      #分钟为单位
        vicecontroler.ControlerCount+=1

    def display(self):
        print "从控机数目 %d" % vicecontroler.ControlerCount
        print "房间号 %d" % self.room
        print "已使用电量 %d" % self.used_energy
        print "使用时长 %d " % self.used_time
        print "应付金额 %d" % self.used_pay

Controler=vicecontroler(431,0,0,0)
Controler.display()

