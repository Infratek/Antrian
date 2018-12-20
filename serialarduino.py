import time
import subprocess
import os
import uinput
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
device = uinput.Device([uinput.KEY_1, uinput.KEY_A, uinput.KEY_2, uinput.KEY_B, uinput.KEY_3, uinput.KEY_C, uinput.KEY_4, uinput.KEY_D])

#Tombol panggil LCD 1
def loket_1():
   path = '/var/www/html/audio_counter/data1.txt'
   loket_1 = open(path,'r')
   lihat = loket_1.read()
   data = int(lihat)
   loket_1.close()
   return data;

def sisa_1():
   path = '/var/www/html/audio_counter/loket1.txt'
   sisa_1 = open(path,'r')
   ceksisa1 = sisa_1.read()
   left_1 = int(ceksisa1)
   sisa_1.close()
   return left_1;

def tombol_1():
   device.emit_click(uinput.KEY_1)

#Tombol panggil LCD 2
def loket_2():
   path = '/var/www/html/audio_counter/data2.txt'
   loket_2 = open(path,'r')
   lihat = loket_2.read()
   data = int(lihat)
   loket_2.close()
   return data;

def sisa_2():
   path = '/var/www/html/audio_counter/loket2.txt'
   sisa_2 = open(path,'r')
   ceksisa2 = sisa_2.read()
   left_1 = int(ceksisa2)
   sisa_2.close()
   return left_1;

def tombol_2():
   device.emit_click(uinput.KEY_2)

   #Tombol panggil LCD 3
def loket_3():
   path = '/var/www/html/audio_counter/data3.txt'
   loket_3 = open(path,'r')
   lihat = loket_3.read()
   data = int(lihat)
   loket_3.close()
   return data;

def sisa_3():
   path = '/var/www/html/audio_counter/loket3.txt'
   sisa_3 = open(path,'r')
   ceksisa3 = sisa_3.read()
   left_1 = int(ceksisa3)
   sisa_3.close()
   return left_1;

def tombol_3():
   device.emit_click(uinput.KEY_3)

#Tombol panggil LCD 4
def loket_4():
   path = '/var/www/html/audio_counter/data4.txt'
   loket_4 = open(path,'r')
   lihat = loket_4.read()
   data = int(lihat)
   loket_4.close()
   return data;

def sisa_4():
   path = '/var/www/html/audio_counter/loket4.txt'
   sisa_4 = open(path,'r')
   ceksisa4 = sisa_4.read()
   left_1 = int(ceksisa4)
   sisa_4.close()
   return left_1;

def tombol_4():
   device.emit_click(uinput.KEY_4)

while True:
	x = int(ser.readline())
	#Panggilan LCD loket 1
	if x==1:
		#device.emit_click(uinput.KEY_1)
		tampil = int(loket_1())
		tiket = int(sisa_1())
		sisa = tiket - tampil
		print ("tampil",tampil)
		print ("tiket",tiket)
		print ("sisa",sisa)
		if int(sisa > 0):
			print "oke"
			tombol_1()
			time.sleep(1)
			os.system('python /home/pi/python/LCDloket1.py')
			os.system('python /home/pi/python/loket1.py')
			
		else : #int(sisa < 1):
			print "ulang oy"
		        device.emit_click(uinput.KEY_A)
	elif x==2:
		device.emit_click(uinput.KEY_A)
		print "eko"
		time.sleep(1)

	#Panggilan LCD loket 2
	elif x==3:
		#device.emit_click(uinput.KEY_2)
		tampil = int(loket_2())
		tiket = int(sisa_2())
		sisa = tiket - tampil
		print ("tampil",tampil)
		print ("tiket",tiket)
		print ("sisa",sisa)
		if int(sisa > 0):
			print "oke"
			tombol_2()
			device.emit_click(uinput.KEY_2)
			time.sleep(1)
			os.system('python /home/pi/python/LCDloket2.py')
			os.system('python /home/pi/python/loket2.py')
			
		else : #int(sisa < 1):
			print "ulang oy"
		        device.emit_click(uinput.KEY_B)
	elif x==4:
		device.emit_click(uinput.KEY_B)
		print "eko"
		time.sleep(1)

	#Panggilan LCD loket 3
	elif x==5:
		#device.emit_click(uinput.KEY_3)
		tampil = int(loket_3())
		tiket = int(sisa_3())
		sisa = tiket - tampil
		print ("tampil",tampil)
		print ("tiket",tiket)
		print ("sisa",sisa)
		if int(sisa > 0):
			print "oke"
			tombol_3()
			device.emit_click(uinput.KEY_3)
			time.sleep(1)
			os.system('python /home/pi/python/LCDloket3.py')
			os.system('python /home/pi/python/loket3.py')
			
		else : #int(sisa < 1):
			print "ulang oy"
		        device.emit_click(uinput.KEY_C)
	elif x==6:
		device.emit_click(uinput.KEY_C)
		print "eko"
		time.sleep(1)

	#Panggilan LCD loket 4
	elif x==7:
		#device.emit_click(uinput.KEY_4)
		tampil = int(loket_4())
		tiket = int(sisa_4())
		sisa = tiket - tampil
		print ("tampil",tampil)
		print ("tiket",tiket)
		print ("sisa",sisa)
		if int(sisa > 0):
			print "oke"
			tombol_4()
			device.emit_click(uinput.KEY_4)
			time.sleep(1)
			os.system('python /home/pi/python/LCDloket4.py')
			os.system('python /home/pi/python/loket4.py')
			
		else : #int(sisa < 1):
			print "ulang oy"
		        device.emit_click(uinput.KEY_D)
	elif x==8:
		device.emit_click(uinput.KEY_D)
		print "eko"
		time.sleep(1)
