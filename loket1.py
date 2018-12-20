import smbus
import time
bus = smbus.SMBus(1)
address = 0x06
def writeNumber(data):
	bus.write_byte(address, data)
	#bus.write_byte_data(address, 0, value)
	return -1
while True:
	path = '/var/www/html/audio_counter/data1.txt'
	loket_1 = open(path,'r')
	lihat = loket_1.read()
	data = int(lihat)
	writeNumber(data)
	print ("Pin 26 Next")
	print (data)
	loket_1.close()
	time.sleep(1)
	break
