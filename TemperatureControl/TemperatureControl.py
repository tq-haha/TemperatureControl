# coding=UTF-8 
import time;
import thread;

#��ȡʱ��

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


class vicecontroler:

    ControlerCount=0

    def __init__(self,room):
        self.room=room          #�����
        self.state=0                 #0Ϊ�ر�״̬,1Ϊ����״̬
        self.model=0               #0Ϊ����,1Ϊ����
        self.used_energy=0    #��Ϊ��λ
        self.used_pay=0        #��Ϊ��λ
        self.used_time=0      #����Ϊ��λ
        vicecontroler.ControlerCount+=1
    def display(self):
        print "�ӿػ���Ŀ %d" % vicecontroler.ControlerCount
        print "����� %d" % self.room
        print "��ʹ�õ��� %d" % self.used_energy
        print "ʹ��ʱ�� %d " % self.used_time
        print "Ӧ����� %d" % self.used_pay

class controlpanel(vicecontroler):

    def __init__(self):
        self.state=input("input 1 to start")
        self.model=input("input 0  to cold,input 1  to heat")
        self.AimTemperarture=input("input temperature")
        self.WindSpeed=input("input windspeed")                #0Ϊͣ,1,2,3��������

class workstate(controlpanel):
     
    def Sensor(self):
        return 5

    def __init__(self):
        self.PresentTemperature=self.Sensor()  
        self.AimTemperature=0
        self.WindSpeed=1

    def display(self):
        print "��ǰ�¶� %d" % self.PresentTemperature
        print "Ŀ���¶� %d" % self.AimTemperature
        print "��ǰ���� %d" % self.WindSpeed

    def TemperatureChange(self):                                #�¶ȱ仯
        while signal_1==1:
            print "��ǰ�¶� %.2f " % self.PresentTemperature
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


worker.AimTemperature=xcontroler.AimTemperarture   #��ȡң������Ŀ���¶�
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

