# Pyrogue

This is a working title - we may or may not come up with a better one. Our plan is to make a fully functional roguelike within the few weeks that we have for the project. This shouldn't be too much of a hurdle - we already have a character on the screen.

If you haven't already, you should be able to clone this repo and have everything that you need (except an editor and python, but I'm assuming you already have that). Here's a quick and dirty guide to getting your computer set up so that you can work on the project:

# Set up

You will need python installed, but since we have been using python all year I won't cover that. In addition, you will need a decent text editor, the github for windows app, and you need python on your PATH.

## Editors

There are many to choose from, but we have pretty much defaulted to Sublime Text. You can download it [here](http://www.sublimetext.com/2). You can drag the project folder on to Sublime when it is open, and it will allow you to quickly switch between the different files in the project. The project folder should be (if you used github for windows) in the Github folder in your My Documents.

## Github for Windows

You can download the Github desktop app [here](https://windows.github.com/). This should be much easier than using the commands on Windows. You simply clone this repo, then make changes, commit them, and then sync them. Rob was having trouble with the sync command; if that happens to you, open the git command line and run git push.

## Adding Python to your PATH

Your python should be in C:\Python34 (make sure). Go to my computer, system properties, advanced system properties, environment variables, then scroll through the list on the bottom until you find PATH. Edit this variable, and add a semicolon at the end, followed by C:\Python34 (or where ever your python is). You should now be able to run your code from within Notepad++ or Sublime Text (Control-b runs your code in Sublime).

# Python

We went over functions and classes today in our meeting, but I know some of you had class so you had to leave. I suggest these learning materials if you want to go over functions and classes:

These are going to be links from Learn Python the Hard Way, which is a great free resource, and it's how I learned Python, but it uses Python 2, which is a little different (but mostly the same). You probably won't be able to type these in verbatim and have them run, but you should only need to change a few things (print didn't need parentheses back then, that's the main one).

## Functions

http://learnpythonthehardway.org/book/ex19.html
http://learnpythonthehardway.org/book/ex20.html
http://learnpythonthehardway.org/book/ex21.html

## Dictionaries

http://learnpythonthehardway.org/book/ex39.html

## Classes and Objects

http://learnpythonthehardway.org/book/ex40.html
http://learnpythonthehardway.org/book/ex41.html
http://learnpythonthehardway.org/book/ex42.html
http://learnpythonthehardway.org/book/ex43.html
http://learnpythonthehardway.org/book/ex44.html

# Roguelike Development

We are using a library called [libtcod](http://doryen.eptalys.net/libtcod/), which handles a lot of the tedious stuff like making a window, and drawing in it, for us. There is a tutorial that uses python and libtcod on Roguebasin [here](http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_1#Moving_around), and I'm going to be going through it to familiarize myself with the library. I suggest you do the same, but you don't have to. I'm going to be handling most of the drawing to screen code, and you guys will be working with normal python most of the time.

# TODO

Here is a list of things that need to be done before our game is complete. I may assign some of these, but you should just choose the ones that look the most interesting. I'm going to break these down into design and code.

If you work on an aspect of design, please write up your ideas in a markdown file like this one and push it to the repo. That way we can all colaborate on them and keep on the same page. (Markdown is really simple - you just write like normal and headers are "#" before the word - more "#"s is a smaller header).

If you work on code, please comment it thoroughly and write test cases for your code. I will go into how to do this next time we meet, but it will help us make sure our code does what we want it to. (I will write the test cases at first so we can get started faster).

## Design

General Theme and Storyline (doesn't have to be super in depth - this isn't an RPG)

### Character

Races
Classes
Attributes
Rules for generating stats (should involve some randomness and class/race)

### Monsters

Races
Classes?
Attributes (should be same or similar to character)
Rules for stat gen (should be similar to character)

### Clothing / Armor

Slots
Types
Huge list of names associated with attributes (i.e. Helm of drowsiness - -1 alertness, what have you)

### Weapons

Slots
Types
Similar list to clothing/armor

### Jewelry

Slots
Types
List

### Special Attacks

Cost (hunger, mana, etc.)
Damage or power
Effects
List

#### Spells

Same idea as the special attacks, but more effects
Element or type?
etc.

### Supernatural

Dungeon Crawl Stone Soup has a large number of deities which give the player bonuses, etc. May be interesting to include. If not deities something similar - possibly political or philosophical ideologies since we are making a steam punk game?

### Rules of engagement

What stats are important in combat?
How does the physics of combat work (i.e. do we want to deal with the granularity of broken bones/fingers and have that influence the ability to block, or do we just want to go with damage and percentage chance?)

## Code

### Levels

Need a data structure to store a level efficiently, and be able to update all creatures in the level every turn (may be just storing the level and creatures independently - something to look in to)

Need an algorithm for generating levels of an arbitrary size pretty quickly, and populating a level with loot, random events, monsters, etc.

Need a way to make sure there is always at least one path from level to level - may not be too difficult, but it could become a problem if there are locked doors, etc.

Need to figure out how monsters could follow the player through the stairs without having to simulate the entire dungeon the whole time - maybe simulating the two adjecent floors wouldn't be too bad? Something to look into

### Creatures

Need a class that represents creatures - player and monsters would inherit from this. It should contain attributes, how to generate them, attack/defend code, special attack and spells code, inventory, wearing/equiped items should influence stats, etc.

Monster class would add on some AI - what direction should I move next? Do I need to eat or drink or rest? Should I equip this or this, etc.

Character class wouldn't need much more since the player will handle movement and AI himself.

### Graphics

Need a way to show only the visible tiles (brogue does this, I believe)

Need a way to color characters depending on environment (brogue, again)

Need to figure out best symbols for various game entities (but this is more design)

Need a menu, tutorial, instructions, quit, etc.
