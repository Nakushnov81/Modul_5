class StringVar:

    def set_srt(self, x):
        self.x = x
        return x

    def get_str(self):
        return print(self.x)

st = StringVar()

st.set_srt(input('Введите строку: '))

st.get_str()
