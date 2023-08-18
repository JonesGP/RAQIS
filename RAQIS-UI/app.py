#:kivy 2.2.1
import kivy
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder
from kivy.core.window import Window
from pathlib import Path
Builder.load_file('ui.kv')
Window.size = (1200, 720)
Window.minimum_width = 1200
Window.minimum_height = 640
                
#base rgb para colocar no paletton 201010
#base rgb para colocar no paletton 6B2F2F claras
# C:\Users\Jon3s\Desktop\Novos Projetos\Nova pasta    pasta para testa todos os arquivos
class layoutprincipal(BoxLayout):
    pass

class Meu_app(App): # O App é uma classe do Kivy, nessa linha estamos criando uma classe que herda da classe App do kivy
    def __init__(self, **kwargs):
        super(Meu_app, self).__init__(**kwargs)
        self.textdir = ''
        
    def verificar_options(self, optio):
        if optio.isnumeric():
            print(f"O valor digitado foi: {optio}")
            pass
        else:
            print(f"O valor digitado foi: nada")
        
    def verificar_arq(self, text):
        ap = App.get_running_app()
        folder = Path(text)
        folder_name = folder.name
        ap.root.ids.pasta.text = f'A pasta é: {folder_name}'
        tupla_arq = []
        for arquivo in folder.iterdir():
            tupla_arq.append(arquivo.name)
        formated_tupla_arq = "\n".join(tupla_arq)
        ap.root.ids.conteudo_pasta.text = str(formated_tupla_arq)
    
    def tirar_first_char(self, char, dire):
        textdir = self.root.ids.dir_input.text
        folder = Path(dire)
        text = self.textdir
        if char.isnumeric():
            try:
                for arquivo in folder.iterdir():
                    novo_nome = arquivo.name[int(char):]
                    novo_caminho = arquivo.with_name(novo_nome)
                    arquivo.rename(novo_caminho)
            except Exception as error:
                self.verificar_options(char, error)
        else:
            print(f"O valor digitado não é um numero inteiro")
        print(textdir)
        self.verificar_arq(text = textdir)
    
    def remove_last_char(self, dire, char_end):
        textdir = self.root.ids.dir_input.text
        folder = Path(dire)
        if char_end.isnumeric():
            try:
                for arquivo in folder.iterdir():
                    old_name, extension = arquivo.stem, arquivo.suffix
                    novo_nome = old_name[:(len(old_name) - int(char_end))] + extension
                    novo_caminho = arquivo.with_name(novo_nome)
                    try:
                        arquivo.rename(novo_caminho)
                    except Exception as error:
                        print(f"Não foi possivel remover os caracteres de: {arquivo.name}")
                        print(f"Ocorreu um erro: {str(error)}")
            except Exception as error:
                print("Ocorreu um erro: " + str(error))
        self.verificar_arq(text = textdir)
        
    def numerar_arquivos(self, dire):
        textdir = self.root.ids.dir_input.text
        folder = Path(dire)
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
        self.verificar_arq(text = textdir)
    
    #função para fechar o aplicativo
    def exit_app(self):
        sys.exit()
        
    def build(self):
        self.title = "RAQIS - Renomeador de Arquivos - Developer by JonesGP Studio"

        return layoutprincipal() # Retornando a boxlayout
if __name__ == '__main__': #__main__ é uma variavel especial que é definida como __main__ quando voce executa o arquivo diretamente
    Meu_app().run()
    