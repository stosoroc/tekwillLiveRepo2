class Author:
    username: str


class Icon:
    name: str
    image: str
    url: str


class Category:
    name: str


class IconSet:
    icons: list[Icon]
    author: Author
    download_url: str
    category: Category


class Sticker(Icon):
    pass


class InterfaceIcon(Icon):
    pass


class AnimatedIcon(Icon):
    images: list[bytes]



