#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пример автоматизированного тестирования GUI калькулятора
"""

import tkinter as tk
from main import GraphicalCalculator
import time

class CalculatorDemo:
    """Демонстрация возможностей GUI калькулятора"""
    
    def __init__(self):
        self.calc = GraphicalCalculator()
        
    def demonstrate_basic_operations(self):
        """Демонстрация основных операций"""
        print("=== ДЕМОНСТРАЦИЯ ГРАФИЧЕСКОГО КАЛЬКУЛЯТОРА ===\n")
        
        # Демонстрация сложения
        print("1. Демонстрация сложения: 15 + 25")
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("5")
        self.calc.operation_click("+")
        self.calc.number_click("2")
        self.calc.number_click("5")
        self.calc.calculate()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Демонстрация вычитания
        print("\n2. Демонстрация вычитания: 100 - 37")
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.number_click("0")
        self.calc.operation_click("-")
        self.calc.number_click("3")
        self.calc.number_click("7")
        self.calc.calculate()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Демонстрация умножения
        print("\n3. Демонстрация умножения: 8 * 7")
        self.calc.clear()
        self.calc.number_click("8")
        self.calc.operation_click("*")
        self.calc.number_click("7")
        self.calc.calculate()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Демонстрация деления
        print("\n4. Демонстрация деления: 84 / 12")
        self.calc.clear()
        self.calc.number_click("8")
        self.calc.number_click("4")
        self.calc.operation_click("/")
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.calculate()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Демонстрация возведения в степень
        print("\n5. Демонстрация возведения в степень: 3 ^ 4")
        self.calc.clear()
        self.calc.number_click("3")
        self.calc.operation_click("^")
        self.calc.number_click("4")
        self.calc.calculate()
        print(f"   Результат: {self.calc.display_var.get()}")
        
    def demonstrate_special_functions(self):
        """Демонстрация специальных функций"""
        print("\n=== СПЕЦИАЛЬНЫЕ ФУНКЦИИ ===\n")
        
        # Квадратный корень
        print("1. Квадратный корень: √64")
        self.calc.clear()
        self.calc.number_click("6")
        self.calc.number_click("4")
        self.calc.sqrt()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Возведение в квадрат
        print("\n2. Возведение в квадрат: 9²")
        self.calc.clear()
        self.calc.number_click("9")
        self.calc.square()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Обратное значение
        print("\n3. Обратное значение: 1/8")
        self.calc.clear()
        self.calc.number_click("8")
        self.calc.reciprocal()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Процент
        print("\n4. Процент: 75%")
        self.calc.clear()
        self.calc.number_click("7")
        self.calc.number_click("5")
        self.calc.percentage()
        print(f"   Результат: {self.calc.display_var.get()}")
        
        # Изменение знака
        print("\n5. Изменение знака: ±42")
        self.calc.clear()
        self.calc.number_click("4")
        self.calc.number_click("2")
        self.calc.plus_minus()
        print(f"   Результат: {self.calc.display_var.get()}")
    
    def demonstrate_complex_calculation(self):
        """Демонстрация сложного вычисления"""
        print("\n=== СЛОЖНЫЕ ВЫЧИСЛЕНИЯ ===\n")
        
        # Пример: (15 + 25) * 2 = 80
        print("1. Последовательное вычисление: (15 + 25) * 2")
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("5")
        self.calc.operation_click("+")
        self.calc.number_click("2")
        self.calc.number_click("5")
        self.calc.calculate()  # Получаем 40
        print(f"   15 + 25 = {self.calc.display_var.get()}")
        
        self.calc.operation_click("*")
        self.calc.number_click("2")
        self.calc.calculate()  # Получаем 80
        print(f"   40 * 2 = {self.calc.display_var.get()}")
        
        # Пример: √(16 + 9) = 5
        print("\n2. Комбинированное вычисление: √(16 + 9)")
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("6")
        self.calc.operation_click("+")
        self.calc.number_click("9")
        self.calc.calculate()  # Получаем 25
        print(f"   16 + 9 = {self.calc.display_var.get()}")
        
        self.calc.sqrt()  # Получаем 5
        print(f"   √25 = {self.calc.display_var.get()}")
    
    def demonstrate_error_handling(self):
        """Демонстрация обработки ошибок"""
        print("\n=== ОБРАБОТКА ОШИБОК ===\n")
        
        print("1. Деление на ноль:")
        self.calc.clear()
        self.calc.number_click("5")
        self.calc.operation_click("/")
        self.calc.number_click("0")
        # calculate() покажет ошибку через messagebox
        print("   Ошибка будет показана в диалоговом окне")
        
        print("\n2. Квадратный корень из отрицательного числа:")
        self.calc.clear()
        self.calc.number_click("5")
        self.calc.plus_minus()  # Делаем -5
        # sqrt() покажет ошибку через messagebox
        print("   Ошибка будет показана в диалоговом окне")
        
        print("\n3. Обратное значение от нуля:")
        self.calc.clear()
        self.calc.number_click("0")
        # reciprocal() покажет ошибку через messagebox
        print("   Ошибка будет показана в диалоговом окне")
    
    def run_demo(self):
        """Запуск всех демонстраций"""
        print("ДЕМОНСТРАЦИЯ ВОЗМОЖНОСТЕЙ ГРАФИЧЕСКОГО КАЛЬКУЛЯТОРА")
        print("=" * 55)
        
        self.demonstrate_basic_operations()
        self.demonstrate_special_functions()
        self.demonstrate_complex_calculation()
        self.demonstrate_error_handling()
        
        print("\n" + "=" * 55)
        print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
        print("\nДля полного тестирования GUI запустите:")
        print("py main.py")

def main():
    """Основная функция"""
    demo = CalculatorDemo()
    demo.run_demo()

if __name__ == "__main__":
    main() 