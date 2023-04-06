#include <iostream>

using namespace std;

                                     //Прототипи функцій:
int fact(int);                       //Знаходження факторіалу
void pascal(int);                    //Виведення трикутника Паскаля

int main()
{
    setlocale(LC_ALL, "ukr");
    int n;
    cout << "Введiть n: ";
    cin >> n;
    pascal(n);
}

int fact(int c) {                    
    if (c == 0) {                    //0!=1
        return 1;
    }
    else {
        int s = 1;                   //Змінна факторіалу числа
        for (int i = 2;i <= c;i++) { //Знаходження факторіалу за допомогою аритметичного циклу
            s *= i;
        }
        return s;                    //Повертаємо значення факторіалу
    }
}
void pascal(int b) {
    int o;                                          //Змінна комбінації
    for (int k = 0;k <= b;k++) {                    //Цикл для рядків трикутника Паскаля
        for (int j = 0;j <= k;j++) {                //Цикл для елементів у конкретному рядку
            o = fact(k) / (fact(k - j) * fact(j));  
            cout << o << " ";                       //Виводимо комбінацію без переходу на новий рядок
        }
        cout << endl;
    }
}