# Notes

## Challenge: 2Warm

The problem given was **"Can you convert the number 42 (base 10) to binary (base 2)?"**
Using bc (a command line calculator) we can convert the number 42 to binary.

### Command:

```bash
echo "obase=2; 42" | bc
```

### Output:

```bash
101010
```

The flag:

```bash
picoCTF{101010}
```
