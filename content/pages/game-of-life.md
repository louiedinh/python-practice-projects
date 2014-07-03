Title: Game of Life
Date: 2014-07-01
Category: Pages
Tags: project
Slug: game-of-life
Author: Louie Dinh
Summary: Problem definition for a Game Of Life

Motivation
----------

Sorry to disapoint you but the word game is used very loosely here. We'll be trying
to build [Conway's Game Of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). 
You should click the link and take a look. I'll give you a sec...

Welcome back! The whole fascination behind the GOL is the shocking simplicity behind
these shockingly complex interactions. Just playing around with the demonstration is 
enough to drive home the true beauty of emergent complexity.

As the player, your only interaction is to set the initial configuration of the system.
After you hit the start button, you can just sit back and watch how the cute little
cells evolve into colonies or go extinct.

Here are a few especially notable patterns that arise.

Glider - a colony of cells that crawls across the screen:

![Glider Image](http://upload.wikimedia.org/wikipedia/commons/f/f2/Game_of_life_animated_glider.gif)

Loaf - a stable pattern, looks a bit like bread I guess.

![Loaf Image](http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Game_of_life_loaf.svg/98px-Game_of_life_loaf.svg.png)

Pulsar - A complex repeating pattern that will continue indefinitely when left alone.

![Pulsar Image](http://upload.wikimedia.org/wikipedia/commons/0/07/Game_of_life_pulsar.gif)


Dependencies
-----------

You'll need some sort of graphical library to handle the drawing bits. I recommend
using [curses](https://docs.python.org/3/library/curses.html) library. It's widely
available and is very simple to use.

You can get away with just learning how to move the cursor, insert a character, 
deleting a character, and clearing the screen. 


Problem Statement
-----------------

The Game of Life has two modes and some very simple rules.

The entire game exists on a grid. You can make the grid the size of your
screen (in characters).

In phase 1, the player gets to create a starting layout. If you're
using the curses library then just allow the player to navigate
the cursor around with the arrow keys and create a cell with the space bar.
I usually use the character 'o' to represent a filled in cell and a blank
space for an empty cell.

Once the player has created an initial layout, he starts the simulation. 
The simulation proceeds in a series of time slices. A designated keypress,
will advance the simulation by one time slice and shows the next calculated 
frame.

Each spot on the board evolves according to the state of the 8 neighbouring spots.
Here are the rules for the evolution.

    Any cell that has less than two neighbouring cells dies from loneliness.
    A cell that has two or three neighbour stays alive for the next generation.
    A cell that has more than three neighbhour dies of overcrowding.
    Any empty spots that has exactly 3 (party eh?) cells as neighbhours gets a live cell from reproduction.

Your Task
---------

Build the Game of Life! 

Bonus Points:
    Color code the cells based on the generation in which they were born.
    Have a way to record and replay previous evolutions.
    Have more intuitive interactions like "play for 10 generations" 


References
-----------

* [Wikipedia](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) - Wikipedia
