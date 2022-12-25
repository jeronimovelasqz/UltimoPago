from tkinter import *



class Pago:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("836x692")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 692,
            width = 836,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.img0 = PhotoImage(file = f"img0Pago.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b0.place(
            x = 33, y = 563,
            width = 288,
            height = 50)

        self.img1 = PhotoImage(file = f"img1Pago.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b1.place(
            x = 354, y = 563,
            width = 264,
            height = 50)

        self.background_img = PhotoImage(file = f"backgroundPago.png")
        self.background = self.canvas.create_image(
            456.0, 279.5,
            image=self.background_img)

        self.entry0_img = PhotoImage(file = f"img_textBox0Pago.png")
        self.entry0_bg = self.canvas.create_image(
            107.5, 525.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#88c9d8",
            highlightthickness = 0)

        self.entry0.place(
            x = 43.0, y = 500,
            width = 129.0,
            height = 48)

        self.entry1_img = PhotoImage(file = f"img_textBox1Pago.png")
        self.entry1_bg = self.canvas.create_image(
            207.0, 405.0,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#88c9d8",
            highlightthickness = 0)

        self.entry1.place(
            x = 42.0, y = 380,
            width = 330.0,
            height = 48)

        self.entry2_img = PhotoImage(file = f"img_textBox2Pago.png")
        self.entry2_bg = self.canvas.create_image(
            504.5, 405.0,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#88c9d8",
            highlightthickness = 0)

        self.entry2.place(
            x = 440.0, y = 380,
            width = 129.0,
            height = 48)

        self.entry3_img = PhotoImage(file = f"img_textBox3Pago.png")
        self.entry3_bg = self.canvas.create_image(
            211.0, 302.0,
            image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#88c9d8",
            highlightthickness = 0)

        self.entry3.place(
            x = 46.0, y = 277,
            width = 330.0,
            height = 48)

        self.window.resizable(False, False)
        self.window.mainloop()


    def btn_clicked(self):
        print("Button Clicked")

eso = Pago()