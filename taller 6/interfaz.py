import customtkinter # Tkinter es una biblioteca de Python para crear interfaces gráficas de usuario (GUI). 
#CustomTkinter es una extensión de Tkinter que proporciona widgets personalizados y un estilo moderno 
# para mejorar la apariencia de las aplicaciones Tkinter. CustomTkinter permite a los desarrolladores crear 
# aplicaciones más atractivas y personalizables utilizando la misma funcionalidad básica de Tkinter.

# Create the main application window
app = customtkinter.CTk()

# Set the title and size of the window
app.title("CustomTkinter Example")
app.geometry("400x300")

# Create a label
label = customtkinter.CTkLabel(app, text="Hello, CustomTkinter!", font=("Arial", 16))
label.pack(pady=20)

# Create a button
def button_callback():
    label.configure(text="Button Clicked!")

button = customtkinter.CTkButton(app, text="Click Me", command=button_callback)
button.pack(pady=10)

# Create an entry field
entry = customtkinter.CTkEntry(app, placeholder_text="Type something...")
entry.pack(pady=10)

# Run the application
app.mainloop()
