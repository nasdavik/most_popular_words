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

        self.textbox = customtkinter.CTkTextbox(master=self, corner_radius=0, fg_color="white",
                                                font=("calibri", 40), text_color="black")
        self.textbox.grid(row=0, column=0, padx=(200, 10), pady=(50, 10), sticky="NWES", columnspan=2, rowspan=2)
        self.textbox.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox.insert("0.0",
                            "Добро пожаловать\n"
                            "Тебе нужно выбрать уровень чтобы приступить к обучению\n"
                            "Для начала лучше освоить самые базовые слова, "
                            "чтобы перейти к следующим\n"
                            "Однако слова будут дублироваться от уровня к уровню. "
                            "Так основы основ гораздо лучше заркепяться в голове")


if __name__ == "__main__":
    app = App()
    app.mainloop()
