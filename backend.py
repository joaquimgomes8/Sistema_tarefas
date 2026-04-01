import os
from flask import Flask, render_template, request, redirect
#======================FUNCOES===================================
def Menu():
    os.system('cls')
    print("Lista de tarefas:\n")
    print("01 - Mostrar lista;")
    print("02 - Adicionar na lista;")
    print("0 - Sair\n")
    escolha = input("Digite:")
    return escolha

def Mostrar_lista():
    os.system('cls')
    print("Lista:\n")
    for item in lista:
        print(item)
    input("\nDigite uma tecla para continuar...")

#======================LISTA====================================

# backend.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lista = [] # Variável global onde as tarefas serão guardadas

@app.route('/')
def index():
    # Envia a lista para o index.html exibir as tarefas
    return render_template('index.html', tarefas=lista)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Captura o texto do input pelo atributo name="tarefa_digitada" do HTML
    nova_tarefa = request.form.get('tarefa_digitada') 
    
    if nova_tarefa:
        lista.append(nova_tarefa) # Adiciona à lista
        
    return redirect('/') # Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True)

#======================COMEÇO====================================

verdadeiro = 1

while verdadeiro == 1:
    opcao = Menu()

    if opcao == "1":
        os.system('cls')
        Mostrar_lista()
    elif opcao == "2":
        os.system('cls')
        adicionar_na_lista = input("Digite uma tarefa:")
        lista.append(adicionar_na_lista)
    elif opcao == "0":
        verdadeiro = 2
    else:
        os.system('cls')
        print("Opcao nao reconhecida!")


