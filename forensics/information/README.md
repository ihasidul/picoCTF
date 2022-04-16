# Notes
## Challenge: Information
File type 
### Command
```bash 
file cat.jpg
```
### Output
```bash
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```

Using [exiftool](https://exiftool.org/) to extract information from the file.
### Command
```bash
exiftool cat.jpg
```
### Output
```bash
ExifTool Version Number         : 11.88
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 kB
File Modification Date/Time     : 2021:03:16 00:24:46+06:00
File Access Date/Time           : 2022:04:16 20:09:49+06:00
File Inode Change Date/Time     : 2022:04:16 20:09:37+06:00
File Permissions                : rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
The license in this output looks promising. Using oline tools it looks like it is a **base64** encoded string.Decoding the string shows the flag. 
get-flag.sh script contains the solution script. 