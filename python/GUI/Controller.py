from GUI import GUI
class Controller:
    def __init__(self, model=None, gui=GUI()) -> None:
        self.model = None
        self.gui = gui

        self.gui.loop()
    