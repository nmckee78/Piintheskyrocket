from adafruit_motor import servo
import pwmio
import board
import time
import digitalio
import adafruit_mpl3115a2
import busio

pwm_servo = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo2 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo3 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo4 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
button = digitalio.DigitalInOut(board.GP22)
button.pull = digitalio.Pull.UP
sda_pin =  board.GP14
scl_pin =  board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
threshold_altitude = 72
list_altitude = []
list_time = []

while True:
    altitude = sensor.altitude
    print(altitude)
    list_altitude.append(altitude)
    list_time.append(time.monotonic())

    if button.value == True and altitude <= threshold_altitude:
        servo1.angle = 0
        servo2.angle = 0
        servo3.angle = 0
        servo4.angle = 0
    if button.value == False:
        servo1.angle = 180
        servo2.angle = 180
        servo3.angle = 180
        servo4.angle = 180
    if altitude >= threshold_altitude:
        servo1.angle = 180
        servo2.angle = 180
        servo3.angle = 180
        servo4.angle = 180
    print(list_altitude)
    print(list_time)