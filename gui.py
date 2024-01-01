import customtkinter as tk
import pyperclip
import string
import random

class RandomStringGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("PrismaPass")

        self.length_label = tk.CTkLabel(master, text="Length: 0")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_slider = tk.CTkSlider(master, from_=1, to=100, command=self.update_length)
        self.length_slider.grid(row=0, column=1, padx=10, pady=10)

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbox = tk.CTkCheckBox(master, text="Uppercase", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=1, column=0, columnspan=2, pady=5, sticky="W")

        self.special_chars_var = tk.BooleanVar()
        self.special_chars_checkbox = tk.CTkCheckBox(master, text="Special", variable=self.special_chars_var)
        self.special_chars_checkbox.grid(row=2, column=0, columnspan=2, pady=5, sticky="W")

        self.digits_var = tk.BooleanVar()
        self.digits_checkbox = tk.CTkCheckBox(master, text="Numbers", variable=self.digits_var)
        self.digits_checkbox.grid(row=3, column=0, columnspan=2, pady=5, sticky="W")

        self.generate_button = tk.CTkButton(master, text="Generate", command=self.generate_random)
        self.generate_button.grid(row=4, column=0, pady=10)

        self.copy_button = tk.CTkButton(master, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=1, pady=10)

        self.result_label = tk.CTkLabel(master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def update_length(self, event):
        length = int(self.length_slider.get())
        self.length_label.configure(text=f"Length: {length}")

    def generate_random(self):
        characters = self.get_selected_characters()
        length = int(self.length_slider.get())
        random_string = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.configure(text=random_string)

    def copy_to_clipboard(self):
        result_text = self.result_label.cget("text")
        pyperclip.copy(result_text)

    def get_selected_characters(self):
        selected_chars = string.ascii_letters if self.uppercase_var.get() else string.ascii_lowercase
        selected_chars += string.digits if self.digits_var.get() else ''
        selected_chars += string.punctuation if self.special_chars_var.get() else ''
        return selected_chars
