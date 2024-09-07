from bs4 import BeautifulSoup
# import lxml sometimes html.parser can fail then we will use it

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.h1)
# print(soup.p)
# print(soup.prettify())
# print(soup.p)
# print(soup.a)
all_paragraph_tags = soup.findAll(name="p")

for tag in all_paragraph_tags:
    # print(tag.getText())
    pass

all_anchor_tags = soup.findAll(name="a")

for tag in all_anchor_tags:
    # print(tag.get('href'))
    pass

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

heading_class = soup.select_one(selector=".heading")
print(heading_class)