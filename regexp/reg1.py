import sys
import re

pattern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    if(len(re.findall(pattern,line))>=2):
        print(line) 
    if(line == ''): break

    

# pattern = r'cat'
# string = 'catcatca'

# print(re.findall(pattern,string))