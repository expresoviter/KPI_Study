#include "classes.h"

int main()
{
	setlocale(LC_ALL, "ukr");
	Numeral_8 n1;
	int v;
	cout << "Введiть вiсiмкове число №2: "; cin >> v;
	Numeral_8 n2(v);
	Numeral_8 n3(n2);
	cout << "Створенi об'єкти класу вiсiмкових чисел: ";
	cout << "\nN1 (за замовчуванням) = "<<n1.getNum();
	cout << "\nN2 (введене) = "<<n2.getNum();
	cout << "\nN3 (копiя N2) = "<<n3.getNum();
	++n1;
	int x;
	cout << "\nВведiть число, на скiльки збiльшити N2: "; cin >> x;
	Numeral_8 n4(x);
	n2 += n4;
	cout << "\nЗмiненi числа:\nN1 (iнкрементовано) = "<<n1.getNum(); 
	cout << "\nN2 (додане введене число) = "<<n2.getNum();
	n3 = n1 + n2;
	cout << "\nЗмiнене N3 (сума змiнених N1 i N2) = "<<n3.getNum();
	n3.getBin();

}
