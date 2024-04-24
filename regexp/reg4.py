# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).


import sys
import re

pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if(re.findall(pattern,line)):
        print(line) 
    if(line == ''): break