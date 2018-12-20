import smbus
import time
bus = smbus.SMBus(1)
address = 0x08
def writeNumber(data):
	bus.write_byte(address, data)
	#bus.write_byte_data(address, 0, value)
	return -1
while True:
	path = '/var/www/html/audio_counter/data3.txt'
	loket_3 = open(path,'r')
	lihat = loket_3.read()
	data = int(lihat)
	writeNumber(data)
	print ("Pin 13 Next")
	print (data)
	loket_3.close()
	time.sleep(1)
	break