# A simple program to test the driver

import time
import HTU21DF

while True:
	print("sending reset...")
	HTU21DF.htu_reset
	temperature = HTU21DF.read_temperature()
	print("The temperature is %f C." % temperature)
	time.sleep(1)
	humidity = HTU21DF.read_humidity()
	print("The humidity is %F percent." % humidity)
	time.sleep(1)
