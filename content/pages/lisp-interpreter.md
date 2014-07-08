Title: Lisp Interpreter
Date: 2013-10-20
Category: Pages
Tags: lisp
Slug: lisp
Author: Louie Dinh
Summary: Problem definition for a lisp interpreter

Lisp Interpreter
===============

Motivation
----------

Any serious attempt at studying the art of computer programming must include a component on programming languages. Code is 
a programmer's raw material, like paint to an artist or words to a writer. Starting out, we all tend to see a programming language
as a set of directives that can be used to manipulate data. Code lives in one world and data another.  This is a limit that holds you
back from really jumping down the computation rabbit hole. The best way, that I've found, to get really understand the idea 
"code is data" is to implement your own interpreter.

This project is focused on producing a Lisp interpreter, more specifically a Scheme interpreter. You may be wondering, why are we writing 
an interpreter for an outdated AI language? Lisp is a good project because the syntax is exceedingly simple. There is one main
syntax construct and a few special cases that make up the entire language. This simplicity clears away a slew of problems and 
exposes the main insight of code/data equivalence.

Also, Lisp is worth learning because it makes you a better programmer. That's not only my opinion. Great hackers of the past
have agreed with the sentiment.

>Lisp is worth learning for the profound enlightenment experience you will have when you finally get it;
>that experience will make you a better programmer for the rest of your days,
>even if you never actually use Lisp itself a lot.
-Eric Raymond

Prerequisites
------------

**Recursion**: Before dealing with Lisp, you should have a firm grasp of recursion. The best resource I've found for exploring
            recursion is the book The Little Schemer.

**Basic Lisp**: It is helpful if you've downloaded a Lisp interpreter like Dr Racket and typed in a few commands. You don't need
             extensive knowledge, but an hour noodling around with the interpreter would be beneficial. Once again, I recommend
             The Little Schemer if you want a thorough introduction.


Problem Statement
-----------------
In his landmark paper, 
[Recursive Functions Of Symbolic Expressions And Their Computation By Machine](http://www-formal.stanford.edu/jmc/recursive.html), 
John McCarthy builds a programming language on a handful of primitive expressions. He called the language LISP for List Processing.

In this problem, Lisp will always refer to McCarthy's original Lisp.

For this project, your job is to write a Lisp Interpreter. The interpreter will take in a
text file containing a Lisp program, execute it, and then display the result.

Here is a simple Lisp program:

    (+ 2 2) => 3    # => stands for "evalutes to"

Lisp is a functional language. Every Lisp expression evalutes to value. A Lisp expression
is either an atom or a list. Atoms are strings of characters, basically anything except a parentheses.
A list is a number of expressions enclosed within parentheses. Notice how I didn't say a list of atoms.

Examples of atoms: 

    1
    +
    john
    burger

Let's take a look at these atom examples. 1 is just a number, similar to an int in C or Python.
 However, +, john and burger are a bit unusual. In Lisp, these are called symbols. You may find
 it tempting to draw an analogy of strings to symbols. Don't. They are completely different beasts. 

The concept of a symbol is implicit in other languages, Lisp just exposes the concept explicitly.
 In other languages, symbols are used as variable names. To execute your programs, a compiler/interpreter
 will tokenize your source code and then identify these symbols. In Lisp, symbols are also used to
 as identifiers for variables, however you get to muck with them directly. Symbols are just entities
 that you can bind values to.

Now let's talk about lists. A list is just the symbol '(', followed by a series of elements
separated by spaces, and then a closing ')'.

Example of lists:

    (a b c)
    (john jack jim)
    ((a b c) (1 2 3) (d e f))     # This list as 3 elements. Each element is also a list.
    (+ 1 1)                       # Yes, this is a list too.


### Normal Forms ###

For the sake of simplicity, let's build a Lisp that only has 4 normal builtin functions:

    +
    -
    *
    /

They do exactly what you think they do: Add, subtract, multiply and divide.

The rules for evaluating a normal lisp expression or form is easy. Take first element in
a list, look up it's value and apply it to the other elements in the list. For example:

(+ 1 2) => 3

Remember our discussion about symbols earlier? + is just a symbol which is by default bound
to the function we know as addition. So when we enter the form (+ 1 2) into the interpreter,
Lisp looks up the function associated with +, which is addition, and then applies it to the
arguments 1 and 2. 

If the arguments are also lists, rather than atoms, then evaluate the arguments first
before evaluating the parent expression. Example:

    (/ (+ 2 10) 3) #=> 4

The nesting of the expression completely defines the order of operations. This is nice because
there is never any ambiguity.

### Special Forms ###

Now here is where the magic happens. Remember how I said Lisp only has a handful of primitives?
Here are ALL the primitives required for a fully functioning Lisp. 

    eq?
    quote
    cons
    car
    cdr
    atom?
    define
    lambda
    cond

Let's go through each in turn. Pay attention because some of these forms _do_ _not_
follow the normal evaluation order we learned above. 

**eq?** just tests for equality. It returns True if the two arguments
are the same, otherwise false.

    (eq? 1 1) #=> True
    (eq? 1 2) #=> False

**quote** is the first special form we will encounter. Quote says to Lisp, "don't evaluate what I'm 
about to pass in, just give me back the symbols exactly as I typed them".

    (quote a) #=> 'a
    (quote '(1 2 3) #=> '(1 2 3)

The little ', is Lisp's way of saying that everything that follows is a symbol.

**cons**, **car** and **cdr** go together. Cons is like a piece of velcro, it sticks two things together.
Car let's to get back the first piece and cdr lets you get the second piece.

    (define box (cons 3 4))
    (car box) #=> 3
    (cdr box) #=> 4

Lists are just boxes within boxes, like russian dolls. When you take the car of a list,
you get back the first item. When you take the cdr, you get a list with the rest of the elements.
When you keep opening them, eventually you get left with an empty box.

    (define some-list '(1 2 3))
    (car some-list) #=> 1
    (cdr some-list) #=> '(2 3)
    (cdr (cdr (cdr some-list))) #=> '() which is our empty list, sometimes called nil

**atom?** will tell you whether or not the argument is an atom.

    (atom? 3) #=> True
    (atom? '(1 2 3) #=> False


**define** binds values to symbols.

    (define a 5)
    a #=> 5
    (define b (+ a 1))
    b #=> 6
    (+ a b) #=> 11

**lambda** creates a function. It takes in a list of parameters and a body 
and spits out a function that takes in the parameters and executes the body
with the parameters substituted with the passed in values.

    (define square (lambda (x) (* x x)))
    (square 5) #=> 25
    (define divides_evenly? 
        (lambda (x y) 
            (eq? (* x 
                 (/ x y)) 
            y)))
    (divides_evenly? 5 2) #=> False

Finally we have **cond**, the generalized if statement. It is just a bunch of
if/else blocks that executes the first matching condition and returns
the associated value. Here is the example:

    (define a 3)
    (cond  ((eq? a 1) 'one)
           ((eq? a 2) 'two)
           ((eq? a 3) 'three)
           (else 'no-idea)) # => 'three 

Your Task
---------

Write a small Lisp interpreter that supports all the functionality described above.


Code References
-----------

* [Lispy](http://norvig.com/lispy.html) - Peter Norvig
* [Lithp](https://github.com/readevalprintlove/lithp) - Michael Fogus

Background Readings
-------------------

* [Rich Programmer Food](http://steve-yegge.blogspot.ca/2007/06/rich-programmer-food.html) - Steve Yegge
* [Beating The Averages](http://www.paulgraham.com/avg.html) - Paul Graham
* [The Art of Lisp and Writing](http://www.dreamsongs.com/ArtOfLisp.html) - Richard Gabriel

Acknowledgements
----------------

Thanks to Manish Gill for proof-reading drafts.

