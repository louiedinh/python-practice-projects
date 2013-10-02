Title: Lisp Interpreter
Date: 2013-08-19
Category: Pages
Tags: lisp
Slug: lisp
Author: Louie Dinh
Summary: Problem definition for a lisp interpreter

Motivation
----------

Any serious attempt at studying the art of computer programming must include a component on programming languages. Code is 
a programmer's raw material, like paint to an artist or words to a writer. Starting out, we all tend to see a programming language
as a set of directives that can be used to manipulate data. Code lives in one world and data another.  This is a limit that holds you
back from really jumping down the computation rabbit hold. The best way, that I've found, to get really understand the idea 
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


Problem Statement
-----------------
In his landmark paper ([Recursive Functions Of Symbolic Expressions And Their Computation By Machine](http://www-formal.stanford.edu/jmc/recursive.html), 
John McCarthy builds a programming language on a handful of primitive expressions. He called the language LISP for List Processing.

In this problem, Lisp will always refer to McCarthy's original Lisp.

For this project, your job is to write a Lisp Interpreter. The interpreter will take in a
text file containing a Lisp program, execute it, and then display the result.

Here is a simple Lisp program:

    (+ 2 2) => 3    # => stands for "evalutes to"

Lisp is a functional language. Every Lisp expression evalutes to value. A Lisp expression
is either an atom or a list. Atoms are strings of characters, basically anything except a parentheses.
 A list is a number of expressions enclosed within parentheses. Notice how I didn't say a list of atoms.

If you don't know recursion, I recommend you stop now and go learn recursion first. The Little Schemer
is a good place to start.

Examples of atoms: 

    a 
    1
    +
    john
    burger

Example of lists:

    (a b c)
    (john jack jim)
    ((a b c) (1 2 3) (d e f))     # This list as 3 elements. Each element is also a list.
    (+ 1 1)                       # Yes, this is a list too.

### Primitives ###

Here are all the primitives in Lisp.

    define
    lambda
    quote
    cond
    atom?
    eq?
    cons
    car
    cdr

That's it. We'll add in the basic arithmetic operators as well. They are good for examples. 
You can do clever things to derive arithmetic using only the primitives listed above,
but that's a pretty academic exercise. So we're adding:

    +
    -
    *
    /

### Expressions ###

If primitives are commands, then expressions are how you structure those
commands in such a way that the Lisp interpreter understands.

An atom alone will just evalute to it's bound value. We'll see how to bind
values to atoms in a minute.

An expression is represented as a list. The first element in the list
is the command and the other items are arguments. If any of the arguments
are also expressions, then evaluate those first.

    (+ 1 2) => 3
    (+ 3 (- 5 4)) => 4

Here are the primitives in action:

    # define is for binding a value to an atom
    (define a 3)
    a => 3
    # quote returns the atom itself, instead of evaluating it.
    (quote a) => a
    

### Evaluation ###







Code References
-----------

* [Lispy](http://norvig.com/lispy.html) - Peter Norvig
* [Lithp](https://github.com/readevalprintlove/lithp) - Michael Fogus

Background Readings
-------------------

* [Rich Programmer Food](http://steve-yegge.blogspot.ca/2007/06/rich-programmer-food.html) - Steve Yegge
* [Beating The Averages](http://www.paulgraham.com/avg.html) - Paul Graham
* [The Art of Lisp and Writing](http://www.dreamsongs.com/ArtOfLisp.html) - Richard Gabriel

