import RPi.GPIO as GPIO
import time
import keyboard

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

def move_forward():
    motorA_forward()
    motorB_forward()

def move_backward():
    motorA_backward()
    motorB_backward()

def turn_right():
    motorA_forward()
    motorB_backward()

def turn_left():
    motorA_backward()
    motorB_forward()

try:
    print("Press W to move forward, S to move backward, A to turn left, D to turn right. Press Q to quit.")
    while True:
        if keyboard.is_pressed('w'):
            print("Moving forward")
            move_forward()
        elif keyboard.is_pressed('s'):
            print("Moving backward")
            move_backward()
        elif keyboard.is_pressed('a'):
            print("Turning left")
            turn_left()
        elif keyboard.is_pressed('d'):
            print("Turning right")
            turn_right()
        elif keyboard.is_pressed('q'):
            print("Quitting")
            break
        else:
            stop_motors()
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage

except KeyboardInterrupt:
    print("Program stopped")

finally:
    stop_motors()
    GPIO.cleanup()
