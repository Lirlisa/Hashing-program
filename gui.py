from tkinter import filedialog
import tkinter as tk
import hashes


class clase:

    path = ""
    def __init__(self, master):
        self.setFrames(master)
        self.setEntries()
        self.setButtons()
        self.setMenus()

    def setFrames(self, master):
        self.frame1 = tk.Frame(master, pady=10, padx=5)
        self.frame1.grid(row=0)
        self.frame2 = tk.Frame(master, pady=10, padx=5)
        self.frame2.grid(row=1)
        self.frame3 = tk.Frame(master, pady=10, padx=5)
        self.frame3.grid(row=2)

    def setEntries(self):
        self.entry1_str = tk.StringVar()
        self.entry1_str.set("Elija un archivo")
        self.entry1 = tk.Entry(self.frame1, text=self.entry1_str, bg="white", width=50)
        self.entry1.grid(row=0, column=0)

        entry2_str = tk.StringVar()
        entry2_str.set("Texto plano")
        self.entry2 = tk.Entry(self.frame2, textvariable=entry2_str, width=50)
        self.entry2.grid(sticky="w")

        self.entry3_str = tk.StringVar()
        self.entry3_str.set("")
        self.entry3 = tk.Entry(self.frame3, text=self.entry3_str, bg="white", width=50)
        self.entry3.pack()

    def setButtons(self):
        self.boton1_browse = tk.Button(self.frame1, text="browse", command=self.arc)
        self.boton1_browse.grid(row=0, column=1)
        self.boton1_algorithm = tk.Button(self.frame1, text="hash", command=self.hashFile)
        self.boton1_algorithm.grid(row=1, column=1)

        self.boton2 = tk.Button(self.frame2, text="hash", command=self.hashStr)
        self.boton2.grid(row=1, column=1)

    def setMenus(self):
        lista = ['sha1', 'sha256', 'md5', 'sha512', 'sha3_256', 'sha3_512']
        self.menu1_str = tk.StringVar()
        self.menu1_str.set("md5")
        self.menu1 = tk.OptionMenu(self.frame1, self.menu1_str, *lista)
        self.menu1.grid(row=1, column=0, sticky="w")

        self.menu2_str = tk.StringVar()
        self.menu2_str.set("md5")
        self.menu2 = tk.OptionMenu(self.frame2, self.menu2_str, *lista)
        self.menu2.grid(row=1, column=0, sticky="w")

    def arc(self):
        self.path = filedialog.askopenfilename(initialdir = "/",
            title = "Select file",filetypes = (("all files","*.*"), ("jpeg files","*.jpg")))
        self.entry1_str.set(self.path)

    def hashFile(self):
        try:
            if self.path != "":
                self.entry3_str.set(hashes.calcFile(self.path, self.menu1_str.get()))
        except:
                self.entry3.set("No se puede acceder a la ruta especificada")

    def hashStr(self):
        self.entry3_str.set(hashes.calcStr(self.menu2_str.get(),self.entry2.get()))

root = tk.Tk()
root.title("Hash!")
root.iconbitmap(default='transparent.ico')
root.resizable(width=False, height=False)
ventana = clase(root)

root.mainloop()
