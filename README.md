# pyrgb
Python RGB Conversion Library


## Installation
### Source Code
- Download [Latest Source ](https://github.com/Moduland/pyrgb/archive/master.zip)

- `python3 setup.py install`


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


##License

<a href="https://github.com/Moduland/pyrgb/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
			


