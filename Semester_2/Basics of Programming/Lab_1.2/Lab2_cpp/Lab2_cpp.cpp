#include "binFiles.h"

int main()
{
	setlocale(LC_ALL, "ukr");
	int act;
	cout << "Очистити данi файлу (0) чи додати (1) до iснуючих? : ";	//Додавання до файлу - уведіть 1, очищення - 0
	cin >> act;
	inputData(act);
	int n;
	cout << "Уведiть кiлькiсть клiєнтiв: ";
	cin >> n;
	verify(n, "input.bin");

}
