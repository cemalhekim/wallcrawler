# Wall-Crawler

Wall-Crawler is a 4-wheeled autonomous robot designed for building inspections, equipped with advanced sensors for comprehensive structural analysis. Ideal for monitoring, maintenance, and safety assessments, it efficiently navigates vertical surfaces.

The brain of the robot is Raspberry Pi 4.

![image](https://github.com/cemalhekim/wallcrawler/assets/98236326/0d5b813b-ce1a-4b29-a540-47517e711fd7)


Robot will have 4 DC Motor powered wheels. Every 2 motors are connected in parallel. That's why we only need 1 motor driver which can control 2 motors. As the motor driver MX1919 DC Dual Motor Driver is in use. 

![image](https://github.com/cemalhekim/wallcrawler/assets/98236326/d29daeac-bd34-42cf-87e3-cae727282469)

The power supply for this module is a 7.4 Volt 2 Cells LiPo battery.

The wire connections between LiPo and MX1919 are:


VDD => +

GND => -


The wire connections between raspberry pi 4 and MX1919 are:


IN1 => GPIO 17

IN2 => GPIO 27

IN3 => GPIO 22

IN4 => GPIO 23

GND => GND


As DC motors I choose ... model. The DC motors on the left should be parallel connected as well as the motors on the right. The reason is we want to control 2 motors with the same power signals. That's how they are gonna work in synchron.





