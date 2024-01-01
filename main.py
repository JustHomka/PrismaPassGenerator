from gui import RandomStringGeneratorApp
import customtkinter as tk

if __name__ == "__main__":
    root = tk.CTk()
    root.resizable(False, False)
    app = RandomStringGeneratorApp(root)
    root.mainloop()