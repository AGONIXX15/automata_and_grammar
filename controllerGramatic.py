from typing import Dict, List, Set
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkTextbox, CTkEntry
from tkinter import messagebox as mb

from gramaticModel import Gramatic

from gramatic import language1


class GrammarController:
    def __init__(self, output_panel):
        self.gramatic = Gramatic()
        self.output_panel = output_panel

    def build_grammar(self, nts: str, ts: str, rules_text: str):
        self.output_panel.textbox.configure(state="normal")
        nts_list: list[str] = [c.strip() for c in nts.split(",")]
        print(nts_list)
        if not all(len(c) == 1 for c in nts_list):
            # error tirar mensaje nodos no terminales deben ser de 1 de largo
            return

        ts_list = [s.strip() for s in ts.split(",")]
        print(ts_list)
        if not all(len(c) == 1 for c in ts_list):
            # error tirar messagebox mensaje nodos terminales deben de ser de 1 de largo
            return

        self.gramatic.set_non_terminals(nts_list)
        self.gramatic.set_terminals(ts_list)
        if nts_list is None:
            # error no habia caracteres no terminales
            return

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
                    print(f"error produccion en no terminales")
                    return
                rhs_parts = [r.strip() for r in rhs.split("|") if r.strip()]
                if not all(c in self.gramatic.vocabulary for string in rhs_parts for c in string):
                    # error
                    print(
                        f"error se encontro caracter que no pertenece al vocabulario en la linea {line}")
                    return

                for rhs in rhs_parts:
                    self.gramatic.add_production(lhs, rhs)

        self.show_output("Gramática procesada correctamente.")

    def show_output(self, text: str):
        self.output_panel.show(text)

    def show_grammar(self):
        self.show_output(str(self.gramatic))
        self.output_panel.textbox.configure(state="disable")

    def generate_words(self):
        self.output_panel.textbox.configure(state="normal")
        st: set[str] = language1(self.gramatic, 30)
        res: list[str] = [str(i) + '. ' + v for i, v in enumerate(st, start=1)]
        res.sort()
        string = "\n".join(res)
        self.show_output(str(self.gramatic) + '\n' +
                         string)


# if __name__ == "__main__":
#     app = GramaticGui()
#     app.mainloop()
