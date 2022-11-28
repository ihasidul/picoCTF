# Notes

## Challenge: advanced-potion-making

Running strings on the file and looking into the initial part some text like IHDR, sRGB, gAMA is given.This indicates that the given file is a png file.

```
IHDR
sRGB
gAMA
```

After googling these i found out about file signature.

### The head signature of the given file is

```
00000000: 8950 4211 0d0a 1a0a 0012 1314 4948 4452  .PB.........IHDR
```

which is not correct for png file.

### Correct signature for png file is

```
89 50 4E 47 0D 0A 1A 0A
```

[List of file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) Shows that .
