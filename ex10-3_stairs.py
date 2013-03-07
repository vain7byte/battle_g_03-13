#abwandlung die zusammentreffenden stufen haben eine höhe


stockwerke = 5
stairs = "_______"
stab = "|"
end = 8
start = 0

def stairs_ltr():
    for i in range(start, end):
        tab = "\t"*i
        if start < i < end - 1:
            print tab + stab + stairs

def stairs_ltr_first():
    for i in range(start, end):
        tab = "\t"*i
        if i == start:
            print " " + stairs
        if start < i < end - 1:
            print tab + stab + stairs

def stairs_ltr_last(): 
    for i in range(start, end):
        tab = "\t"*i
        if start < i < end - 1:
            print tab + stab + stairs
        if i == end - 1:
            print tab + stab
          
def stairs_rtl():
    for i in range(start, end):
        i_r = (end - i - 1)     #i reverse
        tab_r = "\t"*i_r        #tabs reverse
        if start <= i_r and i_r < end - 2:
            print tab_r + " " + stairs + stab
            
def stairs_rtl_first():
    for i in range(start, end):
        i_r = (end - i - 1)     #i reverse
        tab_r = "\t"*i_r        #tabs reverse
        if i_r == end - 2:
            print tab_r + " " + stairs
        if start <= i_r and i_r < end - 2:
            print tab_r + " " + stairs + stab

def stairs_rtl_last():
    for i in range(start, end):
        i_r = (end - i - 1)     #i reverse
        tab_r = "\t"*i_r        #tabs reverse
        if start < i_r and i_r < end - 2:
            print tab_r + " " + stairs + stab
        if i_r == start:
            print " " + stairs + stab + "\n" + stab


def stairs_generator (stockwerke_f):
    stairs_rtl_first()
    for i in range(1,stockwerke_f):
        stairs_ltr()
        stairs_rtl()
        
    stairs_ltr_last()
    
stairs_generator(stockwerke)

