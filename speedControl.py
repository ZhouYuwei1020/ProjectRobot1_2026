from microbit import display, Image, sleep
import tinybit

#begin with zero speed
tinybit.car_run(0,0)
sleep(2000)
#accelerate
tinybit.car_run(50,50)
sleep(2000)
tinybit.car_run(100,100)
sleep(2000)
tinybit.car_run(150,150)
sleep(2000)
tinybit.car_run(200,200)
sleep(1500)
#max speed
tinybit.car_run(255,255)
sleep(1500)
#decelerate
tinybit.car_run(150,150)
sleep(2000)
tinybit.car_run(50,50)
sleep(2000)
tinybit.car_stop()
