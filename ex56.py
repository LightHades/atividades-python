class Fidelidade:
    def __init__(self):
        self.livro = 0
        self.pontos = 0

    def comprarLivro(self, qnt_livro):
        self.livro += qnt_livro
        if qnt_livro == 0:
            self.pontos += 0
        elif qnt_livro == 1:
            self.pontos += 5
        elif qnt_livro == 2:
            self.pontos += 15
        elif qnt_livro == 3:
            self.pontos += 30
        else:
            self.pontos += 60

    def consultarPontos(self):
        return self.pontos

    def listarBrindes(self):
        if self.pontos >= 20 and self.pontos <= 30:
            return ['EcoBag', 'Caneta personalizada']
        elif self.pontos >= 35 and self.pontos <= 60:
            return ['Livro (valor máximo R$30,00)', 'Luminária de cabeceira']
        elif self.pontos > 65:
            return ['2 Livros (valor máximo R$100,00)', 'Powerbank']
        else:
            return []

    def pegarBrinde(self, brinde):
        if brinde in self.listarBrindes():
            self.listarBrindes().remove(brinde)
            return 'Brinde selecionado: {}'.format(brinde)
        else:
            return 'Brinde indisponível.'

livraria = Fidelidade()
while True:
    print('\n[ 1 ] Comprar livro\n[ 2 ] Consultar pontos\n[ 3 ] Listar brindes\n[ 4 ] Pegar brinde')
    opt = int(input('\n>>> '))
    
    if opt == 1:
        qnt_livro = int(input('\nQuantidade de livros: '))
        livraria.comprarLivro(qnt_livro)
    elif opt == 2:
        print(f'\nVocê possui {livraria.consultarPontos()} pontos.')
    elif opt == 3:
        if livraria.listarBrindes():
            print(f'\nBrindes disponíveis: {livraria.listarBrindes()}')
            #for brinde in livraria.listarBrindes():
            #    print(' - ', brinde)
        else:
            print('\nVocê não tem direito a brindes.')
    elif opt == 4:
        brinde = input('\nDigite o nome do brinde que deseja escolher: ')
        resultado = livraria.escolher_brinde(brinde)
        print(resultado)
    elif opt == 5:
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')