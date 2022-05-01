# Notes
## Challenge: File types
A pdf file names Flag.pdf is given. Using file command on it shows that it is "shell archive text"
### Command:
```bash
file Flag.pdf
```
### Output:
```bash
Flag.pdf: shell archive text
```
I could not read open the pdf file using any pdf viewer. So copied the file and renamed it with .shar extension. For shell archive text files .shar extension is used.
Now opening the .shar file in a text editor shows that it is a shell archive text file. It contains shell code.

Running the .sher file generates a file called **flag**. Running file command it showed that it is a archive file. Renamed it to flag.ar. Extracted the archive using ar command.
### Command:
```bash
ar -x flag.ar
```
Get another file called **flag**. Running file command on it shows that it is a **cpio archive** file.So renamed it with cpio extension and extracted the archive using cpio command.
### Command:
```bash
cpio -idv < flag.cpio
```
It gives another file called **flag**. Running file command on it shows that it is a **bzip2 compressed data**.So renamed it with bz2 extension and extracted the archive using bzip2 command.
### Command:
```bash
bzip2 -d flag.bz2
```
It gives another file called **flag**. Running file command on it shows that it is a **gzip compressed data**.So renamed it with gz extension and extracted the archive using gzip command.
### Command:
```bash
gzip -d flag.gz
```
It gives another file called **flag**. Running file command on it shows that it is a **lzip**.So renamed it with lz extension and extracted the archive using lzip command.
### Command:
```bash
lzip -d flag.lz
```
It gives another file called **flag**. Running file command on it shows that it is a **LZ4** file.So renamed it with lz4 extension and extracted the archive using lz4 command.
### Command:
```bash
lz4 flag.lz4
```
It gives another file called **flag**. Running file command on it shows that it is a **LZMA compressed data, non-streamed, size 255** file.So renamed it with lzma extension and extracted the archive using lzma command.
### Command:
```bash
lzma -d flag.lzma
```
It gives another file called **flag**. Running file command on it shows that it is a **lzop compressed data - version 1.040, LZO1X-1, os: Unix** file.So renamed it with lzo extension and extracted the archive using lzop command.
### Command:
```bash
lzop -d flag.lzo
```
It gives another file called **flag**. Running file command on it shows that it is a **lzip**.So renamed it with lz extension and extracted the archive using lzip command.
### Command:
```bash
lzip -d flag.lz
```
It gives another file called **flag**. Running file command on it shows that it is a **xz**.So renamed it with xz extension and extracted the archive using xz command.
### Command:
```bash
xz -d flag.xz
```
It gives another file called **flag**. Running file command on it shows that it is a **ASCII** text file.This file contains a hax string.Converting the hax to ASCII gives the flag.
### Command:
```bash
 echo 7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f33633739633562617d0a | xxd -r -p
```
### The flag:
```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
```
