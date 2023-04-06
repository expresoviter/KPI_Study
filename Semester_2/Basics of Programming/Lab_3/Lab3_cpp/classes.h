#pragma once
#include <iostream>
#include <string>
using namespace std;

class Numeral_8 {
	int number;
	int toBin();
public:
	Numeral_8();
	Numeral_8(int);
	Numeral_8(const Numeral_8&);
	int getNum();
	int getBin();
	Numeral_8 operator++();
	Numeral_8 operator+=(const Numeral_8);
	Numeral_8 operator+(const Numeral_8);
};

int toNum(int, int, int);