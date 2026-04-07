#!/usr/bin/env python3
"""
Программа для пересчета различных величин
Поддерживает: длину, массу, температуру, объем, площадь, скорость, время
"""

class UnitConverter:
    def __init__(self):
        # Конвертация длины (базовая единица - метр)
        self.length_units = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344
        }
        
        # Конвертация массы (базовая единица - килограмм)
        self.mass_units = {
            'mg': 0.001,
            'g': 0.001,
            'kg': 1.0,
            'ton': 1000.0,
            'oz': 0.0283495,
            'lb': 0.453592
        }
        
        # Конвертация температуры (специальная обработка)
        self.temp_units = ['C', 'F', 'K']
        
        # Конвертация объема (базовая единица - литр)
        self.volume_units = {
            'ml': 0.001,
            'l': 1.0,
            'm3': 1000.0,
            'cup': 0.236588,
            'pint': 0.473176,
            'gallon': 3.78541
        }
        
        # Конвертация площади (базовая единица - квадратный метр)
        self.area_units = {
            'cm2': 0.0001,
            'm2': 1.0,
            'km2': 1000000.0,
            'acre': 4046.86,
            'hectare': 10000.0
        }
        
        # Конвертация скорости (базовая единица - м/с)
        self.speed_units = {
            'm/s': 1.0,
            'km/h': 0.277778,
            'mph': 0.44704,
            'knot': 0.514444
        }
        
        # Конвертация времени (базовая единица - секунда)
        self.time_units = {
            's': 1.0,
            'min': 60.0,
            'h': 3600.0,
            'day': 86400.0,
            'week': 604800.0
        }
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Специальная конвертация температур"""
        # Сначала конвертируем в Цельсий
        if from_unit == 'C':
            celsius = value
        elif from_unit == 'F':
            celsius = (value - 32) * 5/9
        elif from_unit == 'K':
            celsius = value - 273.15
        else:
            raise ValueError(f"Неизвестная единица температуры: {from_unit}")
        
        # Затем конвертируем из Цельсия в целевую единицу
        if to_unit == 'C':
            return celsius
        elif to_unit == 'F':
            return celsius * 9/5 + 32
        elif to_unit == 'K':
            return celsius + 273.15
        else:
            raise ValueError(f"Неизвестная единица температуры: {to_unit}")
    
    def convert(self, value, from_unit, to_unit, category):
        """Общая функция конвертации"""
        if category == 'length':
            units = self.length_units
        elif category == 'mass':
            units = self.mass_units
        elif category == 'volume':
            units = self.volume_units
        elif category == 'area':
            units = self.area_units
        elif category == 'speed':
            units = self.speed_units
        elif category == 'time':
            units = self.time_units
        elif category == 'temperature':
            return self.convert_temperature(value, from_unit.upper(), to_unit.upper())
        else:
            raise ValueError(f"Неизвестная категория: {category}")
        
        if from_unit not in units or to_unit not in units:
            available = ', '.join(units.keys())
            raise ValueError(f"Неизвестная единица. Доступные: {available}")
        
        # Конвертируем через базовую единицу
        base_value = value * units[from_unit]
        result = base_value / units[to_unit]
        
        return result
    
    def get_available_units(self, category):
        """Получить список доступных единиц для категории"""
        if category == 'length':
            return list(self.length_units.keys())
        elif category == 'mass':
            return list(self.mass_units.keys())
        elif category == 'temperature':
            return self.temp_units
        elif category == 'volume':
            return list(self.volume_units.keys())
        elif category == 'area':
            return list(self.area_units.keys())
        elif category == 'speed':
            return list(self.speed_units.keys())
        elif category == 'time':
            return list(self.time_units.keys())
        else:
            return []


def print_menu():
    """Вывод меню программы"""
    print("\n" + "="*50)
    print("       ПРОГРАММА ПЕРЕСЧЕТА ВЕЛИЧИН")
    print("="*50)
    print("\nДоступные категории:")
    print("1. Длина (length)")
    print("2. Масса (mass)")
    print("3. Температура (temperature)")
    print("4. Объем (volume)")
    print("5. Площадь (area)")
    print("6. Скорость (speed)")
    print("7. Время (time)")
    print("0. Выход")
    print("="*50)


def main():
    converter = UnitConverter()
    
    while True:
        print_menu()
        choice = input("\nВыберите категорию (1-7 или 0 для выхода): ").strip()
        
        if choice == '0':
            print("\nДо свидания!")
            break
        
        category_map = {
            '1': 'length',
            '2': 'mass',
            '3': 'temperature',
            '4': 'volume',
            '5': 'area',
            '6': 'speed',
            '7': 'time'
        }
        
        if choice not in category_map:
            print("❌ Неверный выбор. Попробуйте снова.")
            continue
        
        category = category_map[choice]
        available_units = converter.get_available_units(category)
        
        print(f"\n📏 Категория: {category}")
        print(f"Доступные единицы: {', '.join(available_units)}")
        
        try:
            # Ввод значения
            value = float(input("\nВведите значение: "))
            
            # Ввод исходной единицы
            from_unit = input("Из какой единицы: ").strip().lower()
            
            # Ввод целевой единицы
            to_unit = input("В какую единицу: ").strip().lower()
            
            # Конвертация
            result = converter.convert(value, from_unit, to_unit, category)
            
            # Вывод результата
            print(f"\n✅ Результат:")
            print(f"   {value} {from_unit} = {result:.6f} {to_unit}")
            
            # Для больших/малых чисел показываем в научном формате
            if abs(result) > 1000000 or (abs(result) < 0.001 and result != 0):
                print(f"   или {result:.6e} {to_unit}")
                
        except ValueError as e:
            print(f"\n❌ Ошибка: {e}")
        except Exception as e:
            print(f"\n❌ Произошла ошибка: {e}")
        
        # Предложение продолжить
        cont = input("\nПродолжить? (y/n): ").strip().lower()
        if cont != 'y':
            print("\nДо свидания!")
            break


if __name__ == "__main__":
    main()
