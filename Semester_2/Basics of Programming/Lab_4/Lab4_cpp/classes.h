#pragma once
#include <iostream>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>

using namespace std;

class TIntNumber {
public:
	string number;
	int base;
	TIntNumber();						//Конструктори
	TIntNumber(string,int);
	TIntNumber(const TIntNumber&);
	string getValue();
	TIntNumber toBase(int);				//Переведення між системами
	TIntNumber compare(TIntNumber);
	TIntNumber add(TIntNumber);
};

class TIntNumber2 :public TIntNumber {
public:
	TIntNumber2();
	TIntNumber2(string);
	TIntNumber2(const TIntNumber&);
	TIntNumber2 compare(TIntNumber2&);
	TIntNumber toBase(int);
};

class TIntNumber8 :public TIntNumber {
public:
	TIntNumber8();
	TIntNumber8(string);
	TIntNumber8(const TIntNumber&);
	TIntNumber toBase(int);
};

TIntNumber* createNum(int, int);		//Масив випадкових чисел відповідної системи