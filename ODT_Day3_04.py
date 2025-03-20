# this code is a colourful ring

from machine import Pin
import neopixel

bob = neopixel.NeoPixel(Pin(4), 16) # connect 5v with 3v3, ground with ground and di with any gpio (pin)
bob[0] = (25, 25, 25) # white
bob[1] = (25, 0, 0) # red
bob[2] = (0, 25, 0) # green
bob[3] = (25, 0, 25) # purple
bob[4] = (0, 0, 25) # blue
bob[5] = (15, 25, 0) # lime green
bob[6] = (0, 15, 15) # light blue
bob[7] = (25, 0, 5) # pink
bob[8] = (25, 5, 0) # orange
bob[9] = (0, 20, 10) # turquoise
bob[10] = (20, 10, 0) # yellow
bob[11] = (20, 0, 10) # saturated purple
bob[12] = (10, 30, 0) # light green
bob[13] = (50, 10, 10) # skin
bob[14] = (10, 0, 30) # purpleish blue
bob[15] = (5, 30, 5) # pastel ish green

bob.write()
