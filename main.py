from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

###### Criando o primeiro usuario

# usuario = Usuario.create(nome="ProgramadorPython", email="teste@gmail.com",senha="123456")
# print("Novo usuario: ", usuario.id, usuario.nome, usuario.email)

###### Criando outros 3 uuarios

# Usuario.create(nome="Joao", email="joao@gmail.com", senha="124589")
# Usuario.create(nome="Paulo", email="pauloo@gmail.com", senha="seilapaulo")
# Usuario.create(nome="Marcos", email="aidentro@gmail.com", senha="olokomeu")

###### Listando os usuarios no banco de dados

# lista_usuarios = Usuario.select()
# print("Listando usuarios:")
# for u in lista_usuarios:
#     print("-", u.id, u.nome, u.email)


###### Fazendo update

# joao = Usuario.get( Usuario.nome == "Joao" )
# joao.nome = "Joaozinho"
# joao.save()
# print("Joao atualizado: ", joao.nome)

###### Tentando criar usuario que ja exite! 

# print("Tentando criar um usuario com email duplicado:")

# try:
#     usuario_duplicado = Usuario.create(nome="Duplicado", email="aidentro@gmail.com", senha="seilamermao")
# except:
#     print("Email ja cadastrado!")

###### Deletando usuario 

# usuario_deletado = Usuario.get( Usuario.email == "aidentro@gmail.com" )
# usuario_deletado.delete_instance()

# try:
#     Usuario.get( Usuario.email == "aidentro@gmail.com")
# except:
#     print("Usuar deletado")
