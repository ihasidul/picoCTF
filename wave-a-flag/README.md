# Notes
THe warm file is a binary file.
### Command:
```bash 
file warm
```
### Output:
```
warm: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3181a501366281ab5eba1c41e54a1f40800e3966, with debug_info, not stripped
```
Make the binary executable:
### Command:
```bash
chmod +x warm
```
Running it in the terminal:
### Command:
```bash
./warm
```
### Output:
```
Hello user! Pass me a -h to learn what I can do!
```
Running it with the **-h** flag:
### Command:
```bash
./warm -h
```
### Output:
```
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
```
To get the flag directly make the binary executable and run **get-flag.sh** or the command below:
### Command:
```bash
./warm -h | cut -d : -f2 | tr -d  " "
```
### Output:
```
picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
```