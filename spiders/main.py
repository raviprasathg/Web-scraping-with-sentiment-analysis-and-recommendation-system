from tkinter import *
from tkinter import filedialog, messagebox
import os
import FKScrape

path_name = ""
def open_file():
    global path_name
    path = filedialog.askopenfile(initialdir = "/", title = "Select Files", filetypes = (("text files","*.txt"),("all files","*.*")))

    path_name = path.name
    username_login_entry.insert(0,path_name)

    
def scrape():
    try:
        FKScrape.FKScrape(path_name)
    except:
        messagebox.showerror("Web Scraping with Sentimental Analysis and RPA","Unfortunatey some error ocured")
        return
    messagebox.showinfo("Web Scraping with Sentimental Analysis and RPA","SCRAPING SUCCESSFUL")


screen = Tk()
screen.title("Web Scraping with Sentimental Analysis and RPA")
screen.iconbitmap(f"{os.getcwd()}\\Icon\\flipkart_logo_icon.ico")
screen.geometry("700x300")
Label(screen, text="⏰TIME is your greatest ASSET⏰\n", font = (10),fg = 'green').pack()
Label(screen, text="").pack()
Label(screen, text="Please browse the file that contain the links", font = (10)).pack()
Label(screen, text="").pack()
username_login_entry = Entry(screen, textvariable="File Location", width = 40)
username_login_entry.pack()
Button(screen, text="Browse", width=10, height=1, command = open_file).pack()
Label(screen, text="").pack()
Button(screen, text="Scrape", width=10, height=1,font = (6),command = scrape).pack()
screen.mainloop()

