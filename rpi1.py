import os
import time
os.chdir('/home/pi')
import lcd
lcd.lcd_init()
try:
	while(1>0):
		if(lcd.GPIO.input(lcd.pir)==1):
			lcd.GPIO.output(lcd.led,lcd.GPIO.LOW)
			lcd.GPIO.output(16,lcd.GPIO.HIGH)
			lcd.lcd_string('Detection',lcd.LCD_LINE_1)
			lcd.lcd_string('Sector 1',lcd.LCD_LINE_2)
			time.sleep(1)
			lcd.GPIO.output(16,lcd.GPIO.LOW)
		else:
			lcd.lcd_string(time.strftime('It is %d.%m.%Y'),lcd.LCD_LINE_1)
			lcd.lcd_string(time.strftime('%H:%M:%S'),lcd.LCD_LINE_2)
			lcd.GPIO.output(lcd.led,lcd.GPIO.LOW)
			time.sleep(1)
			lcd.GPIO.output(lcd.led,lcd.GPIO.HIGH)
except KeyboardInterrupt:
	lcd.lcd_string('Program stop',lcd.LCD_LINE_1)
	lcd.lcd_string('',lcd.LCD_LINE_2)
	lcd.lcd_string('3',lcd.LCD_LINE_2)
	time.sleep(1)
	lcd.lcd_string('2',lcd.LCD_LINE_2)
	time.sleep(1)		
	lcd.lcd_string('1',lcd.LCD_LINE_2)
	time.sleep(1)
	lcd.lcd_init()
	lcd.GPIO.cleanup()

