import customtkinter as ctk
import tkinter.filedialog as fd
import tkinter as tk
from tkinter import messagebox  

def choose_directory():
    dir_path = fd.askdirectory()
    if dir_path:
        dir_entry.configure(state="normal")
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, dir_path)
        dir_entry.configure(state="readonly")

def save_settings():

    messagebox.showinfo("Saved", "Successfully Saved!")

main = ctk.CTk()
main.title("EmRec - Emergency Recording")
main.geometry("600x420")
main.minsize(500, 300)
main.configure(fg_color="#23272D")

main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure(2, weight=1)
main.grid_rowconfigure(6, weight=1)


label = ctk.CTkLabel(master=main, text="SETTINGS:", font=("Arial", 25), text_color="#ffffff")
label.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="n")


label1 = ctk.CTkLabel(master=main, text="Save Directory:", text_color="#000", fg_color="#E4E2E2")
label1.grid(row=1, column=0, padx=10, sticky="w")

dir_entry = ctk.CTkEntry(master=main, width=280)
dir_entry.configure(state="readonly", text_color="#000")
dir_entry.grid(row=2, column=0, padx=10, pady=5, sticky="we")

browse_button = ctk.CTkButton(master=main, text="Browse", command=choose_directory)
browse_button.configure(width=80, fg_color="#029CFF", text_color="#fff", border_color="#000")
browse_button.grid(row=2, column=1, sticky="w", padx=10)


label2 = ctk.CTkLabel(master=main, text="Resolution:", text_color="#000", fg_color="#E4E2E2")
label2.grid(row=3, column=0, pady=(20, 5), padx=10, sticky="w")

res_var = ctk.IntVar()
res_frame = ctk.CTkFrame(master=main, fg_color="transparent")
res_frame.grid(row=4, column=0, padx=10, sticky="w")

res_0 = ctk.CTkRadioButton(master=res_frame, variable=res_var, text="720p", value=0, text_color="#000", fg_color="#E4E2E2", border_color="#000")
res_1 = ctk.CTkRadioButton(master=res_frame, variable=res_var, text="1080p", value=1, text_color="#000", fg_color="#E4E2E2", border_color="#000")
res_2 = ctk.CTkRadioButton(master=res_frame, variable=res_var, text="480p", value=2, text_color="#000", fg_color="#E4E2E2", border_color="#000")
res_0.pack(anchor="w")
res_1.pack(anchor="w")
res_2.pack(anchor="w")

label3 = ctk.CTkLabel(master=main, text="Duration:", text_color="#000", fg_color="#E4E2E2")
label3.grid(row=3, column=1, pady=(20, 5), padx=10, sticky="w")

dur_var = ctk.IntVar()
dur_frame = ctk.CTkFrame(master=main, fg_color="transparent")
dur_frame.grid(row=4, column=1, padx=10, sticky="w")

dur_0 = ctk.CTkRadioButton(master=dur_frame, variable=dur_var, text="10 sec", value=0, text_color="#000", fg_color="#E4E2E2", border_color="#000")
dur_1 = ctk.CTkRadioButton(master=dur_frame, variable=dur_var, text="30 sec", value=1, text_color="#000", fg_color="#E4E2E2", border_color="#000")
dur_2 = ctk.CTkRadioButton(master=dur_frame, variable=dur_var, text="1 min", value=2, text_color="#000", fg_color="#E4E2E2", border_color="#000")
dur_0.pack(anchor="w")
dur_1.pack(anchor="w")
dur_2.pack(anchor="w")


save_button = ctk.CTkButton(master=main, text="Save Settings", command=save_settings,
                            fg_color="#029CFF", text_color="#fff", border_color="#000", width=120, height=40)
save_button.grid(row=5, column=2, padx=10, pady=(20, 10), sticky="e")

# Footer
footer = ctk.CTkLabel(master=main, text="by DragonDreat", text_color="#aaaaaa", font=("Arial", 12))
footer.grid(row=6, column=0, columnspan=3, pady=(10, 10), sticky="s")

main.mainloop()
