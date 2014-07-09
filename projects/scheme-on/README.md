Syntax
======
scheme-on only implements the bare-bone essentials of a Lisp. 
There is enough here to write anything you want though.

Booleans
--------
#t is True
#f is False

Numbers
-------
1, 2, 3, ... You get the idea.

Lists
-----
(cons x y) => Returns the cons cell of two things
(car z) => Returns the first part of the cons cell
(cdr z) => Returns the second part of the cons cell

Predicates
----------
Always returns a boolean.
atom? => Check if an object is an atom
eq? => Checks if two atoms are equal
empyt? => Checks if a list is empty

Functions
---------
Use lambda to define a function
(lambda (var1 var2 ...) body)

Quoting
-------
(quote x) will return the symbol x rather than the value bound to x.

Definitions
-----------
(define var value) => Binds value to variable


The Interpreter
===============
python3 scheme_on.py

Running Tests
-------------
python3 tests.py


Sample Code
================
(define + (lambda (x y) 
    (cond ((zero? x) y)
          (#t (+ (sub1 x) (add1 y))))))
