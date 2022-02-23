# The Traveling Salesman Problem

The objective of this application is to find an efficient route for multiple package delivery trucks, a variation of the “traveling salesman problem.” 
I chose to use the “nearest neighbor” algorithm as my solution to this challenge as it is able to generate a reasonably efficient route without taking an unacceptable 
amount of computation time. This algorithm simply iterates through a list of vertices in a graph data structure, and stores the smallest edge weight, i.e., the nearest neighbor. 
The algorithm runs repeatedly until all packages have been delivered.

## Program Overview

The program begins by loading all package data from the provided csv file and inserts it into a hash table. A hash table is used because it allows for insertion and 
search operations in constant – O (1) time complexity. This enables the insert and search methods to scale to an arbitrarily high number of packages. 
To load package data, I opened the file with python’s built-in csv library and iterated through the file. Each item in each line was then used to create a package object. 
This operation scales linearly with the number of packages in the file, leading to a time complexity of 0(n). The space complexity also scales linearly with the number of packages.

The next process is to create a graph data structure and load the address data from another csv file. I chose a weighted graph structure for the address data and 
used the distance information as the weights for the edges. This is somewhat more complicated than the package data because each address has a connection to every other address. 
This leads to quadratic complexity of O (n^2) because the program must iterate through each address and then iterate through each connection for that address.

From here, the program can “load” the packages onto the trucks. This is a relatively simple operation that iterates through the packages until all have been delivered. 
There are some conditional statements used in each iteration to check special notes on the package, but these do not significantly add to the time complexity. This operation 
occurs in O (n) linear time. The operation repeats until all packages have been loaded, so n is multiplied by the number of repetitions, but this is a constant that does not
alter the time complexity.

The final aspect of the program is to create the delivery route. This is done using the nearest neighbor algorithm on the list of packages loaded onto the truck. The truck 
finds the edge weights between its current address and the delivery address of all packages. The lowest edge weight (i.e., the shortest distance) is chosen as the next delivery 
stop. For each address, this is a linear time operation, O (n). It must be repeated for each package in the list, however, rendering an overall time complexity of O (n^2) 
quadratic time.

The nearest neighbor algorithm would dominate the computational requirements of the program. The other elements are fast enough that they don’t need to be considered for the 
overall complexity of the program. Combining all the segments of the program leads to a quadratic O (n^2) time complexity. 

## Environment

This program was developed using Python version 3.9.1 and the Pycharm Community 2020.3 edition IDE. The csv methods from the python standard library are used and no
external libraries are employed.

## Employed Data Structures

**Hash tables** - are very useful data structures when search and insertion time is important. They are able to scale to an arbitrarily high number of items and maintain the celerity 
of these operations. The biggest drawback is that it is somewhat difficult to search for items by anything other than the unique identifier. If one wants to search by special 
notes of each package, for example, the program will have to iterate through all packages and return the items with matching values. This will begin to take an unacceptably 
long amount of time as the number of packages increases. 

**Graphs** - are another useful data structure for simulating geographic locations and distances. The use of an edge weight list allows for easy lookup of distances between 
vertices for use in the nearest neighbor algorithm. One issue with weighted graphs is that the edge weight list could become exceedingly large as the number of vertices 
increases, but it may still prove to be the most viable structure to use.

## Scalability

My solution to this version of the traveling salesman problem can scale to much larger number of packages. The first scalable aspect of the program is the use of a hash table 
to store packages. Because a hash table creates an index for each package by “hashing” a unique identifier, search and insert methods are constant time operations. This means 
they are unaffected by the number of packages in the table. My implementation of the nearest neighbor algorithm also enables the program to scale very well. By keeping the 
route creation to quadratic time, the algorithm can scale reasonably well to an increasing number of packages, certainly better than a brute force method. This scaling has its 
limits, though. Quadratic time can become unacceptable at large numbers of packages and different algorithms would be needed to yield an answer in a reasonable time frame.

## Potential Shortcomings

The nearest neighbor (NN) algorithm is not a perfect solution to the traveling salesman problem. Some research has shown that the route it generates can be 15% longer than 
the optimal solution. This doesn’t mean that it isn’t useful, however. NN is able to create a solution in sub quadratic time, which is significantly faster than other, more 
accurate solutions. Furthermore, NN  is relatively easy to implement, requiring only one for loop and a comparison to find the smallest distance. For these reasons, I believe 
the nearest neighbor algorithm was the best choice for my program.

## Possible Alternatives

There are some alternatives to the nearest neighbor algorithm for solving this problem. The simplest would be a “brute-force search”, where the program tries all permutations 
of possible routes and picks the one with the shortest distance. Although this is easy to implement in code, it would have extremely long computation times for even relatively 
small numbers of nodes. Since the number of permutations is a factorial of the number of nodes, this type of algorithm would have a time complexity of O(n!), out of the range 
of acceptability for this application (Johnson, 1997).
Another alternative algorithm is called Ant Colony Optimization. This solution is modelled after ants and the method they use to find efficient routes in the real world. 
“Ants” in the code travel along edges in the graph and leave “pheromones” on each edge (Blum, 2005). The pheromones are subtracted from the edge weights, and other ants will 
choose the edges with the most pheromones. This leads to near optimal solutions after many ants have traveled the graph. Although Ant Colony Optimization can produce near 
optimal results in a reasonable amount of time, the ant and pheromone systems are rather complicated to implement. For the scale of this application, I determined nearest 
neighbor was a better solution.

