import doctest
from math import ceil
def hsv_rgb(H,S,V):
    '''
    This function Convert HSV to RGB
    :param H: Hue (0<=H<360)
    :type H:int
    :param S: Saturation (0<S<1)
    :type S:float
    :param V: Value (0<V<1)
    :type V:float
    :return: RGB as list [R,G,B]
    >>> hsv_rgb(240,1,0.5)
    [0, 0, 128]
    >>> hsv_rgb(60,1,1)
    [255, 255, 0]
    '''
    try:
        C=V*S
        X=C*(1-abs(((H/60)%2)-1))
        m=V-C

        if H>=0 and H<60:
            R_prime=C
            G_prime=X
            B_prime=0
        elif H>=60 and H<120:
            R_prime = X
            G_prime = C
            B_prime = 0
        elif H>=120 and H<180:
            R_prime = 0
            G_prime = C
            B_prime = X
        elif H>=180 and H<240:
            R_prime = 0
            G_prime = X
            B_prime = C
        elif H>=240 and H<300:
            R_prime = X
            G_prime = 0
            B_prime = C
        else:
            R_prime = C
            G_prime = 0
            B_prime = X
        R=ceil((R_prime+m)*255)
        G=ceil((G_prime+m)*255)
        B=ceil((B_prime+m)*255)
        return [R,G,B]
    except Exception as e:
        print("Input Error")


def hsl_rgb(H,S,L):
    '''
    This function convert hsl to rgb
    :param H: Hue (0<=H<360)
    :type H:int
    :param S: Saturation (0<S<1)
    :type S:float
    :param L: Lightness (0<L<1)
    :type L:float
    :return: RGB as list [R,G,B]
    >>> hsl_rgb(240,1,0.25)
    [0, 0, 128]
    >>> hsl_rgb(0,0,0.75)
    [192, 192, 192]
    '''
    try:
        C=(1-abs(2*L-1))*S
        X=C*(1-abs(((H/60)%2)-1))
        m=L-(C/2)

        if H>=0 and H<60:
            R_prime=C
            G_prime=X
            B_prime=0
        elif H>=60 and H<120:
            R_prime = X
            G_prime = C
            B_prime = 0
        elif H>=120 and H<180:
            R_prime = 0
            G_prime = C
            B_prime = X
        elif H>=180 and H<240:
            R_prime = 0
            G_prime = X
            B_prime = C
        elif H>=240 and H<300:
            R_prime = X
            G_prime = 0
            B_prime = C
        else:
            R_prime = C
            G_prime = 0
            B_prime = X
        R=ceil((R_prime+m)*255)
        G=ceil((G_prime+m)*255)
        B=ceil((B_prime+m)*255)

        return [R,G,B]
    except Exception as e:
        print("Input Error")

def hex_rgb(hex_code):
    '''
    This function convert hex_code to RGB
    :param hex_code: hex_code input
    :type hex_code:str
    :return: RGB as list [R,G,B]
    >>> hex_rgb('00FF00')
    [0, 255, 0]
    >>> hex_rgb('808080')
    [128, 128, 128]
    '''
    try:
        R=int(hex_code[0:2],16)
        G=int(hex_code[2:4],16)
        B=int(hex_code[4:6],16)
        return [R,G,B]
    except Exception as e:
        print("Input Error")

def cmyk_rgb(C,M,Y,K):
    '''
    This function convert CMYK to RGB
    :param C: Cyan [0,1]
    :type C:float
    :param M: Magenta [0,1]
    :type M:float
    :param Y: Yellow [0,1]
    :type Y:float
    :param K: Black Key Color [0,1]
    :type K:float
    :return: RGB as list [R,G,B]
    >>> cmyk_rgb(0,0,0,1)
    [0, 0, 0]
    >>> cmyk_rgb(1,0,0,0)
    [0, 255, 255]
    '''
    try:
        R=255*(1-C)*(1-K)
        G=255*(1-M)*(1-K)
        B=255*(1-Y)*(1-K)
        return [R,G,B]
    except Exception as e:
        print("Input Error")

if __name__=="__main__":
    doctest.testmod()







