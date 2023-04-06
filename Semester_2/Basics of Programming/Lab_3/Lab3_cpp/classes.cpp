#include "classes.h"

Numeral_8::Numeral_8() { number = 7; }		//����������� �� �������������

Numeral_8::Numeral_8(int n) {				//����������� � ����������
	if (to_string(n).find('8')!=string::npos || to_string(n).find('9')!=string::npos) {
		cout << "\n�� �i�i����� �����. ������� �� ������������� 16.\n";
		number = 16;
	}
	else
		number = n;
}

Numeral_8::Numeral_8(const Numeral_8& obj) { number = obj.number; }		//����������� ���������

int Numeral_8::getNum() { return number; }

int Numeral_8::getBin(){
	cout << "\n1 ����i�:"; int n=(*this).toBin();
	cout << "\n2 ����i�:"; toNum(8, 2, (*this).getNum());
	return n;
}

int Numeral_8::toBin() {						//����� ����������� �������
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
	cout << "\n\t� ��i����i� ������i: " << stoll(s);
	return stoll(s);
}


Numeral_8 Numeral_8::operator++() {			//������������� ���������� ���������
	int c = 0;
	while (number % 10 == 7) {				//�������� ������ ����
		c++;
		number /= 10;
	}
	number++;
	number *= pow(10, c);
	return *this;
}

Numeral_8 Numeral_8::operator+(Numeral_8 obj) {
	int s = toNum(8, 10, (*this).getNum()) + toNum(8, 10, obj.getNum());	//���� � ���������
	s = toNum(10, 8, s);				//������ � �������
	return Numeral_8(s);
}

Numeral_8 Numeral_8::operator+=(const Numeral_8 obj) {
	number = (*this + obj).number;		//�������������� ����������
	return *this;
}

int toNum(int f, int t, int number) {		//����������� �� ���������
	int dec = 0; string temp = to_string(number);
	for (int i = 0; i < temp.length(); i++)
		dec += (int)(temp[i] - '0') * pow(f, temp.length() - i - 1);	//������ � ���������
	if (t == 2)
		cout << "\n\t� ��������i� ������i: " << dec;
	string bintemp = "";
	while (dec != 0) {						//������ ������� � �������
		bintemp += to_string(dec % t);
		dec /= t;
	}
	reverse(bintemp.begin(), bintemp.end());	//�������� ������
	if (t == 2)
		cout << "\n\t� ��i����i� ������i: " << stoll(bintemp);
	return stoll(bintemp);
}