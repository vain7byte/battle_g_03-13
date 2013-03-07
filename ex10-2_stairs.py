stairs = "_______"
stab = "|"
end = 8
start = 0

def stairs_ltr():
    for i in range(start, end):
        tab = "\t" * i
        if i == start:
            print " " + stairs
        if start < i < end - 1:
            print tab + stab + stairs
        # if i == end - 1:
            # print tab + stab

          
def stairs_rtl():
    for i in range(start, end):
        i_r = (end - i - 1) #i reverse
        tab_r = "\t" * i_r #tabs reverse
        # if i_r == end - 2:
            # print tab_r + " " + stairs
        # print i_r
        if start < i_r < end - 1:
            print tab_r + " " + stairs + stab
        # print i_r, ":", start
        if i_r == start:
            print " " + stairs + stab + "\n" + stab


stairs_ltr()
stairs_rtl()    