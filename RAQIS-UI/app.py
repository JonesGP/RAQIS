#:kivy 2.2.1
import kivy
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder
from kivy.core.window import Window
from pathlib import Path
Window.size = (1200, 720)
Window.minimum_width = 1200
Window.minimum_height = 640

kv_string = '''
#:kivy 2.2.1
BoxLayout:
    orientation: 'horizontal'
    canvas.before:
        Color:
            rgba: 0.17, 0.02, 0.02, 1
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'horizontal'
    size_hint: 1, 1
    padding: 20
    BoxLayout:
        orientation: 'vertical'
        id: 'menu1'
        size_hint: 0.1, 1
        spacing: 10
        padding: 10
        canvas.before:
            Color: 
                rgba: 0.25, 0.08, 0.08, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            id: 'titulo'
            text: 'Menu'
            font_size: 20
            size_hint: 1, 0.05
        BoxLayout:
            id: submenu
            orientation: 'vertical'
            size_hint: 1, 0.75
            BoxLayout:
                id: idsubmenuone
                orientation: 'vertical'
                size_hint: 1, 0.8
                spacing: 10
                Label:
                    text: 'Digite quantos caracteres deseja tirar ou clique em numerar arquivos para numerar os arquivos:'
                    text_size: self.size
                    size_hint: 1, 0.4
                    halign: 'left'
                TextInput:
                    id: idquantidade
                    size_hint: 1, 0.08
                    hint_text: 'Quantidade...'
                Button:
                    id: idtir_first_car
                    text: 'Tirar pri. carac.'
                    size_hint: 1, 0.1
                    background_color: 0.16, 0.52, 0.52, 1
                    on_release: app.tirar_first_char(char = idquantidade.text, dire = dir_input.text)
                Button:
                    id: idtir_last_car
                    text: 'Tirar ult. carac.'
                    size_hint: 1, 0.1
                    background_color: 0.16, 0.52, 0.52, 1
                    opacity: 1
                    on_release: app.remove_last_char(char_end = idquantidade.text, dire = dir_input.text)
                Button:
                    id: idnum_arq
                    text: 'Num. arq.'
                    size_hint: 1, 0.1
                    background_color: 0.16, 0.52, 0.52, 1
                    opacity: 1
                    on_release: app.numerar_arquivos(dir_input.text)
            Label:
                id: 'vazio'
                size_hint: 1, 0.4
        Button:
            id: testebtn
            text: 'Sair'
            size_hint: 1, 0.1
            on_release: app.exit_app()
            background_color: 0.16, 0.52, 0.52, 1
            opacity: 1
        Label:
            id: idversion
            text: 'V0.0.1 JonesGP'
            font_size: 15
            size_hint: 1, 0.02
    BoxLayout:
        orientation: 'vertical'
        id: 'conteudo'
        size_hint: 0.8, 1
        padding: 10
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.05
            spacing: 10
            #quero um input text
            TextInput:
                id: dir_input
                #quero adicionar um placeholder
                hint_text: 'Digite o diretório...'
                size_hint: 0.9, 1
                spacing: [0, 0, 10, 0]
            Button:
                text: 'Verificar'
                size_hint: 0.1, 1
                on_release: app.verificar_arq(dir_input.text)
                background_color: 0.16, 0.52, 0.52, 1
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.05
            Label:
                id: pasta
                size_hint: 1, 0.5
                text: f'A pasta:'
                pos: -500, 0
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.9
            ScrollView:
                Label:
                    id: conteudo_pasta
                    multi_line: True
                    text: 'Arquivos'
                    font_size: 20
                    size_hint: None, None
                    height: self.texture_size[1]
                    width: self.texture_size[0]
            Label:
                id: 'vazio'
                size_hint: 0.5, 1
'''

#base rgb para colocar no paletton 201010
#base rgb para colocar no paletton 6B2F2F claras
# C:\Users\Jon3s\Desktop\Novos Projetos\Nova pasta    pasta para testa todos os arquivos

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

        return Builder.load_string(kv_string) # Retornando a boxlayout
if __name__ == '__main__': #__main__ é uma variavel especial que é definida como __main__ quando voce executa o arquivo diretamente
    Meu_app().run()
    