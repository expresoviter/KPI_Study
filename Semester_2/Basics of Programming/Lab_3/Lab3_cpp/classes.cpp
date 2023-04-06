#include "classes.h"

Numeral_8::Numeral_8() { number = 7; }		//Конструктор за замовчуванням

Numeral_8::Numeral_8(int n) {				//Конструктор з параметром
	if (to_string(n).find('8')!=string::npos || to_string(n).find('9')!=string::npos) {
		cout << "\nНе вiсiмкове число. Задання за замовчуванням 16.\n";
		number = 16;
	}
	else
		number = n;
}

Numeral_8::Numeral_8(const Numeral_8& obj) { number = obj.number; }		//Конструктор копіювання

int Numeral_8::getNum() { return number; }

int Numeral_8::getBin(){
	cout << "\n1 спосiб:"; int n=(*this).toBin();
	cout << "\n2 спосiб:"; toNum(8, 2, (*this).getNum());
	return n;
}

int Numeral_8::toBin() {						//Спосіб переведення тріадами
	string s = "", temp=to_string(number);
	for (int i = 0; i < temp.length(); i++) {
		switch (temp[i]) {
		case '0': 
			s += "000"; 
			break;
		case '1':
			s += "001";
			break;
		case '2':
			s += "010";
			break;
		case '3':
			s += "011";
			break;
		case '4':
			s += "100";
			break;
		case '5':
			s += "101";
			break;
		case '6':
			s += "110";
			break;
		case '7':
			s += "111";
			break;
		}
	}
	cout << "\n\tу двiйковiй системi: " << stoll(s);
	return stoll(s);
}


Numeral_8 Numeral_8::operator++() {			//Перевизначаємо префіксний інкремент
	int c = 0;
	while (number % 10 == 7) {				//Забираємо останні сімки
		c++;
		number /= 10;
	}
	number++;
	number *= pow(10, c);
	return *this;
}

Numeral_8 Numeral_8::operator+(Numeral_8 obj) {
	int s = toNum(8, 10, (*this).getNum()) + toNum(8, 10, obj.getNum());	//Сума в десятковій
	s = toNum(10, 8, s);				//Перевід у вісімкову
	return Numeral_8(s);
}

Numeral_8 Numeral_8::operator+=(const Numeral_8 obj) {
	number = (*this + obj).number;		//Перевизначеним додаванням
	return *this;
}

int toNum(int f, int t, int number) {		//Переведення між системами
	int dec = 0; string temp = to_string(number);
	for (int i = 0; i < temp.length(); i++)
		dec += (int)(temp[i] - '0') * pow(f, temp.length() - i - 1);	//Перевід у десяткову
	if (t == 2)
		cout << "\n\tу десятковiй системi: " << dec;
	string bintemp = "";
	while (dec != 0) {						//Перевід діленням у вихідну
		bintemp += to_string(dec % t);
		dec /= t;
	}
	reverse(bintemp.begin(), bintemp.end());	//Обертаємо остачі
	if (t == 2)
		cout << "\n\tу двiйковiй системi: " << stoll(bintemp);
	return stoll(bintemp);
}