tes
import RPi.GPIO as GPIO
import time
#import popen

import subprocess
import os
#import win32com.client
#import uinput
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(6,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(5,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(11,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(9,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(10,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(22,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(27,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(21,GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(20,GPIO.IN, GPIO.PUD_UP)
#device = uinput.Device([uinput.KEY_1, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_A, uinput.KEY_B, uinput.KEY_C, uinput.KEY_D, uinput.KEY_E, uinput.KEY_F])
def loket_1():
	path1 = '/var/www/html/audio_counter/loket1.txt'
	r1 = open(path1,'r1')
	lihat = r1.read()
	v1 = int(lihat)
	r1.close()
	return v1;
	
def loket_2():
	path2 = '/var/www/html/audio_counter/loket2.txt'
	r2 = open(path2,'r2')
	lihat = r2.read()
	v2 = int(lihat)
	r2.close()
	return v2;
	
def loket_3():
	path3 = '/var/www/html/audio_counter/loket3.txt'
	r3 = open(path3,'r3')
	lihat = r3.read()
	v3 = int(lihat)
	r3.close()
	return v3;
	
def loket_4():
	path4 = '/var/www/html/audio_counter/loket4.txt'
	r4 = open(path4,'r4')
	lihat = r4.read()
	v4 = int(lihat)
	r4.close()
	return v4;

#def cetak_1():
#	os.system('sudo python /home/pi/python-epson-printer/epson-printer/cetak1.py')	
while True:
	if(GPIO.input(26) == GPIO.LOW):
		v = loket_1()
		print (int(v))
		v += 1
		x = v
		#time.sleep(1)
		path1 = '/var/www/html/audio_counter/loket1.txt'
		f = open(path1,'w')
		f.write("%03d" % x)
		print("%03d" % x)
		x +=1
		f.close()
		time.sleep(1)
		#cetak_1 ()
		os.system('sudo python /home/pi/python-epson-printer/epson-printer/cetak1.py')
		#os.system('sudo python /home/pi/python/LCDloket1_rs.py')
		time.sleep(2)
	elif(GPIO.input(19) == GPIO.LOW):
		v = loket_2()
		print (int(v))
		v += 1
		x = v
		#time.sleep(1)
		path2 = '/var/www/html/audio_counter/loket2.txt'
		f = open(path2,'w')
		f.write("%03d" % x)
		print("%03d" % x)
		x +=1
		f.close()
		time.sleep(1)
		os.system ('sudo python /home/pi/python-epson-printer/epson-printer/cetak2.py')
		time.sleep(2)
	elif(GPIO.input(13) == GPIO.LOW):
		v = loket_3()
		print (int(v))
		v += 1
		x = v
		#time.sleep(1)
		path3 = '/var/www/html/audio_counter/loket3.txt'
		f = open(path3,'w')
		f.write("%03d" % x)
		print("%03d" % x)
		x +=1
		f.close()
		time.sleep(1)
		os.system ('sudo python /home/pi/python-epson-printer/epson-printer/cetak3.py')
		time.sleep(2)
	elif(GPIO.input(6) == GPIO.LOW):
		v = loket_4()
		print (int(v))
		v += 1
		x = v
		#time.sleep(1)
		path4 = '/var/www/html/audio_counter/loket4.txt'
		f = open(path4,'w')
		f.write("%03d" % x)
		print("%03d" % x)
		x +=1
		f.close()
		time.sleep(1)
		os.system ('sudo python /home/pi/python-epson-printer/epson-printer/cetak4.py')
		time.sleep(2)
	#elif(GPIO.input(21) == GPIO.LOW):
	#	f1 = open('/var/www/html/audio_counter/loket1.txt', 'r+')
	#	f2 = open('/var/www/html/audio_counter/loket2.txt', 'r+')
	#	f3 = open('/var/www/html/audio_counter/loket3.txt', 'r+')
	#	f4 = open('/var/www/html/audio_counter/loket4.txt', 'r+')
	#	f1.truncate(0)
	#	f1.write('0')
	#	f2.truncate(0)
	#	f2.write('0')
	#	f3.truncate(0)
	#	f3.write('0')
	#	f4.truncate(0)
	#	f4.write('0')
	#	print('reset')
	#	break
				
