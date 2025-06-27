import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400+500+200")
        self.title("Automatas y gramáticas")
        self.window_title = "Bienvenido a la aplicación de autómatas y gramáticas"
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def display(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)
        ctk.CTkLabel(self, text=self.window_title, font=("Arial", 24, "bold")).grid(
            row=0, column=0, columnspan=2, pady=20, sticky="ew"
        )
        ctk.CTkLabel(self, text="Esta aplicación te permite trabajar con autómatas y gramáticas.", 
                    font=("Arial", 14, "bold")).grid(
            row=1, column=0, columnspan=2, pady=10, sticky="ew"
        )
        ctk.CTkLabel(self, text="Con que quieres trabajar.", font=("Arial", 14, "bold")).grid(
            row=2, column=0, columnspan=2, pady=10, sticky="ew"
        )
        ctk.CTkButton(self, text="Trabajar con gramáticas", 
                     font=("Arial", 14, "bold"), 
                     command=self.go_to_gramatic).grid(
            row=3, column=0, pady=20, padx=20, sticky="ew"
        )
        ctk.CTkButton(self, text="Trabajar con autómatas", 
                     font=("Arial", 14, "bold"),
                     command=self.go_to_state_machine).grid(
            row=3, column=1, pady=20, padx=20, sticky="ew"
        )
        ctk.CTkButton(self, text="Salir", 
                     font=("Arial", 14, "bold"), 
                     command=self.destroy).grid(
            row=4, column=0, columnspan=2, pady=0, padx=100, sticky="ew"
        )
        
        self.mainloop()

    def go_to_gramatic(self):
        from .gramaticView import GramaticGui
        self.withdraw()
        GramaticGui(self)
    
    def go_to_state_machine(self):
        from .state_machine_view import StateMachineView
        self.withdraw()
        StateMachineView(self)

if __name__ == "__main__":
    app = MainApp()
    app.display()
