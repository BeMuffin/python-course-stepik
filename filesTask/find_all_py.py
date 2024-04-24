import os

current_directory = os.getcwd()

files_list = []
for root,dirs,files in os.walk(current_directory+'/filesTask/main'):
    for file in files:
        if file[-3:] == '.py':
            filepath = os.path.join(root).replace('/home/hanna/Documents/DS/python-courses/filesTask/', '')
            if filepath not in files_list: 
                files_list.append(filepath)

sorted_list = sorted(files_list)
print (sorted_list)

with open('filesTask/output_files_path.txt', 'w') as file:
    for filepath in sorted_list:
        file.write(filepath +'\n')
        