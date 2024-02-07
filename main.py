import tkinter as tk


def logout():
    hub.pack_forget()
    start_vindu()

def login():
    start_vindu.pack_forget()
    hub()

def elever():
    pass

def ny_elev():
    pass

def klasser():
    pass

def annet():
    pass


def hub():
    hub = tk.Frame(root, width=500, height=500, bg="red")
    hub.pack()

    title_lable = tk.Label(hub, text="velkommen", font=("Arial", 24), bg="red")
    title_lable.place(x=250, y=100, anchor="center")

    logout_btn = tk.Button(hub, text="Logout", command=logout)
    logout_btn.place(x=420, y=420, anchor="se")

    # elever, ny elev, klasser, annet knapper
    elever_btn = tk.Button(hub, text="Elever", command=elever)
    elever_btn.place(x=250, y=200, anchor="center")

    ny_elev_btn = tk.Button(hub, text="Ny elev", command=ny_elev)
    ny_elev_btn.place(x=250, y=250, anchor="center")

    klasser_btn = tk.Button(hub, text="Klasser", command=klasser)
    klasser_btn.place(x=250, y=300, anchor="center")

    annet_btn = tk.Button(hub, text="Annet", command=annet)
    annet_btn.place(x=250, y=350, anchor="center")




root = tk.Tk()
root.title("database")

start_vindu = tk.Frame(root, width=500, height=500, bg="white")
start_vindu.pack()

title_lable = tk.Label(start_vindu, text="Database", font=("Arial", 24), bg="white")
title_lable.place(x=250, y=100, anchor="center")

username = tk.Entry(start_vindu, width=30)
username.place(x=265, y=200, anchor="w")

username_label = tk.Label(start_vindu, text="Username", bg="white")
username_label.place(x=245, y=200, anchor="e")

password = tk.Entry(start_vindu, width=30)
password.place(x=265, y=250, anchor="w")

password_label = tk.Label(start_vindu, text="Password", bg="white")
password_label.place(x=245, y=250, anchor="e")

btn = tk.Button(start_vindu, text="Login", command=login)
btn.place(x=250, y=300, anchor="center")

root.mainloop()
