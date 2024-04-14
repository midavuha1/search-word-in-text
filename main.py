import fitz
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename()
    if filepath == "":
        return
    search_term = text_input.get()
    pdf = fitz.open(filepath)
    for current_page in range(len(pdf)):
        page = pdf.load_page(current_page)

        if page.search_for(search_term):
            page_text = page.get_text()
            for i in page_text.split('\t'):
                if search_term in i:
                    with open(f"{name_input.get()}.txt", "a") as file:
                        file.write(f"\n\n{i}")


def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


window = tk.Tk()

window.resizable(width=True, height=True)

window.title("Поиск абзацев с нужным словом")

window.geometry('720x360')

search_text = tk.Label(window, text="Сюда введи слово для поиска", font=("Arial Bald", 16), fg="black")
search_text.place(x=180, y=25)

text_input = tk.Entry(width=47)
text_input.place(x=180, y=65)

name_text = tk.Label(window, text="Придумай название для файла", font=("Arial Bald", 16), fg="black")
name_text.place(x=180, y=200)

name_input = tk.Entry(width=47)
name_input.place(x=180, y=250)

search_button = tk.Button(window, text="Поиск", width=47, height=2, command=open_file)
search_button.place(x=180, y=110)

text_editor = Text()


window.mainloop()
