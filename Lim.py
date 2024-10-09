from tkinter import *
from PIL import Image, ImageTk
from requests import *

def main_app():
    global root
    root.deiconify()  
    root.title("INSPIRATIONAL IMAGE")
    root.geometry("1000x600+50+50")
    f = ("Calibri", 30, "bold")

    def gi():
        try:
            url = "https://zenquotes.io/api/image"
            res = get(url)
            with open("image.png", "wb") as f:
                f.write(res.content)
            img = Image.open("image.png")
            imgtk = ImageTk.PhotoImage(image=img)
            lab.configure(image=imgtk)
            lab.photo = imgtk

        except Exception as e:
            print("issue", e)

    btn = Button(root, text="Get Image", font=f, command=gi)
    lab = Label(root, font=f)

    btn.pack(pady=10)
    lab.pack(pady=10)

def show_splash():
    splash = Toplevel()
    splash.title("App made by Nishant")
    splash.geometry("600x400+100+100")
    splash.configure(background='lightgreen')
    splash_label = Label(splash, text="App made by Aisan Shaikh", font=("Calibri", 30, "bold"), bg='lightgreen')
    splash_label.pack(expand=True)

    def close_splash():
        splash.destroy()
        main_app()

    splash.after(3000, close_splash)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the main root window
    show_splash()
    root.mainloop()
