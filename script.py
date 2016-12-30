if __name__ == "__main__":
   
    import sys    
    import os
    import shutil
    
    print (sys.argv[1])

    chaveAbertos = 0
    aspasAbertas = 0
    novasPastas = []
    novosArquivos = []
    arquivosValores = []
    buffer = ""
    tipo = ""
    variavel = ""
    valor = ""
    moverPasta = 0

    f = open(sys.argv[1], 'r')
    endereco = f.readline()
    endereco = endereco.split("\n")[0]
    os.chdir(endereco)

    texto = f.read()
    texto = texto.replace("\n", "")
    texto = texto.replace("\t", "")
    texto = texto.replace(" ", "")
    f.close()

    for letra in texto:
        if letra == ":":
            variavel = buffer
            buffer = ""
        elif letra == ",":
            buffer = buffer
        elif letra == "{":
            tipo = "pasta"
            moverPasta = +1
            chaveAbertos += 1
            os.system('mkdir '+variavel)
            os.chdir(variavel)
            
        elif letra == "}":
            moverPasta = -1
            chaveAbertos -= 1       
        elif letra == '"':
            if(aspasAbertas == 0):
                tipo = "arquivo"
                f = open(variavel, 'w')
                aspasAbertas =1                
            elif aspasAbertas == 1:
                aspasAbertas =0
                valor = buffer
                f.write(valor)
                f.close()               
                buffer = ""
        elif letra != ":":
            buffer += letra

        if moverPasta == -1:
            os.chdir(os.getcwd()+"/..")
            print(os.getcwd())
            moverPasta = 0

        
            
            

        

    if chaveAbertos == 0:
        print ("válido")
    else:
        print("inválido")
    
    
    

