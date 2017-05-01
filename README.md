<div align="center">
<img src="http://moduland.github.io/pyrgb/rgb-lamps.jpg" height=240px width=320px>
<a href="https://badge.fury.io/py/pyrgb"><img src="https://badge.fury.io/py/pyrgb.svg" alt="PyPI version" height="18"></a>
<a href="http://www.python.org"><img src="https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-blue.svg"></a>
</br>

</div>


----------


# pyrgb
Python RGB Conversion Library


## Installation
### Source Code
- Download [Version 0.1](https://github.com/moduland/pyrgb/archive/v0.1.zip) or [Latest Source ](https://github.com/Moduland/pyrgb/archive/master.zip)

- `python3 setup.py install`

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip3 install pyrgb`


## Functions

```python
import pyrgb

#1- hsv_rgb

[R,G,B]=pyrgb.hsv_rgb(H,S,V)  

#2- hsl_rgb

[R,G,B]=pyrgb.hsl_rgb(H,S,L)

#3- hex_rgb

[R,G,B]=pyrgb.hex_rgb('hex_string')

#4- cmyk_rgb

[R,G,B]=pyrgb.cmyk_rgb(C,M,Y,K)

#5- rgb_hex

hex_string=pyrgb.rgb_hex(R,G,B)

#6- rgb_hsv

[H,S,V]=pyrgb.rgb_hsv(R,G,B)

#7- rgb_hsl

[H,S,L]=pyrgb.rgb_hsl(R,G,B)

#8- rgb_cmyk

[C,M,Y,K]=pyrgb.rgb_cmyk(R,G,B)


```
- H: Hue (0<=H<360) 
- S: Saturation (0<S<1)
- V: Value (0<V<1)
- L: Lightness (0<L<1)
- C,M,Y,K : (0,1)
- R,G,B : (0-255)


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@moduland.ir](mailto:info@moduland.ir "info@moduland.ir"). 


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 


## License

<a href="https://github.com/Moduland/pyrgb/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
			


