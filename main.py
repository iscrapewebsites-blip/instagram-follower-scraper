from lxml import html

page = ''
with open('page.html', 'r', encoding='utf-8') as f:
     page = f.read()

tree = html.fromstring(page)
elems = tree.xpath('//span[@class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"]')
data = []
for elem in elems:
     if elem is not None:
          if elem.text is not None:
               name = elem.text.strip().replace('  ', ' ')
               name_list = name.split('  ')
               title = name_list[0]
               title = title.strip()
               sur = name_list[-1]
               sur = sur.strip()
               if title==sur:
                    sur=''
               data.append(f'{title} {sur}')

               
with open('followers.txt', 'w', encoding='utf-8') as f:
     for name in data:
          f.write(f'{name} \n')
