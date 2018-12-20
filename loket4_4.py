while True:
	path = '/var/www/html/audio_counter/data4.txt'
	loket_4 = open(path,'r')
	lihat = loket_4.read()
	data = int(lihat)
	#writeNumber(data)
	print ("Pin 09 Next")
	print (data)
	loket_4.close()
	time.sleep(1)