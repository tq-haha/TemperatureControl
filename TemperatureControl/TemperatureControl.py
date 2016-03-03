# coding=UTF-8 
import time;
import thread;

#获取时间

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


class vicecontroler:

    ControlerCount=0

    def __init__(self,room,state,model,used_energy,used_pay,used_time):
        self.room=room          #房间号
        self.state=0                 #0为关闭状态,1为状态
        self.model=0               #0为制冷,1为制热
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

class controlpanel(vicecontroler):

    def __init__(self,Switch,Model,AimTemperature,WindSpeed):
        self.Switch=input("input 1 to start")
        self.Model=input("input 0  to cold,input 1  to heat")
        self.AimTemperarture=input("input temperature")
        self.WindSpeed=input("input windspeed")

class workstate(vicecontroler):
     
    def Sensor(self):
        return 5

    def __init__(self,PresentTemperature,AimTemperature,WindSpeed):
        self.PresentTemperature=self.Sensor()  
        self.AimTemperature=0
        self.WindSpeed=1

    def display(self):
        print "当前温度 %d" % self.PresentTemperature
        print "目标温度 %d" % self.AimTemperature
        print "当前风速 %d" % self.WindSpeed

    def TemperatureChange(self):
        while signal_1==1:
            print self.PresentTemperature
            if self.PresentTemperature<self.AimTemperature:
                time.sleep(10)
                self.PresentTemperature=self.PresentTemperature+1
            else:
                time.sleep(10)
                self.PresentTemperature=self.PresentTemperature-1
        thread.daemon= True


class Timeslot(vicecontroler,workstate):

    def __init__(self,starttime):
        self.starttime=time.asctime( time.localtime(time.time()) )

    def Getlasttime(self):
        while signal_1==1:
            self.endtime=time.asctime( time.localtime(time.time()) )
            time.sleep(1)
            #print self.endtime
        thread.daemon = True

    #def Accouting(self):



Controler=vicecontroler(431,0,0,0,0,0)
xcontroler=controlpanel(0,0,0,0)
worker=workstate(0,0,0)


worker.AimTemperature=xcontroler.AimTemperarture   #获取遥控器的目标温度
worker.WindSpeed=xcontroler.WindSpeed

worker.display()


xtime=Timeslot(0)
signal_1=1
thread.start_new_thread(xtime.Getlasttime,())
thread.start_new_thread(worker.TemperatureChange,())
signal_1=input("tounch a button to stop")


worker.display()

