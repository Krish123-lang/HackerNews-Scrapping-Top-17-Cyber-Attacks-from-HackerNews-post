import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://thehackernews.com/search/label/Cyber%20Attack'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')


# with open(r'hacker.html', 'w') as h:
#     h.write(r.text)


data = soup.find_all('div', class_='body-post clear')

posts = []

for attack in data:
    title = attack.find("h2", class_="home-title").text.strip()

    date_published = attack.find("span", class_="h-datetime")
    if date_published is not None:
        date_published = date_published.text.replace("\ue802", "").strip()
    else:
        date_published = ""

    category = attack.find("span", class_="h-tags")
    if category is not None:
        category = category.text.strip()
    else:
        category = ""

    description = attack.find("div", class_="home-desc")
    if description is not None:
        description = description.text.strip()
    else:
        description = ""

    post = {
        'Title': title,
        'Date Published': date_published,
        'Category': category,
        'Description': description
    }
    posts.append(post)

df = pd.DataFrame(posts)
df.to_csv(r'Cyber_Attack.csv', index=None)
