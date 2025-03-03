def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return (decimal_to_binary(next)) + str(digit)



# print(decimal_to_binary(10))   # "1010"
# print(decimal_to_binary(255))  # "11111111"
# print(decimal_to_binary(1))    # "1"

def binary_to_decimal(b:str):
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1

