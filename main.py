import tkinter as tk
from tkinter import ttk

def create_frame(root, color):
    frame = tk.Frame(root, width=500, height=500, bg=color)
    frame.pack()
    return frame

def create_label(frame, text, color, x, y):
    label = tk.Label(frame, text=text, font=("Arial", 24), bg=color)
    label.place(x=x, y=y, anchor="center")
    return label

def create_button(frame, text, command, x, y):
    button = tk.Button(frame, text=text, command=command)
    button.place(x=x, y=y, anchor="center")
    return button

def show_frame(frame_to_show, frame_to_hide):
    frame_to_hide.pack_forget()
    frame_to_show.pack()

def home():
    show_frame(start_vindu, hub)

def logout():
    show_frame(start_vindu, hub)

def login():
    show_frame(hub, start_vindu)

def show_elever():
    show_frame(elever, hub)

def show_ny_elev():
    show_frame(ny_elev, hub)

def show_ansat():
    show_frame(ansat, hub)

def show_klasser():
    show_frame(klasser, hub)

def klasser_Hub():
    show_frame(hub, klasser)

def ansat_Hub():
    show_frame(hub, ansat)

def 


    
root = tk.Tk()
root.title("database")

start_vindu = create_frame(root, "white")
create_label(start_vindu, "Database", "white", 250, 100)

username = tk.Entry(start_vindu, width=30)
username.place(x=265, y=200, anchor="w")

username_label = tk.Label(start_vindu, text="Username", bg="white")
username_label.place(x=245, y=200, anchor="e")

password = tk.Entry(start_vindu, width=30)
password.place(x=265, y=250, anchor="w")

password_label = tk.Label(start_vindu, text="Password", bg="white")
password_label.place(x=245, y=250, anchor="e")

create_button(start_vindu, "Login", login, 250, 300)

hub = create_frame(root, "red")
hub.pack_forget()

create_label(hub, "velkommen", "red", 250, 100)

create_button(hub, "Logout", logout, 420, 420)
create_button(hub, "Elever", show_elever, 250, 200)
create_button(hub, "Ny elev", show_ny_elev, 250, 250)
create_button(hub, "Ansat", show_ansat, 250, 300)
create_button(hub, "Klasser", show_klasser, 250, 350)

# Elever frame
elever = create_frame(root, "blue")
elever.pack_forget()

title_lable = create_label(elever, "Elever", "blue", 250, 100)

personer = [("Ola", "", "Nordmann"), ("Kari", "", "Nordmann"), ("Per", "Nordmann"), ("Pål", "", "Nordmann")]

column = ("Fornavn", "mellomnavn", "Etternavn")

treeview = ttk.Treeview(elever, columns=column, show="headings")
treeview.pack()

treeview.heading("Fornavn", text="Fornavn")
treeview.heading("mellomnavn", text="Mellomnavn")
treeview.heading("Etternavn", text="Etternavn")

for p in personer:
    treeview.insert("", "end", values=p)

title_lable = create_label(elever, "Elever", "blue", 250, 100)

HomeBTN1 = create_button(elever, "Hjem", show_hub, 250, 400)

# Ny elev frame
ny_elev = create_frame(root, "green")
ny_elev.pack_forget()

title_lable = create_label(ny_elev, "Ny elev", "green", 250, 100)

HomeBTN2 = create_button(ny_elev, "Hjem", show_hub, 250, 400)

# Ansat frame
ansat = create_frame(root, "yellow")
ansat.pack_forget()

title_lable = create_label(ansat, "Ansat", "yellow", 250, 100)

HomeBTN3 = create_button(ansat, "Hjem", show_hub, 250, 400)

# Klasser frame
klasser = create_frame(root, "purple")
klasser.pack_forget()

title_lable = create_label(klasser, "Klasser", "purple", 250, 100)

HomeBTN4 = create_button(klasser, "Hjem", show_hub, 250, 400)

root.mainloop()