class StringVar:
    def __init__(self, x = str(input('Введите строку: '))):
        self.x = x

    def set_srt(self, x):
        self.x = x
        return x

    def get_str(self):
        return print(self.x)

st = StringVar()

st.get_str()

st.set_srt(input('Измените строку: '))

st.get_str()


class Point:
    color = 'red'
    size = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return print(self.x, self.y)

    def set_coord(self, x, y):
        self.x = x
        self.y = y
        return x, y

pt = Point(2, 3)

pt.get_coord()

pt.set_coord(5, 7)

pt.get_coord()


