from tkinter import*
from PIL import Image, ImageTk
import tkinter.messagebox
import validation as vd
import subprocess

username = ""
password = ""


class LoginSystem:
    def __init__(self, root1):
        self.root = root1
        self.root.title("Login System")
        self.root.geometry("1199x599+100+50")
        self.root.resizable(FALSE, FALSE)
        self.u_name = tkinter.StringVar()
        self.pass_wd = tkinter.StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(Image.open(r"img\Imagebg.jpg"))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login frame
        frame_login = Frame(self.root, bg="#8FDDE7")
        frame_login.place(x=200, y=100, width=800, height=400)

        # login images
        self.logo = PhotoImage(file=r"img\Login_icon.png")
        self.user_icon = PhotoImage(file=r"img\Logousername15.png")
        self.pass_icon = PhotoImage(file=r"img\Password15.png")

        # Login frame module
        title = Label(frame_login, text="Login Here", bg="#8FDDE7", fg="#000C66", font=("Impact", 35, "bold"))
        title.place(x=300, y=5)
        login_logo = Label(frame_login, image=self.logo)
        login_logo.place(x=20, y=80, width=300, height=300)
        login_input = Frame(frame_login, bg="white")
        login_input.place(x=360, y=80, width=420, height=300)

        # login_input frame
        # heading "User Login Area"
        Label(login_input, text="User Login Area", bg="white", fg="#000C66",
              font=("Goudy old style", 20, "bold")).grid(row=0, columnspan=4, pady=10)
        # title: "Username" with icon
        Label(login_input, image=self.user_icon, text="Username", compound=LEFT, bg="white", fg="#000C66",
              font=("Goudy old style", 15, "bold")).grid(row=1, column=0, padx=20, pady=10)
        # username entry area
        Entry(login_input, textvariable=self.u_name, bd=5, relief=GROOVE,
              font=("", 15)).grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        # title: "Password" with icon
        Label(login_input, image=self.pass_icon, text="Password", compound=LEFT, bg="white", fg="#000C66",
              font=("Goudy old style", 15, "bold")).grid(row=2, column=0, padx=20, pady=10)
        # password entry area
        Entry(login_input, textvariable=self.pass_wd, bd=5, relief=GROOVE, show="*",
              font=("", 15)).grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        # Action buttons
        # forget password
        Button(login_input, text="forget password?", bg="white", fg="#000C66", bd=0, cursor="hand2",
               command=self.fg_function, font=("Goudy old style", 13, "italic", "underline")).grid(row=3, column=3,
                                                                                                   padx=10, pady=5)
        # sign in
        Button(login_input, text="Sign In for new user", bg="white", fg="#000C66", bd=0, cursor="hand2",
               font=("Goudy old style", 13, "italic", "underline"),
               command=self.sign_in_function).grid(row=4, column=3, padx=10, pady=0)
        # log in button
        Button(login_input, text="Log In", bg="white", fg="#000C66", cursor="hand2", command=self.login_function,
               font=("Goudy old style", 13, "bold", "underline"), width=10).grid(row=5, column=2,  padx=0, pady=10)
        # cancel button
        Button(login_input, text="Cancel", bg="white", fg="#000C66", width=10, cursor="hand2", command=self.root.quit,
               font=("Goudy old style", 13, "bold", "underline")).grid(row=5, column=3, padx=0, pady=10)

    def login_function(self):
        user_name = self.u_name.get()
        pass_word = self.pass_wd.get()

        if self.u_name.get() == "" or self.pass_wd.get() == "":
            tkinter.messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            result, f_name, s_name = vd.ck_val(user_name, pass_word)

            if result == 0:
                tkinter.messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                tkinter.messagebox.showinfo("Login Successful", f"Welcome, {f_name} {s_name}!\n Have a nice day.",
                                            parent=self.root)
        self.root.quit()

    def sign_in_function(self):
        subprocess.run('python signinform.py')
        self.root.quit()

    def fg_function(self):
        subprocess.run('python forgotpassword.py')
        self.root.quit()


root = Tk()
obj = LoginSystem(root)

root.mainloop()
