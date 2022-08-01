from kivy.app import App
from kivy.uix.label import Label   #import label
from kivy.uix.button import Button  #import button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class firstApp(App):
    def build(self):
    
        duzen = GridLayout(cols=2)

        duzen.add_widget(Label(text='Kullanıcı Adı:'))
        kullanici_adi = TextInput()
        duzen.add_widget(kullanici_adi)

        duzen.add_widget(Label(text='Parola:'))
        parola = TextInput()
        duzen.add_widget(parola)

        duzen.add_widget(Widget())

        gir_dugme=Button(text='Gir')
        duzen.add_widget(gir_dugme)
        
        self.title = "Giriş Formu"  

        return duzen

firstApp().run()
