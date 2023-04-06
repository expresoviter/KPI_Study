#include "tree.h"

TNode* ExpTree::build(TNode* node,string s) {		//Побудова дерева
	int c = 0;
	for (int i = 0; i < s.length(); i++) {
		if (isdigit(s[i])==0 && s[i]!='.')
			c = 1;
	}
	if (c==0){										//Якщо вираз - число
		node->inf = s;
		node->left = NULL;
		node->right = NULL;
		return node;
	}

	else {
		if (s[0] == '(' && s[s.length() - 1] == ')')
			s = s.substr(1, s.length() - 2);
		c = 0;
		TNode* nextLeft = new TNode;
		TNode* nextRight = new TNode;
		int* a = operatorLoop(c, 0, s, '+', '-');	//Шукаємо оператори з найменшим пріоритетом
		int i = a[1];	c = a[0];
		a = operatorLoop(c, i, s, '*', '/');
		i = a[1];	c = a[0];
		a = operatorLoop(c, i, s, '^', '^');
		i = a[1];
		
		node->inf = s[i];
		node->left = build(nextLeft, s.substr(0, i));
		node->right = build(nextRight, s.substr(i + 1, s.length() - i - 1));
		return node;

	}

}

float ExpTree::search(TNode* curr) {		//Обчислюємо вираз
	if (isdigit(curr->inf[0])==0) {
		float lIn = search(curr->left); 
		float rIn = search(curr->right);
		switch ((curr->inf)[0]) {
		case '+':
			return lIn + rIn;
			break;
		case '-':
			return lIn - rIn;
			break;
		case '*':
			return lIn * rIn;
			break;
		case '/':
			return lIn / rIn;
			break;
		case '^':
			return pow(lIn, rIn);
		}
	}
	else
		return stof(curr->inf);
}

void ExpTree::printTree(string prefix, TNode* node, bool isLeft)		//Виводимо дерево на консоль
{
	if (node != NULL)
	{
		cout << prefix+"|__";
		cout << node->inf << endl;

		printTree(prefix + (isLeft ? "|   " : "    "), node->left, true);
		printTree(prefix + (isLeft ? "|   " : "    "), node->right, false);
	}
}

int* operatorLoop(bool c,int i,string s, char fir, char sec) {		//Шукаємо оператори
	int d = 0;
	if (c == 0) {
		i = s.length() - 1;
		while (i != -1) {
			if (s[i] == ')')
				d++;
			if (s[i] == '(')
				d--;
			if (d==0 && c == 0 && (s[i] == fir || s[i] == sec)) {
				c = 1;
				break;
			}
			i--;
		}
	}
	int a[2] = { c,i };
	return a;
}