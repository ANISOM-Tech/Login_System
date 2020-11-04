from tkinter import *
from tkcalendar import DateEntry
import tkinter.messagebox
import newreg as nrg


class ForgotPassword:
    def __init__(self, root1):
        self.root = root1
        self.root.title("Sign In Form")
        self.root.geometry("400x600+400+50")
        self.root.resizable(FALSE, FALSE)
        Label(self.root, bg="#D4F1F4").place(x=0, y=0, relwidth=1, relheight=1)

        # catch variables
        self.name = tkinter.StringVar()
        self.surname = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.checkbox = IntVar()

        # heading "User Details"
        Label(self.root, text="Enter Your Details", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 20, "bold", "underline")).place(x=80, y=10)
        # title: First Name
        Label(self.root, text="First Name", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 15, "bold")).place(x=30, y=60)
        # 1st name entry area
        Entry(self.root, bd=1, relief=GROOVE, textvariable=self.name,
              font=("", 15)).place(x=30, y=90, width=340, height=30)
        # title: Surname
        Label(self.root, text="Surname", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 15, "bold")).place(x=30, y=140)
        # surname entry area
        Entry(self.root, bd=1, relief=GROOVE, textvariable=self.surname,
              font=("", 15)).place(x=30, y=170, width=340, height=30)

        # title: "date of birth" with icon
        Label(self.root, text="Date of birth", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 15, "bold")).place(x=30, y=220)
        # dob entry area
        self.cal = DateEntry(self.root, bd=1, relief=GROOVE, font=("", 15), date_pattern='dd/MM/yyyy')
        self.cal.place(x=30, y=250, width=340, height=30)
        # title: "e-mail address"
        Label(self.root, text="e-mail address", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 15, "bold")).place(x=30, y=300)
        # e-mail address entry area
        Entry(self.root, bd=1, relief=GROOVE, textvariable=self.email,
              font=("", 15)).place(x=30, y=330, width=340, height=30)
        # title: "contact number" with icon
        Label(self.root, text="Contact Number", bg="#D4F1F4", fg="#000C66",
              font=("Goudy old style", 15, "bold")).place(x=30, y=380)
        # contact number entry area
        Entry(self.root, bd=1, relief=GROOVE, textvariable=self.contact,
              font=("", 15)).place(x=30, y=410, width=340, height=30)

        # check box
        Checkbutton(self.root, text="I am accepting all terms and condition.", offvalue=0, bg="#D4F1F4",
                    fg="#000C66", variable=self.checkbox).place(x=30, y=450)

        # Action buttons
        # log in button
        Button(self.root, text="Register", bg="white", fg="#000C66", cursor="hand2", command=self.fg_pass,
               font=("Goudy old style", 13, "bold", "underline"), width=15).place(x=30, y=520)
        # cancel button
        Button(self.root, text="Cancel", bg="white", fg="#000C66", width=15, cursor="hand2", command=self.root.quit,
               font=("Goudy old style", 13, "bold", "underline")).place(x=210, y=520)

    def fg_pass(self):
        i = self.cal.get_date()
        if self.name.get() == "" or self.surname.get() == "" or self.email.get() == "" or self.contact.get() == "" or \
                self.checkbox.get() == 0 or i.year == 2020:
            tkinter.messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            user_n, passwd = nrg.reg_new(self.name.get(), self.surname.get(), i, self.email.get(), self.contact.get())
            tkinter.messagebox.showinfo("Registration Successful",
                                        f"Welcome, {self.name.get()}!\n Your Username is {user_n}"
                                        f"\n Your password is {passwd}", parent=self.root)
            self.root.quit()


root = Tk()
obj = ForgotPassword(root)
root.mainloop()
