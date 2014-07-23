Title: Become A Better Programmer - How To Read Source Code
Date: 2014-07-19
Category: Blog
Tags: practice, reading, command-line-parser
Slug: how-to-read-source-code
Author: Louie Dinh
Summary: How to profitably read source code

Reading soure code has many benefits. You will discover new constructs and libraries,
 develop empathy for others maintaining your code, and most importantly learn 
how to structure your code so that it doesn't fall over from internal complexity.

There is one drawback though, reading source code is darned hard. 
When I look at a new code base, this sickening feeling washes over me.
 My mind just doesn't want to dive into this perceived mess.  

This is (hopefully) a normal response. When our brains sees too much novelty,
it just tends to shy away. There is nothing for our amazing biological pattern matching
machine to latch onto. The abstractions are all new. It's never seen the
class names before. Where does execution even start?

The general tips I can offer are the following:
    1. Find and establish an initial base for your mind to latch onto. Usually the main entry point.
    2. Start from your base and explore the major features.
    3. Take notes on what you've seen.

Start At The Beginning.
-------------
The trick is to give your mind a starting point. Here is what I do. I just
run the program with the -h option and invoke the help. Then I copy one of the
help strings and do a search over the code base to see where this help text
is located. Usually the help invocation is pretty close to where the main entry
point to the program is.

Identify The Shape Of The Program
---------------------------------

Once I've found the main entry point, I run a few toy examples included
in the documentation. Then I try to trace the main blocks of code
to just get a rough sketch of how the piece fit together.

Is there a manager that invokes a ton of helper functions and classes? Are there
a bunch of classes that act as peers and hand control off between each 
other? Is there a main queue of tasks that gets consumed over time?

Getting the big picture helps you slot in the little pieces. You tend to get
overwhelmed by the details if you try to forge ahead without understanding
the main flow.

Take Notes
----------

I tend to take notes right in the source code. When writing I use a special
comment character (e.g #=> instead of the typical #) so that I can distinguish
between my own notes and the original author's comments. 

Make a note on all the clever tricks, confusing flows, beautiful usgae of 
programming constructs, and anything else you want to remember. If you're stuck,
you can also make a note about coming back to that particular section.

By writing down your thoughts, you're really making that piece of source code your
own. Over time, the constructs you pick up will start leaking into your own works.

Becoming Your Own Person
------------------------

Learning to program is a continuous process of reading code and writing code.
By exposing yourself to a variety of styles, you'll eventually develop a
unique perspective and voice. 


