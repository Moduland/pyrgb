import doctest
def zero_insert(i):
    '''
    This function insert zero to input string
    :param i: input string
    :type i:int
    :return: modified string

    >>> zero_insert("2")
    '02'
    >>> zero_insert("02")
    '02'
    '''
    if len(i)==1:
        return "0"+i
    else:
        return i
def rgb_hex(R,G,B):
    '''
    This function convert RGB to HEX Format
    :param R: Red Color Code (0-255)
    :type R:int
    :param G: Green Color Code (0-255)
    :type G:int
    :param B: Blue Color Code (0-255)
    :type B:int
    :return: hex code as string
    >>> rgb_hex(0,0,0)
    '000000'
    >>> rgb_hex(192,192,192)
    'C0C0C0'
    >>> rgb_hex(0,128,0)
    '008000'
    '''
    try:
        R=zero_insert(str(hex(R)).replace("0x",""))
        G = zero_insert(str(hex(G)).replace("0x",""))
        B = zero_insert(str(hex(B)).replace("0x",""))
        response=(R+G+B).upper()
        return response
    except Exception as e:
        print("Input Error")

def rgb_hsv(R,G,B):
    '''
    This function convert RGB to HSV
    :param R: Red Color Code (0-255)
    :type R:int
    :param G: Green Color Code (0-255)
    :type G:int
    :param B: Blue Color Code (0-255)
    :type B:int
    :return: HSV as list [H,S,V]
    >>> rgb_hsv(255,0,0)
    [0, 1.0, 1.0]
    >>> rgb_hsv(128,128,0)
    [60, 1.0, 0.5]
    '''
    try:
        R_prime=R/255
        G_prime=G/255
        B_prime=B/255
        C_max=max(R_prime,G_prime,B_prime)
        C_min=min(R_prime,G_prime,B_prime)
        delta=C_max-C_min
        if delta==0:
            H=0
        elif C_max==R_prime:
            H=60*(((G_prime-B_prime)/delta)%6)
        elif C_max==G_prime:
            H = 60 * (((B_prime - R_prime) / delta) +2)
        else:
            H = 60 * (((R_prime - G_prime) / delta) + 4)
        H=round(H)
        if C_max==0:
            S=0
        else:
            S=round(delta/C_max,2)
        V=round(C_max,2)
        return [H,S,V]
    except Exception as e:
        print("Input Error")


def rgb_hsl(R,G,B):
    '''
    This function convert rgb to hsl
    :param R: Red Color Code (0-255)
    :type R:int
    :param G: Green Color Code (0-255)
    :type G:int
    :param B: Blue Color Code (0-255)
    :type B:int
    :return: HSL as list [H,S,L]
    >>> rgb_hsl(128,0,0)
    [0, 1.0, 0.25]
    >>> rgb_hsl(255,255,0)
    [60, 1.0, 0.5]

    '''
    try:
        R_prime=R/255
        G_prime=G/255
        B_prime=B/255
        C_max=max(R_prime,G_prime,B_prime)
        C_min=min(R_prime,G_prime,B_prime)
        delta=C_max-C_min
        if delta==0:
            H=0
        elif C_max==R_prime:
            H=60*(((G_prime-B_prime)/delta)%6)
        elif C_max==G_prime:
            H = 60 * (((B_prime - R_prime) / delta) +2)
        else:
            H = 60 * (((R_prime - G_prime) / delta) + 4)
        H=round(H)
        L = round((C_max+C_min)/2,2)

        if C_max==0:
            S=0
        else:
            S=round(delta/(1-abs(2*L-1)),2)
        return [H,S,L]
    except Exception as e:
        print("Input Error")


def rgb_cmyk(R,G,B):
    '''
    This function convert RGB to CMYK
    :param R: Red Color Code (0-255)
    :type R:int
    :param G: Green Color Code (0-255)
    :type G:int
    :param B: Blue Color Code (0-255)
    :type B:int
    :return: CMYK as list [C,M,Y,K]
    >>> rgb_cmyk(0,0,255)
    [1.0, 1.0, 0.0, 0.0]
    >>> rgb_cmyk(0,255,255)
    [1.0, 0.0, 0.0, 0.0]
    '''
    try:
        R_prime=R/255
        G_prime=G/255
        B_prime=B/255
        K=round(1-max(R_prime,G_prime,B_prime),2)
        C=round((1-R_prime-K)/(1-K),2)
        M=round((1-G_prime-K)/(1-K),2)
        Y=round((1-B_prime-K)/(1-K),2)
        return [C,M,Y,K]
    except Exception as e:
        print("Input Error")

if __name__=="__main__":
    doctest.testmod()



