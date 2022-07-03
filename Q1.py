codigo = int(input())
senha = int(input())

print("Codigo: {}".format(codigo))
print("Senha: {}".format(senha))




def validaAcesso(codigo, senha):
    if(codigo == senha):
        print("Saída: Acesso permitido")
    else:
        print("Saida: Usuario invalido!")


validaAcesso(codigo, senha)



