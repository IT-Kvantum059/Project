import cv2 as cv2
import difflib
import hashlib
hash1=("/home/sophia/Изображения/dwa.png")
hash2=("/home/sophia/Изображения/dwa.png")
image = cv2.imread(hash1)
import cv2 as cv2
import difflib
image = cv2.imread(hash1)
image1 = cv2.imread(hash2)
resized1= cv2.resize(image1, (8,8), interpolation = cv2.INTER_AREA) #Уменьшим картинку,INTER_AREA это передискретизации с использованием отношения площади пикселя, понятия не имею что это, но оно работае

resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) #Уменьшим картинку,INTER_AREA это передискретизации с использованием отношения площади пикселя, понятия не имею что это, но оно работае
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Переведем в черно-белый формат
gray_image1 = cv2.cvtColor(resized1, cv2.COLOR_BGR2GRAY)
avg=gray_image.mean()#функция mean ищет среднее арифметическое масива изображения
avg1=gray_image1.mean()
s,threshold_image=cv2.threshold(gray_image,avg,255, 0)#Функция threshold возвращает изображение, в котором все пиксели, которые темнее 127 заменены на 0, а все, которые ярче 127, — на 255

d,threshold_image1=cv2.threshold(gray_image1,avg1,255, 0)#Функция threshold возвращает изображение, в котором все пиксели, которые темнее 127 заменены на 0, а все, которые ярче 127, — на 255




second_hash = hashlib.md5()#начало иницилизируем                                                                                   

second_hash1 = hashlib.md5()
second_hash.update(threshold_image)#Этот метод используется для расчитывает хеш-объекта с заданным аргументом

second_hash1.update(threshold_image1)
hash2=second_hash.digest()
hash1=second_hash1.digest()#выбираем как будет выводиться значение есть digest() и тд
print(str(hash1))
print(str(hash2))
if hash2!=hash1:
    print("yps")
#def CompareHfash(hash1,hash2):
l=len(hash1)#считывает колво элементов в строке
print(l)



        
