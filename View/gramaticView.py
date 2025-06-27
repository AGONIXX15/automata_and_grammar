from typing import Optional
from tkinter import messagebox as mb
from customtkinter import CTkButton, CTkFrame, \
    CTkLabel, CTkScrollableFrame, CTkTextbox, CTkToplevel, CTkEntry, CTk

import customtkinter as ctk

from Controller.controllerGramatic import GrammarController


class GrammarPanel(CTkFrame):
    def __init__(self, master, controller: GrammarController):
        super().__init__(master)
        self.controller = controller
        self.n_words = "10"

        CTkLabel(self, text="No terminales (separados por coma):").grid(
            row=0, column=0, sticky="w", padx=10)
        self.entry_nt = CTkEntry(self, width=400)
        self.entry_nt.grid(row=1, column=0, padx=10, pady=(0, 10))

        CTkLabel(self, text="Terminales (separados por coma):").grid(
            row=2, column=0, sticky="w", padx=10)
        self.entry_t = CTkEntry(self, width=400)
        self.entry_t.grid(row=3, column=0, padx=10, pady=(0, 10))

        CTkLabel(self, text="Reglas de producción (una por línea):").grid(
            row=4, column=0, sticky="w", padx=10)
        self.rules_textbox = CTkTextbox(self, width=500, height=200)
        self.rules_textbox.grid(row=5, column=0, padx=10, pady=(0, 10))

        CTkButton(self, text="Aceptar", command=self.accept).grid(
            row=6, column=0, pady=(10, 5))
        CTkButton(self, text="Ver gramática actual",
                  command=self.controller.show_grammar).grid(row=7, column=0, pady=5)

        self.entry_generate = CTkEntry(
            self, width=300, placeholder_text="Cantidad de palabras a generar (por defecto 10)")
        self.entry_generate.grid(
            row=8, column=0, padx=10, pady=(10, 5))

        CTkButton(self, text="generar palabras", command=self.generate).grid(
            row=10, column=0, pady=10)

        CTkLabel(self, text="verificar palabra").grid(row=11, column=0, sticky="w", padx=10)
        self.entry_verify = CTkEntry(self, width=300, placeholder_text="Ingrese palabra a verificar")
        self.entry_verify.grid(row=12, column=0, padx=10, pady=(0, 10))
        CTkButton(self, text="verificar", command=self.verify).grid(
            row=13, column=0, pady=(0, 10))

    def accept(self):
        nts = self.entry_nt.get()
        ts = self.entry_t.get()
        n_words = self.entry_generate.get()
        rules = self.rules_textbox.get("0.0", "end")
        self.controller.build_grammar(nts, ts, rules, n_words)

    def generate(self):
        n_words = self.entry_generate.get()
        if not n_words.isdecimal():
            n_words = "10"
        self.controller.generate_words(n_words)

    def verify(self):
        if not self.controller.is_build():
            mb.showerror("Error", "Debe construir la gramática primero.")
            return
        word = self.entry_verify.get()
        if not word:
            mb.showerror("Error", "Debe ingresar una palabra a verificar.")
            return
        self.controller.verify_word(word)


class OutputPanel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.textbox = CTkTextbox(self, width=400, height=400)
        self.textbox.pack(expand=True, fill="both", padx=10, pady=10)

    def show(self, text: str):
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", text)


class GramaticGui(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("Gramatic GUI")

        self.output_panel: OutputPanel = OutputPanel(self)
        self.output_panel.pack(side="right", fill="both", expand=True)

        self.controller: GrammarController = GrammarController(
            self.output_panel)

        self.grammar_panel: GrammarPanel = GrammarPanel(self, self.controller)
        self.grammar_panel.pack(side="left", fill="both",
                                expand=True, padx=20, pady=20)


if __name__ == '__main__':
    app = GramaticGui()
    app.mainloop()
