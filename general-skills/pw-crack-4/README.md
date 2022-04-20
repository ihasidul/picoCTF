# Notes
## Challenge: PW Crack 4

Running the given level4.py file wants a password.Going through the python code shows that it checks with a hashed password with the user password.
Now there is also a list of password in the python file which includes one correct password.The list have 100 password.Modify the level4.py file and make it so that it checks with the list of passwords. The modified code is in modified_level4.py.
Running the modified code should gives the flag.
Saved the output of the modified code in a file.Finding **pico** in the output with **grep** gives the flag.
### Command:
```bash
cat output_of_modified_code.txt| grep pico
```
### Output:
```
picoCTF{fl45h_5pr1ng1ng_ae0fb77c}
```
