graph={'b': ['a'], 'c': ['b'], 'd': ['c'], 'e': ['d']}

def get_all_parents(search_child,parents, graph):
    if(search_child in graph):
        for parent in graph[search_child]:
            if(parent not in parents):
                parents.append(parent)
            get_all_parents(parent,parents, graph)
        return parents

print(get_all_parents('a',[],graph))       