# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class MasterApp(App):
    def build(self):
        self.title = "Столярная мастерская 'Рассея'"
        Window.clearcolor = (0.98, 0.95, 0.90, 1)
        main_layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        title_label = Label(text='Столярная мастерская "Рассея"', font_size='28sp', color=(0.36, 0.25, 0.20, 1), bold=True)
        contacts_label = Label(text='Телефон: +7(918)307-76-22\n\nEmail: ras@sea123.ru', font_size='18sp')
        action_btn = Button(text='Заказать консультацию', size_hint=(1, 0.15), background_color=(0.55, 0.27, 0.07, 1), color=(1, 1, 1, 1))
        main_layout.add_widget(title_label)
        main_layout.add_widget(contacts_label)
        main_layout.add_widget(action_btn)
        return main_layout

if __name__ == '__main__':
    MasterApp().run()