#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тесты для графического калькулятора
"""

import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
import math
from main import GraphicalCalculator

class TestGraphicalCalculator(unittest.TestCase):
    """Тесты для класса GraphicalCalculator"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.root = tk.Tk()
        self.calc = GraphicalCalculator()
        self.calc.root = self.root
        self.calc.display_var = tk.StringVar()
        self.calc.display_var.set("0")
        self.calc.first_number = 0
        self.calc.operation = ""
        self.calc.new_number = True
    
    def tearDown(self):
        """Очистка после каждого теста"""
        self.root.destroy()
    
    def test_number_click(self):
        """Тест ввода цифр"""
        # Тест первой цифры
        self.calc.number_click("5")
        self.assertEqual(self.calc.display_var.get(), "5")
        
        # Тест добавления цифры
        self.calc.number_click("3")
        self.assertEqual(self.calc.display_var.get(), "53")
        
        # Тест новое число
        self.calc.new_number = True
        self.calc.number_click("7")
        self.assertEqual(self.calc.display_var.get(), "7")
    
    def test_operation_click(self):
        """Тест выбора операции"""
        self.calc.display_var.set("10")
        self.calc.operation_click("+")
        
        self.assertEqual(self.calc.first_number, 10.0)
        self.assertEqual(self.calc.operation, "+")
        self.assertTrue(self.calc.new_number)
    
    def test_calculate_addition(self):
        """Тест сложения"""
        self.calc.first_number = 5.0
        self.calc.operation = "+"
        self.calc.display_var.set("3")
        
        self.calc.calculate()
        self.assertEqual(self.calc.display_var.get(), "8")
    
    def test_calculate_subtraction(self):
        """Тест вычитания"""
        self.calc.first_number = 10.0
        self.calc.operation = "-"
        self.calc.display_var.set("3")
        
        self.calc.calculate()
        self.assertEqual(self.calc.display_var.get(), "7")
    
    def test_calculate_multiplication(self):
        """Тест умножения"""
        self.calc.first_number = 4.0
        self.calc.operation = "*"
        self.calc.display_var.set("5")
        
        self.calc.calculate()
        self.assertEqual(self.calc.display_var.get(), "20")
    
    def test_calculate_division(self):
        """Тест деления"""
        self.calc.first_number = 15.0
        self.calc.operation = "/"
        self.calc.display_var.set("3")
        
        self.calc.calculate()
        self.assertEqual(self.calc.display_var.get(), "5")
    
    @patch('tkinter.messagebox.showerror')
    def test_calculate_division_by_zero(self, mock_showerror):
        """Тест деления на ноль"""
        self.calc.first_number = 10.0
        self.calc.operation = "/"
        self.calc.display_var.set("0")
        
        self.calc.calculate()
        mock_showerror.assert_called_once_with("Ошибка", "Деление на ноль невозможно!")
    
    def test_calculate_power(self):
        """Тест возведения в степень"""
        self.calc.first_number = 2.0
        self.calc.operation = "^"
        self.calc.display_var.set("3")
        
        self.calc.calculate()
        self.assertEqual(self.calc.display_var.get(), "8")
    
    def test_sqrt(self):
        """Тест квадратного корня"""
        self.calc.display_var.set("9")
        self.calc.sqrt()
        self.assertEqual(self.calc.display_var.get(), "3")
        
        self.calc.display_var.set("16")
        self.calc.sqrt()
        self.assertEqual(self.calc.display_var.get(), "4")
    
    @patch('tkinter.messagebox.showerror')
    def test_sqrt_negative(self, mock_showerror):
        """Тест квадратного корня из отрицательного числа"""
        self.calc.display_var.set("-4")
        self.calc.sqrt()
        mock_showerror.assert_called_once_with("Ошибка", "Квадратный корень из отрицательного числа!")
    
    def test_square(self):
        """Тест возведения в квадрат"""
        self.calc.display_var.set("4")
        self.calc.square()
        self.assertEqual(self.calc.display_var.get(), "16")
        
        self.calc.display_var.set("5")
        self.calc.square()
        self.assertEqual(self.calc.display_var.get(), "25")
    
    def test_reciprocal(self):
        """Тест обратного значения"""
        self.calc.display_var.set("4")
        self.calc.reciprocal()
        self.assertEqual(self.calc.display_var.get(), "0.25")
        
        self.calc.display_var.set("2")
        self.calc.reciprocal()
        self.assertEqual(self.calc.display_var.get(), "0.5")
    
    @patch('tkinter.messagebox.showerror')
    def test_reciprocal_zero(self, mock_showerror):
        """Тест обратного значения от нуля"""
        self.calc.display_var.set("0")
        self.calc.reciprocal()
        mock_showerror.assert_called_once_with("Ошибка", "Деление на ноль!")
    
    def test_plus_minus(self):
        """Тест изменения знака"""
        self.calc.display_var.set("5")
        self.calc.plus_minus()
        self.assertEqual(self.calc.display_var.get(), "-5")
        
        self.calc.display_var.set("-3")
        self.calc.plus_minus()
        self.assertEqual(self.calc.display_var.get(), "3")
    
    def test_percentage(self):
        """Тест процента"""
        self.calc.display_var.set("50")
        self.calc.percentage()
        self.assertEqual(self.calc.display_var.get(), "0.5")
        
        self.calc.display_var.set("25")
        self.calc.percentage()
        self.assertEqual(self.calc.display_var.get(), "0.25")
    
    def test_clear(self):
        """Тест полной очистки"""
        self.calc.display_var.set("123")
        self.calc.first_number = 45.0
        self.calc.operation = "+"
        self.calc.new_number = False
        
        self.calc.clear()
        
        self.assertEqual(self.calc.display_var.get(), "0")
        self.assertEqual(self.calc.first_number, 0)
        self.assertEqual(self.calc.operation, "")
        self.assertTrue(self.calc.new_number)
    
    def test_clear_entry(self):
        """Тест очистки ввода"""
        self.calc.display_var.set("123")
        self.calc.new_number = False
        
        self.calc.clear_entry()
        
        self.assertEqual(self.calc.display_var.get(), "0")
        self.assertTrue(self.calc.new_number)

if __name__ == '__main__':
    print("Запуск тестов графического калькулятора...")
    unittest.main(verbosity=2) 