#include "classes.h"

int main()
{
	setlocale(LC_ALL, "");
	int m, n;
	cout << "Введiть кiлькiсть двiйкових чисел: ";
	cin >> m;
	cout << "Введiть кiлькiсть вiсiмкових чисел: ";
	cin >> n;
	TIntNumber* binArr = createNum(m,2), *octArr = createNum(n, 8);
	TIntNumber2 sBin("0");
	TIntNumber8 sOct("0");
	cout << "\nДвiйковi числа:\n";
	for (int i = 0; i < m; i++) {
		binArr[i].getValue();
		sBin.add(binArr[i]);
	}
	cout << "\nВiсiмковi числа:\n";
	for (int i = 0; i < n; i++) {
		octArr[i].getValue();
		sOct.add(octArr[i]);
	}
	cout << "\n\nСума двiйкових чисел = ";
	sBin.getValue();
	cout << "\nСума вiсiмкових чисел = ";
	sOct.getValue();
	TIntNumber2 s8Bin = sOct.toBase(2);
	cout << "\n\nСума вiсiмкових у двiйковому форматi = ";
	s8Bin.getValue();
	cout << endl;
	sBin.compare(s8Bin);
	delete[] binArr;
	delete[] octArr;

}
