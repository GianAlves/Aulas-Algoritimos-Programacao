from Lista import Lista

lista = Lista()
opcao = "" 

while( opcao != "0" ):
    print("\n----------------------")
    print("1 - Adicionar no Início")
    print("2 - Adicionar no Fim")
    print("3 - Remover do Início")
    print("4 - Remover do Fim")
    print("5 - Imprimir")
    print("6 - Imprimir Inverso")
    print("0 - Sair")

    opcao = input("Digite sua opção:")

    if opcao == "1":
        dado = input("Informe um valor: ")
        lista.adicionarInicio( dado )

    if opcao == "2":
        dado = input("Informe um valor: ")
        lista.adicionarFim( dado )

    if opcao == "3":
        lista.excluirInicio()

    if opcao == "4":
        lista.excluirFim()

    if opcao == "5":
        lista.imprimir()

    if opcao == "6":
        lista.imprimirReverso()

