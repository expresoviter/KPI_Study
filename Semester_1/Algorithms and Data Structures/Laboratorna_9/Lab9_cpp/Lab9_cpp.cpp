#include <iostream>
#include <ctime>

using namespace std; 

void inputMatrix(double**, int, int);				//Прототипи функцій: введення матриці
void outputMatrix(double**, int, int);				//Виведення матриці
void processMatrix(double**, int, int, double);		//Обробка згідно з умовою

int main()
{
	setlocale(LC_ALL, "ukr");
	int m, n;
	double x;
	cout << "Введiть кiлькiсть рядкiв i стовпцiв матрицi: ";
	cin >> m >> n;
	double** matr = new double* [m];				//Ініціалізація динамічного масиву вказівників
	inputMatrix(matr, m, n);
	cout << "\nПочаткова матриця:\n";
	outputMatrix(matr, m, n);
	cout << "\nВведiть дiйсне число x: ";
	cin >> x;
	processMatrix(matr, m, n, x);
	cout << "\nЗмiнена матриця:\n";
	outputMatrix(matr, m, n);


}

void inputMatrix(double **matr, int m, int n) {
	srand(time(NULL));
	for (int i = 0;i < m;i++)
		matr[i] = new double[n];
	for (int i = 0;i < m;i++)
		for (int j = 0;j < n;j++) {
			matr[i][j] = rand() % 30 - 15;			//Заповнення матриці випадковим чином від -15 до 15
		}
}

void outputMatrix(double** matr, int m, int n) {
	for (int i = 0;i < m;i++) {
		for (int j = 0;j < n;j++) {
			cout << matr[i][j] << " ";
		}
		cout << endl;
	}
}

void processMatrix(double**matr, int m, int n, double x) {
	bool k = 0;
	int h;
	for (int j = 0; j < n; j++)						//Обхід матриці по стовпцях
		for (int i = 0;i < m;i++) {
			if (j % 2 == 0)
				h = i;
			else
				h = m - i-1;
			if (matr[h][j] == x && !k) {			//Перше входження елементу X по стовпцях
				cout << "\nЕлемент X = " << x << " знайдено в " << h + 1 << " рядку й " << j + 1 << " стовпцi." << endl;
				double tmp = matr[m/2][j];
				matr[m/2][j] = matr[h][j];		//Обмінюємо Х з елементом середнього рядка того ж стовпця
				matr[h][j] = tmp;
				k = 1;
			}
		}

}

