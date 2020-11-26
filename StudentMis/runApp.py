import  tkinter as tk
from MainApp.main import MainInterface

root = tk.Tk()

main = MainInterface(master=root)
root.title(string="Student management information system")
root.resizable(width=tk.TRUE,height=tk.TRUE)

root.mainloop()


