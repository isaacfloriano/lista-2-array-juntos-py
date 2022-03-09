lista_usuario = ["maria@gmail.com", "pedro@hotmail.com", "joao@outlook.com"]
lista_senha = ["mari321", "pd123", "jjCatuaba"]

for usuario, senha in zip(lista_usuario, lista_senha):
    print(f"{usuario}|{senha}")