# Notes

## Challenge: Based

### Description

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 29956.`

### Connection Details

```bash
nc jupiter.challenges.picoctf.org 29956
```

After connecting to the server a binary number is given to convert that binary in to word.So that can be solved using binary to ascii conversion.

After providing the converted word as input an Octal number is given to convert that octal in to word.So that can be solved using octal to ascii conversion.

After providing the converted word as input a hexadecimal number is given to convert that hexadecimal in to word.So that can be solved using hexadecimal to ascii conversion.

To do all of these conversion i made a helper script called [helper.py](helper.py) in python.

### helper.py

```python
#!/usr/bin/env python3
import binascii

def octal_to_ascii(octal_str):
    '''
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    '''
    str_converted = ""
    for octal_char in octal_str.split(" "):
        str_converted += chr(int(octal_char,base=8))
    return str_converted

binary_input = input("Enter the  Binary number: ").replace(" ","")
n = int(binary_input,2)
ascii_version = binascii.unhexlify('%x' % n)
data = str(ascii_version, 'UTF-8')
print(f"BINARY: {binary_input} ==> ASCII: {data}")

octal_input = str(input("Enter the Octal number: ")).strip(" ")
data = octal_to_ascii(octal_input)
print(f"Octal: {octal_input} ==> ASCII: {data}")

hax_input = str(input("Enter the Hax number: ")).strip(" ")
data = binascii.unhexlify(hax_input).decode('utf-8')
print(f"Hax: {hax_input} ==> ASCII: {data}")
```

After final input it shows the output with the flag.

```
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_b375bb16}
```
