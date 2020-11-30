import  tkinter as tk
from MainApp.main import MainInterface

root = tk.Tk()

main = MainInterface()
main.grid(row=1,column=2,padx=5,pady=5)
root.title(string="Student management information system")
root.resizable(width=tk.TRUE,height=tk.TRUE)

root.mainloop()


