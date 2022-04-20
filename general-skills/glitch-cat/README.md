# Notes
## Challenge: Glitch Cat

Given Link and port
```
saturn.picoctf.net 65353
```
Running nc on it.
### Command:
```bash
nc saturn.picoctf.net 65353
```
### Output:
```bash
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```
Saving the output in a python file because it seems like e python code because of the chr function. Storing the output in a variable and printing it shows the flag.
### The flag:
```
picoCTF{gl17ch_m3_n07_9c42a45d}
```