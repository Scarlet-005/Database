import tkinter as tk
import Database
from tkinter import ttk


# ---------------- GUI FUNCTIONS ---------------- #

# ADD RECORD
def gui_add_record():

    username = username_entry.get()
    display_name = display_entry.get()

    affiliation = affiliation_var.get()

    skill = (
        skill_num_var.get() + " | " +
        skill_rank_var.get() + " | " +
        skill_state_var.get()
    )

    Database.add_record(
        username,
        display_name,
        affiliation,
        skill
    )

    gui_view_records()


# VIEW RECORDS
def gui_view_records():

    rows = Database.view_records()

    # NEW WINDOW
    view_window = tk.Toplevel(root)

    view_window.title("View Records")

    view_window.geometry("900x500")


    # TABLE
    table = ttk.Treeview(
        view_window,
        columns=("ID", "Username", "Display Name", "Affiliation", "Skill"),
        show="headings"
    )

    table.heading("ID", text="ID")
    table.heading("Username", text="Username")
    table.heading("Display Name", text="Display Name")
    table.heading("Affiliation", text="Affiliation")
    table.heading("Skill", text="Skill Level")


    table.column("ID", width=50)
    table.column("Username", width=150)
    table.column("Display Name", width=150)
    table.column("Affiliation", width=100)
    table.column("Skill", width=250)

    table.pack(fill="both", expand=True)


    # INSERT DATA
    for row in rows:
        table.insert("", tk.END, values=row)
# SEARCH RECORD
def gui_search_record():

    username = username_entry.get()

    rows = Database.search_record(username)

    # NEW WINDOW
    search_window = tk.Toplevel(root)

    search_window.title("Search Results")

    search_window.geometry("900x500")


    # TABLE
    table = ttk.Treeview(
        search_window,
        columns=("ID", "Username", "Display Name", "Affiliation", "Skill"),
        show="headings"
    )

    table.heading("ID", text="ID")
    table.heading("Username", text="Username")
    table.heading("Display Name", text="Display Name")
    table.heading("Affiliation", text="Affiliation")
    table.heading("Skill", text="Skill Level")

    table.column("ID", width=50)
    table.column("Username", width=150)
    table.column("Display Name", width=150)
    table.column("Affiliation", width=100)
    table.column("Skill", width=250)

    table.pack(fill="both", expand=True)


    # INSERT SEARCH RESULTS
    for row in rows:
        table.insert("", tk.END, values=row)
# DELETE RECORD
def gui_delete_record():

    record_id = id_entry.get()

    Database.delete_record(record_id)

    gui_view_records()


# UPDATE RECORD
def gui_update_record():

    record_id = id_entry.get()

    new_skill = (
        skill_num_var.get() + " | " +
        skill_rank_var.get() + " | " +
        skill_state_var.get()
    )

    Database.update_record(record_id, new_skill)

    gui_view_records()


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()

root.title("Database System")


# CENTER WINDOW
window_width = 900
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# TITLE
title = tk.Label(
    root,
    text="Database System",
    font=("Arial", 20)
)

title.pack(pady=20)


# ID ENTRY FOR DELETE/UPDATE
id_label = tk.Label(root, text="Record ID (For Delete/Update)")
id_label.pack()

id_entry = tk.Entry(
    root,
    justify="center",
    width=20
)

id_entry.pack(pady=5)


# USERNAME ENTRY
username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(
    root,
    justify="center",
    width=40
)

username_entry.pack(pady=5)


# DISPLAY NAME ENTRY
display_label = tk.Label(root, text="Display Name")
display_label.pack()

display_entry = tk.Entry(
    root,
    justify="center",
    width=40
)

display_entry.pack(pady=5)


# AFFILIATION DROPDOWN
affiliation_label = tk.Label(root, text="Affiliation")
affiliation_label.pack()

affiliation_var = tk.StringVar()
affiliation_var.set("Ally")

affiliation_menu = tk.OptionMenu(
    root,
    affiliation_var,
    "Ally",
    "Enemy"
)

affiliation_menu.pack(pady=5)


# SKILL LEVEL LABEL
skill_label = tk.Label(root, text="Skill Level")
skill_label.pack()


# SKILL NUMBER DROPDOWN
skill_num_var = tk.StringVar()
skill_num_var.set("1")

skill_num_menu = tk.OptionMenu(
    root,
    skill_num_var,
    "1",
    "2",
    "3"
)

skill_num_menu.pack(pady=3)


# SKILL RANK DROPDOWN
skill_rank_var = tk.StringVar()
skill_rank_var.set("Low")

skill_rank_menu = tk.OptionMenu(
    root,
    skill_rank_var,
    "Low",
    "Mid",
    "High"
)

skill_rank_menu.pack(pady=3)


# SKILL STATE DROPDOWN
skill_state_var = tk.StringVar()
skill_state_var.set("Weak")

skill_state_menu = tk.OptionMenu(
    root,
    skill_state_var,
    "Weak",
    "Stable",
    "Strong"
)

skill_state_menu.pack(pady=3)


# BUTTON FRAME
button_frame = tk.Frame(root)

button_frame.pack(pady=20)


# ADD BUTTON
add_button = tk.Button(
    button_frame,
    text="Add Record",
    width=15,
    command=gui_add_record
)

add_button.grid(row=0, column=0, padx=5)


# VIEW BUTTON
view_button = tk.Button(
    button_frame,
    text="View Records",
    width=15,
    command=gui_view_records
)

view_button.grid(row=0, column=1, padx=5)


# SEARCH BUTTON
search_button = tk.Button(
    button_frame,
    text="Search Record",
    width=15,
    command=gui_search_record
)

search_button.grid(row=0, column=2, padx=5)


# DELETE BUTTON
delete_button = tk.Button(
    button_frame,
    text="Delete Record",
    width=15,
    command=gui_delete_record
)

delete_button.grid(row=1, column=0, pady=10)


# UPDATE BUTTON
update_button = tk.Button(
    button_frame,
    text="Update Skill",
    width=15,
    command=gui_update_record
)

update_button.grid(row=1, column=1, pady=10)


# TREEVIEW TABLE
table = ttk.Treeview(
    root,
    columns=("ID", "Username", "Display Name", "Affiliation", "Skill"),
    show="headings",
    height=15
)

table.heading("ID", text="ID")
table.heading("Username", text="Username")
table.heading("Display Name", text="Display Name")
table.heading("Affiliation", text="Affiliation")
table.heading("Skill", text="Skill Level")


table.column("ID", width=50)
table.column("Username", width=150)
table.column("Display Name", width=150)
table.column("Affiliation", width=100)
table.column("Skill", width=250)

table.pack(pady=20, fill="both", expand=True)
# RUN GUI
root.mainloop()