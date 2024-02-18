# Treat (Tree-it)

## Some definitions
First let's define some terms:

- A Tree: will be the Tree ID followed by it's coordinates
- A Treater: will be a city employee with a name given and a starting point
- Quests: A list of Trees and a treater that will take care of those given trees in order and a map to help


## This POC takes into account
- The starting position: it is made in a way that starts with any given starting position for each treater, and also if they all start from the same point
- To have an average of 'numbers of trees treated' / 'distance traveled' to make it fair for most employees

## Some Edge Cases
This script is a proof of concept and doesn't take into account
- The time needed to cut down a tree (The entire procedure + mishaps)
- The available time a treater has in a day (+ breaks ect)
- The different trees and how much time they take to be treated

### INPUT

- A list of treaters with their starting coordinates

### OUTPUT 

- A planning for each treater of their path to take for X time (not provided)