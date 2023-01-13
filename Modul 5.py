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
