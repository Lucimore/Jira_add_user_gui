from tkinter import *

window = Tk()
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth() // 2 - windowWidth // 2)
positionDown = int(window.winfo_screenheight() // 2 - windowHeight // 2)
window.minsize(300, 200)
window.geometry("+{}+{}".format(positionRight, positionDown))
window.title("Add users to project")


def clicked():
    global baseURL, login, password, project, role
    baseURL = jira_txt.get()
    login = login_txt.get()
    password = passwd_txt.get()
    project = (project_txt.get()).upper()
    role = selected.get()
    window.destroy()


jira_lbl = Label(window, text="Jira URL")
jira_lbl.grid(column=0, row=0, sticky="W")
jira_txt = Entry(window, width=30)
jira_txt.grid(column=1, row=0, sticky="W")

login_lbl = Label(window, text="Login")
login_lbl.grid(column=0, row=1, sticky="W")
login_txt = Entry(window, width=30)
login_txt.grid(column=1, row=1, sticky="W")

passwd_lbl = Label(window, text="Password")
passwd_lbl.grid(column=0, row=2, sticky="W")
passwd_txt = Entry(window, width=30, show="*")
passwd_txt.grid(column=1, row=2, sticky="W")

project_lbl = Label(window, text="Project")
project_lbl.grid(column=0, row=3, sticky="W")
project_txt = Entry(window, width=6)
project_txt.grid(column=1, row=3, sticky="W")

selected = StringVar(None, '10001')
rad1 = Radiobutton(window, text='Developer', value='10001', variable=selected)
rad2 = Radiobutton(window, text='User', value='10000', variable=selected)
rad1.grid(column=0, row=4, sticky="W")
rad2.grid(column=1, row=4, sticky="W")

btn = Button(window, text="Start", command=clicked, height=2, width=5,
             fg='#37d3ff',
             bg='#001d26',
             bd=10,
             highlightthickness=4,
             highlightcolor="#37d3ff",
             highlightbackground="#37d3ff",
             borderwidth=4
             )
btn.grid(column=0, row=6)

window.mainloop()
