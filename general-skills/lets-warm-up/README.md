# Notes
## Challenge: Lets Warm Up

Challenge Description: 
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
Using xxd the hax can be reversed to ASCII.
### Command:
```bash
   echo "0x70" |  xxd -r -p 
```
### Output:
```bash
p
```
### The flag:
```
picoCTF{p}
```