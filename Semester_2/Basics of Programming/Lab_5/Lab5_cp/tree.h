#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

struct TNode {					//Структура вершини
	string inf;
	TNode* left, * right;
};

class ExpTree {					//Клас дерева
public:
	TNode* root;
	string form;

	ExpTree(string s) { root = new TNode; form = s; }
	~ExpTree() { delete root; }
	TNode* build(TNode*, string);
	float search(TNode*);
	void printTree(string, TNode*, bool);
};

int* operatorLoop(bool, int,string, char, char);
