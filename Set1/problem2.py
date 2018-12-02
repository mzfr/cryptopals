s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

# Take strings as base 16 integer, then use XOR(^) function.
xord = hex(int(s1, 16) ^ int(s2, 16))

print("XOR'd string is: ", xord[2:])
