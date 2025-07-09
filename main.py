#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Графический калькулятор с интерфейсом на tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

class GraphicalCalculator:
    """Класс графического калькулятора"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Переменные для хранения данных
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.first_number = 0
        self.operation = ""
        self.new_number = True
        
        self.setup_ui()
        
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # Стиль
        style = ttk.Style()
        style.theme_use('clam')
        
        # Дисплей
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(fill=tk.X)
        
        display = ttk.Entry(display_frame, textvariable=self.display_var, 
                          font=('Arial', 20), state='readonly', justify='right')
        display.pack(fill=tk.X, pady=(0, 10))
        
        # Основной фрейм для кнопок
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Кнопки очистки
        clear_frame = ttk.Frame(main_frame)
        clear_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(clear_frame, text="C", command=self.clear,
                  style='Clear.TButton').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(clear_frame, text="CE", command=self.clear_entry,
                  style='Clear.TButton').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Специальные операции
        special_frame = ttk.Frame(main_frame)
        special_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(special_frame, text="√", command=self.sqrt,
                  style='Special.TButton').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(special_frame, text="x²", command=self.square,
                  style='Special.TButton').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        ttk.Button(special_frame, text="1/x", command=self.reciprocal,
                  style='Special.TButton').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Основные кнопки
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Создаем grid для кнопок
        button_grid = ttk.Frame(buttons_frame)
        button_grid.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Настраиваем веса колонок и строк для равномерного распределения
        for i in range(4):
            button_grid.columnconfigure(i, weight=1)
        for i in range(6):
            button_grid.rowconfigure(i, weight=1)
        
        # Перепланируем расположение кнопок для лучшего разделения
        # Левая часть - цифры и основные кнопки
        number_buttons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['±', '0', '.'],
            ['%', '=', '^'],
            ['', '', '']
        ]
        
        # Правая колонка - операции (отдельно + и -)
        operation_buttons = ['/', '*', '-', '+', '', '']
        
        # Создаем кнопки с правильным выравниванием
        # Сначала создаем цифры и основные кнопки (левая часть)
        for i, row in enumerate(number_buttons):
            for j, text in enumerate(row):
                if text == '':
                    continue
                    
                if text.isdigit() or text == '.':
                    cmd = lambda t=text: self.number_click(t)
                    style = 'Number.TButton'
                elif text == '=':
                    cmd = self.calculate
                    style = 'Equal.TButton'
                elif text == '±':
                    cmd = self.plus_minus
                    style = 'Special.TButton'
                elif text == '%':
                    cmd = self.percentage
                    style = 'Special.TButton'
                elif text == '^':
                    cmd = lambda t=text: self.operation_click(t)
                    style = 'Operation.TButton'
                else:
                    cmd = lambda t=text: self.operation_click(t)
                    style = 'Operation.TButton'
                
                btn = ttk.Button(button_grid, text=text, command=cmd, style=style)
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2, ipady=10)
        
        # Создаем операции (правая колонка)
        for i, text in enumerate(operation_buttons):
            if text == '':
                continue
                
            cmd = lambda t=text: self.operation_click(t)
            style = 'Operation.TButton'
            
            btn = ttk.Button(button_grid, text=text, command=cmd, style=style)
            btn.grid(row=i, column=3, sticky='nsew', padx=2, pady=2, ipady=10)
        
        # Настройка стилей кнопок
        self.setup_styles()
        
    def setup_styles(self):
        """Настройка стилей кнопок"""
        style = ttk.Style()
        
        # Стиль для цифр
        style.configure('Number.TButton',
                       font=('Arial', 14, 'bold'),
                       foreground='black')
        
        # Стиль для операций
        style.configure('Operation.TButton',
                       font=('Arial', 14, 'bold'),
                       foreground='blue')
        
        # Стиль для равно
        style.configure('Equal.TButton',
                       font=('Arial', 14, 'bold'),
                       foreground='white',
                       background='orange')
        
        # Стиль для специальных операций
        style.configure('Special.TButton',
                       font=('Arial', 12, 'bold'),
                       foreground='darkgreen')
        
        # Стиль для очистки
        style.configure('Clear.TButton',
                       font=('Arial', 12, 'bold'),
                       foreground='red')
    
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
    
    def operation_click(self, op):
        """Обработка нажатия операции"""
        try:
            if self.operation and not self.new_number:
                self.calculate()
            
            self.first_number = float(self.display_var.get())
            self.operation = op
            self.new_number = True
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def calculate(self):
        """Выполнение вычислений"""
        try:
            if not self.operation:
                return
            
            second_number = float(self.display_var.get())
            result = 0
            
            if self.operation == '+':
                result = self.first_number + second_number
            elif self.operation == '-':
                result = self.first_number - second_number
            elif self.operation == '*':
                result = self.first_number * second_number
            elif self.operation == '/':
                if second_number == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
                    return
                result = self.first_number / second_number
            elif self.operation == '^':
                result = self.first_number ** second_number
            
            # Форматирование результата
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
            
            self.operation = ""
            self.new_number = True
            
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка вычисления: {str(e)}")
    
    def sqrt(self):
        """Квадратный корень"""
        try:
            number = float(self.display_var.get())
            if number < 0:
                messagebox.showerror("Ошибка", "Квадратный корень из отрицательного числа!")
                return
            
            result = math.sqrt(number)
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
            
            self.new_number = True
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def square(self):
        """Возведение в квадрат"""
        try:
            number = float(self.display_var.get())
            result = number ** 2
            
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
            
            self.new_number = True
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def reciprocal(self):
        """Обратное значение (1/x)"""
        try:
            number = float(self.display_var.get())
            if number == 0:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                return
            
            result = 1 / number
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
            
            self.new_number = True
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def plus_minus(self):
        """Изменение знака"""
        try:
            number = float(self.display_var.get())
            result = -number
            
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def percentage(self):
        """Процент"""
        try:
            number = float(self.display_var.get())
            result = number / 100
            
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(round(result, 8)))
            
            self.new_number = True
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат числа!")
    
    def clear(self):
        """Полная очистка"""
        self.display_var.set("0")
        self.first_number = 0
        self.operation = ""
        self.new_number = True
    
    def clear_entry(self):
        """Очистка текущего ввода"""
        self.display_var.set("0")
        self.new_number = True
    
    def run(self):
        """Запуск калькулятора"""
        # Центрирование окна
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"400x600+{x}+{y}")
        
        # Привязка клавиатуры
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<KP_Enter>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        
        # Запуск главного цикла
        self.root.mainloop()

def main():
    """Основная функция программы"""
    print("Запуск графического калькулятора...")
    calc = GraphicalCalculator()
    calc.run()

if __name__ == "__main__":
    main() 