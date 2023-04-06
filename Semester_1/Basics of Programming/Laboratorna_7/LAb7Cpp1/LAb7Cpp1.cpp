#include <iostream>
#include <ctime>

using namespace std;

void input(double[], int);                          //Прототипи: введення масиву
void output(double[], int, int);                    //Виведення результату
int findQ(double[], int);                           //Знаходження знаменника прогресії

int main()
{
    setlocale(LC_ALL, "ukr");
	int size;
	cout << "Введiть кiлькiсть елементiв: ";
	cin >> size;
	double* arr = new double[size];                      //Ініціалізація динамічного масиву
	input(arr, size);
    int q = findQ(arr, size);                            //Знаходимо знаменник прогресії
	output(arr, size, q);
    delete[]arr;
}

void input(double arr[], int size) {
	srand(time(NULL));
    cout << "Введена послiдовнiсть: ";
	for (int i = 0; i < size;i++) {
		arr[i] = rand() % 60 - 30;                   //Заповнюємо масив випадковим чином елементами від -30 до 30         
        cout << arr[i] << " ";
	}
    cout << endl;
}

int findQ(double arr[], int size) {
    int q1, q;
    if (arr[0] == 0) {                                //Перший елемент = 0, г.п. не утворюється
        q = 0;
    }
    else {
        q = arr[1] / arr[0];
        for (int i = 0;i < size - 1; i++) {            //Перебираємо частки сусідніх елементів
            q1 = arr[i + 1] / arr[i];
            if (q != q1) {                          //Поточна частка не збігається з першою            
                q = 0;
            }
        }

    }
    return q;
}

void output(double arr[], int size, int q) {
    if (q != 0) {
        cout << "Це геометрична прогресiя, q = " << q << endl;
    }
    else {
        double s = (arr[0] + arr[size - 1]) / 2;
        cout << "Середнє аритметичне першого i останнього елементiв = " << s << endl;
        for (int i = 0; i < size;i += 2) {
            arr[i] = s;
        }
        cout << "Змiнений масив: ";
        for (int i = 0; i < size; i++) {
            cout << arr[i] << " ";
        }
    }
}