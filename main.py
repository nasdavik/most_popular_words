import customtkinter


class MainButtons(customtkinter.CTkFrame):
    # Фрейм для основных кнопок. При нажатии должен меняться self.textbox
    def __init__(self, master, *args):
        super().__init__(master, fg_color="#eeeeee")
        self.buttons = []

        for i, value in enumerate(args):
            button = customtkinter.CTkButton(self, text=value[0], command=value[1])
            button.grid(row=i, column=0, padx=15, pady=(20, 0))
            self.buttons.append(button)


class FunctionsMixin:
    def test(self):
        print("yeah, all right")


class App(customtkinter.CTk, FunctionsMixin):
    def __init__(self):
        super().__init__(fg_color="white")

        self.title("Most Popular Words")
        self.geometry("1024x768")
        self.minsize(width=800, height=600)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # настройки главного окна

        self.sections = MainButtons(self, ("100 words", self.size), ("1000 words", self.test),
                                    ("2000 words", self.test), ("3000 words", self.test),
                                    ("5000 words", self.test), ("7000 words", self.test),
                                    ("10000 words", self.test), ("20000 words", self.test))
        self.sections.grid(row=0, column=0, padx=15, pady=(50, 20), sticky="nsw")
        # настройки секции с кнопками

        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.progressbar.grid(row=0, column=0, padx=15, pady=(15, 15), sticky="nw")
        # верхний раздел

        self.textbox = customtkinter.CTkTextbox(master=self, corner_radius=0, fg_color="white",
                                                font=("calibri", 76), text_color="black",
                                                border_spacing=15, activate_scrollbars=False)
        self.textbox.grid(row=0, column=0, padx=(200, 30), pady=(50, 10), sticky="NWES", columnspan=2, rowspan=2)
        self.textbox.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox.insert("0.0",
                            "Нужно выбрать раздел\n"
                            "  с колличеством слов\n"
                            "      для изучения")

        print(self.size())

    def size(self):
        start = self.geometry().split("+")
        print(int(start[0].split("x")[1]))



if __name__ == "__main__":
    app = App()
    app.mainloop()
    # запуск программы из основного файла
