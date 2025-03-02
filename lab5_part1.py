def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == "0" and len(part) > 1: return False
        return 256 > i_part >= 0
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    for part in ip.split('.'):
        if len(ip.split('.')) < 4: return False
        if not is_valid_part(part): return False
    return True



# print(is_valid_part('127'), is_valid_part('1111'), is_valid_part('AAA'), is_valid_part('-2'), is_valid_part('01'),is_valid_part('0'))
print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.256.1"))
print(is_valid_ip("192.168.1"))
print(is_valid_ip("192.168.01.1"))
