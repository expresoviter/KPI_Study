#include "tree.h"

int main()
{
	ifstream file("input.txt");
	string s;
	getline(file, s);
	file.close();
	cout << "Entered expression: " << s << endl;
	ExpTree tree(s);
	tree.build(tree.root, tree.form);
	cout << "\nCalculated value = "<<tree.search(tree.root) << endl;
	cout << "\n\nBuilt tree:\n\n";
	tree.printTree("", tree.root, false);
}
