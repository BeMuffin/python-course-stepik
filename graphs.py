# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
# Sample Input:

# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A

# Sample Output:

# Yes
# Yes
# Yes
# No

# def add_to_graph (parent, childs, graph):
#     graph[parent] = childs
#     return graph

# def find_path (graph, start, end):



# n = int(input())

# for i in range(n):
#     parent, childs = input().split(' : ')
#     childs = childs.split(' ')
#     graph = add_to_graph (parent, childs, graph)
#     print (graph)

class graph:
   def __init__(self,gdict=None):
      if gdict is None: 
         gdict = {}
      self.gdict = gdict
    
    
   def is_parent(self, search_child, search_parent, graph):
        if search_parent == search_child:
            return True
        if search_child not in graph:
            return False
        for parent in graph[search_child]:
            if self.is_parent(parent, search_parent, graph):
                return True
        return False
   
   # def create_graph (self, n):
   #    graph = {}  
   #    for i in range(n):
   #       str = input()
   #       if (len(str.split(' '))==1):
   #          graph[str] = []
   #       else:
   #          child, parents = str.replace('\n','').split(' : ')
   #          parents = parents.split(' ')
   #          graph[child] = parents
         
   #    return graph
   
   def create_graph (self, n):
      graph = {} 
      
      with open('classes.txt', 'r') as file:
         parents_array = []
         for line in file:
            if (len(line.split(' '))==1):
               graph[line] = []
            else:
               child, parents = line.replace('\n','').split(' : ') 
               if child in graph:
                  parents_array.extend(parents.split(' '))
                  graph[child] = parents_array
               else:
                  parents = parents.split(' ')
                  parents_array = parents
                  graph[child] = parents
               
      return graph
   
   def check_graph_element (self,q, graph):
      with open('checks.txt', 'r') as file:
         for line in file:
            parent, child = line.replace('\n','').split(' ')
            result = self.is_parent(child, parent, graph)
            if(result == True): print('Yes')
            else: print('No')
   

g = graph()


n = int(input())
graph_elements = g.create_graph(n)
print(graph_elements)

q = int(input())
g.check_graph_element(q,graph_elements)
 






