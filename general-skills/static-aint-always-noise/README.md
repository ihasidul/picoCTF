# Notes

## Challenge: Static ain't always noise

Running file on the static file gives us the following output:

### Command

```bash
file static
```

### Output

```bash
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=33934f7b8aea8e359749ed57dca4cd26d6059acf, not stripped
```

Make the given script executable.

### Command

```bash
chmod +x ltdis.sh
```

Running the script with input as the **static** file gives us the following output:

### Command

```bash
./ltdis.sh static
```

### Output

```bash
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

After running the ltdis script two file is generated.These are

```
static.ltdis.strings.txt
static.ltdis.x86_64.txt
```

Running a cat and grep using flag gives us some clue.

### Command

```bash
cat static.ltdis.strings.txt | grep flag
```

### Output

```bash
6e8 Oh hai! Wait what? A flag? Yes, it's around here somewhere!
1858 flag
```

All the flags of picoCTF challenges has the format **picoCTF{flag}**.So we can assume that the flag is somewhere in the static.ltdis.x86_64.txt file. Running a cat and grep using **picoCTF** gives us the flag.

### Command

```bash
cat static.ltdis.x86_64.txt | grep picoCTF
```

### The flag

```bash
picoCTF{d15a5m_t34s3r_1e6a7731}
```
