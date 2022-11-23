# Notes

## Challenge: Bases

Given problem:
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

### Encoded string

```bash
bDNhcm5fdGgzX3IwcDM1
```

It looks like a base64 encoded string. Let's decode it.

### Command

```bash
echo bDNhcm5fdGgzX3IwcDM1 | base64 -d
```

### Output

```
l3arn_th3_r0p35
```

### The flag

```
picoCTF{l3arn_th3_r0p35}
```
