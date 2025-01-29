# Hoi! Itz Da Dokz!  
welcome to the documentations for the NekoMimi python module 
as our goals for this module is to help making your coding a bit easier then a befitting easy doc is a must  

# Architecture and Submodules  
* Legacy submodules wont be covered as they will be removed in `v2.0.0`  
| SubModule      | Description                                   |
|--------------- | --------------------------------------------- |
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
```
## readCell (method) [str]  
Reads the content of a cell in the NekoPyRegistry  

# utils  
kk im beat, time to sleep lmao  
