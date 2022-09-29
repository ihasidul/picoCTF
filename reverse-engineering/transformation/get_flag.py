enc = open("enc").read()
hax_string = ""
for item in enc:
    hax_string = hax_string + hex(ord(item))[2:]
flag = bytearray.fromhex(hax_string).decode()
print(flag)
