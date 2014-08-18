This is my take on the game of life. It implements all the fundamental logic of the traditional game, but 
adds a few nice shortcuts.

Normal Mode lets you play the traditional game.
Insert Mode allows you to quickly drop cells rather than one at a time.
Pan Mode lets you scroll around the infinite landscape to see your off-screen critters.

There is also a secret mode ;) See if you can't figure out what it does.


Starting the Game
------------------
python3 game_of_life.py

Running Tests
-------------
python3 tests.py

Controls:
---------
* left/right/up/down - Move cursor or pans depending on mode.
* q - quit
* c - insert a cell
* x - delete a cell
* space - step to next generation

Advanced Controls:
------------------
* i - Switch to insert mode. Cursor leaves a trail of cells.
* p - Switch to pan mode. Pans around map. Doesn't move cursor.
* n - Switch back to normal mode. 




