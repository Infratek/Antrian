import time
import subprocess
import os
#import uinput
#import serial
import smbus
#ser = serial.Serial('/dev/ttyUSB0', 9600)
#device = uinput.Device([uinput.KEY_4, uinput.KEY_D])
#x = int(ser.readline())

#define GPIO 14 as DHT11 data pin

# Define some device parameters
I2C_ADDR  = 0x26 # I2C device address, if any error, change this address to 0x27
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def loket_4():
   path = '/var/www/html/audio_counter/data4.txt'
   loket_4 = open(path,'r')
   lihat = loket_4.read()
   data = int(lihat)
   loket_4.close()
   return data;
def sisa_4():
   path1 = '/var/www/html/audio_counter/loket4.txt'
   sisa_4 = open(path1,'r')
   ceksisa4 = sisa_4.read()
   left_1 = int(ceksisa4)
   sisa_4.close()
   return left_1;
while True:
   lcd_init()
   #writeNumber(data)
   print ("Pin 19 Next")
   x = loket_4()
   y = sisa_4()
   z = y - x
   print (z)
     
 #  time.sleep(1)
   
   #print (sisa_antrian)
   lcd_string("Antrian:"+str(x),LCD_LINE_1)
   lcd_string("Sisa:"+str(z),LCD_LINE_2)
 #  device.emit_click(uinput.KEY_1)
   time.sleep(1)
   break
   #os.system('python/home/pi/loket2.py')
#elif x==2:
 #  device.emit_click(uinput.key_A)
#   print "eko"

