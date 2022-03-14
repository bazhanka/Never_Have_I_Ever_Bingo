# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import HORIZONTAL, VERTICAL
from tkinter import ttk
from gamepresent import *
import os


# game(first) window - multiple chose select package
#                    - number of players
#                    - generate package button
#                       -- generate from text to list of cards
#                       -- generate pptx from list of cards

# YaCreativny
class Base_Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Я никогда не бинго")
        self.window.geometry('650x400')

        self.lbl = Label(self.window, text="Добро пожаловать в игру\nЯ никогда не бинго!", fg="black",
                         font=("Verdana", 30))
        self.lbl.grid(column=0, row=0)
        self.lbl.place(x=55, y=20)

        self.lblenter = Label(self.window, text="Введите количество гостей: ", fg="black", font=("Verdana", 8))
        self.lblenter.place(x=220, y=250)

        self.entry = Entry(self.window, fg='black', width=5)
        self.entry.place(x=390, y=250)

        GAMES = []
        dir_name = "C:/Users/user/Downloads/pythonProject"
        self.test = os.listdir(dir_name)
        for item in self.test:
            if item.endswith(".txt"):
                GAMES.append(item)

        self.list_of_games = ttk.Combobox(self.window,
                                          values=GAMES)
        self.list_of_games.current(1)
        self.list_of_games.grid(column=0, row=1)
        self.list_of_games.place(x=250, y=150)

        #        self.selected = IntVar()
        #        self.selected.set(0)
        #        self.rad1 = Radiobutton(self.window, text='Для выпускного', value=1, variable=self.selected,
        #                                font=("Verdana", 8))
        #        self.rad2 = Radiobutton(self.window, text='Для свадьбы', value=2, variable=self.selected, font=("Verdana", 8))
        #        self.rad3 = Radiobutton(self.window, text='Для корпоратива', value=3, variable=self.selected,
        #                                font=("Verdana", 8))
        #        self.rad4 = Radiobutton(self.window, text='Для девичника', value=4, variable=self.selected, font=("Verdana", 8))
        #        self.rad5 = Radiobutton(self.window, text='Для мальчишника', value=5, variable=self.selected,
        #                                font=("Verdana", 8))
        #        self.rad6 = Radiobutton(self.window, text='Для дня рождения', value=6, variable=self.selected,
        #                                font=("Verdana", 8))

        #        self.rad1.grid(column=0, row=0)
        #        self.rad2.grid(column=1, row=0)
        #        self.rad3.grid(column=2, row=0)
        #        self.rad4.grid(column=0, row=1)
        #        self.rad5.grid(column=1, row=1)
        #        self.rad6.grid(column=2, row=1)

        #        self.rad2.place(x=250, y=150)
        #        self.rad3.place(x=400, y=150)
        #        self.rad4.place(x=100, y=200)
        #        self.rad5.place(x=250, y=200)
        #        self.rad6.place(x=400, y=200)

        self.btn_main = Button(self.window, text="Нажмите, чтобы продолжить", command=self.clicked_button,
                               font=("Verdana", 8))
        self.btn_main.grid(column=1, row=10)
        self.btn_main.place(x=230, y=290)

        self.btn_creative = Button(self.window, text="Я креативный", command=self.i_am_creative, font=("Verdana", 8))
        self.btn_creative.grid(column=1, row=10)
        self.btn_creative.place(x=260, y=320)

        self.window.mainloop()

    # def clicked_button(self):
    #     input_file = ''
    #     if self.entry.get() == '':
    #         messagebox.showinfo('Я никогда не бинго', 'Упс! Введите количество гостей.')
    #     elif self.selected.get() != 0 and self.entry.get() != '':
    #         try:
    #             get = int(self.entry.get())
    #             if get < 2:
    #                 messagebox.showinfo('Я никогда не бинго',
    #                                     'Упс! Для игры необходимо не менее 2х игроков. Время позвонить друзьям!')
    #             else:
    #                 messagebox.showinfo('Я никогда не бинго',
    #                                     'Поздравляем! Карточки для игры успешно сохранены\nПриятной игры!')
    #                 if self.selected.get() == 1:
    #                     input_file = 'Fants.txt'
    #                 elif self.selected.get() == 2:
    #                     input_file = 'Wedding.txt'
    #                 elif self.selected.get() == 3:
    #                     input_file = 'Corporate.txt'
    #                 elif self.selected.get() == 4:
    #                     input_file = 'Girls.txt'
    #                 elif self.selected.get() == 5:
    #                     input_file = 'Boys.txt'
    #                 elif self.selected.get() == 6:
    #                     input_file = 'Anniv.txt'
    #                 inch = int(self.entry.get())
    #                 output_file = "Cards.pptx"
    #                 GamePresent(inch, input_file, output_file).generate_table()
    #         except ValueError:
    #             messagebox.showinfo('Я никогда не бинго', 'Упс! Введите целое число.')
    #             pass
    #     else:
    #         messagebox.showinfo('Я никогда не бинго', 'Упс! Выберите пакет вопросов.')

    def clicked_button(self):
        if self.entry.get() == '':
            messagebox.showinfo('Я никогда не бинго', 'Упс! Введите количество гостей.')
        elif self.list_of_games.get() != 0 and self.entry.get() != '':
            try:
               get = int(self.entry.get())
               if get < 2:
                  messagebox.showinfo('Я никогда не бинго',
                                     'Упс! Для игры необходимо не менее 2х игроков. Время позвонить друзьям!')
               else:
                  messagebox.showinfo('Я никогда не бинго',
                                      'Поздравляем! Карточки для игры успешно сохранены\nПриятной игры!')
                  input_file = self.list_of_games.get()
                  inch = int(self.entry.get())
                  output_file = self.list_of_games.get().translate({ord(i): None for i in '.txt'})
                  output_file = output_file + '.pptx'
                  count = 1
                  while output_file in self.test:
                      output_file = self.list_of_games.get().translate({ord(i): None for i in '.txt'}) + f'({count})'+".pptx"
                      count+=1
                  GamePresent(inch, input_file, output_file).generate_table()
            except ValueError:
               messagebox.showinfo('Я никогда не бинго', 'Упс! Введите целое число.')
               pass

    def i_am_creative(self):
        new_window = Middle_Window()


class Middle_Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Я креативный")
        self.window.geometry('650x400')

        self.lbl = Label(self.window, text="Создайте свои фанты для игры\nЯ никогда не бинго!", fg="black",
                         font=("Verdana", 25))
        self.lbl.grid(column=0, row=0)
        self.lbl.place(x=55, y=20)

        self.lblenter = Label(self.window, text="Введите количество гостей: ", fg="black", font=("Verdana", 8))
        self.lblenter.place(x=220, y=250)

        self.lblname = Label(self.window, text="Введите название: ", fg="black", font=("Verdana", 8))
        self.lblname.place(x=190, y=220)

        self.entry = tkinter.Entry(self.window, fg='black', width=5)
        self.entry.place(x=390, y=250)

        self.entryname = tkinter.Entry(self.window, fg='black', width=35)
        self.entryname.place(x=315, y=220)

        self.btn = Button(self.window, text="Нажмите, чтобы продолжить", command=self.create_lines, font=("Verdana", 8))
        self.btn.grid(column=1, row=10)
        self.btn.place(x=230, y=290)

        self.window.mainloop()

    def create_lines(self):
        if self.entry.get() == "":
            messagebox.showinfo('Я никогда не бинго', 'Упс! Введите количество гостей.')
            return
        try:
            num_guest = int(self.entry.get())
            if num_guest < 2:
                messagebox.showinfo('Я никогда не бинго',
                                    'Упс! Для игры необходимо не менее 2х игроков. Время позвонить друзьям!')
                return
            file = self.entryname.get()
            fwin = Fants_window(file)
            fwin.label(num_guest)
        except ValueError:
            messagebox.showinfo('Я никогда не бинго', 'Упс! Введите целое число')


class Fants_window:
    def __init__(self, file):
        self.window = Tk()
        self.window.title("Пишем фанты")
        self.window.geometry('900x600')
        #self.scroll_x = tkinter.Scrollbar(self.window, orient=tkinter.HORIZONTAL)
        #self.scroll_y = tkinter.Scrollbar(self.window, orient=tkinter.VERTICAL)
        self.entry_strings = []
        self.count = 1
        self.y_num = 80
        self.file = file
        self.input_file = self.file + '.txt'
        self.output_file = self.file + '.pptx'

    def morelines(self):
        entry_string_var = StringVar()
        text = Label(self.window, text='{}. Я никогда не '.format(self.count))
        text.place(x=55, y=self.y_num)
        entry = tkinter.Entry(self.window, fg='black', width=100, textvariable=entry_string_var)
        self.entry_strings.append(entry)
        entry.pack()
        entry.place(x=170, y=self.y_num)
        self.y_num += 20
        if self.y_num > 600:
            n = 600 + (self.y_num - 600)
            self.window.geometry('900x{}'.format(n))
        self.count += 1



    def new_pack(self):
        for el in self.entry_strings:
            if el.get() != "":
                my_file = open(self.input_file, "a+", encoding='utf-8')
                my_file.write('Я никогда не ')
                my_file.write(el.get().strip())
                my_file.write("\n")
                my_file.close()
        inch = int(self.count)
        GamePresent(inch, self.input_file, self.output_file).generate_table()
        messagebox.showinfo('Я никогда не бинго',
                            'Поздравляем! Карточки для игры успешно сохранены\nПриятной игры!')

    def label(self, num_guest):
        desired_number = num_guest // 3
        if desired_number < 9:
            desired_number = (9 - num_guest // 3) + desired_number
        self.lbl = Label(self.window,
                         text="Минимальное количество фантов для вашей игры - {}".format(desired_number),
                         fg="black",
                         font=("Verdana", 20))
        self.lbl.grid(column=0, row=0)
        self.lbl.place(x=55, y=20)
        while self.count <= desired_number:
            self.morelines()
        self.plusbut = Button(self.window, text="Еще!", command=self.morelines, font=("Verdana", 8))
        self.plusbut.place(x=800, y=400)
        self.exitbutton = Button(self.window, text="Готово!", command=self.new_pack, font=("Verdana", 8))
        self.exitbutton.grid(column=1, row=10)
        self.exitbutton.place(x=790, y=450)


if __name__ == '__main__':
    base_window = Base_Window()
