import sys
import re

pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    if(len(re.findall(pattern,line))!=0):
        line = re.sub(pattern,'computer', line)
        print(line)
    if(line == ''): break