#include <iostream>
#include<ctime>

using namespace std;

void inputMatrix(double[5][5]);					//Прототипи: введення матриці
int diagArr(double[5][5],double[]);				//Утворення одновимірного масиву
void outputMatrix(double[5][5]);				//Виведення матриці
void sortAndOutput(double[], int);				//Сортування вставками та виведення масиву

int main()
{
	setlocale(LC_ALL, "ukr");
	double arr1[5][5];
	inputMatrix(arr1);
	double arr2[5];
	int size = diagArr(arr1, arr2);				//Знаходження масиву і його розміру
	cout << "Двовимiрний масив:\n";
	outputMatrix(arr1);
	sortAndOutput(arr2, size);

}

void inputMatrix(double arr1[5][5]) {
	srand(time(NULL));
	for (int i = 0;i < 5;i++) 
		for (int j = 0;j < 5;j++) {
			arr1[i][j] = rand() % 30 - 15;		//Заповнення матриці випадковим чином від -15 до 15
		}
}

int diagArr(double arr1[5][5], double arr2[]) {
	int sizeArr = 0;
	for (int i = 0;i < 5;i++) {
		if (arr1[i][4-i] < 0) {
			arr2[sizeArr] = arr1[i][4-i];		//Шукаємо від'ємні елементи на побічній діагоналі
			sizeArr++;
		}
	}
	return sizeArr;
}

void outputMatrix(double arr1[5][5]) {
	for (int i = 0;i < 5;i++) {
		for (int j = 0;j < 5;j++) {
			cout << arr1[i][j] << " ";
		}
		cout << endl;
	}
}

void sortAndOutput(double arr2[], int size) {
	if (size == 0)
		cout << "\nВiдсутнi вiд'ємнi елементи, масив не утворюється";
	else {
		cout << "\nУтворений масив:\n";
		if (size == 1)
			cout << arr2[0];
		else {
			bool k;
			double elem;
			for (int i = 1;i < size;i++) {				//Сортування вставками
				elem = arr2[i];
				k = 0;
				for (int j = i - 1; j >= 0;j--) {
					if (arr2[j] < elem && !k) {			//Якщо поточний більший за попередній
						arr2[j + 1] = arr2[j];			//Переставляємо їх місцями
						arr2[j] = elem;
					}
					else 					
						k = 1;
				}
			}
			for (int i = 0;i < size;i++)
				cout << arr2[i] << " ";
		}
	}
}