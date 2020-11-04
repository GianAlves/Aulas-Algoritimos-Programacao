arquivo = open("arq01.txt", "x")
if arquivo == None :
    print( "Arquivo ja existe" )
else:
    arquivo.write("Índios")
    arquivo.close()
    
    arquivo = open( "arq01.txt")
    print( arquivo.read() )