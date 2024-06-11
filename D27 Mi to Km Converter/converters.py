from tkinter import *
import pandas

MIKM = 0.62137

class Convert():
        def __init__(self, unit1, unit2):
            self.unit1 = unit1
            self.unit2 = unit2


            self.entry = Entry(width=10, )
            self.entry.insert(END, string="0")
            self.entry.grid(column=1, row=0)

            self.entry_text = Label(text=unit1)
            self.entry_text.grid(column=2, row=0)

            self.equals = Label(text="Equals")
            self.equals.grid(column=0, row=1)

            self.result = Label(text="0.0")
            self.result.grid(column=1, row=1)

            self.result_text = Label(text=unit2)
            self.result_text.grid(column=2, row=1)



            self.button = Button(text="Calculate", command=self.calculate)
            self.button.grid(column=1, row=2)

        def calculate(self):
            data = pandas.read_csv("converters.csv")
            units = {row[0]: index for (index, row) in data.iterrows()}
            self.cal = round(float(self.entry.get()) / float(data[self.unit2][units[self.unit1]]), 3)
            self.result.config(text=f"{self.cal}")
        #
        # def inches_centimeters(self):
        #     self.entry = Entry(width=5)
        #     self.entry.grid(column=1, row=0)
        #
        #     self.entry_text = Label(text="Inches")
        #     self.entry_text.grid(column=2, row=0)
        #
        #     self.equals = Label(text="Is equal to ")
        #     self.equals.grid(column=0, row=1)
        #
        #     self.result = Label(text="0")
        #     self.result.grid(column=1, row=1)
        #
        #     self.result_text = Label(text="Centimeters")
        #     self.result_text.grid(column=2, row=1)
        #
        #     self.button = Button(text="Calculate", command=self.cal_MiKm)
        #     self.button.grid(column=1, row=2)

        # def cal_InCm(self):
        #     self.result.config(text=f"{round(float(self.entry.get()) * 1.609, 2)






