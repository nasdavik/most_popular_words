import customtkinter


def test():
    print("yeah, all right")


class MainButtons(customtkinter.CTkFrame):
    def __init__(self, master, *args):
        super().__init__(master)
        self.buttons = []

        for i, value in enumerate(args):
            button = customtkinter.CTkButton(self, text=value[0], command=value[1])
            button.grid(row=i, column=0, padx=10, pady=10)
            self.buttons.append(button)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="white")

        self.title("Most Popular Words")
        self.geometry("1024x768")
        self.minsize(width=800, height=600)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sections = MainButtons(self, ("100 words", test), ("1000 words", test), ("2000 words", test),
                                     ("3000 words", test))
        self.sections.grid(row=0, column=0, padx=10, pady=(40, 20), sticky="nsw")

        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.progressbar.grid(row=0, column=0, padx=10, pady=(15, 15), sticky="nw")

        self.textbox = customtkinter.CTkTextbox(master=self, width=600, corner_radius=0, fg_color="white")
        self.textbox.grid(row=0, column=0, padx=200, pady=50, sticky="nsew", columnspan=2)
        self.textbox.insert("0.0",
                            "Добро пожаловать. Тебе нужно выбрать уровень чтобы приступить к обучению. Для начала"
                            "лучше освоить самые базовые слова, чтобы перейти к следующим. Однако слова будут"
                            "дублироваться от уровня к уровню. Так основы основ гораздо лучше заркепяться в голове")


if __name__ == "__main__":
    app = App()
    app.mainloop()
