# Markdown (Заголовок - ур. 1)
## Markdown (Заголовок - ур. 2)
### Markdown (Заголовок - ур. 3)
#### Markdown (Заголовок - ур. 4)
##### Markdown (Заголовок - ур. 5)
###### Markdown (Заголовок - ур. 6)

*Markdown (Курсив)*

**Markdown (жирненький)**


***Markdown (жирненький - наколнный)***

Ниже представлен пример отображения разметки на языке Markdown, написанной в файле README.md в [репозитории](https://github.com/laravel/laravel).

<strong> MarkDown </strong> - простоя язык разметки

Список всех HTML-тегов вы можете найти [здесь](https://html5book.ru/html-tags/).

# <center> Центрирование заголовка </center>

- Список (вариант 1)
* Список (вариант 2)
+ Список (вариант 3)
    + вложенный спсок

1. Нумерация
2. Нумерация

# Обозначение кода

- одинарный парный — для вставки строки кода в текст;
- двойной парный — для вставки небольшого участка кода, содержащего -одинарный апостроф, в текст;
- тройной парный — для вставки блока программного кода.

`print('Hello world!')` - обозначение кода 

```python

lst = [10, 34, 21, 21, 3]

summa = sum(lst)

```
![alt text](image.png)

***Для оформления цитат используется знак «больше» (>):***

> Цитируемый текст
![alt text](image-1.png)

# ФОРМУЛЫ
**Когда в проекте есть математическая составляющая, важно отразить её в описании.**

Чтобы начать использовать KaTeX в Markdown, необходимо воспользоваться символом '$'.

Если обрамить формулу с обеих сторон одним символом $, то её можно встроить в текст, а если двумя — формула автоматически центрируется.

**Например, следующий синтаксис**

Пусть задано выражение:

$$a = b +c,$$

где $a=0$

**Греческие символы**

$\alpha$

$\gamma$

$\sigma$

**Степени**

$a^2$

$b_{ij}$

$w^{ij}_n$

**Для того чтобы создать «двухэтажную» дробь, можно воспользоваться оператором \frac с двумя параметрами, которые передаются в фигурных скобках (числитель и знаменатель). Например:**

$\frac{1+x}{n}$

**Вставка изображения по ссылке**

![](https://i.imgur.com/n59SqxM.jpg)

$f(x) = \frac{1+x^2}{x^2+5x+1}$

# ***Можно настраивать размеры изображений***
<center> <img src=https://raw.githubusercontent.com/Vrushti24/Face-Mask-Detection/logo/Logo/facemaskdetection.ai%20%40%2051.06%25%20(CMYK_GPU%20Preview)%20%2018-02-2021%2018_33_18%20(2).png width=300 height=300> </center>

Face Mask Detection system built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts in order to detect face masks in static images as well as in real-time video streams.

<center> <img src="https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/Readme_images/Screen%20Shot%202020-05-14%20at%208.49.06%20PM.png?raw=true" width=300 height=200> </center>