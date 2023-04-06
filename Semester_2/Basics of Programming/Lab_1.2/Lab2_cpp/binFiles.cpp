#include "binFiles.h"

void inputData(int act) {
    fstream inFile;
    if (act == 0) {                                         //Якщо обрано очищення файлу
        inFile.open("input.bin", ios::out | ios::binary);
        inFile.close();
    }
    vector<int> aMins = readAndTranslate("input.bin");      //Отримуємо масив уже введених перерв
    int tMins[2] = { 0,0 };
    int pos = 0;
    cin.ignore();
    string time;
    cout << "\nвведення вiдбувається у форматi ГГ:ХХ" << endl;
    cout << "\nпочаток (stop для завершення роботи): ";
    getline(cin,time);
    inFile.open("input.bin", ios::app | ios::binary);
    string temp;
    while (time != "stop") {
        int h = -1, m = -1;
        if (isdigit(time[0]) && isdigit(time[1]) && isdigit(time[3]) && isdigit(time[4])) { //Перевірка на коректність
            temp = ""; temp += time[0]; temp += time[1];
            h = stoi(temp);
            temp = ""; temp += time[3]; temp += time[4];
            m = stoi(temp);
        }
        if (time[2] != ':' || h < 0 || h>23 || m < 0 || m>59) {
            cout << "Некоректний ввiд. Неправильний формат даних." << endl;
            if (pos == 1) {
                cout << "Початок перерви не дiйсний" << endl;
                pos = 0;
            }
        }
        else {                                  //Якщо  коректно, додаємо у проміжковий масив перерви
            if (pos == 0) {
                tMins[0] = h * 60 + m;
                pos = 1;
            }
            else {
                if (h * 60 + m > tMins[0])
                    tMins[1] = h * 60 + m;
                else
                    cout << "Некоректний ввiд. Початок перерви не дiйсний" << endl;
                pos = 0;
            }
        }
        int inc = 0;
        if (tMins[0] == 0 || tMins[1] == 0)
            inc = 1;
        for (int i = 0;i < aMins.size(); i += 2)
            if (inc == 0 && (tMins[0] >= aMins[i] && tMins[0]<aMins[i + 1] || tMins[1]>aMins[i] && tMins[1] <= aMins[i + 1] || tMins[0] <= aMins[i] && tMins[1] >= aMins[i + 1])) {
                cout << "Перерва накладається на iснуючу" << endl;
                inc = 1;
            }
        if (inc == 0) {                                     //Не накладається - додаємо у сталий масив перерв і записуємо
            aMins.push_back(tMins[0]);
            aMins.push_back(tMins[1]);
            inFile.write((char*)&tMins[0], sizeof(int));
            inFile.write((char*)&tMins[1], sizeof(int));
        }
        if (pos == 0) {
            tMins[0] = 0;
            tMins[1] = 0;
            cout << "початок (stop для завершення роботи): ";
        }
        else
            cout << "кiнець (stop для завершення роботи): ";
        cin >> time;
    }
    inFile.close();
}


vector<int> readAndTranslate(string name) {
    ifstream inFile(name, ios::binary);
    vector<int>arrMins;
    int aMin, m=0;
    cout << "Вмiст файлу: \n";
    while (inFile.read((char*)&aMin, sizeof(int))) {            //Вичитуємо перерви з файлу і виводимо їх на консоль
        cout << aMin/60 << ":"<<aMin-(aMin/60)*60<<" ";
        if (m == 0) {
            cout << "- ";
            m = 1;
        }
        else
            m = 0;
        arrMins.push_back(aMin);
    }
    inFile.close();
    return arrMins;
}

void verify(int n, string name) {
    int time = 24 * 60;
    vector<int> aMins = readAndTranslate(name);
    for (int i = 0; i < aMins.size(); i += 2)           //Віднімаємо від усього часу час кожної з перерв
        time -= (aMins[i + 1] - aMins[i]);
    cout << "\nВи маєте в запасi " << time << " хвилин." << endl;
    cout << "На " << n << " клiєнтiв знадобиться " << n * 15 << " хвилин." << endl;
    time -= n * 15;                                     //Розрахунок 15 хв на клієнта
    if (time < 0)
        cout << "Часу недостатньо";
    else
        cout << "Часу достатньо";
}