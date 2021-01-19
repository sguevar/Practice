from Stack import Stack


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    
    dec_num = int(dec_num)
    s = Stack()
    binary = ''
    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num = dec_num // 2
    while not s.is_empty():
        binary += str(s.pop())
    return binary


print(convert_int_to_bin("242"))
