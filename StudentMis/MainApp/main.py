import tkinter as tk


class MainInterface(tk.Frame):

    def __init__(self, master=None,**kw):
        super().__init__(master=master,**kw)
        self.master = master
        first_label = tk.Label(master=self.master,
                            cnf={
                                'text':"First Label",'padx':2,'pady':3,
                                'borderwidth':3,'highlightbackground':"black",
                                'highlightcolor':"red",
                                'underline':tk.TRUE,
                                'activebackground':"green",
                                'background':"yellow",
                                'takefocus':tk.TRUE,
                                })
        first_label.grid(row=0,column=1)

        first_entry = tk.Entry(master=self.master,cnf={
            'width':40})
        first_entry.grid(row=0,column=2)