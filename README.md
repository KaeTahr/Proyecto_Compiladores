# Language++
A small programming language for our Compiler Design class.

## Syntax
The language requires the first line of every program to be:

### Program start
```program programName;```

### Class Declaration
After this, classes can be defined using the following syntax:
```C++
class ClassName {
  attributes
    int at1;
    float at2;
    char at3;
  methods
    int function getAt1() { return(at1); }
  };
  
 ```
 Classes support inheritance for up to one level.
 
 In order to have a class inherit from another one, the syntax is the following:

#### Inheritance
```C++
class class2 inherits className {
   ...
```

### Variable declaration
After class declaration, global variables may be declared using the following syntax:

```C++
variables {
   int: var1, var2, var3;
}
```

### Function declaration
After global declaration, functions may be declared using the following syntax:

```C++
int function add(a:int, b:int)
{
   return(a + b);
}
```

### Main
Finally, a main must be declared. Note that the main doesn't have local variables, and may only interact
directly with global variables.

```C++
main() {
write(add(3,4));
}
```

## Limitations
The language has some limitations:
- Objects declared locally in functions may have their methods not work.
- As classes must be defined before globals, methods may not interact with globals
- 2D matrices and arrays are supported, but not as attributes

## Compiling a program
In order to compile the program, run the parser located in source directory, on the text file containing your source code:
```shell
python parser.py source.txt
```

## Running a program
 The parser will generate a file called intermediate.out.
 
 In order to run your program, you must run this file using the virual machine
 
 ```shell
 python virtualmachine.py intermediate.out
```

## Examples
Full examples are located in the source/tests directory.
