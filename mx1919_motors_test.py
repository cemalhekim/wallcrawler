import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motor driver
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup the motor control pins as outputs
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def motorA_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def motorA_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def motorB_forward():
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def motorB_backward():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop_motors():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

try:
    while True:
        print("Motor A Forward")
        motorA_forward()
        time.sleep(2)
        print("Motor A Backward")
        motorA_backward()
        time.sleep(2)
        print("Motor B Forward")
        motorB_forward()
        time.sleep(2)
        print("Motor B Backward")
        motorB_backward()
        time.sleep(2)
        print("Stopping Motors")
        stop_motors()
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Program stopped")

finally:
    stop_motors()
    GPIO.cleanup()
