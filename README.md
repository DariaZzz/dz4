Конфигурационное управление, домашнее задание №4, вариант 8, выполнила Захарова Дарья, ИКБО-40-23
Разработать ассемблер и интерпретатор для учебной виртуальной машины 
(УВМ). Система команд УВМ представлена далее. 
Для ассемблера необходимо разработать читаемое представление команд 
УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к 
которой задается из командной строки. Результатом работы ассемблера является 
бинарный файл в виде последовательности байт, путь к которому задается из 
командной строки. Дополнительный ключ командной строки задает путь к файлу
логу, в котором хранятся ассемблированные инструкции в духе списков 
“ключ=значение”, как в приведенных далее тестах. 
Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ 
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон 
также указывается из командной строки. 
Форматом для файла-лога и файла-результата является json. 
Необходимо реализовать приведенные тесты для всех команд, а также 
написать и отладить тестовую программу. 
41 
Загрузка константы 
A 
B 
C 
Биты 0—5 
Биты 6—33 
Биты 34—44 
30 
Константа 
Адрес 
Размер команды: 6 байт. Операнд: поле B. Результат: ячейка памяти по 
адресу, которым является поле C. 
Тест (A=30, B=359, C=442): 
0xDE, 0x59, 0x00, 0x00, 0xE8, 0x06 
Чтение из памяти 
A 
B 
C 
Биты 0—5 
Биты 6—16 
Биты 17—27 
14 
Адрес 
Адрес 
Размер команды: 4 байт. Операнд: ячейка памяти по адресу, которым 
является ячейка памяти по адресу, которым является поле B. Результат: ячейка 
памяти по адресу, которым является поле C. 
Тест (A=14, B=525, C=522): 
0x4E, 0x83, 0x14, 0x04 
Запись в память 
A 
B 
C 
Биты 0—5 
Биты 6—16 
Биты 17—27 
7 
Адрес 
Адрес 
Размер команды: 4 байт. Операнд: ячейка памяти по адресу, которым 
является поле B. Результат: ячейка памяти по адресу, которым является ячейка 
памяти по адресу, которым является поле C. 
Тест (A=7, B=151, C=50): 
0xC7, 0x25, 0x64, 0x00 
Унарная операция: побитовое "не" 
42 
A 
B 
C 
Биты 0—5 
Биты 6—16 
Биты 17—27 
36 
Адрес 
Адрес 
Размер команды: 4 байт. Операнд: ячейка памяти по адресу, которым 
является ячейка памяти по адресу, которым является поле C. Результат: ячейка 
памяти по адресу, которым является поле B. 
Тест (A=36, B=193, C=268): 
0x64, 0x30, 0x18, 0x02 
Тестовая программа 
Выполнить поэлементно операцию побитовое "не" над вектором длины 8. 
Результат записать в новый вектор.
