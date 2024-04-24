import sys
import re

pattern = r'[aA]+\b'
for line in sys.stdin:
    line = line.rstrip()
    if(len(re.findall(pattern,line))!=0):
        line = re.sub(pattern,'argh', line,1)
        print(line)
    if(line == ''): break