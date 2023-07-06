import customtkinter

font = "fonts\\d9464-arkhip_font.ttf"


class ProgressBars(customtkinter.CTkFrame):

    # фрейм для верхнего поля прогресса
    def __init__(self, master, *args):
        super().__init__(master, fg_color="#eeeeee")
        self.buttons = []

        for i in enumerate(args):
            button = customtkinter.CTkProgressBar(self, orientation="vertical", height=40, width=15)
            button.grid(row=0, column=i, padx=15, pady=5)
            self.buttons.append(button)


class MainButtons(customtkinter.CTkFrame):

    # фрейм для основных кнопок. При нажатии должен меняться self.textbox
    def __init__(self, master, *args):
        super().__init__(master, fg_color="#eeeeee")
        self.buttons = []

        for i, value in enumerate(args):
            button = customtkinter.CTkButton(self, font=(font, 18), text=value[0], command=value[1],
                                             fg_color="#F0685F")
            button.grid(row=i, column=0, padx=20, pady=15)
            self.buttons.append(button)


class FunctionsMixin:
    def test(self):
        print(self.winfo_width())


class App(customtkinter.CTk, FunctionsMixin):
    def __init__(self):
        super().__init__(fg_color="white")

        # настройки главного окна
        self.title("Most Popular Words")
        self.geometry("1024x768")
        self.minsize(width=800, height=600)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # тригер на изменения размеров экрана
        self.bind("<Configure>", self.on_resize)

        # настройки секции с кнопками
        self.sections = MainButtons(self,
                                    ("100 words", self.test),
                                    ("1 000 words", self.test),
                                    ("2 000 words", self.test),
                                    ("3 000 words", self.test),
                                    ("5 000 words", self.test),
                                    ("7 000 words", self.test),
                                    ("10 000 words", self.test),
                                    ("20 000 words", self.test))
        self.sections.grid(row=0, column=0, padx=15, pady=(80, 20), sticky="nw")

        # верхний раздел
        self.progressbar = ProgressBars(self, range(0, 8))
        self.progressbar.grid(row=0, column=0, padx=20, pady=15, sticky="nw")

        # область с основным текстом
        self.textbox = customtkinter.CTkTextbox(master=self, corner_radius=0, fg_color="white",
                                                font=("calibri", int(self.winfo_width() / 16)), text_color="black",
                                                border_spacing=15, activate_scrollbars=False)
        self.textbox.grid(row=0, column=0, padx=(220, 0), pady=(100, 0), sticky="NWES", columnspan=2, rowspan=2)
        self.textbox.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox.insert("0.0",
                            "Нужно выбрать раздел\n"
                            "  с колличеством слов\n"
                            "      для изучения   ")


    # меняет размер текста в блоке с текстом
    def on_resize(self, event):
        self.textbox.configure(font=(font, int(self.winfo_width() / 16)))


if __name__ == "__main__":
    app = App()
    app.mainloop()

# попытка сделать фрейм для прогрессбаров
