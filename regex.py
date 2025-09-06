import re

page = ''
with open('followers.txt', 'r', encoding='utf-8') as f:
     page = f.read()

females = re.findall(r'\b\w+[yi]\s\w+\b', page)

for i, fname in enumerate(females):
     print(i+1, fname)