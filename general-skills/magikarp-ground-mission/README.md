# Notes
# Challenge: Magikarp Ground Mission

User:
```
ctf-player
```
Domain:
```
venus.picoctf.net
```
Connect to the server:
### Command:
```bash
ssh ctf-player@venus.picoctf.net -p 56818
```
From drop-in directory get the first part of the flag:
### Command:
```bash
cat 1of3.flag.txt
```
### Output:
```
picoCTF{xxsh_
```
Get the next instructions from instructions-to-2of3.txt
### Command:
```bash
cat instructions-to-2of3.txt
```
### Output:
```
Next, go to the root of all things, more succinctly `/`
```
So go to the root directory.
### Command:
```bash
cd /
```
ls shows
### Output:
```
2of3.flag.txt  boot  etc   instructions-to-3of3.txt  lib64  mnt  proc  run   srv  tmp  var
bin            dev   home  lib                       media  opt  root  sbin  sys  usr
```
Get the second part of the flag from 2of3.flag.txt
### Command:
```bash
cat 2of3.flag.txt
```
### Output:
```
0ut_0f_\/\/4t3r_
```
Get the next instructions form instructions-to-3of3.txt file
### Command:
```bash
cat instructions-to-3of3.txt
```
### Output:
```
Lastly, ctf-player, go home... more succinctly `~`
```
So go home.
### Command:
```bash
cd ~
```
### Command:
```bash
ls
```
### Output:
```
3of3.flag.txt  drop-in
```
Get the 3rd and final part of the flag from 3of3.flag.txt
### Command:
```bash
cat 3of3.flag.txt
```
### Output:
```
5190b070}
```
Concatenate the 3 parts of the flag together.
### The flag:
```
picoCTF{xxsh_0ut_0f_\/\/4t3r_5190b070}
```