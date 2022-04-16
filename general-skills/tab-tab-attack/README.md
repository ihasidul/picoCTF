# Notes
## Challenge: Tab, Tab, Attack
Unzip the file.
### Command:
```bash
unzip Addadshashanammu.zip
```
Using tree on the unzipped directory shows the following:
### Command:
```bash
tree Addadshashanammu/
```
### Output:
```bash
Addadshashanammu/
└── Almurbalarammi
    └── Ashalmimilkala
        └── Assurnabitashpi
            └── Maelkashishi
                └── Onnissiralis
                    └── Ularradallaku
                        └── fang-of-haynekhtnamet
```
Go to the directory using cd.
### Command:
```bash
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku
```
Checking the file type.
### Command:
```bash
file fang-of-haynekhtnamet
```
### Output:
```bash
fang-of-haynekhtnamet: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=e34ce4e4ee2f7ce7fb251c8f5ab036da9882bc55, not stripped
```
Make the file executable.
### Command:
```bash
chmod +x fang-of-haynekhtnamet
```
Running the file.
### Command:
```bash
./fang-of-haynekhtnamet
```
Running the file shows the flag.
### Output:
```bash
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}
```
Running get-flag.sh script to get the flag.
