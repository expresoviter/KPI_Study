from fileModule import *

act=int(input("Clear (0) or append (1)? : "))           #Додавання до файлу чи очищення
enter(act)
writing("input.txt","output.txt")
print("Entered file:")
output("input.txt")
print("\nCreated file:")
output("output.txt")

