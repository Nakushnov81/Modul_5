class StringVar:
    x = ''
    def set_srt(self, x):
        self.x = x
        return x

    def get_str(self, x):
        return x

st = StringVar()

st.set_srt(input('Введите строку: '))
print(st.__dict__)

st.get_str(input('Внесите изменения: '))
print(st.__dict__)