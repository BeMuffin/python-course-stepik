import sys
import re

pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if(re.findall(pattern,line)):
        print(line) 
    if(line == ''): break