from base import Base
from constant import ArduinoCommand as ac
from time import sleep
def main():
	base = Base()
	if base.find_arduino() == True:
		base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MAXPOWER)
		base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MAXPOWER)
		sleep(5)
		base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MINPOWER)
		base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MINPOWER)




main()
