import PySimpleGUI as sg  
sg.theme("DarkBlue3")
sg.theme_text_color("#000000")

window = sg.Window(title="Profile",
    layout=[
         [sg.Text("SELAMAT DATANG DI KELAS"
                  ,font=("Times",25,"bold","underline","italic"))],
         [sg.Text("NPM      : 2210010024",)],  
         [sg.Text("Nama     : Khaironi Fajerin")],  
         [sg.Text("Kelas     : 5B Non Regular Banjarmasin")],  
         [sg.Text("Matkul   : Pemrograman Visual 3")],  
    ], size=(490,250),
    font=("Arial",18))
window()
window.close() 