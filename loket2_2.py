while True:
	path = '/var/www/html/audio_counter/data2.txt'
	loket_2 = open(path,'r')
	lihat = loket_2.read()
	data = int(lihat)
	#writeNumber(data)
	print ("Pin 09 Next")
	print (data)
	loket_2.close()
	time.sleep(1)