# Eager Dijkstra's Algorithm Tool in Python3

This is a implementation of Eager Dijkstra's algorithm in Python3. I built it in a day so still needs polishing


Dijkstra's algorithm is used to find shortest path from a given starting point to the destination. It has many applications from Google map navigation, Uber rider assignment to functioning of the internet. Open shortest path first and IS-IS algorithms are based on Dijkstra's algorithm


**Requirements -**
The only requirement is `pandas` which can be installed by `pip install pandas`


**Installation -** 
Just clone the repo and place text file with node and edge info in the same directory. 


**Usage -**
To be added


**Flow -**
- Reads nodes and edges from `map.txt`. The format is as follows ---- {node1 node2 distance}
- Converts the dataframe in dictionary for faster processing
- Passes the dictionary to search() function
- search() function returns list with shortest path and the distance on that path


### I found these videos really helpful in implementation -
- [Dijkstra's Algorithm - Computerphile](https://www.youtube.com/watch?v=GazC3A4OQTE)
- [Dijkstra's Shortest Path Algorithm | Graph Theory](https://www.youtube.com/watch?v=pSqmAO-m7Lk)


### TODO -
- [ ] Make it general purpose
- [ ] Accept user input in an efficient manner
- [ ] Speed optimizations
- [ ] Comment the code 
