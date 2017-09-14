'''
>>> from pyrgb import *
>>> import coverage
>>> cov = coverage.Coverage()
>>> cov.start()
>>> hsv_rgb(240,1,0.5)
[0, 0, 128]
>>> hsv_rgb(60,1,1)
[255, 255, 0]
>>> hsl_rgb(240,1,0.25)
[0, 0, 128]
>>> hsl_rgb(0,0,0.75)
[192, 192, 192]
>>> hex_rgb('00FF00')
[0, 255, 0]
>>> hex_rgb('808080')
[128, 128, 128]
>>> cmyk_rgb(0,0,0,1)
[0, 0, 0]
>>> cmyk_rgb(1,0,0,0)
[0, 255, 255]
>>> cov.stop()
>>> cov.save()

'''