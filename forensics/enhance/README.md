### Notes:
To see the file type.
Command:
```bash
file drawing.flag.svg
```
Output:
```
drawing.flag.svg: SVG Scalable Vector Graphics image
```
After inspecting the code of the SVG file, it seems like the flag is hidden in code of the SVG file. To extract the flag from the SVG file, command mentioned below was used.
```bash
cat drawing.flag.svg | grep "</tspan" | cut -d ">" -f2 | cut -d "<" -f1 | tr -d "\n" | tr -d " "
```
get-flag.sh also contains the same solution.
