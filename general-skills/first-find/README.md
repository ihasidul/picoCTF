# Notes

## Challenge: First Find

A zip file is given.

### Instruction

Unzip this archive and find the file named 'uber-secret.txt'
Unzip the file.

### Command

```bash
unzip files.zip
```

Applying find command to find the file.

### Command

```bash
find files -name 'uber-secret.txt'
```

### Output

```
files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Applying cat on the file gives the flag.

### Command

```bash
cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

### The flag

```bash
picoCTF{f1nd_15_f457_ab443fd1}
```
