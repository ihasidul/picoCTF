# Mob psycho
In this challenge an apk file is provided.

- Unziped the file 
```bash
unzip mobpsycho.apk
```
- From the files after unzip i ran find to see if there is any files with name
flag
```bash
find mobpsycho -name '*flag*'
```
Output
```
mobpsycho/res/color/flag.txt
```
- This file contains a hax string 
```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37343664666133397d
```
- Decoding the hax string gives the flag
```
 echo -n '7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37343664666133397d' | xxd -r -p
```
### Flag
```
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_746dfa39}
```
