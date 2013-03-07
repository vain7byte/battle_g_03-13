stairs = "_______"
stab = "|"
end = 8

fat_cat = """
I'll do a stairs:
\t %s
\t\t %s
\t\t\t %s\n\t\t\t\t %s \n|
""" % (stairs, stairs, stairs, stairs)

for i in range(0, end):
    tab = "\t" * i
    if i == 0:
        print stairs + "_"
    if 0 < i < end - 1:
        print tab + stab + stairs
    if i == end - 1:
        print tab + stab
        
#tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat