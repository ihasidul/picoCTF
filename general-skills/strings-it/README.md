# Notes
# Challenge: strings it
 
Let's see the file type of the file.
### Command:
```bash
file strings
```
### Output:
```
strings: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0cdedfba33422d235dba8c90e00fb77b235f1ff8, not stripped
```
Using **strings** on it and save the printout to a file.
### Command:
```bash
strings strings > strings-output.txt
```
Seemed like a big file to go through.
Then i used **grep** to find pico in the output of strings.That did the job.
### Command:
```bash
strings -d strings | grep "pico"
```
### Output:
```
picoCTF{5tRIng5_1T_7f766a23}
```