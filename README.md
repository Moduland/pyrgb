<div align="center">
<img src="http://moduland.github.io/pyrgb/rgb-lamps.jpg" height=240px width=320px>

</br>
<a href="https://badge.fury.io/py/pyrgb"><img src="https://badge.fury.io/py/pyrgb.svg" alt="PyPI version" height="18"></a>
<a href="http://www.python.org"><img src="https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-blue.svg"></a>
<a href="http://moduland.github.io/pyrgb"><img src="https://img.shields.io/badge/doc-latest-red.svg"></a>
<a href="https://zenodo.org/badge/latestdoi/89876759"><img src="https://zenodo.org/badge/89876759.svg" alt="DOI"></a>
<a href="https://codecov.io/gh/Moduland/pyrgb">
  <img src="https://codecov.io/gh/Moduland/pyrgb/branch/master/graph/badge.svg" alt="Codecov" />
</a>

</div>


----------


# pyrgb
Python RGB Conversion Library


## Installation
### Source Code
- Download [Version 0.1](https://github.com/moduland/pyrgb/archive/v0.1.zip) or [Latest Source ](https://github.com/Moduland/pyrgb/archive/master.zip)

- `python3 setup.py install` or `python setup.py install` (Need Root Access)

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip3 install pyrgb` or `pip install pyrgb` (Need Root Access)


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

## Automated Build				
				
<div align="center">
<table style="border:1px solid black">
<tr>
<th>Linux</th>
<th>Windows</th>

</tr>

<tr>
<td><a href="https://travis-ci.org/Moduland/pyrgb"><img src="https://travis-ci.org/Moduland/pyrgb.svg?branch=master"></a></td>
<td> <a href="https://ci.appveyor.com/project/sepandhaghighi/pyrgb"><img src="https://ci.appveyor.com/api/projects/status/7sqa1r0n22gq23ne?svg=true"></a>	</td>

</tr>	

</table>

</div>


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@moduland.ir](mailto:info@moduland.ir "info@moduland.ir"). 


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 					


## Donate to our project
					
If you feel like our project is important can you please support us?			
Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do.					

<h3>Bitcoin :</h3>					

```1XGr9qbZjBpUQJJSB6WtgBQbDTgrhPLPA```
				

<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>


## Citing
If you use pyrgb in your research , please cite this ;-)

<blockquote>
<p>Sepand Haghighi. (2017, July 28). Moduland/pyrgb: Version 0.1. Zenodo. http://doi.org/10.5281/zenodo.835824</p>
</blockquote>


## License
<div align="center">
<a href="https://github.com/Moduland/pyrgb/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
<br/>
<a href="http://www.moduland.ir" target="_blank" title="Moduland Website"><img src="http://www.orangetool.ir/images/moduland.jpg" height="128px" width="128px" alt="Moduland Website"></a>

</div>



			


