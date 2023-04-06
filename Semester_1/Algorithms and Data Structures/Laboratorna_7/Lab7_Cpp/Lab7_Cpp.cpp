#include <iostream>
using namespace std;

void initArrays1And2(char[], char[]);			//Прототипи функцій: ініціалізація першого і другого масивів
int initArray3(char[], char[], char[]);			//Заповнення третього масиву
void processArray3(char[],int);					//Обробка третього масиву
void outputArray(char[], int);

int main()
{
	setlocale(LC_ALL, "ukr");
	char arr1[10], arr2[10], arr3[10];
	initArrays1And2(arr1, arr2);
	int sizeArr3 = initArray3(arr1, arr2, arr3);
	cout << "Перший масив: ";
	outputArray(arr1, 10);
	cout << "\nДругий масив: ";
	outputArray(arr2, 10);
	cout << "\nТретiй масив: ";
	outputArray(arr3, sizeArr3);
	processArray3(arr3, sizeArr3);
}

void initArrays1And2(char arr1[], char arr2[]) {
	for (int i = 0;i < 10;i++) {
		arr1[i] = char(60 - 2 * i);				//Заповненнями виразами, заданими в умові
		arr2[i] = char(40 + 3 * i);
	}
}

int initArray3(char arr1[], char arr2[], char arr3[]) {
	int size = 0;
	for (int i = 0;i < 10;i++) {
		for (int j = 0;j < 10;j++) {
			if (arr1[i] == arr2[j]) {
				arr3[size] = arr1[i];					
				size++;
			}

		}
		
	}
	return size;
}

void outputArray(char arr[], int size) {
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
}
void processArray3(char arr3[], int size){
	bool k = 0;									//Змінна для перевірки знаходження першого входження
	for (int i=0;i<size;i++){
		if (int(arr3[i]) == 52 && !k) {
			cout << "\n\nПерше входження елементу з кодом 52 ('4') в третьому масивi пiд iндексом i = " << i;
			k = 1;
		}

		
	}
}