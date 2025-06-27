from typing import Dict, List, Set
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkTextbox, CTkEntry
from tkinter import messagebox as mb

from Model.gramaticModel import Gramatic

from Model.gramatic import language1


class GrammarController:
    def __init__(self, output_panel):
        self.gramatic = Gramatic()
        self.output_panel = output_panel
        self.n_words = 10  # Default number of words to generate

    def build_grammar(self, nts: str, ts: str, rules_text: str, n_words: str):
        self.output_panel.textbox.configure(state="normal")
        if nts.strip() == "":
            mb.showerror("Error", "Debe ingresar al menos un no terminal.")
            return

        if ts.strip() == "":
            mb.showerror("Error", "Debe ingresar al menos un terminal.")
            return

        nts_list: list[str] = [c.strip() for c in nts.split(",")]
        if not all(len(c) == 1 for c in nts_list):
            mb.showerror(
                "Error", "Los no terminales deben ser de un solo caracter.")
            return

        ts_list = [s.strip() for s in ts.split(",")]
        if not all(len(c) == 1 for c in ts_list):
            mb.showerror(
                "Error", "Los terminales deben ser de un solo caracter.")
            return

        self.gramatic.set_non_terminals(nts_list)
        self.gramatic.set_terminals(ts_list)

        # primer simbolo es el de inicio
        self.gramatic.set_start_symbol(nts_list[0])
        self.gramatic.set_vocabulary()
        self.gramatic.delete_productions()
        for line in rules_text.strip().splitlines():
            if "->" in line:
                lhs, rhs = line.split("->", maxsplit=1)
                lhs = lhs.strip()
                if lhs not in self.gramatic.non_terminals:
                    # error
                    return
                rhs_parts = [r.strip() for r in rhs.split("|") if r.strip()]
                if not all(c in self.gramatic.vocabulary for string in rhs_parts for c in string):
                    # error
                    mb.showerror(
                        "Error", "Las producciones deben contener solo no terminales y terminales válidos.")
                    return

                for rhs in rhs_parts:
                    self.gramatic.add_production(lhs, rhs)

        self.show_output("Gramática procesada correctamente.")

    def show_output(self, text: str):
        self.output_panel.show(text)

    def show_grammar(self):
        self.show_output(str(self.gramatic))
        self.output_panel.textbox.configure(state="disable")

    def generate_words(self, n_words: str = "10"):
        if n_words.isdecimal():
            self.n_words = int(n_words)
        else:
            mb.showerror(
                "Error", "La cantidad de palabras debe ser un número entero.")
            return
        self.output_panel.textbox.configure(state="normal")
        st: set[str] = language1(self.gramatic, 200, self.n_words)
        res: list[str] = list(st)
        res.sort(reverse=True)
        res = [f"{i + 1}. {word}" for i, word in enumerate(res)]
        string = "\n".join(res)
        self.show_output(str(self.gramatic) + '\n' +
                         string)
        self.output_panel.textbox.configure(state="disable")

<<<<<<< HEAD
    def verify_word(self, word: str):
        if not word:
            mb.showerror("Error", "Debe ingresar una palabra para verificar.")
            return

        if any(c not in self.gramatic.terminals for c in word):
            mb.showinfo("resultado", f"la palabra {word} no es válida.")
            return
        from earley import earley_parser
        gramatic: Gramatic = self.gramatic
        is_valid: bool = earley_parser(
            word, gramatic.productions, gramatic.start_symbol, gramatic.terminals)
        if is_valid:
            mb.showinfo("Resultado", f"La palabra '{word}' es válida.")
        else:
            mb.showinfo("Resultado", f"La palabra '{word}' no es válida.")

    def is_build(self) -> bool:
        """Verifica si la gramática ha sido construida."""
        return bool(self.gramatic.non_terminals and self.gramatic.terminals and self.gramatic.productions)

    def go_back(self, window, parent):
        window.destroy()
        parent.deiconify()
        
    def verify_word(self, word: str):
        if not word:
            mb.showerror("Error", "Debe ingresar una palabra para verificar.")
            return

        if any(c not in self.gramatic.terminals for c in word):
            mb.showinfo("resultado", f"la palabra {word} no es válida.")
            return
        from earley import earley_parser
        gramatic: Gramatic = self.gramatic
        is_valid: bool = earley_parser(
            word, gramatic.productions, gramatic.start_symbol, gramatic.terminals)
        if is_valid:
            mb.showinfo("Resultado", f"La palabra '{word}' es válida.")
        else:
            mb.showinfo("Resultado", f"La palabra '{word}' no es válida.")

    def is_build(self) -> bool:
        """Verifica si la gramática ha sido construida."""
        return bool(self.gramatic.non_terminals and self.gramatic.terminals and self.gramatic.productions)


# if __name__ == "__main__":
#     app = GramaticGui()
#     app.mainloop()
