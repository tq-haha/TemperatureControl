# coding=UTF-8 
import time;

#��ȡʱ��

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


class vicecontroler:

    ControlerCount=0

    def __init__(self,room,used_energy,used_pay,used_time):
        self.room=room          #�����
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

Controler=vicecontroler(431,0,0,0)
Controler.display()

