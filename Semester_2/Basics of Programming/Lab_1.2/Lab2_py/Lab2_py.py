from binFiles import *

act=int(input("Очистити дані файлу (0) чи додати (1) до існуючих? : "))
inputData(act)
n=int(input("Уведіть кількість клієнтів: "))
verify(n, "input.bin")
