
class Graph():

    def __init__(self, input_array, step_rules):
        self.array_values = input_array
        self.step_rules = step_rules
        self.adjacency_list = {}
        self.distance = {}
        self.predecessor = {}
        self.found_longest_paths = False
    
    def traverse(self):
        queue = list()
        queue.append(0)
        while len(queue) > 0:
            node = queue.pop(0)
            self.add_node(node)
            for neighbor in self.adjacency_list[node]:
                if not neighbor in self.adjacency_list:
                    queue.append(neighbor)
                    self.add_node(neighbor)
                # Check if current total distance to neighbor can be improved
                if self.distance[neighbor] < self.distance[node] + self.array_values[neighbor]:
                    # Set new maximum total distance
                    self.distance[neighbor] = self.distance[node] + self.array_values[neighbor]
                    # Note that the node is the current best option leading to this neighbor
                    self.predecessor[neighbor] = node
    
    def find_longest_paths(self):
        if len(self.adjacency_list) == 0:
            self.traverse()
        
        for x in range(len(self.adjacency_list)-1):
            for node in self.adjacency_list:
                for neighbor in self.adjacency_list[node]:
                    # Check if current total distance to neighbor can be improved
                    if self.distance[neighbor] < self.distance[node] + self.array_values[neighbor]:
                        # Set new maximum total distance
                        self.distance[neighbor] = self.distance[node] + self.array_values[neighbor]
                        # Note that the node is the current best option leading to this neighbor
                        self.predecessor[neighbor] = node
        self.found_longest_paths = True
    
    def add_node(self, idx):
        # Even though the +3 Step or +4 Step cover almost all indexes, it's possible some other Step Rules
        # might want to be implemented. This method gives a good entry point
        if not idx in self.adjacency_list:
            # Initialize the Distance to the new Node (-Infinity) or array[0] for the first Node
            self.distance[idx] = self.array_values[idx] if idx == 0 else float('-inf')
            # Initialize valid adjacent indexes.
            self.adjacency_list[idx] = [x for x in [f(idx) for f in self.step_rules] if x < len(self.array_values)]
            for neighbor in self.adjacency_list[idx]:
                if not neighbor in self.distance:
                    self.distance[neighbor] = float('-inf')

    def find_max_sum_dag(self):
        if len(self.adjacency_list) == 0:
            self.traverse()
            self.found_longest_paths = True
        return max(self.distance.values())
    
    def find_max_sum(self):
        if not self.found_longest_paths:
            self.find_longest_paths()
        return max(self.distance.values())

    def longest_paths(self):
        if not self.found_longest_paths:
            self.find_longest_paths()
        max_value = max(self.distance.values())
        max_keys = [k for k, v in self.distance.items() if v == max_value]
        return [self.generate_path(max_key) for max_key in max_keys]
    
    def generate_path(self, origin):
        next_node = origin
        path = []
        while next_node != 0:
            path.append(self.predecessor[next_node])
            next_node = self.predecessor[next_node]
        return path[::-1]

    def print_paths(self):
        print(self.longest_paths())
    
    def print_distances(self):
        if not self.found_longest_paths:
            self.find_longest_paths()
        print(len(self.distance))

given_step_rules = [lambda x: x + 3, lambda x: x + 4]
test_array_1 = [14, 28, 79, -87, 29, 34, -7, 65, -11, 91, 32, 27, -5]
test_graph_1 = Graph(test_array_1, given_step_rules)
test_answer_1 = test_graph_1.find_max_sum_dag()
print(test_answer_1)
test_graph_1.print_paths()

test_array_2 = [
    95, 69, 68, 44, 0, 53, 34, -83, -8, 38, -63, -89, 34, -91, 1, 39, -7, -54, 85, -25, -47, 89,
    -57, -18, -22, -50, -74, -91, -38, 99, 73, 7, 44, -47, -35, -70, 26, -54, -28, 7, -26, -73, -48, 
    -76, -18, 94, -54, 65, -71, -10, 5, 64, 55, 68, 7, 41, -52, 57, -75, 90, -21, -47, -88, -5, -9, 46, 
    -8, 71, 34, 82, 10, -37, 37, 1, 49, 91, 80, 57, -56, 83, -58, 24, -34, 30, -65, 42, -28, -84, -58, -62, 
    20, 89, -43, -16, 9, 37, -21, -71, -27, 93, 93, 3, 24, 51, 19, -54, -20, 43, 96, 15, -4, -30, -12, -88, 
    95, -89, 63, 63, 26, 34, 9, 66, 40, 59, -69, -29, -3, -89, -58, 45, 68, 45, 92, -51, 89, -75, 0, 14, 46, 
    -20, -90, -83, 82, 29, -32, 68, 55, 41, -85, 56, 97, -11, -25, -28, 65, 61, 54, -36, -24, 98, 49, 19, 3, 
    -94, -46, 26, 92, -72, -29, 93, 71, 15, 3, -89, -66, -85, -42, 83, 43, 27, 76, 71, 62, 44, 9, 2, 40, 8, 
    78, -6, -61, -93, 28, -46, -48, 25, -34, -91, 73, 90, 77, -5, 98, 1, -5, -85, 63, -15, 57, 20, 71, -67, 
    -60, -46, -71, -9, 62, 99, 80, -15, 53, 29, 52, -91, -78, -77, -57, 21, -74, 46, -11, 74, -21, -48, -7, 
    -56, 54, 8, -51, -61, -46, 79, 42, 97, 61, 40, -99, -13, 55, -53, -71, 80, 31, -35, 77, 89, -2, 75, 59, 
    -66, 87, 23, 48, 80, -28, 86, 54, 37, -41, 95, -87, 79, -49, 8, -95, 66, 79, -38, 75, 49, -30, 7, -46, 
    -44, 43, -26, -63, 23, 77, -8, 36, 83, 10, 12, -34, 32, -63, -32, 47, -5, 53, 66, 32, 14, 24, 28, 57, 
    -48, -89, -51, -26, -21, -37, -41, -17, -40, 19, 25, 89, -11, 92, -43, -50, 53, -36, 50, -12, 68, -28, 
    18, 62, -48, -86, 87, -80, 58, 73, -93, 81, -86, 26, 3, 51, 74, 37, 45, 85, 12, 49, 93, -93, -5, 61, -64, 
    -48, -11, 68, -36, -83, -18, 30, -53, -88, 6, 43, -38, 50, -28, 91, 49, 21, 86, -15, -18, 2, 0, 55, -73, 
    85, -49, -18, -90, 89, 79, -21, 23, 38, 43, 83, 72, 63, 14, -35, 81, -2, -71, 70, 51, -26, -20, 74, 10, 
    -37, 61, -29, -62, 18, -46, 75, 98, 18, -4, 25, 13, 70, -34, 79, 16, -55, -7, -56, -55, 79, 29, 13, -31, 
    -12, -29, -33, 12, 17, -5, -59, -12, 76, -6, -4, -5, -90, -45, -33, -14, -56, 64, -99, -65, -98, -97, 35, 
    -50, -63, 8, -7, -46, 3, -69, 24, -23, -6, 78, -21, 2, -99, -29, 75, 40, -30, -40, 10, -41, -65, -42, -88, 
    -8, -32, -2, -39, -95, -73, 32, 99, -35, -88, 81, -32, -19, 58, 83, -73, -23, 1, -34, -40, -39, 35, -52, 
    -24, 57, -44, 2
    ]

test_graph_2 = Graph(test_array_2, given_step_rules)
test_answer_2 = test_graph_2.find_max_sum_dag()
print(test_answer_2)
test_graph_2.print_paths()