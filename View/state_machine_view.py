import customtkinter as ctk
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.state_machine import fsm_final

class StateMachineView(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.parent = parent
        self.trasmisions = []
        self.validations = []
        self.title("Automatas")
        self.state('zoomed')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.go_back)
        self.display()

    def display(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=2)
        main_frame.grid_rowconfigure(0, weight=1)
        
        left_frame = ctk.CTkFrame(main_frame, width=600)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_frame.grid_propagate(False)
        
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.grid(row=0, column=1, sticky="nsew")
        
        ctk.CTkLabel(left_frame, text="Automatas", font=("Arial", 24, "bold")).pack(pady=20)
        
        ctk.CTkLabel(left_frame, text="Ingresar transmiciones.", font=("Arial", 14, "bold")).pack(anchor="w", padx=20)
        self.trasmisions_textbox = ctk.CTkTextbox(left_frame, height=100, font=("Arial", 12))
        self.trasmisions_textbox.pack(fill="x", padx=20, pady=(5, 10))
        
        ctk.CTkLabel(left_frame, text="Ingresar validaciones.", font=("Arial", 14, "bold")).pack(anchor="w", padx=20)
        self.validations_textbox = ctk.CTkTextbox(left_frame, height=100, font=("Arial", 12))
        self.validations_textbox.pack(fill="x", padx=20, pady=(5, 10))
        
        ctk.CTkButton(left_frame, text="Guardar Esquema", font=("Arial", 14, "bold"), command=self.save_scheme).pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(right_frame, text="Resultados del autómata.", font=("Arial", 14, "bold")).pack(anchor="w", padx=20, pady=(20, 5))
        self.results_textbox = ctk.CTkTextbox(right_frame, font=("Arial", 12), state="disabled")
        self.results_textbox.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        ctk.CTkButton(left_frame, text="Validar cadena", font=("Arial", 14, "bold"), command=self.validate_string).pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(main_frame, text="Volver", font=("Arial", 14, "bold"), command=self.go_back).grid(row=1, column=0, columnspan=2, pady=20, padx=100, sticky="ew")

    def save_scheme(self):
        self.trasmisions = self.trasmisions_textbox.get("1.0", "end-1c").strip().splitlines()
        self.validations = self.validations_textbox.get("1.0", "end-1c").strip().splitlines()
        
        if not self.trasmisions or not self.validations:
            ctk.CTkMessageBox.show_error("Error", "Por favor, ingrese las transmiciones y validaciones.")
            return

        trasmisions = "\n".join(self.trasmisions)
        validations = "\n".join(self.validations)
        self.results_textbox.configure(state="normal")
        self.results_textbox.insert("end", f"Esquema guardado:\nTransmisiones:\n\n{trasmisions}\n\nValidaciones:\n\n{validations}\n")
        self.results_textbox.configure(state="disabled")
    def validate_string(self):
        if not self.trasmisions or not self.validations:
            ctk.CTkMessageBox.show_error("Error", "Por favor, ingrese las transmiciones y validaciones.")
            return
        self.results_textbox.configure(state="normal")
        self.results_textbox.insert("end", f"Porcentaje de error: {fsm_final(self.trasmisions, self.validations)}%\n")

        
    
    def go_back(self):
        self.parent.deiconify()
        self.destroy()