from microbit import display, Image, sleep
import tinybit

#move forward
tinybit.car_run(150)
display.show(Image.ARROW_S)
sleep(2000)
#move back
tinybit.car_back(150)
display.show(Image.ARROW_N)
sleep(2000)
#turn left with one side wheel
tinybit.car_left(150)
display.show(Image.ARROW_E)
sleep(1500)
#turn right with one side wheel
tinybit.car_right(150)
display.show(Image.ARROW_W)
sleep(1500)
#turn left
tinybit.car_spinleft(150)
display.show(Image.ARROW_E)
sleep(1000)
#turn right
tinybit.car_spinright(150)
display.show(Image.ARROW_W)
sleep(1000)
#stop
tinybit.car_stop()
display.clear()

