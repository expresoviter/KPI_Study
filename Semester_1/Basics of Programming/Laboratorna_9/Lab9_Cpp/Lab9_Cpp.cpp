#include <iostream>
#include <string>

using namespace std;

int iscorrect(string);
void minAndMax(string, int[], int);											//Прототипи: знаходження максимуму і мінімуму
string replacement(string, int[], int);										//Заміна значень

int main()
{
	setlocale(LC_ALL, "ukr");
	string st;
	cout << "Введiть  рядок  з  цифрами  i  пробiлами  : ";
	getline(cin, st);
	int cor = iscorrect(st);
	int arr[4];
	minAndMax(st, arr, cor);
	string stOut=replacement(st, arr, cor);
	cout <<"Рядок iз замiненими максимумом i мiнiмумом: "<< stOut;

}

int iscorrect(string st) {
	int j = 0;
	for (int i = 0;i < st.length();i++)
		if (int(st[i]) < 48 && int(st[i])!=32 || int(st[i]) > 57)
			j = 1;
	return j;
}
void minAndMax(string st, int arr[], int cor) {
	string temp;
	int i = 0, j=0, err=0, ind;
	while (i != st.length() && cor==0) {								//Проходимо до кінця рядка
		if (st[i] != ' ') {												//Знаходимо перший символ після пробілу - початок числа
			temp = "";
			ind = i;
			while (i != st.length() && st[i] != ' ') {					//Поки йдуть цифри за першою
				temp += st[i];											//Формуємо число в окремій змінній
				i++;
			}
			if (j == 0) {												//Перше входження - перше число
				arr[0] = stoi(temp);
				arr[2] = stoi(temp);
				arr[1] = ind;
				arr[3] = ind;
				j = 1;
			}
			else {
				if (stoi(temp) < arr[0]) {
					arr[0] = stoi(temp);
					arr[1] = ind;
				}
				if (stoi(temp) > arr[2]) {
					arr[2] = stoi(temp);
					arr[3] = ind;
				}
			}
		}
		else
			i++;
	}
}

string replacement(string st, int arr[], int cor) {
	string stOut = "";
	if (cor == 1)
		stOut = "Некоректний заданий текст";
	else {
		int i = 0;
		while (i != st.length()) {
			if (i == arr[1]) {							//Індекс мінімуму - додаємо до нової змінної максимум
				stOut += to_string(arr[2]);
				i += to_string(arr[0]).length();
			}
			if (i == arr[3]) {							//Індекс максимуму - додаємо мінімум
				stOut += to_string(arr[0]);
				i += to_string(arr[2]).length();
			}
			else {
				stOut += st[i];
				i++;
			}
		}
	}
	return stOut;
}
