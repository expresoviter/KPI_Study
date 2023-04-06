#include <iostream>
#include <ctime>

using namespace std;

void processMatrixA(double*[], int);					//Прототипи функцій: обробка першої матриці
void processMatrixB(double* [], double* [], int);		//Обробка нової матриці
void outputMatrix(double* [], int);						//Виведення матриці
void deleteMatrix(double* [], int);						//Видалення, вивільнення пам'яті під матрицю

int main()
{
	setlocale(LC_ALL, "ukr");
	int size;
	cout << "Введiть розмiр матрицi: ";
	cin >> size;
	double** arrA = new double*[size];					
	processMatrixA(arrA, size);
	double** arrB = new double* [size];	
	processMatrixB(arrA, arrB, size);
	cout << "\nВведена матриця А:\n";
	outputMatrix(arrA, size);
	cout << "\nПобудована матриця B:\n";
	outputMatrix(arrB, size);
	deleteMatrix(arrA, size);
	deleteMatrix(arrB, size);
}

void processMatrixA(double *arrA[], int size) {
	for (int i = 0;i < size;i++)
		arrA[i] = new double[size];					//Ініціалізація динамічних масивів у масиві для створення матриці
	srand(time(NULL));
	for (int i = 0;i < size;i++)
		for (int j = 0;j < size;j++)
			arrA[i][j] = rand() & 30 - 15;			//Заповнюємо матрицю випадковим чином від -15 до 15
}

void processMatrixB(double* arrA[], double* arrB[], int size) {
	for (int i = 0;i < size;i++)
		arrB[i] = new double[size];
	if (size == 1)									//Матриця одного елементу
		arrB[0][0] = arrA[0][0];
	else {
		int num;
		double sum;
		for (int i = 0;i < size;i++) {
			for (int j = 0;j < size;j++) {
				sum = 0;
				num = 0;
				if (i >= 1) {						//Існує елемент a[i-1][j]
					sum += arrA[i - 1][j];
					num++;
				}
				if (i < size - 1) {					//Існує елемент a[i+1][j]
					sum += arrA[i + 1][j];
					num++;
				}
				if (j >= 1) {						//Існує елемент a[i][j-1]
					sum += arrA[i][j - 1];
					num++;
				}
				if (j < size - 1) {					//Існує елемент a[i][j+1]
					sum += arrA[i][j + 1];
					num++;
				}
				arrB[i][j] = sum / num;
			}
		}
	}
}

void outputMatrix(double* arr[], int size) {
	for (int i = 0;i < size;i++) {
		for (int j = 0;j < size;j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
}

void deleteMatrix(double* arr[], int size) {
	for (int i = 0;i < size;i++)
		delete[] arr[i];
	delete[] arr;
}