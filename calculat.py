#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Графический калькулятор в стиле киберпанк с интерфейсом на tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

class CyberpunkCalculator:
    """Класс графического калькулятора в стиле киберпанк"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CYBER CALCULATOR v2.0")
        self.root.geometry("450x750")
        self.root.resizable(False, False)
        
        # Киберпанк цветовая схема
        self.colors = {
            'bg_main': '#0a0a0a',           # Основной фон - глубокий черный
            'bg_secondary': '#1a1a1a',      # Вторичный фон - темно-серый
            'bg_display': '#000000',        # Фон дисплея - черный
            'neon_cyan': '#00ffff',         # Неоновый голубой
            'neon_pink': '#ff00ff',         # Неоновый розовый
            'neon_green': '#00ff00',        # Неоновый зеленый
            'neon_orange': '#ff8800',       # Неоновый оранжевый
            'neon_purple': '#8800ff',       # Неоновый фиолетовый
            'text_primary': '#ffffff',      # Основной текст - белый
            'text_secondary': '#cccccc',    # Вторичный текст - серый
            'border': '#333333',            # Границы
            'danger': '#ff0040',            # Опасность - красный
            'warning': '#ffff00'            # Предупреждение - желтый
        }
        
        # Настройка окна
        self.root.configure(bg=self.colors['bg_main'])
        
        # Переменные для хранения данных
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.operation_display_var = tk.StringVar()  # Для отображения операций
        self.operation_display_var.set("")
        self.first_number = 0
        self.operation = ""
        self.new_number = True
        self.operation_history = []  # История операций
        
        self.setup_ui()
        
    def setup_ui(self):
        """Настройка пользовательского интерфейса в стиле киберпанк"""
        # Настройка стилей
        self.setup_styles()
        
        # Заголовок
        title_frame = tk.Frame(self.root, bg=self.colors['bg_main'], height=50)
        title_frame.pack(fill=tk.X, pady=(10, 0))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="◢◤ CYBER CALC ◢◤", 
                             font=('Courier New', 16, 'bold'),
                             fg=self.colors['neon_cyan'],
                             bg=self.colors['bg_main'])
        title_label.pack(pady=10)
        
        # Дисплей операций (вторичный дисплей)
        operation_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        operation_frame.pack(fill=tk.X, padx=15, pady=(10, 5))
        
        # Рамка для дисплея операций
        operation_border = tk.Frame(operation_frame, bg=self.colors['neon_purple'], height=1)
        operation_border.pack(fill=tk.X, pady=(0, 1))
        
        self.operation_display = tk.Entry(operation_frame, textvariable=self.operation_display_var, 
                                        font=('Courier New', 12, 'bold'),
                                        fg=self.colors['neon_purple'],
                                        bg=self.colors['bg_display'],
                                        bd=0,
                                        highlightthickness=1,
                                        highlightcolor=self.colors['neon_purple'],
                                        highlightbackground=self.colors['border'],
                                        justify='right',
                                        state='readonly')
        self.operation_display.pack(fill=tk.X, ipady=8)
        
        # Нижняя рамка дисплея операций
        operation_border_bottom = tk.Frame(operation_frame, bg=self.colors['neon_purple'], height=1)
        operation_border_bottom.pack(fill=tk.X, pady=(1, 0))
        
        # Основной дисплей
        display_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        display_frame.pack(fill=tk.X, padx=15, pady=(5, 10))
        
        # Рамка для дисплея с неоновым эффектом
        display_border = tk.Frame(display_frame, bg=self.colors['neon_cyan'], height=2)
        display_border.pack(fill=tk.X, pady=(0, 2))
        
        self.display = tk.Entry(display_frame, textvariable=self.display_var, 
                               font=('Courier New', 24, 'bold'),
                               fg=self.colors['neon_green'],
                               bg=self.colors['bg_display'],
                               bd=0,
                               highlightthickness=2,
                               highlightcolor=self.colors['neon_cyan'],
                               highlightbackground=self.colors['border'],
                               justify='right',
                               state='readonly',
                               insertbackground=self.colors['neon_cyan'])
        self.display.pack(fill=tk.X, ipady=15)
        
        # Нижняя рамка дисплея
        display_border_bottom = tk.Frame(display_frame, bg=self.colors['neon_cyan'], height=2)
        display_border_bottom.pack(fill=tk.X, pady=(2, 0))
        
        # Основной фрейм для кнопок
        main_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Кнопки очистки
        clear_frame = tk.Frame(main_frame, bg=self.colors['bg_main'])
        clear_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.create_cyber_button(clear_frame, "CLEAR", self.clear, 
                                self.colors['danger'], side=tk.LEFT, expand=True, padx=10)
        self.create_cyber_button(clear_frame, "CE", self.clear_entry, 
                                self.colors['warning'], side=tk.LEFT, expand=True)
        
        # Специальные операции
        special_frame = tk.Frame(main_frame, bg=self.colors['bg_main'])
        special_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.create_cyber_button(special_frame, "√", self.sqrt, 
                                self.colors['neon_purple'], side=tk.LEFT, expand=True, padx=5)
        self.create_cyber_button(special_frame, "x²", self.square, 
                                self.colors['neon_purple'], side=tk.LEFT, expand=True, padx=5)
        self.create_cyber_button(special_frame, "1/x", self.reciprocal, 
                                self.colors['neon_purple'], side=tk.LEFT, expand=True, padx=5)
        
        # Основные кнопки
        buttons_frame = tk.Frame(main_frame, bg=self.colors['bg_main'])
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Создаем grid для кнопок
        self.create_button_grid(buttons_frame)
        
    def create_cyber_button(self, parent, text, command, color, side=None, expand=False, padx=0, pady=0):
        """Создание кнопки в стиле киберпанк"""
        button = tk.Button(parent, text=text, command=command,
                          font=('Courier New', 12, 'bold'),
                          fg=color,
                          bg=self.colors['bg_secondary'],
                          activeforeground=self.colors['bg_main'],
                          activebackground=color,
                          bd=0,
                          highlightthickness=2,
                          highlightcolor=color,
                          highlightbackground=self.colors['border'],
                          relief='flat',
                          cursor='hand2')
        
        if side:
            button.pack(side=side, fill=tk.X, expand=expand, padx=padx, pady=pady, ipady=8)
        else:
            return button
    
    def create_button_grid(self, parent):
        """Создание сетки кнопок"""
        # Создаем grid контейнер
        grid_frame = tk.Frame(parent, bg=self.colors['bg_main'])
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Настройка весов для grid
        for i in range(4):
            grid_frame.columnconfigure(i, weight=1)
        for i in range(6):
            grid_frame.rowconfigure(i, weight=1)
        
        # Определяем кнопки и их цвета
        button_layout = [
            [('7', 'num'), ('8', 'num'), ('9', 'num'), ('/', 'op')],
            [('4', 'num'), ('5', 'num'), ('6', 'num'), ('*', 'op')],
            [('1', 'num'), ('2', 'num'), ('3', 'num'), ('-', 'op')],
            [('±', 'special'), ('0', 'num'), ('.', 'num'), ('+', 'op')],
            [('%', 'special'), ('=', 'equal'), ('^', 'op'), ('', '')],
        ]
        
        # Цвета для разных типов кнопок
        button_colors = {
            'num': self.colors['neon_cyan'],
            'op': self.colors['neon_orange'],
            'equal': self.colors['neon_green'],
            'special': self.colors['neon_pink']
        }
        
        # Создаем кнопки
        for row_idx, row in enumerate(button_layout):
            for col_idx, (text, btn_type) in enumerate(row):
                if text == '':
                    continue
                
                # Определяем команду
                if btn_type == 'num':
                    cmd = lambda t=text: self.number_click(t)
                elif btn_type == 'op':
                    cmd = lambda t=text: self.operation_click(t)
                elif btn_type == 'equal':
                    cmd = self.calculate
                elif btn_type == 'special':
                    if text == '±':
                        cmd = self.plus_minus
                    elif text == '%':
                        cmd = self.percentage
                    else:
                        cmd = lambda t=text: self.operation_click(t)
                
                # Создаем кнопку
                color = button_colors[btn_type]
                button = tk.Button(grid_frame, text=text, command=cmd,
                                 font=('Courier New', 14, 'bold'),
                                 fg=color,
                                 bg=self.colors['bg_secondary'],
                                 activeforeground=self.colors['bg_main'],
                                 activebackground=color,
                                 bd=0,
                                 highlightthickness=2,
                                 highlightcolor=color,
                                 highlightbackground=self.colors['border'],
                                 relief='flat',
                                 cursor='hand2')
                
                button.grid(row=row_idx, column=col_idx, sticky='nsew', 
                           padx=3, pady=3, ipady=12)
                
                # Добавляем эффект наведения
                self.add_hover_effect(button, color)
    
    def add_hover_effect(self, button, color):
        """Добавление эффекта наведения для кнопок"""
        def on_enter(event):
            button.configure(bg=color, fg=self.colors['bg_main'])
        
        def on_leave(event):
            button.configure(bg=self.colors['bg_secondary'], fg=color)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    
    def setup_styles(self):
        """Настройка стилей"""
        # Настройка стилей для ttk (если используется)
        style = ttk.Style()
        style.theme_use('clam')
        
        # Настройка цветов для различных элементов
        style.configure('Cyber.TFrame', background=self.colors['bg_main'])
    
    def update_operation_display(self, text=""):
        """Обновление дисплея операций"""
        if text:
            self.operation_display_var.set(text)
        else:
            # Показываем текущую операцию
            if self.operation and hasattr(self, 'first_number'):
                op_symbols = {'+': '+', '-': '-', '*': '×', '/': '÷', '^': '^'}
                symbol = op_symbols.get(self.operation, self.operation)
                display_text = f"{self.first_number} {symbol} "
                self.operation_display_var.set(display_text)
            else:
                self.operation_display_var.set("")
    
    def add_to_history(self, operation):
        """Добавление операции в историю"""
        self.operation_history.append(operation)
        # Ограничиваем историю последними 5 операциями
        if len(self.operation_history) > 5:
            self.operation_history.pop(0)
    
    def number_click(self, number):
        """Обработка нажатия цифры"""
        if self.new_number:
            self.display_var.set(number)
            self.new_number = False
        else:
            current = self.display_var.get()
            if current == "0":
                self.display_var.set(number)
            else:
                self.display_var.set(current + number)
        
        # Обновляем дисплей операций, если есть текущая операция
        if self.operation:
            self.update_operation_display()
    
    def operation_click(self, op):
        """Обработка нажатия операции"""
        try:
            if self.operation and not self.new_number:
                self.calculate()
            
            self.first_number = float(self.display_var.get())
            self.operation = op
            self.new_number = True
            
            # Обновляем дисплей операций
            self.update_operation_display()
            
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def calculate(self):
        """Выполнение вычислений"""
        try:
            if not self.operation:
                return
            
            second_number = float(self.display_var.get())
            result = 0
            
            # Создаем строку операции для истории
            op_symbols = {'+': '+', '-': '-', '*': '×', '/': '÷', '^': '^'}
            symbol = op_symbols.get(self.operation, self.operation)
            operation_string = f"{self.first_number} {symbol} {second_number} = "
            
            if self.operation == '+':
                result = self.first_number + second_number
            elif self.operation == '-':
                result = self.first_number - second_number
            elif self.operation == '*':
                result = self.first_number * second_number
            elif self.operation == '/':
                if second_number == 0:
                    self.show_error("Деление на ноль невозможно!")
                    return
                result = self.first_number / second_number
            elif self.operation == '^':
                result = self.first_number ** second_number
            
            # Форматирование результата
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))
            
            # Обновляем дисплеи
            self.display_var.set(result_str)
            self.update_operation_display(operation_string + result_str)
            
            # Добавляем в историю
            self.add_to_history(operation_string + result_str)
            
            self.operation = ""
            self.new_number = True
            
        except ValueError:
            self.show_error("Неверный формат числа!")
        except Exception as e:
            self.show_error(f"Ошибка вычисления: {str(e)}")
    
    def sqrt(self):
        """Квадратный корень"""
        try:
            number = float(self.display_var.get())
            if number < 0:
                self.show_error("Квадратный корень из отрицательного числа!")
                return
            
            result = math.sqrt(number)
            operation_string = f"√{number} = "
            
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))
            
            self.display_var.set(result_str)
            self.update_operation_display(operation_string + result_str)
            self.add_to_history(operation_string + result_str)
            
            self.new_number = True
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def square(self):
        """Возведение в квадрат"""
        try:
            number = float(self.display_var.get())
            result = number ** 2
            operation_string = f"{number}² = "
            
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))
            
            self.display_var.set(result_str)
            self.update_operation_display(operation_string + result_str)
            self.add_to_history(operation_string + result_str)
            
            self.new_number = True
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def reciprocal(self):
        """Обратное значение (1/x)"""
        try:
            number = float(self.display_var.get())
            if number == 0:
                self.show_error("Деление на ноль!")
                return
            
            result = 1 / number
            operation_string = f"1/{number} = "
            
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))
            
            self.display_var.set(result_str)
            self.update_operation_display(operation_string + result_str)
            self.add_to_history(operation_string + result_str)
            
            self.new_number = True
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def plus_minus(self):
        """Изменение знака"""
        try:
            number = float(self.display_var.get())
            result = -number
            
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
                
            # Обновляем дисплей операций если есть текущая операция
            if self.operation:
                self.update_operation_display()
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def percentage(self):
        """Процент"""
        try:
            number = float(self.display_var.get())
            result = number / 100
            operation_string = f"{number}% = "
            
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))
            
            self.display_var.set(result_str)
            self.update_operation_display(operation_string + result_str)
            self.add_to_history(operation_string + result_str)
            
            self.new_number = True
        except ValueError:
            self.show_error("Неверный формат числа!")
    
    def clear(self):
        """Полная очистка"""
        self.display_var.set("0")
        self.operation_display_var.set("")
        self.first_number = 0
        self.operation = ""
        self.new_number = True
        self.operation_history = []
    
    def clear_entry(self):
        """Очистка текущего ввода"""
        self.display_var.set("0")
        self.new_number = True
        # Обновляем дисплей операций если есть текущая операция
        if self.operation:
            self.update_operation_display()
    
    def show_error(self, message):
        """Показать ошибку в киберпанк стиле"""
        # Создаем кастомное окно ошибки
        error_window = tk.Toplevel(self.root)
        error_window.title(">>> SYSTEM ERROR <<<")
        error_window.geometry("400x200")
        error_window.configure(bg=self.colors['bg_main'])
        error_window.resizable(False, False)
        
        # Центрируем окно
        error_window.transient(self.root)
        error_window.grab_set()
        
        # Заголовок ошибки
        header = tk.Label(error_window, text="◢◤ ERROR ◢◤",
                         font=('Courier New', 16, 'bold'),
                         fg=self.colors['danger'],
                         bg=self.colors['bg_main'])
        header.pack(pady=20)
        
        # Сообщение об ошибке
        msg_label = tk.Label(error_window, text=message,
                           font=('Courier New', 12),
                           fg=self.colors['text_primary'],
                           bg=self.colors['bg_main'],
                           wraplength=350)
        msg_label.pack(pady=10)
        
        # Кнопка OK
        ok_button = tk.Button(error_window, text="OK",
                            command=error_window.destroy,
                            font=('Courier New', 12, 'bold'),
                            fg=self.colors['neon_green'],
                            bg=self.colors['bg_secondary'],
                            activeforeground=self.colors['bg_main'],
                            activebackground=self.colors['neon_green'],
                            bd=0,
                            highlightthickness=2,
                            highlightcolor=self.colors['neon_green'],
                            relief='flat',
                            cursor='hand2')
        ok_button.pack(pady=20, ipadx=20, ipady=5)
        
        # Центрируем окно относительно родительского
        error_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (400 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (200 // 2)
        error_window.geometry(f"400x200+{x}+{y}")
    
    def run(self):
        """Запуск калькулятора"""
        # Центрирование окна
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.root.winfo_screenheight() // 2) - (750 // 2) # Adjusted height
        self.root.geometry(f"450x750+{x}+{y}")
        
        # Привязка клавиатуры
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<KP_Enter>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        
        # Добавляем привязки для цифр
        for i in range(10):
            self.root.bind(str(i), lambda e, num=str(i): self.number_click(num))
        
        # Привязки для операций
        self.root.bind('+', lambda e: self.operation_click('+'))
        self.root.bind('-', lambda e: self.operation_click('-'))
        self.root.bind('*', lambda e: self.operation_click('*'))
        self.root.bind('/', lambda e: self.operation_click('/'))
        self.root.bind('.', lambda e: self.number_click('.'))
        
        # Фокус на окно для работы с клавиатурой
        self.root.focus_set()
        
        # Запуск главного цикла
        self.root.mainloop()

def main():
    """Основная функция программы"""
    print(">>> Запуск киберпанк калькулятора...")
    calc = CyberpunkCalculator()
    calc.run()

if __name__ == "__main__":
    main() 