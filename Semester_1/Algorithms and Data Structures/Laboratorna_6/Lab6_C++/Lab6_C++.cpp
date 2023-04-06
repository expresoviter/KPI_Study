#include <iostream>
#include <math.h>

using namespace std;

int fact(int);                                  //Прототипи функцій: знаходження факторіалу
double summ(int, int, double, double);          //Знаходження суми

int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    double  s = summ(1, n, 1, 1);
    cout << "Sum = " << s;
}
double summ(int k, int n, double a, double b) {
    int f = fact(k);
    if (k == n) {                               //Термінальна гілка:
        return (a - b) / f;               //Повертаємо останній доданок суми
    }
    else {                                      //Рекурсивна гілка
        return ((a - b) / f) + summ(k + 1, n, 0.5 * (sqrt(b) + 5 * sqrt(a)), 2 * a * a + b);  
                                                //Повертаємо поточний доданок + сума вже без нього
    }
}
int fact(int c) {
    if (c > 1) {                                //Рекурсивна гілка
        return c * fact(c - 1);
    }
    else {                                      //Термінальна гілка
        return 1;
    }
}