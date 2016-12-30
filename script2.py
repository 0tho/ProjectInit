def url(path):
    print(path[0:4])
    if path[0:4] == "http":
        return 1
    else:    
        return 0

if __name__ == "__main__":
   
    import sys    
    import os
    import urllib.request
    import shutil

    print (sys.argv[1])

	
    chavesAbertas = 0
    colchetesAbertos = 0
    aspasAbertas = 0
    novasPastas = []
    novosArquivos = []
    arquivosValores = []
    buffer = ""
    tipo = ""
    variavel = ""
    valor = ""
    moverPasta = 0
    dataInFile = 0    
    referencia = 0  

    variaveis = []
	
    f = open(sys.argv[1], 'r')
    endereco = f.readline()
    endereco = endereco.split("\n")[0]
    os.chdir(endereco)

    texto = f.read()
    f.close()

	
    for letra in texto:
        if dataInFile:
            if letra == '"':
                dataInFile = 0
        else:
            if letra == '[':
                colchetesAbertos+=1
            elif letra == ']':
                colchetesAbertos-=1
            elif letra == '{':
                chavesAbertas+=1
            elif letra == '}':
                chavesAbertas-=1
            elif letra == '"':
                dataInFile = 1
	
    if colchetesAbertos != 0 or chavesAbertas != 0 or dataInFile:
        print("Invalido")
    else:
        print("valido")
        for letra in texto:
            if referencia == 1:
                if letra == ']':
                    valor = buffer
                    if(url(valor)):
                        urllib.request.urlretrieve(valor, (os.getcwd()+"\\"+variavel))
                    else:
                        valor = valor.replace("/", "\\")
                        os.system ("copy %s %s" % (valor, (os.getcwd()+"\\"+variavel)))                        
                    buffer = ""
                    referencia = 0
                else:
                    buffer += letra
            elif aspasAbertas == 0:            
                if letra == '"':
                    f = open(variavel, 'w')
                    aspasAbertas = 1                   
                elif letra == ":":
                    variavel = buffer
                    variavel = variavel.replace("\n", "")
                    variavel = variavel.replace("\t", "")
                    variavel = variavel.replace(" ", "")
                    buffer = ""
                elif letra == ",":
                    buffer = buffer
                elif letra == "{":                
                    moverPasta = +1                
                    os.system('mkdir '+variavel)
                    os.chdir(variavel)                
                elif letra == "}":
                    moverPasta = -1 
                elif letra == "[":
                    buffer = ""
                    referencia = 1
                elif letra != "\n" or letra!=" " or letra !="\t":
                    buffer += letra                    
                if moverPasta == -1:
                    os.chdir(os.getcwd()+"/..")
                    print(os.getcwd())
                    moverPasta = 0
            elif letra == '"':                
                aspasAbertas =0
                valor = buffer
                f.write(valor)
                f.close()               
                buffer = ""
            else:
                buffer += letra

