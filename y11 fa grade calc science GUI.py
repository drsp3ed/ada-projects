import customtkinter as ctk
root = ctk.CTk()
ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('system')
root.geometry('400x320')
root.title('ADA Science gpa calculator')

def button_pressed():
    a = list(map(float, entry.get().split(" ")))
    b = float(entry2.get())
    cpa=((a[0]+a[1]+a[2]+a[3])*0.2/4)
    aa=a[4]*0.15
    pa=a[5]*0.25
    fa=(b-cpa-aa-pa)/0.4
    label.configure(text=f"You need to get {fa:.02f} from the final exam")


frame = ctk.CTkFrame(root)

button = ctk.CTkButton(frame, command=button_pressed, text="Calculate", width=350)
entry = ctk.CTkEntry(frame, placeholder_text='CPA2 CPA3 CPA4 CPA5 AA PA (space as separator)', width=350)
label = ctk.CTkLabel(frame, text = "Overall", width=350)
entry2 = ctk.CTkEntry(frame, placeholder_text="Desirable overall", width=350)

frame.pack(pady=30)

entry.pack()
entry2.pack()
button.pack(pady = 5)
label.pack(pady = 0)

root.mainloop()