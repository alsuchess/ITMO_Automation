# class Button:
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/katalog')
#
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('/n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())


class Input:

    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text


search = Input('test1', 'test2')

print(search.Loc, search.text)

class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        return self.url

home = Page('test_url')
print(home.get())

class Soda:

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
           print(f'Газировка и {self.add}')
        else:
            print('Обычная газировка')

drink1 = Soda('Лимон')
drink2 = Soda()
drink1.show_my_drink()
drink2.show_my_drink()

