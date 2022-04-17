# Notes
## Challenge: Nice netcat...
I used netcat to connect to a server and saw the response. Saved the responses in a text file.
### Command:
```bash
nc -v mercury.picoctf.net 43239 > nc-output.txt
```
Cleaned up the new lines and saved in another file 
### Command:
```bash
cat nc-output.txt | tr -d "\n"
```
### Output:
```bash
112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 55 99 48 56 50 49 102 53 125 10
```
These seems like ASCII. I tried to convert these using some online tools. They were not that helpful. Wrote a python script to do the conversion.
### Python Script:
```python
#!/usr/bin/env python3

ascii_nums = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 55, 99, 48, 56, 50, 49, 102, 53, 125, 10]
flag = ""
for a in ascii_nums:
    flag += chr(a)
print(flag)
```
The ascii_solver.py contains the script.Running the python script gives the flag.
### Command:
```bash
python3 ascii_solver.py
```
### Output:
```bash
picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}
```