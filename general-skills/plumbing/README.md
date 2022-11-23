# Notes

## Challenge: plumbing

### Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427.

Connecting using **nc** using the given connection details:

```bash
nc jupiter.challenges.picoctf.org 4427
```

Piping the output of the nc into grep and searching for the flag:

```bash
nc jupiter.challenges.picoctf.org 4427 | grep picoCTF
```

### The flag

```
picoCTF{digital_plumb3r_5ea1fbd7}
```
