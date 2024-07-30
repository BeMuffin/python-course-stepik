# classes_list = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

classes_list = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

# Ch : P
# A  :  -
# B  :  A, C
# C  :  A
# D  :  C, F
# E  :  D
# F  :  -


# A for A,B, C, D, E - 5
# B for B - 1
# C for C,B,D,E
# D for D,E
# E for E
# F for D,E,F



import json

js = json.loads(input())


print(js)
parents_count_dict = {

}

def find_parrents_count(classes_list, parent_count_dict):
    for cl in classes_list:
        if cl['name'] not in parent_count_dict:
            parents = get_all_parents(cl['name'],[],classes_list)
            if parents is not None:
                parent_count_dict[cl['name']] = len(parents) + 1
            else:
                parent_count_dict[cl['name']] = 0


def get_all_parents(search_parent,parents, classes):
    for cl in classes:
        # if cl['name'] == search_child:
        if search_parent in cl['parents']:  
            parents.append(search_parent)
            # get_all_parents(parent,parents, classes)
    return parents


find_parrents_count(js, parents_count_dict)
print (parents_count_dict)
for key, value in parents_count_dict.items():
    print(f'{key} : {value} ')   