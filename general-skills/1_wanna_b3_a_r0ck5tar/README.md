# Notes

## Challenge: 1_wanna_b3_a_r0ck5tar

A rockstar program is given.

### The lyrics

```
Rocknroll is right
Silence is wrong
A guitar is a six-string
Tommy's been down
Music is a billboard-burning razzmatazz!
Listen to the music
If the music is a guitar
Say "Keep on rocking!"
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!
Music is amazing sensation
Jamming is awesome presence
Scream Music!
Scream Jamming!
Tommy is playing rock
Scream Tommy!
They are dazzled audiences
Shout it!
Rock is electric heaven
Scream it!
Tommy is jukebox god
Say it!
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"
Break it down
```

Running the code on the [online interpreter](https://codewithrockstar.com/online) gives an error.

### The error

```
Rock is electric heaven
       ^
Expected [A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞĀĂĄĆĈĊČĎĐĒĔĖĘĚĜĞĠĢĤĦĨĪĬĮİĲĴĶĸĹĻĽĿŁŃŅŇŊŌŎŐŒŔŖŘŚŜŞŠŢŤŦŨŪŬŮŰŲŴŶŸŹŻŽ] or [a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþāăąćĉċčďđēĕėęěĝğġģĥħĩīĭįıĳĵķĸĺļľŀłńņňŋōŏőœŕŗřśŝşšţťŧũūŭůűųŵŷÿźżžŉß] but " " found.
line 21 col 8
```

I was removing the inputs first and removing the line until i get error free run of the code.The [wihtout_input_lyrics.txt](without_input_lyrics.txt) file contains that version of the lyrics.

That gave me the following output.

```
Keep on rocking!
66
79
78
74
79
79
73
Program completed in 32 ms
```

The (get_flag.py)[get_flag.py] script converts the output to ascii and gives the flag.
Running the get_flag.py script provides the following output.

```
BONJOOI
```

Trying the word in a different format gives the flag.

### The flag

```
picoCTF{BONJOVI}
```
