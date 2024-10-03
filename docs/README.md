# Общее описание проекта geometric_lib

Проект `geometric_lib` представляет собой библиотеку для работы с геометрическими операциями, такими как вычисление площади квадрата, круга, вычисление периметра треугольника, круга, квадрата, вычисление полупериметра треугольника.

# How to use calculator:

1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas

## Area

- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter

- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание функций

## Функция `calc`

Функция применяет запрошенную функцию к запрошенной фигуре с запрошенными данными

### Пример использования:

`calc(Square, area, 2)`
>>> 4

## Функция `area` для квадрата 

Функция вычисляет площадь квадрата.

### Пример использования:

`area(2)`
>>> 4

## Функция `perimeter` для квадрата

Функция вычисляет периметр квадрата.

### Пример использования:

`area(2)`
>>> 8

## Функция `area` для треугольника

Функция вычисляет полупериметр треугольника.

### Пример использования:

`area(2,4,6)`
>>> 6

## Функция `perimeter` для треугольника

Функция вычисляет периметр треугольника.

### Пример использования:

`area(2,6,4)`
>>> 12

## Функция `area` для круга

Функция вычисляет площадь круга.

### Пример использования:

`area(10)`
>>> 314.1592653589793

## Функция `perimeter` для круга

Функция вычисляет периметр круга.

### Пример использования:

`area(10)`
>>> 62.83185307179586

# История изменений

- b5b0fae: Update docs for calculate.py
- d76db2a: Add calculate.py
- 51c40eb: Doc updated for triangle
- d080c78: Triangle added
- d078c8d: Docs added
- 8ba9aeb: Circle and square added
