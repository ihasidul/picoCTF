# Notes

## Challenge: Transformation

From the code given in the problem with the enc file seems like the flag was made using some shifting and then changing it into a UTF-16 string. So I wrote a python script to convert each character into hex and then turning that into ASCII. That is how i got the flag.Run get_flag.py to get the flag.

### Command:

```bash
python3 get_flag.py
```

### Output:

```bash
picoCTF{16_bits_inst34d_of_8_04c0760d}
```
