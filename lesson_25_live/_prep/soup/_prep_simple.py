from bs4 import BeautifulSoup

html_code = """
<html lang="en">
<body>
<h1 id="welcome-message">Welcome to my page</h1>
<div class="main-info">
    <p>Hey everyone, thanks for visiting my page</p>
    <p>My page is very empty, so you better go to <a href="https://google.com">this page</a></p>
    <p>By the way, here's an image of a cat</p>
    <img src="https://i.imgur.com/qZImY9j.jpg" alt="Cat image">
</div>
</body>
</html>"""

soup = BeautifulSoup(html_code)
print(soup.find('img'))  # Finds the first image
# <img alt="Cat image" src="https://i.imgur.com/qZImY9j.jpg"/>
print(soup.find('img').get('src'))
# https://i.imgur.com/qZImY9j.jpg # The source of the image, we can download it from this
paragraphs = soup.find_all('p')  # Finds all paragraphs
for paragraph in paragraphs:
    print(paragraph.text)  # Printing just the text
# Hey everyone, thanks for visiting my page
# My page is very empty, so you better go to this page
# By the way, here's an image of a cat
