# Code challenge

### Updates

I hit send and immediately started to think through a few improvements. I'm going to leave my original submission as `main.py` but I'm going to add them as I implement them. I've got two main ones in mind right now (4:30am my time) but maybe I'll think through a few more as I go:

- I used Bellman-Ford for longest path in my initial submission, but I realized while sleeping that Bellman-Ford with an adjacency list is basically just breadth-first search run `|V|-1` times while tracking distance through each iteration.
  - If I rewrite my current `find_longest_paths` method to include an initial breadth-first search with record-keeping of distance, it should become more flexible with respect to backwards Step Functions while also highlighting some time inefficiencies in my current implementation (& making a space-time trade-off through the use of a queue) but I'd also have to implement a negative cycle check in that case.
  - I think, by thinking of step functions in reverse, I could make this implementation efficiently handle streaming data (i.e. sequential appends to the input array) with a memory overhead to maintain state of the adjacency and distance lists.
  - I was starting to think I could get rid of my adjacency list (because the set of Step functions gives my the same "lookup" when I use each index as an argument in them), but I would probably want to maintain it as a `Set` anyway because it keeps track of which nodes I've visited.
- There are possibly more optimizations to be made with respect to sets of Step Functions that are strictly monotonically increasing, which results in a directed acyclic graph. _I imagine most by-the-book answers probably jump straight to this optimized form, so I hope you don't count it against me._ We can talk about memory-time tradeoffs, but there's also an opportunity cost for choosing extreme specificity vs. generality, and conceptualizing this problem as a graph problem seems more general to me.

### Problem Statment

- We have an array of numbers, and we start at index 0.
- At every point, we're allowed to jump from index i to i+3, i+4, or stop where we are.
- We'd like to find the maximum possible sum of the numbers we visit.
- For example, for the array `[14, 28, 79, -87, 29, 34, -7, 65, -11, 91, 32, 27, -5]`, the answer is 140.
- (starting at the 14, we jump 4 spots to 29, then 3 spots to 65, another 3 to 32, then stop. 14 + 29 + 65 + 32 = 140)
- What's the maximum possible sum we could visit for this `<ommitted>` array:

### Iniital Solution Approach:

The number of paths that can be traversed through the array is finite & can be represented as a graph (adjacency list). Then the value of the array at each index could be considered the weight to that index from any adjacent index. A more general solution might create the adjacency list from a lambda function which defines the set of adjacent indexes, but given that the current specification (+3 or +4 spaces) results in a directed acyclic graph, optimizations can allow for adjacency list to be generated at the same time as the search algorithm, using Bellman Ford to accomodate negative edge weights.
