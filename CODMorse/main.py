class No: #Aqui criei a classe (nó) que representa um nó na classe bina´ria.
    def __init__(self, caractere, codigo_morse): #Aqui é o construtor, ele inicializa um novo nó com um caractere no cod morse.
        self.caractere = caractere # Aqui ele está armazenando o caractere no nó
        self.codigo_morse = codigo_morse # Aqui ele armazena o código morse no nó
        self.esquerdo = None # Aqui ele está inicializando o filho esquerdo como NONE, indica q n tem nó filho.
        self.direito = None # Aqui ele está inicializando o filho direito como NONE.
# O NONE é necessário pq qnd a gente cria o nó, ele não tem filhos, se e´NONE, quer dizer q eu posso inserir um novo nó.

class ArvoreMorse: # Aqui defini a classe ArvoreMorse q representa a árvore binária de busca.
    def __init__(self): #Aqui é apenas o construtor da classe ArvoreMorse.
        self.raiz = None # Aqui indica que a árvore começa vazia.

# MÉTODO INSERIR
def inserir(self, caractere, codigo_morse): # Método para inserir um novo caractere e seu código Morse na árvore.
    if self.raiz is None: # Aqui ele verifica se a árvore está vazia.
        self.raiz = No(caractere, codigo_morse) #Aqui após verificar q ta vazia, ele cria um novo nó e o define como raiz.
    else: # Se a árvore não estiver vazia, chama o método recursivo para inserir o novo nó.
        self._inserir_recursivo(self.raiz, caractere, codigo_morse)

# MÉTODO INSERIR RECURSIVO - Ele é chamado recursivamente até encontrar o local apropriado para um novo nó.
def _inserir_recursivo(self, no, caractere, codigo_morse): # Aqui é um método privado que insere recursivamente um novo nó na árvore.
    if codigo_morse == '': # Se o código Morse estiver vazio, retorna (condição de parada) Se ta vazio, é pq n tem + nd p inserir.
        return # Retorna pois não tem mais nada para ser inserido.
    if codigo_morse[0] == '.': # Se o primeiro caractere for um ponto (.), insere à esquerda.
        if no.esquerdo is None: # Se não houver filho esquerdo, cria um novo nó ali.
            no.esquerdo = No(caractere, codigo_morse[1:]) #Se não houver um filho esquerdo (no.esquerdo=None), criamos um novo nó com o caractere atual
            #e o restante do código Morse (codigo_morse[1:], que representa o código sem o primeiro caractere).
        else: # Se já existir, chama recursivamente para o filho esquerdo.
            self._inserir_recursivo(no.esquerdo, caractere, codigo_morse[1:]) # Se já houver um filho esquerdo, chamamos recursivamente o método para continuar a inserção nesse filho. Passamos o filho esquerdo (no.esquerdo) como o novo nó atual e o restante do código Morse.
    elif codigo_morse[0] == '-': #Aqui verificamos se o primeiro caractere do código Morse é um traço (-). Isso indica que devemos mover para o filho direito.
        if no.direito is None:
            no.direito = No(caractere, codigo_morse[1:]) #Se não houver um filho direito (no.direito é None), criamos um novo nó com o caractere atual e o restante do código Morse.
        else: # Se já houver um filho direito, chamamos recursivamente o método para continuar a inserção nesse filho, passando o filho direito como o novo nó atual.
            self._inserir_recursivo(no.direito, caractere, codigo_morse[1:])

# MÉTODO DECODIFICAR
def decodificar(self, sequencia_morse): # Método que decodifica uma sequência de código Morse.
    resultado = [] # Inicializa uma lista para armazenar os caracteres decodificados.
    no_atual = self.raiz # Começa a partir da raiz da árvore.
    for simbolo in sequencia_morse.split(' '): # Para cada símbolo (caractere Morse) na sequência (separados por espaço).
        no_atual = self.raiz # Reinicia o nó atual para a raiz para cada novo símbolo.
        for char in simbolo: # Para cada caractere do símbolo.
            if char == '.': # Move para o filho esquerdo se for um ponto
                no_atual = no_atual.esquerdo 
            elif char == '-': # Move para o filho direito se for um traço.
                no_atual = no_atual.direito
        resultado.append(no_atual.caractere) # Adiciona o caractere encontrado à lista de resultados.
    return ''.join(resultado) # Retorna a mensagem decodificada como uma string.

# MÉTODO IMPRIMIR ÁRVORE COM CHAT GPT
def imprimir_arvore(self, no, nivel=0):
    if no is not None:
        self.imprimir_arvore(no.direito, nivel + 1)
        print(' ' * 4 * nivel + '-> ' + no.caractere + ' (' + no.codigo_morse + ')')
        self.imprimir_arvore(no.esquerdo, nivel + 1)

# MÉTODO POPULAR ÁRVORE 
def popular_arvore(arvore_morse): # Função para preencher a árvore com os caracteres e seus códigos Morse.
    dicionario_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
    for caractere, codigo in dicionario_morse.items(): # Para cada caractere e código no dicionário.
        arvore_morse.inserir(caractere, codigo) # Insere na árvore.

# FUNÇÃO PRINCIPAL

def principal(): # Função principal do programa.
    arvore_morse = ArvoreMorse() # Cria uma nova instância da árvore Morse.
    popular_arvore(arvore_morse) # Preenche a árvore com os caracteres e seus códigos.
    
    print("Árvore Morse:") # Imprime msg.   
    arvore_morse.imprimir_arvore(arvore_morse.raiz) # Imprime a estrutura da árvore.

    sequencia_morse = input("Digite a sequência em código Morse (separada por espaços): ") # Insere aq a sequência
    mensagem_decodificada = arvore_morse.decodificar(sequencia_morse) # Decodifica a sequência inserida.
    
    print("Mensagem decodificada:", mensagem_decodificada) # Exibe a mensagem decodificada.

if __name__ == "__main__": # Verifica se o arquivo está sendo executado como o programa principal.
    principal() # Chama a função principal para executar o código.

