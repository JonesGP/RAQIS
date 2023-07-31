#:kivy 2.2.1
import kivy
import sys
import scripts
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
from pathlib import Path
from kivy.properties import StringProperty
Builder.load_file('ui.kv')

Window.size = (1280, 720)

#base rgb para colocar no paletton 201010
class layout_principal(BoxLayout):
    pass

class Meu_app(App): # O App é uma classe do Kivy, nessa linha estamos criando uma classe que herda da classe App do kivy
    folder_name = StringProperty("ava")
    def verificar_arq(self, text):
        aplicativo = App.get_running_app()
        
        folder = Path(text)
        folder_name = folder.name
        aplicativo.root.ids.pasta.text = f'A pasta é: {folder_name}'
        tupla_arq = []
        for arquivo in folder.iterdir():
            tupla_arq.append(arquivo.name)
        formated_tupla_arq = "\n".join(tupla_arq)
        aplicativo.root.ids.conteudo_pasta.text = str(formated_tupla_arq)
        print(str(tupla_arq))
    def menu_two(self):
        aplicativo = App.get_running_app()
        aplicativo.root.ids.testebtn.opacity = 1
        
    def build(self):
        return layout_principal() # Retornando a boxlayout
if __name__ == '__main__': #__main__ é uma variavel especial que é definida como __main__ quando voce executa o arquivo diretamente
    Meu_app().run()
    