import numpy as np

array1 = np.array([10, 20, 30, 40, 50])

array2 = np.array(range(1, 13))
reshaped_array = array2.reshape(3, 4)
print("Исходный массив:\n", array2)
print("Массив после изменения формы:\n", reshaped_array)

array3 = np.array([60, 70, 80, 90, 100])
concatenated_array = np.concatenate((array1, array3))
print("Объединенный массив:", concatenated_array)

linspace_array = np.linspace(0, 1, 5)
print("Массив с равномерно распределенными значениями:", linspace_array)

squared_array = array1 ** 2
print("Квадраты элементов массива:", squared_array)

even_elements = array1[array1 % 2 == 0]
print("Четные элементы массива:", even_elements)

unsorted_array = np.array([35, 10, 85, 40, 25])
sorted_array = np.sort(unsorted_array)
print("Отсортированный массив:", sorted_array)

# numpy - довольно популярная библиотека. Она облегчает работу с массивом или матриксом. В основном мне она показался
# интересным в плане работы с массивом. Обьяснение действий кода написаный сверхуЖ
# [1] Изменение формы массива (reshape)
# [2] Создание массива с равномерно распределенными значениями
# [3] Поэлементное возведение в степень
# [4] Булева индексация
# [5] Сортировка массива
