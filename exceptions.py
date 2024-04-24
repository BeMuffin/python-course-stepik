class Exceptions:
    def __init__(self,gdict=None):
      if gdict is None: 
         gdict = {}
      self.gdict = gdict
    
    def get_all_parents(self,search_child,parents, graph):
      if(search_child in graph):
         for parent in graph[search_child]:
            if(parent not in parents):
                  parents.append(parent)
            self.get_all_parents(parent,parents, graph)
         return parents
          
          
    
    def check_exception_called(self, array_exs, graph):
        checked_elements = []
        result = []

        for exception in array_exs:
           parents_list = self.get_all_parents(exception,[],graph)
           print (parents_list)
           if parents_list is not None:
            if exception in checked_elements and exception not in result:
               result.append(exception)
            for parent in parents_list:
               if parent in checked_elements and exception not in result: 
                  result.append(exception)
           checked_elements.append(exception)
        print(result)
        return result
           
    def create_exception_class (self, n):
      exceptions = {} 
      
      with open('exceptions.txt', 'r') as file:
         parents_array = []
         for line in file:
            if (len(line.split(' '))==1):
               exceptions[line.replace('\n','')] = []
            else:
               child, parents = line.replace('\n','').split(' : ') 
               if child in exceptions:
                  parents_array.extend(parents.split(' '))
                  exceptions[child] = parents_array
               else:
                  parents = parents.split(' ')
                  parents_array = parents
                  exceptions[child] = parents
               
      return exceptions
   
    def check_exception (self,q, exceptions_graph):
      array_exs = []
      with open('checkexceptions.txt', 'r') as file:
         for line in file:
            array_exs.append(line.replace('\n',''))
            
      result = self.check_exception_called(array_exs, exceptions_graph)
      for ex in result:
         print(ex)

ex = Exceptions()


n = int(input())
exceptions_graph= ex.create_exception_class(n)
print(exceptions_graph)

q = int(input())
ex.check_exception(q,exceptions_graph)





# class Exceptions:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def get_all_parents(self, search_child, parents, graph):
#         if search_child in graph:
#             for parent in graph[search_child]:
#                 if parent not in parents:
#                     parents.append(parent)
#                 self.get_all_parents(parent, parents, graph)
#             return parents

#     def check_exception_called(self, array_exs, graph):
#         checked_elements = []
#         result = []

#         for exception in array_exs:
#             parents_list = self.get_all_parents(exception, [], graph)
#             if parents_list is not None:
#                 if exception in checked_elements and exception not in result:
#                     result.append(exception)
#                 for parent in parents_list:
#                     if parent in checked_elements and exception not in result:
#                         result.append(exception)
#             checked_elements.append(exception)
#         return set(result)

#     def create_exception_class(self, n):
#         exceptions = {}
#         parents_array = []
#         for line in range(n):
#             ex = input()
#             if len(ex.split(" ")) == 1:
#                 exceptions[ex] = []
#             else:
#                 child, parents = ex.split(" : ")
#                 if child in exceptions:
#                     parents_array.extend(parents.split(" "))
#                     exceptions[child] = parents_array
#                 else:
#                     parents = parents.split(" ")
#                     parents_array = parents
#                     exceptions[child] = parents

#         return exceptions

#     def check_exception(self, q, exceptions_graph):
#         array_exs = []
#         for line in range(q):
#             str = input()
#             array_exs.append(str)
#         result = self.check_exception_called(array_exs, exceptions_graph)
#         for ex in result:
#             print(ex)


# ex = Exceptions()


# n = int(input())
# exceptions_graph = ex.create_exception_class(n)


# q = int(input())
# ex.check_exception(q, exceptions_graph)
