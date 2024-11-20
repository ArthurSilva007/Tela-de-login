# import tkinter

# """" criando janela """

# janela = tkinter.Tk()
# janela.geometry("500x500")


# """ função """
# def clique():
#     print("Fazer login")


# """" criando text label """

# texto = tkinter.Label(janela, text="Fazer login")
# texto.pack(padx=10, pady=10)

# """" buttons """

# botao = tkinter.Button(janela, text="login")
# botao.pack(padx=10, pady=10)




# janela.mainloop()

import customtkinter

"""" stylization """

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

""" criando janela """

janela = customtkinter.CTk()
janela.geometry("500x500")


""" função """
def clique():
     print("Fazer login")


""" criando text """
texto = customtkinter.CTkLabel(janela, text="Fazer login")
texto.pack(padx=10, pady=10)


""" build word email """

email = customtkinter.CTkEntry(janela, placeholder_text="Email")
email.pack(padx=10, pady=10)

""" build for password """

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)


""" check box """

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar-me")
checkbox.pack(padx=10, pady=10)

""" buttons """

botao = customtkinter.CTkButton(janela, text="login",  command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()