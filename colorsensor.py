import sys
import tcs3200
import pigpio
import time

pi = None
s = None

def setup(out, s2, s3, s0, s1, oe):
        global s, pi
        pi = pigpio.pi()

        s = tcs3200.sensor(pi, out, s2, s3, s0, s1, oe)
        s.set_update_period(0.333)
        s.set_frequency(2)
        s.set_sample_size(20)

def cleanup():
        global s, pi
        s.cancel()
        pi.stop()

def get_level():
        global s
        for i in range(5):
                time.sleep(0.333)
                return s.get_Hertz()

def get_black_level():
        return get_level()

def get_white_level():
        return get_black_level()

def set_black_level(level):
        global s
        s.set_black_level(level)

def set_white_level(level):
        global s
        s.set_white_level(level)

def get_rgb():
        global s, pi
        red=21
        green=20
        blue=16

        rgb = s.get_rgb()
        pi.set_PWM_dutycycle(red, rgb[0])
        pi.set_PWM_dutycycle(green, rgb[1])
        pi.set_PWM_dutycycle(blue, rgb[2])
        time.sleep(0.333)
        return rgb

def get_avg_rgb(times):
        red = 0
        green = 0
        blue = 0

        for i in range(times):
                rgb = get_rgb()
                red += rgb[0]
                green += rgb[1]
                blue += rgb[2]

        return_rgb = [0, 0, 0]
        return_rgb[0] = red/times
        return_rgb[1] = green/times
        return_rgb[2] = blue/times

        return return_rgb
