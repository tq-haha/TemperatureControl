# coding=UTF-8 
import time;
import thread;

#获取时间

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


class vicecontroler:

    ControlerCount=0

    def __init__(self,room):
        self.room=room          #房间号
        self.state=0                 #0为关闭状态,1为工作状态
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

    def __init__(self):
        self.state=input("input 1 to start")
        self.model=input("input 0  to cold,input 1  to heat")
        self.AimTemperarture=input("input temperature")
        self.WindSpeed=input("input windspeed")                #0为停,1,2,3依次增大

class workstate(controlpanel):
     
    def Sensor(self):
        return 5

    def __init__(self):
        self.PresentTemperature=self.Sensor()  
        self.AimTemperature=0
        self.WindSpeed=1

    def display(self):
        print "当前温度 %d" % self.PresentTemperature
        print "目标温度 %d" % self.AimTemperature
        print "当前风速 %d" % self.WindSpeed

    def TemperatureChange(self):                                #温度变化
        while signal_1==1:
            print "当前温度 %.2f " % self.PresentTemperature
            if model==1:
                if self.PresentTemperature<self.AimTemperature:
                    time.sleep(2)           
                    self.PresentTemperature=self.PresentTemperature-0.05+float(self.WindSpeed)/10
                else:
                    time.sleep(2)
                    self.PresentTemperature=self.PresentTemperature-0.05
            else:
                if self.PresentTemperature>self.AimTemperature:
                    time.sleep(2)
                    self.PresentTemperature=self.PresentTemperature+0.05-float(self.WindSpeed)/10
                else:
                    time.sleep(2)
                    self.PresentTemperature=self.PresentTemperature+0.05
        thread.daemon= True


class Timeslot(controlpanel):
    number=0

    def __init__(self):
        self.starttime=time.asctime( time.localtime(time.time()) ) 
        number=number+1

    def Getlasttime(self):
        while signal_1==1:
            self.endtime=time.asctime( time.localtime(time.time()) )
            time.sleep(1)
            #print self.endtime
        thread.daemon = True

    #def Accouting(self):



Controler=vicecontroler(431)
xcontroler=controlpanel()

worker=workstate()


worker.AimTemperature=xcontroler.AimTemperarture   #获取遥控器的目标温度
worker.WindSpeed=xcontroler.WindSpeed

worker.display()
signal_1=xcontroler.state
model=xcontroler.model
worker.WindSpeed=xcontroler.WindSpeed

xtime=Timeslot()

thread.start_new_thread(xtime.Getlasttime,())
thread.start_new_thread(worker.TemperatureChange,())
signal_1=input("tounch a button to stop")


worker.display()

