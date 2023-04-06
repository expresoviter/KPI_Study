#include "files.h"

string processLine(string line, int* count) {
	line += " ";
	string lineOut = "",
		lineTemp = "";
	int i = 0, num = 0;
	while (i < line.length()) {
		if (line[i] != ' ') {					//Формуємо слова
			num++;
			lineTemp += line[i];
		}
		else {
			if (num == 2) {						//Враховуємо слова з двох символів
				(*count)++;
				cout << lineTemp << " ";
			}
			else {
				lineOut += lineTemp;
				lineOut += " ";
			}
			num = 0;
			lineTemp = "";
		}
		i++;
	}
	return lineOut;
}

void output(string name) {
	ifstream inFile(name);
	string line;
	while (!inFile.eof()) {
		getline(inFile, line);
		cout << line << endl;
	}
	inFile.close();
}

void input(int act) {
	fstream inFile;
	if (act == 0) {									//Якщо задано очищення вхідного файлу
		inFile.open("input.txt", ios::out);
		inFile.close();
	}
	inFile.open("input.txt", ios::app);
	if (!inFile) {
		cout << "Can`t open input file.";
		return;
	}
	string input, ms;
	cout << "Enter lines (`Shift+e` to finish entering)." << endl;
	char m = _getch();
	cin.ignore();
	while (m != 'E') {								//Перевіряємо, чи введений shift+e для завершення вводу
		cout << m;
		ms = m;
		getline(cin, input);
		inFile << ms+input << endl;
		m = _getch();
	}
	inFile.close();
}

void writing(string inName, string outName) {
	ifstream inFile;
	inFile.open(inName, ios::in);
	ofstream outFile(outName, ios::out);
	outFile.close();
	outFile.open(outName, ios::app);
	if (!inFile || !outFile) {
		cout << "Error to open file(s)";
		return;
	}
	string line, lineOut;
	int count = 0;
	cout << "\nRemoved words: ";
	while (!inFile.eof()) {
		getline(inFile, line);
		lineOut = processLine(line, &count);		//Порядково оброблюємо відповідно до умови
		outFile << lineOut << endl;
	}
	cout << endl;
	outFile << "Amount of removed words = " << count;
	inFile.close();
	outFile.close();
}