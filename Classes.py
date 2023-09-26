class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm
    
    def getUser(self):
        return self.user
    def getSenha(self):
        return self.senha
    def getIDadm(self):
        return self.id_adm
    
    def cadastrar_adm(self, user, senha):
        adm = Adm(user, senha)
        loja.inserir_adm(adm)

    
class Cliente:
    def __init__(self, nome, cpf, idade, endereço, senha, idc):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereço
        self.senhacli = senha
        self.id = idc
    
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCpf(self):
        return self.cpf

    def getEndereco(self):
        return self.endereco

    def get_Senha(self):
        return self.senhacli

    def getId(self):
        return self.id


class Produto:
    def __init__(self, nome_produto, descricao, valor, idp):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.idp = idp

    def get_nome_produto(self):
        return self.nome_produto

    def get_descricao(self):
        return self.descricao

    def get_valor(self):
        return self.valor

    def get_idp(self):
        return self.idp
        

class Carrinho:
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
    
    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.valor

    def get_descricao(self):
        return self.descricao
        
class Loja:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome 
        self.endereco = endereco
        self.cnpj = cnpj
        self.adm = {}
        self.produtos = {}
        self.clientes = {}
    
    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

    def get_cnpj(self):
        return self.cnpj

    def inserir_cliente(self, valor, vetor):
        self.clientes[vetor] = valor
    
    def inserir_produto(self, valor, vetor):
        self.produtos[vetor] = valor

    def inserir_adm(self, valor):
        vetor = len(self.adm) + 1
        self.adm[vetor] = valor


    def listarClientes(self):
        for chave, cliente in self.clientes.items():
            print(f"ID:{chave} - Nome: {cliente.getNome()} - CPF: {cliente.getCpf()} - Idade: {cliente.getIdade()} - Endereço: {cliente.getEndereco()}")

    def listarProdutos(self):
        for chave, produto in self.produtos.items():
            print(f"ID:{chave} - Nome: {produto.get_nome_produto()} - Descrição: {produto.get_descricao()} - Valor: R${produto.get_valor()}")
    
    def excluir_produto(self, vetor):
        self.vetor = vetor-1
        return self.produtos.pop(vetor)

    def excluir_cliente(self, vetor):
        self.vetor = vetor-1
        return self.clientes.pop(vetor)



loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
master = Adm("adm", "admin123",0)
loja.inserir_adm(master)