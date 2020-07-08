            #-*- coding: cp1252 -*-                     #
            # ------------------------------------------#
            # Agenda eletronica em Python.              #
            # @autor: Víctor Donola Ferreira            #
            # ------------------------------------------#

#------------------------------------------------------------------------------#


#--------------------GLOBAL--------------------#
lista = [] # define uma variável para a lista

# lê os dados do arquivo e joga para a lista

arq2 = open("agenda.csv","a+")
lista = arq2.readlines()
arq2.close()
#-----------------------------------------------#
    

#------------------------------------------------------------------------------#

# função: menu, constroi o menu

def menu():
    print ("\n", "=" * 50) 
    print ("""\nAGENDA ELETRONICA\n\n
             escolha a opção: \n
             (1) Inserir contato:\n
             (2) Deletar:\n
             (3) Mostrar agenda:\n
             (4) Finalizar programa:\n""")
    
# fim da função menu



#------------------------------------------------------------------------------#
    
# função: lista_agenda, adiciona, remove e mostra a lista
    
def lista_agenda(nome, data, opc):

    if( opc == 1):
        contato = nome + ";" + data + "\n" # concatena o 'nome' ';' e 'data'
        lista.append(contato)
        lista.sort() # ordena a lista por prioridade

    elif (opc == 2):
        print ("=" * 30)
        if ( lista == []): # se lista for vazia
            print ("Lista Vazia\n")
        else:
            lista.pop(0)# remove o elemento de maior prioridade, ou seja, índice 0 da lista
            print ("Removido o elemento de maior prioridade")
        print ("=" * 30)

    elif (opc == 3):
        print ("=" * 30)
        if (lista == []):
            print ("Lista vazia!")
        else:
            print ("Nome:   | Data: ")
            for i in lista:
                print (i)
        print ("=" * 30)

    elif (opc == 4):
        arq = open("agenda.csv","w") # escreve por cima do arquivo antigo (atualiza lista)
        tam = len(lista) # recebe o tamanho da lista
        # for que insere os valores no arquivo separado por ';' sendo nome = índice par e data = impar

        for i in range(tam):
            arq.write(lista[i])

        arq.close()

# fim da função lista_agenda


        
#------------------------------------------------------------------------------#
# função principal


opc = 0 # variável para o menu

while (opc != 4 ):

    menu() # chama o menu

    while True:
        try:
            opc = int(input('')) # recebe a opção
            break
        except:
            print ("Digite somente numeros válidos")

    if ( opc == 1 ):
        nome = input("Informe o nome do contato: ")
        # print ("Informe o nome do contato: \n")
        # nome = input('\n: ')

        data = input("Informe a data de nascimento: ")
        #print ("informe a data de nascimento: \n")
        # data = input('\n: ')

        lista_agenda(nome, data, 1) # chama a função para inserir na lista

    elif ( opc == 2):
        lista_agenda(0,0,2) # chama a função para deletar o nome na lista

    elif (opc == 3): # chama a função para mostrar na tela
        print ("Lista de contatos: ")
        lista_agenda(0,0,3)
                

lista_agenda(0,0,4) # grava a lista na agenda
print ("FIM DO PROGRAMA! ")

#------------------------------------------------------------------------------#
# fim
    