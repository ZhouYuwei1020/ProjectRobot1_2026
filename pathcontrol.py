from microbit import display, Image, pin12
import tinybit
import neopixel

np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)

#path control
while True:
    left = tinybit.traking_sensor_L()
    right = tinybit.traking_sensor_R()
    if left is False and right is False:
        tinybit.car_run(205)
    elif left is True and right is False:
        tinybit.car_spinleft(80)
    elif left is False and right is True:
        tinybit.car_spinright(80)
    elif left is False and right is False:
        tinybit.car_run(205)
