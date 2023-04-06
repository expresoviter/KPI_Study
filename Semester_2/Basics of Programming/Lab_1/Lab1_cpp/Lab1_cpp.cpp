#include "files.h"

int main()
{
	int act;
	cout << "Clear (0) or append (1)? : ";	//Додавання до файлу чи очищення
	cin >> act;
	input(act);	
	writing("input.txt","output.txt");
	cout << "Entered file:\n";
	output("input.txt");
	cout << "\nCreated file:\n";
	output("output.txt");
	return 0;
}


