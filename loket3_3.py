while True:
	path = '/var/www/html/audio_counter/data3.txt'
	loket_3 = open(path,'r')
	lihat = loket_3.read()
	data = int(lihat)
	#writeNumber(data)
	print ("Pin 09 Next")
	print (data)
	loket_3.close()
	time.sleep(1)