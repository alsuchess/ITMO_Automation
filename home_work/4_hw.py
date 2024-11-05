class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
            return self.width * 2 + self.height * 2

    def square(self):
            return self.width * self.height

piece1 = Rectangle(5, 6)
piece2 = Rectangle(7, 8)
piece3 = Rectangle(9,10)

print(f"Периметр первой фигуры: {piece1.perimeter()}, а площадь: {piece1.square()}")
print(f"Периметр второй фигуры: {piece2.perimeter()}, а площадь: {piece2.square()}")
print(f"Периметр третьей фигуры: {piece3.perimeter()}, а площадь: {piece3.square()}")

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

piece4 = Math(4,1)

piece4.division()
piece4.subtraction()
piece4.addition()
piece4.multiplication()

class Elements:

    def __init__(self, text, type='кнопка', locator=None):
        self.text = text
        self.type = type
        self.locator = locator

    def click_to_button(self):
        print(f"Клик по кнопке {self.text}")

button1 = Elements('Text Box')
button2 = Elements('Check Box')
button3 = Elements('Radio Button')
button4 = Elements('Web Tables')
button5 = Elements('Buttons')
button6 = Elements('Links')
button7 = Elements('Broken Links - Images')
button8 = Elements('Upload and Download')
button9 = Elements('Dynamic Properties')

button1.click_to_button()
button2.click_to_button()
button3.click_to_button()
button4.click_to_button()
button5.click_to_button()
button6.click_to_button()
button7.click_to_button()
button8.click_to_button()
button9.click_to_button()

