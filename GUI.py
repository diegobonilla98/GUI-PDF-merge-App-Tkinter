from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import ImageTk, Image
from PyPDF2 import PdfFileMerger
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.iconbitmap('icon.ico')
        self.title("PDF merge")
        self.minsize(220, 150)
        self.dir = os.getcwd()

        image = ImageTk.PhotoImage(Image.open('pdfmerge.png'))
        self.img = tk.Label(self, image=image)
        self.img.image = image
        self.img.grid(column=0, row=0)

        self.browse = tk.Button(self, text="Browse", command=self.browse_files, width=30)
        self.browse.grid(column=0, row=1)

        self.message = tk.Label(self, text="Press \"Browse\" to select PDFs to merge.", fg="green")
        self.message.grid(column=0, row=2)

        self.submit = tk.Button(self, text="Save merged PDF", command=self.merge_pdf, width=40)
        self.submit.grid(column=0, row=4)

        self.clean = tk.Button(self, text="Clean Files", command=self.cleaner)
        self.clean.grid_forget()

        self.file_names = tk.Label(self)
        self.file_names.grid_forget()

        self.files = []
        self.merger = PdfFileMerger()

    def cleaner(self):
        self.files = []
        self.file_names.config(text="")
        self.file_names.grid_forget()
        self.message.config(text="Press \"Browse\" to select PDFs to merge.")

    def browse_files(self):
        filename = filedialog.askopenfilename(initialdir=self.dir, title="Select A File",
                                              filetype=(("PDF files", "*.pdf"), ("all files", "*.*")))
        if not len(filename) > 0:
            return
        else:
            self.dir = filename
            self.clean.grid(column=1, row=1)
            self.message.config(text="Files:")
        self.files.append(filename)
        self.file_names.config(text='\n'.join(self.files))
        self.file_names.grid(column=0, row=3)
        self.submit.grid(column=0, row=len(self.files)+4)

    def merge_pdf(self):
        if not len(self.files) > 0:
            return
        tempdir = filedialog.askdirectory(parent=self, initialdir=self.dir, title="Output")
        if not len(tempdir) > 0:
            return
        for pdf in self.files:
            self.merger.append(pdf)
        self.merger.write(tempdir + "/fileMerged.pdf")
        self.merger.close()
        messagebox.showinfo("PDF merge says:", "File saved as fileMerged.pdf")


app = App()
app.mainloop()
