#include "classes.h"

TIntNumber::TIntNumber() {
	number = "10";
	base = 10;
}

TIntNumber::TIntNumber(string n, int b) {
	if (b <= 16) {
		number = n;
		base = b;
	}
	else {
		cout << "Основа > 16, задання за замовчуванням числа 73а у 16-iй системi." << endl;
		number = "73a";
		base = 16;
	}
}

TIntNumber::TIntNumber(const TIntNumber& obj) {
	number = obj.number;
	base = obj.base;
}

string TIntNumber::getValue() {
	cout << number<<" ";
	return number;
}

TIntNumber TIntNumber::toBase(int newBase) {
	string dt[10] = {"a","11","b","12","c","13","d","14","e","15"};
	int st,dec = 0;
	string s;
	for (int i = 0; i < number.length(); i++) {						//Переводимо в десяткову
		s = "";
		if (isalpha(number[i])) {
			for (int j = 0; j < 10; j += 2)
				if ("" + number[i] == dt[j])
					s+= dt[j + 1];
		}
		else
			s+=number[i];
		dec += (stoi(s) * pow((*this).base, number.length() - i - 1));
	}
	s = "";
	if (dec == 0)
		return TIntNumber("0", newBase);
	while (dec != 0) {												//Переводимо в нову систему
		if (dec % newBase > 10) {
			for (int j = 1; j < 10; j += 2)
				if (to_string(dec % newBase) == dt[j])
					s += dt[j - 1];
		}
		else
			s += to_string(dec % newBase);
		dec /= newBase;
	}
	reverse(s.begin(), s.end());
	return TIntNumber(s, newBase);
}

TIntNumber TIntNumber::compare(TIntNumber obj) {				//Порівнюємо в загальному випадку
	TIntNumber n1 =toBase(10), n2 = obj.toBase(10);
	if (stoi(n1.number) > stoi(n2.number)) {
		cout << number << " у " << base << "-iй системi > " << obj.number << " у " << obj.base << "-iй системi.\n";
		return *this;
	}
	if (stoi(n1.number) == stoi(n2.number)) {
		cout << number << " у " << base << "-iй системi = " << obj.number << " у " << obj.base << "-iй системi.\n";
		return *this;
	}
	cout << number << " у " << base << "-iй системi < " << obj.number << " у " << obj.base << "-iй системi.\n";
	return obj;
}

TIntNumber TIntNumber::add(TIntNumber obj) {					//Додаємо числа в загальному випадку
	TIntNumber n1 = toBase(10), n2=obj.toBase(10);
	int newNum = stoll(n1.number) + stoll(n2.number);
	number = (TIntNumber(to_string(newNum), 10).toBase(base)).number;
	return *this;
}

TIntNumber2::TIntNumber2() { number = "110"; base = 2; }

TIntNumber2::TIntNumber2(string n): TIntNumber(n, 2) {
	int br = 0;
	for (int i = 0; i < n.length(); i++)
		if (n[i] != '0' && n[i] != '1')
			br = 1;
	if (br == 0)
		number = n;
	else {
		cout << "Не двiйкове число, задання за замовчуванням 110.\n";
		number = "110";
	}
}

TIntNumber2::TIntNumber2(const TIntNumber& obj) {
	number = obj.number;
}

TIntNumber2 TIntNumber2::compare(TIntNumber2 &obj) {				//Порівнюємо в двійковій - стандартно
	int n1 = stoll(number), n2 = stoll(obj.number);
	cout << "У двiйковiй - порiвнюємо TIntNumber2`s\n";
	if (n1 > n2) {
		cout << "Сума вiсiмкових чисел менша\n";
		cout << number << " > " << obj.number;
		return *this;
	}
	if (n1 == n2) {
		cout << "Суми рiвнi\n";
		cout << number << " = " << obj.number;
		return *this;
	}
	cout << "Сума двiйкових чисел менша\n";
	cout << number << " < " << obj.number;
	return obj;
}

TIntNumber TIntNumber2::toBase(int newBase) {			//У вісімкову можливість тріадами
	if (newBase == 8) {
		string dt[16] = { "000","0","001" , "1","010" , "2","011" , "3","100" , "4","101" , "5","110" , "6","111" ,"7" };
		if (number.length() % 3 != 0)
			for (int i = 0; i < (3 - number.length() % 3); i++)
				number = "0" + number;
		string oc = "";
		for (int i = 0; i < number.length(); i += 3)
			for (int j = 0; j < 16; j += 2)
				if (number.substr(i,3) == dt[j])
					oc+= dt[j + 1];
		return TIntNumber8(oc);
	}
	return TIntNumber::toBase(newBase);
}

TIntNumber8::TIntNumber8() { number = "33"; base = 8; }

TIntNumber8::TIntNumber8(string n): TIntNumber(n,8) {
	int br = 0;
	for (int i = 0; i < n.length(); i++)
		if (n[i] == '8' || n[i] == '9' || isalpha(n[i]))
			br = 1;
	if (br == 0)
		number = n;
	else {
		cout << "Не вiсiмкове число, задання за замовчуванням 33.\n";
		number = "33";
	}
}

TIntNumber8::TIntNumber8(const TIntNumber& obj) {
	number = obj.number;
}

TIntNumber TIntNumber8::toBase(int newBase) {					//У двійкову можливість тріадами
	if (newBase == 2) {
		string dt[16] = { "000","0","001" , "1","010" , "2","011" , "3","100" , "4","101" , "5","110" , "6","111" ,"7" };
		string bi = "";
		string s;
		for (int i = 0; i < number.length(); i++)
			for (int j = 1; j < 16; j += 2) {
				s = number[i];
				if (s == dt[j])
					bi += dt[j - 1];
			}
		return TIntNumber2(bi);
	}
	return (*this).TIntNumber::toBase(newBase);
}

TIntNumber* createNum(int size, int base) {				//Створюємо масив відповідної системи й розмірности
	TIntNumber* a = new TIntNumber[size];
	string b;
	srand(time(NULL));
	for (int i = 0; i < size; i++) {
		b = "";
		int dia = 2 + rand() % 4;
		for (int j = 0; j < dia; j++)
			b += to_string(rand() % base);
		if (base==2)
			a[i] = TIntNumber2(to_string(stoi(b)));
		else {
			if (base == 8)
				a[i] = TIntNumber8(to_string(stoi(b)));
			else
				a[i] = TIntNumber(to_string(stoi(b)), base);
		}
	}
	return a;
}