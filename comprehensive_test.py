#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Комплексная проверка всех операций калькулятора
"""

from main import GraphicalCalculator
import time

class ComprehensiveTest:
    """Комплексное тестирование всех операций"""
    
    def __init__(self):
        self.calc = GraphicalCalculator()
        self.passed = 0
        self.failed = 0
        
    def test_operation(self, name, expected, actual, tolerance=1e-10):
        """Проверка операции"""
        if abs(float(actual) - expected) <= tolerance:
            print(f"✅ {name}: {actual} (ожидалось {expected})")
            self.passed += 1
            return True
        else:
            print(f"❌ {name}: {actual} (ожидалось {expected})")
            self.failed += 1
            return False
    
    def test_basic_operations(self):
        """Тестирование основных операций"""
        print("\n🔢 ОСНОВНЫЕ ОПЕРАЦИИ:")
        
        # Сложение
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("5")
        self.calc.operation_click("+")
        self.calc.number_click("2")
        self.calc.number_click("5")
        self.calc.calculate()
        self.test_operation("15 + 25", 40, self.calc.display_var.get())
        
        # Вычитание
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.number_click("0")
        self.calc.operation_click("-")
        self.calc.number_click("3")
        self.calc.number_click("7")
        self.calc.calculate()
        self.test_operation("100 - 37", 63, self.calc.display_var.get())
        
        # Умножение
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.operation_click("*")
        self.calc.number_click("8")
        self.calc.calculate()
        self.test_operation("12 * 8", 96, self.calc.display_var.get())
        
        # Деление
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("4")
        self.calc.number_click("4")
        self.calc.operation_click("/")
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.calculate()
        self.test_operation("144 / 12", 12, self.calc.display_var.get())
        
        # Возведение в степень
        self.calc.clear()
        self.calc.number_click("2")
        self.calc.operation_click("^")
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.calculate()
        self.test_operation("2 ^ 10", 1024, self.calc.display_var.get())
    
    def test_special_functions(self):
        """Тестирование специальных функций"""
        print("\n⚙️ СПЕЦИАЛЬНЫЕ ФУНКЦИИ:")
        
        # Квадратный корень
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.number_click("0")
        self.calc.sqrt()
        self.test_operation("√100", 10, self.calc.display_var.get())
        
        # Возведение в квадрат
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.square()
        self.test_operation("12²", 144, self.calc.display_var.get())
        
        # Обратное значение
        self.calc.clear()
        self.calc.number_click("4")
        self.calc.reciprocal()
        self.test_operation("1/4", 0.25, self.calc.display_var.get())
        
        # Процент
        self.calc.clear()
        self.calc.number_click("8")
        self.calc.number_click("0")
        self.calc.percentage()
        self.test_operation("80%", 0.8, self.calc.display_var.get())
        
        # Изменение знака
        self.calc.clear()
        self.calc.number_click("4")
        self.calc.number_click("2")
        self.calc.plus_minus()
        self.test_operation("±42", -42, self.calc.display_var.get())
        
        # Изменение знака обратно
        self.calc.plus_minus()
        self.test_operation("±(-42)", 42, self.calc.display_var.get())
    
    def test_decimal_operations(self):
        """Тестирование операций с десятичными числами"""
        print("\n🔢 ДЕСЯТИЧНЫЕ ЧИСЛА:")
        
        # Сложение с десятичными
        self.calc.clear()
        self.calc.number_click("3")
        self.calc.number_click(".")
        self.calc.number_click("1")
        self.calc.number_click("4")
        self.calc.operation_click("+")
        self.calc.number_click("2")
        self.calc.number_click(".")
        self.calc.number_click("8")
        self.calc.number_click("6")
        self.calc.calculate()
        self.test_operation("3.14 + 2.86", 6.0, self.calc.display_var.get())
        
        # Умножение с десятичными
        self.calc.clear()
        self.calc.number_click("2")
        self.calc.number_click(".")
        self.calc.number_click("5")
        self.calc.operation_click("*")
        self.calc.number_click("4")
        self.calc.calculate()
        self.test_operation("2.5 * 4", 10.0, self.calc.display_var.get())
        
        # Деление с десятичными
        self.calc.clear()
        self.calc.number_click("7")
        self.calc.number_click(".")
        self.calc.number_click("5")
        self.calc.operation_click("/")
        self.calc.number_click("2")
        self.calc.number_click(".")
        self.calc.number_click("5")
        self.calc.calculate()
        self.test_operation("7.5 / 2.5", 3.0, self.calc.display_var.get())
    
    def test_complex_calculations(self):
        """Тестирование сложных вычислений"""
        print("\n🧮 СЛОЖНЫЕ ВЫЧИСЛЕНИЯ:")
        
        # Цепочка операций: 5 + 3 * 2
        self.calc.clear()
        self.calc.number_click("5")
        self.calc.operation_click("+")
        self.calc.number_click("3")
        self.calc.calculate()  # 8
        self.calc.operation_click("*")
        self.calc.number_click("2")
        self.calc.calculate()  # 16
        self.test_operation("(5 + 3) * 2", 16, self.calc.display_var.get())
        
        # Возведение в степень и корень
        self.calc.clear()
        self.calc.number_click("3")
        self.calc.operation_click("^")
        self.calc.number_click("2")
        self.calc.calculate()  # 9
        self.calc.sqrt()  # 3
        self.test_operation("√(3²)", 3, self.calc.display_var.get())
        
        # Комбинированные операции
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.number_click("0")
        self.calc.operation_click("/")
        self.calc.number_click("4")
        self.calc.calculate()  # 25
        self.calc.square()  # 625
        self.test_operation("(100 / 4)²", 625, self.calc.display_var.get())
    
    def test_edge_cases(self):
        """Тестирование граничных случаев"""
        print("\n⚠️ ГРАНИЧНЫЕ СЛУЧАИ:")
        
        # Ноль
        self.calc.clear()
        self.calc.number_click("0")
        self.calc.operation_click("+")
        self.calc.number_click("5")
        self.calc.calculate()
        self.test_operation("0 + 5", 5, self.calc.display_var.get())
        
        # Операция с нулем
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.operation_click("*")
        self.calc.number_click("0")
        self.calc.calculate()
        self.test_operation("10 * 0", 0, self.calc.display_var.get())
        
        # Единица
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.operation_click("^")
        self.calc.number_click("1")
        self.calc.number_click("0")
        self.calc.number_click("0")
        self.calc.calculate()
        self.test_operation("1 ^ 100", 1, self.calc.display_var.get())
        
        # Квадратный корень из 1
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.sqrt()
        self.test_operation("√1", 1, self.calc.display_var.get())
        
        # Квадрат единицы
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.square()
        self.test_operation("1²", 1, self.calc.display_var.get())
    
    def test_clear_functions(self):
        """Тестирование функций очистки"""
        print("\n🧹 ФУНКЦИИ ОЧИСТКИ:")
        
        # Тест C (полная очистка)
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.number_click("3")
        self.calc.operation_click("+")
        self.calc.number_click("4")
        self.calc.number_click("5")
        self.calc.clear()
        expected_display = "0"
        expected_operation = ""
        actual_display = self.calc.display_var.get()
        actual_operation = self.calc.operation
        
        if actual_display == expected_display and actual_operation == expected_operation:
            print("✅ Полная очистка (C): работает корректно")
            self.passed += 1
        else:
            print(f"❌ Полная очистка (C): дисплей={actual_display}, операция={actual_operation}")
            self.failed += 1
        
        # Тест CE (очистка ввода)
        self.calc.clear()
        self.calc.number_click("1")
        self.calc.number_click("2")
        self.calc.number_click("3")
        self.calc.clear_entry()
        
        if self.calc.display_var.get() == "0":
            print("✅ Очистка ввода (CE): работает корректно")
            self.passed += 1
        else:
            print(f"❌ Очистка ввода (CE): {self.calc.display_var.get()}")
            self.failed += 1
    
    def run_all_tests(self):
        """Запуск всех тестов"""
        print("🧪 КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА")
        print("=" * 50)
        
        self.test_basic_operations()
        self.test_special_functions()
        self.test_decimal_operations()
        self.test_complex_calculations()
        self.test_edge_cases()
        self.test_clear_functions()
        
        print("\n" + "=" * 50)
        print(f"📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
        print(f"✅ Пройдено: {self.passed}")
        print(f"❌ Не пройдено: {self.failed}")
        print(f"📈 Успешность: {self.passed}/{self.passed + self.failed} ({100 * self.passed / (self.passed + self.failed):.1f}%)")
        
        if self.failed == 0:
            print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        else:
            print(f"\n⚠️ Обнаружены проблемы в {self.failed} тестах")
        
        return self.failed == 0

def main():
    """Основная функция"""
    tester = ComprehensiveTest()
    tester.run_all_tests()

if __name__ == "__main__":
    main() 