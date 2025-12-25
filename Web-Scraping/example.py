from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#---prints the file in nicer way---#
# print(soup.prettify())

print(soup.title) #prints the first 'title' tag
print(soup.title.text) #string or text works the same in essence gives the content inside a tag

finding_a_tags = soup.find_all(name='a')
for tag in finding_a_tags:
    print(tag.get('href'))


finding_via_id = soup.find(name='h1',id='name')
print(finding_via_id)

finding_via_class = soup.find(name='h3',class_='heading')
print(finding_via_class)

css_selectors = soup.select_one(selector='.heading') #gives first search
print(css_selectors)

css_headings = soup.select('.heading') #gives all as a list
print(css_headings)