from pathlib import Path #para trabalhar com arquivos e diretórios

def remove_first_char():
    folder = Path(text_input)
    for arquivo in folder.iterdir():
        novo_nome = arquivo.name[char:]
        novo_caminho = arquivo.with_name(novo_nome)
        arquivo.rename(novo_caminho)
    
def remove_last_char():
    for arquivo in folder.iterdir():
        old_name, extension = arquivo.stem, arquivo.suffix
        novo_nome = old_name[:(len(old_name) - char_end)] + extension
        novo_caminho = arquivo.with_name(novo_nome)
        try:
            arquivo.rename(novo_caminho)
        except Exception as error:
            print(f"Não foi possivel remover os caracteres de: {arquivo.name}")
            print(f"Ocorreu um erro: {str(error)}")
        print("saiu do try exception")
        
def numerar_arquivos():
    num = 1
    for arquivo in folder.iterdir():
        novo_nome = str(num).zfill(2) + " - " + arquivo.name #.zfill(2) serve para colocar 2 digitos zeros se o arquivo tiver menos de 2 caracteres
        novo_caminho = arquivo.with_name(novo_nome)
        try:
            arquivo.rename(novo_caminho)
        except Exception as error:
            print(f"Ocorreu um erro: {str(error)}")
            print("Não foi possivel numerar o arquivo: " + arquivo.name) 
            continue   
        num += 1

#while True:
    #folder_dir = input("Digite o diretorio do usuario que deseja manipular: ")
    #folder = Path(folder_dir)
    #print("-" * 30)
    #print("pasta: ", folder.name)
    #for arquivo in folder.iterdir():
    #    print(arquivo.name)
    #print("-" * 30)
    #op_conf = input("São esses os arquivos que deseja renomear? sim/nao\n")
    #if op_conf == "sim":
    #    op = int(input("================\n1 - Tirar os primeiros caracteres \n2 - Tirar os ultimos caracteres \n3 - Numerar os arquivos \n0 - Sair\n===============\n"))
    #    print("-" * 30)
    #    if op == 1:
    #        char = int(input("Digite quantos caracteres deseja tirar do começo para o fim lembrando que espaços sao caracteres: "))
    #        print("-" * 30)
    #        remove_first_char()
    #        print("-" * 30)
    #        print("Pronto!, os primeiros {char} caracteres foram removidos!".format(char=char))
    #    if op == 2:
    #        char_end = int(input("Digite quantos caracteres deseja tirar do fim para o comeco lembrando que espaços sao caracteres: "))
    #        char = 0
    #        remove_last_char()
    #    if op == 3:
    #        try:
    #            numerar_arquivos()
    #            print("Arquivos numerados com sucesso!")
    #        except Exception as error:
    #            print(f"Ocorreu um erro: {str(error)}")
    #            print("Não foi possivel numerar os arquivos!")
    #        print("-" * 30)
    #    if op == 0:
    #        break
#        
#        
#print("-" * 30)
#end = input('adeus!!')