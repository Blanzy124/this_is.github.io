def ret(ret1):
    if ret1 == "pag":
        return "Pay"
def computepay(hr1):
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    try:
        hr = float(hrs)
        rt = float(rate)
    except:
        print('You Must Use Only!')
    if hr <= 40:
        if hr1 == "rtt":
            py1 = hr * rt
            print ("Pay", py1)
    elif hr >= 41:
        ov = hr - 40
        rt1 = rt * 1.5
        py2 = (ov * rt1) + ((hr - ov) * rt)
        if hr1 == "hrt":
            return (py2)
    if hr <= 40:
        computepay("rtt")
    elif hr >= 41:
        print(ret("pag"), computepay("hrt"))