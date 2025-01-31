# Hoi! Itz Da Dokz!  
welcome to the documentations for the NekoMimi python module 
as our goals for this module is to help making your coding a bit easier then a befitting easy doc is a must  

# Architecture and Submodules  
> [!IMPPORTANT]
> Legacy submodules wont be covered as they will be removed in `v2.0.0`  

| SubModule      | Description                                   |
| -------------- | --------------------------------------------- |
|   `__init__`   | Module info and classifications used by bob   |
|   `colourimi`  | Coloured printing SubModule                   |
|  `consoleToys` | Set of tools and wrappers for CLI apps        |
|     `reg`      | Tiny registry for single word data storing    |
|    `utils`     | Main tools and macro code for easy dev        |


# colourimi  
```python
# Usage and examples:

# Initializing the factory and priming it to print "Hi!" in #444444
factory= colourFactory()
factory.text= "Hi!"
factory.colour= "#444444" #could be a hex code suffixed by a hash or one of the 256 color values with no hash
factory.cinit()

# After this you'll get Hi! written with a gray colour
factory.cprint()
```
## colourFactory (class)  
Universal class for working with colours in 256 colour terminals  
### text (variable) [str]  
The text to be manipulated  
### colour (variable) [str]  
The colour of the manipulation  
### newline (variable) [bool]  
Whether to add a new line or write the next character on the same line  
### cinit (method) [None]  
Processes the data into a prefix and suffix to print your manipulated text  
### cprint (method) [None]  
Applies and prints the manipulated text  
  
  
# consoleToys  
```python
# Usage and examples:

# After this you'll get Hi! written with a gray colour
kprint("Hi!", "#444444")
```
## kprint (method) [None]  
Ready wrapper for colourimi  
  
  
# reg  
```python
# Usage and examples:

# The following command will return the data stored in a cell called test
data = readCell("test")
# It also might return two string messages in case the cell doesn't exist or the registry isn't initialized:
# cell: {cell} is not in database
# Registry uninitialized, please use the neko shell to initialize it

#the following command will initialize a Database instance
db= Database("cabinet-id")
#the following command queries and returns the value of a cell called "1" within "cabinet-id"
data= db.query("1") #if the cell doesn't exist it'll return ""
#the following command stored data into "1"
db.store("some text data", "1")
#the following command deletes the cell "1"
db.remove("1")
```
## readCell (method) [str]  
Reads the content of a cell in the NekoPyRegistry  

## Database (class)  
A class to work with databases efficiently  
accepts one argument in the constructor (accessName)  
this argument is what segments fields/cell from another (so you dont have to worry about confliting field names from other developers)  
### query (method) [str]  
returns the contents of a cell, returns "" if not found  
### store (method) [bool]  
returns true on success when storing data to a cell, false otherwise  
### remove (method) [void]  
removes a cell file completely  
  
  
# utils  
```python
# Usage and examples:  

#the following 2 commands write "data" to a file then read the data
write("data", "file.txt")
data= read("file.txt")

#the following command returns the status code of a request to the website, 0 if its down
request_status_code= isUp("web.site")
#the following command returns a string of a figlet formatted string
figlet_converted_string= figlet("Example", "small") #using the "small" figlet font  

#the following command loads a module or python script to sys.modules dynamically
#uwuport is advised to not be used and use load_mod() instead  
uwuport("os") #loads "os" module into sys.modules (and can only be accessed from sys.modules["os"])
#the following command uses uwuport internally but returns a module, returns False on failure
os= load_mod("os")
```
## write (method) [bool]  
## read (method) [str]  
## isUp (method) [int]  
## figlet (method) [str]  
## uwuport (method) [bool]  
## load_mod (method) [py-module]  
