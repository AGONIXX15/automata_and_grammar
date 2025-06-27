from View.state_machine_view import StateMachineView

class StateMachineController:
    def __init__(self, parent):
        self.parent = parent
        self.view = StateMachineView(parent)
        self.view.controller = self

    def go_back(self):
        self.view.parent.deiconify()
        self.view.destroy()