import string

def hex_display(one_line:str='', line_limit:int=32, buffer_size:int=16):
    c = len(one_line) % line_limit
    buf = ''
    for index, i in enumerate(one_line):

        buf += ' ' if i in string.whitespace else i
        print(f"{ord(i):2X}", end=' ')
        if ((index+1) % buffer_size == 0):
            print ('- ', end='')
        if (index+1) % line_limit == 0:
            print(f"  {buf}")
            buf = ''
    while c < line_limit :
        print("  ", end=' ')
        if  ((c+1) % buffer_size == 0) :
            print ('- ', end='')
        if (c+1) % line_limit == 0:
            print(f"  {buf}")
            buf = ''
        c += 1
