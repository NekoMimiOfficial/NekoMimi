from NekoMimi import tools as nm

#Figlet test also tests the banner and colors
nm.yellow(nm.figlet("NekoMimi","larry3d"))

#binary
nm.blue(nm.nekoBinConverter(511))

#urban test which also tests jsonAPI
nm.blue(nm.urban('NekoMimi'))

#isUP test
nm.blue(f"{nm.isUp('https://google.com')} is the status of google.com")

#debug
#add -v for debug
nm.debug("Debug message")

#done
nm.green("Unit test completed")
