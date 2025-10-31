from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.image import Image 
from kivy.core.window import Window 
import webbrowser 
import subprocess 
 
class MasterApp(App): 
    def build(self): 
        self.title = "Stolyarnaya Masterskaya Rasseya" 
        Window.size = (400, 600) 
        Window.clearcolor = (0.9, 0.8, 0.7, 1) 
 
        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30) 
 
        # Фон (пока заглушка) 
        background = Image(source='', allow_stretch=True, keep_ratio=False) 
        main_layout.add_widget(background) 
 
        # Кнопка телефона - ДЛЯ ЗВОНКА 
        phone_btn = Button(text='?? ПОЗВОНИТЬ +7(918)307-76-22', size_hint=(1, 0.12), background_color=(0.2, 0.7, 0.3, 1), color=(1, 1, 1, 1), font_size='16sp') 
        phone_btn.bind(on_press=self.make_call) 
        main_layout.add_widget(phone_btn) 
 
        # Кнопка email 
        email_btn = Button(text='?? НАПИСАТЬ ras@sea123.ru', size_hint=(1, 0.12), background_color=(0.2, 0.5, 0.8, 1), color=(1, 1, 1, 1), font_size='16sp') 
        email_btn.bind(on_press=self.send_email) 
        main_layout.add_widget(email_btn) 
 
        # Кнопка сайта 
        website_btn = Button(text='?? НАШ САЙТ', size_hint=(1, 0.12), background_color=(0.8, 0.5, 0.2, 1), color=(1, 1, 1, 1), font_size='16sp') 
        website_btn.bind(on_press=self.open_website) 
        main_layout.add_widget(website_btn) 
 
        return main_layout 
 
    def make_call(self, instance): 
        # Открывает приложение для звонка 
        subprocess.call(['start', 'tel:+79183077622'], shell=True) 
 
    def send_email(self, instance): 
        # Открывает почту 
        webbrowser.open('mailto:ras@sea123.ru?subject=Заказ%20мебели') 
 
    def open_website(self, instance): 
        # Открывает сайт (ЗАМЕНИТЕ НА ВАШ САЙТ) 
        webbrowser.open('https://ваш-сайт-мастерской.ru') 
 
if __name__ == '__main__': 
    MasterApp().run() 
