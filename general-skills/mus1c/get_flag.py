# !/usr/bin/env python3

ascii_data = f"""114 114 114 111 99 107 110 114 110 48 49 49 51 114"""
flag = ""
for num in ascii_data.split(" "):
    flag = flag + chr(int(num))

print("picoCTF{{{}}}".format(flag))
