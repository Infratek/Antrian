import smbus
import time
bus = smbus.SMBus(1)
address = 0x09
def writeNumber(data):
	bus.write_byte(address, data)
	#bus.write_byte_data(address, 0, value)
	return -1
while True:
	path = '/var/www/html/audio_counter/data4.txt'
	loket_4 = open(path,'r')
	lihat = loket_4.read()
	data = int(lihat)
	writeNumber(data)
	print ("Pin 6 Next")
	print (data)
	loket_4.close()
	time.sleep(1)
	break