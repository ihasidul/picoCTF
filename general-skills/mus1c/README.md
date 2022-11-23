# Notes

## Challenge: mus1c

A song lyrics is given. After seeing the lyric first thing came into my mind was the Rorckstar programming language.So i used the [website](https://codewithrockstar.com/) to run the lyrics which is a rockstar program.

### Output

```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```

The output seemed like ASCII. Wrote a python script to convert the ASCII to text.
The code is in get_flag.py.

### get_flag.py

```python
# !/usr/bin/env python3

ascii_data = f"""114 114 114 111 99 107 110 114 110 48 49 49 51 114"""
flag = ""
for num in ascii_data.split(" "):
    flag = flag + chr(int(num))

print("picoCTF{{{}}}".format(flag))

```

### The flag

```
picoCTF{rrrocknrn0113r}
```
