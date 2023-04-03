# version
```
a variable containing the latest version
```

# figlet(text,font='small')
```
save this to a variable then print it , figlet wrapper
defaults to "small" FIGlet font if font not specified
```

# urban(term)
```
searches the urban dictionary for a "term"
returns an array of all the values a term off urban would have
```

# jsonAPI(url)
```
retrieves data from an API that sends a json output then decodes it
the output is a Python Dictionary
can include get requests in the url itself to send data
```

# brainshopAi(BrainID,Secret,Message)
```
save this to a variable the use its output
sends a request to BrainShop.ai API then retrieves data from AI
good to use for a ChatBot
```

# write(data,file)
```
self explandatory
```

# read(file)
```
save this to a variable
also self explandatory
```

# banner(text)
```
creates a banner best suited for app startups
Generates in random styles
save this to a variable
```

# isUp(website)
```
checks if a given website is up or not
returns True if its up with a response code of 200
returns False if the site is down
returns the response code if the site is up but not functioning correctly
```

# red(text) blue(text) yellow(text) green(text)
```
functions which print text in a single color
```

# nekoBinConverter(int)
```
a silly tool that uses a non standard algorithm to convert a positive integer into binary form, totally unpractical but its there for its non standard operation
```

#debug(message)
```
similar to print() accepts 1 argument which is the debug message
will only print it to the console if "DEBUG" (without "") is in argv
```

#colourFactory() "class"
```
a class which you can write (only write) text with all 256 xterm colors
initialize the class in a variable then edit (text) and (colour) and (newline*)
then initialize the output via cinit()
and finally print the output with cprint()

example:
factory = colourFactory()
factory.text = "Nekos are cute!"
factory.colour = "ff0088"
factory.cinit()
factory.cprint()

you can use both hex values and 0-255 xterm colours

*: newline is optional and its a Bool , defaults to True
   and is made so you can print multiple colours on the same line binary
   by calling the class again or with regular print()
```

NekoMimi Python Module is made for ease-of-use and to be a good begginer friendly module
