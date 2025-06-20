from tkinter import *

#cree la fenetre
window = Tk ()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("PSG-LOGO1.ico")
window.config(background='#4065A4')

#creation d'image
width = 500
height = 500
image = PhotoImage(file="password_onboarding.png").zoom(15).subsample(13)
canvas = Canvas(window, width=width, height=height, bg='#4065A4')
canvas.create_image(width/2, height/2, image=image )
canvas.pack(expand=YES)

#afficher la fenetre
window.mainloop()