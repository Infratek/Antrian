import smbus
import time
bus = smbus.SMBus(1)
address = 0x07
def writeNumber(data):
	bus.write_byte(address, data)
	#bus.write_byte_data(address, 0, value)
	return -1
while True:
	path = '/var/www/html/audio_counter/data2.txt'
	loket_2 = open(path,'r')
	lihat = loket_2.read()
	data = int(lihat)
	writeNumber(data)
	print ("Pin 19 Next")
	print (data)
	loket_2.close()
	time.sleep(1)
	break