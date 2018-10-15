# This is no longer supported
# CobaltLang

<img src="https://raw.githubusercontent.com/MonliH/CobaltLang/master/logo/Main_logo.png" width="200" height="112.5" />

A transpiler for the programming language called Cobalt. Transpiles into Golang.

**Tested only on windows.**

**Still in bata phase, there are lots of bugs in the code**

## Dependencies
* [Python 3](https://www.python.org/)
* [Golang](https://golang.org/)
* [Colorama Module](https://pypi.python.org/pypi/colorama) (For better results)

## Documentation
View [the wiki](https://github.com/MonliH/CobaltLang/wiki) for the documentation.

## Build
In the terminal run these commands:

`cd C:\dir_to_Cobaltlang_src`

`python Cobalt.py C:\dir_to_code\codename.cobalt True`

Or go to the directory of your code:

`cd C:\dir_to_code`

`python C:\dir_to_Cobaltlang_src\Cobalt.py code.cobalt True`

You could also add `bin` to your path and run this:

`cd C:\dir_to_code`

`Cobalt code.cobalt True`

Building the code creates a go file in the same directory as the code.

If you write f, n, no, false, or False at the end, it will compile the Go code, but if you write t, y, yes, True, or true, it will not
compile the Go code but only turn it into Go code

For example this code will not run the Go compiler:

`cd C:\dir_to_code`

`Cobalt code.cobalt False`

## Example
Here is an example of how to print "Hello World" in Cobalt:

~~~
display:"Hello World";
~~~

Save this file as a .cobalt file.

Notice what the Go code looks like:

~~~
package main

import "fmt"

func main() {
	fmt.Println("Hello World")

}
~~~

The Cobalt tranpiller will try to make the go code the most readable.
