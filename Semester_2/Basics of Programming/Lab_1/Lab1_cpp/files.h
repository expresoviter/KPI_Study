#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

void input(int);					//Введення початкового тексту
void writing(string, string);		//Запис у вихідний файл
string processLine(string, int*);	//Обробка рядків
void output(string);				//Вивід на консоль