# Notes

## Challenge: Big Zip

A zip file is given. Have to find out the flag in the zip file.
Unzip the file.

### Command

```bash
unzip big-zip-files.zip
```

Applying grep to all the files and subdirectories in the big-zip-files folder provides the file path containing the flag.

### Command

```bash
grep -rl "pico" big-zip-files
```

Here -r is used to search recursively and -l is used to print the file name that matches.

### Output

```
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
```

Now cat out the file to get the flag.

### Command

```bash
cat big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
```

### Output

```
information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

### The Flag

```
picoCTF{gr3p_15_m4g1c_ef8790dc}
```
