#include "binFiles.h"

void inputData(int act) {
    fstream inFile;
    if (act == 0) {                                         //���� ������ �������� �����
        inFile.open("input.bin", ios::out | ios::binary);
        inFile.close();
    }
    vector<int> aMins = readAndTranslate("input.bin");      //�������� ����� ��� �������� ������
    int tMins[2] = { 0,0 };
    int pos = 0;
    cin.ignore();
    string time;
    cout << "\n�������� �i��������� � ������i ��:��" << endl;
    cout << "\n������� (stop ��� ���������� ������): ";
    getline(cin,time);
    inFile.open("input.bin", ios::app | ios::binary);
    string temp;
    while (time != "stop") {
        int h = -1, m = -1;
        if (isdigit(time[0]) && isdigit(time[1]) && isdigit(time[3]) && isdigit(time[4])) { //�������� �� ����������
            temp = ""; temp += time[0]; temp += time[1];
            h = stoi(temp);
            temp = ""; temp += time[3]; temp += time[4];
            m = stoi(temp);
        }
        if (time[2] != ':' || h < 0 || h>23 || m < 0 || m>59) {
            cout << "����������� ��i�. ������������ ������ �����." << endl;
            if (pos == 1) {
                cout << "������� ������� �� �i�����" << endl;
                pos = 0;
            }
        }
        else {                                  //����  ��������, ������ � ���������� ����� �������
            if (pos == 0) {
                tMins[0] = h * 60 + m;
                pos = 1;
            }
            else {
                if (h * 60 + m > tMins[0])
                    tMins[1] = h * 60 + m;
                else
                    cout << "����������� ��i�. ������� ������� �� �i�����" << endl;
                pos = 0;
            }
        }
        int inc = 0;
        if (tMins[0] == 0 || tMins[1] == 0)
            inc = 1;
        for (int i = 0;i < aMins.size(); i += 2)
            if (inc == 0 && (tMins[0] >= aMins[i] && tMins[0]<aMins[i + 1] || tMins[1]>aMins[i] && tMins[1] <= aMins[i + 1] || tMins[0] <= aMins[i] && tMins[1] >= aMins[i + 1])) {
                cout << "������� ����������� �� i������" << endl;
                inc = 1;
            }
        if (inc == 0) {                                     //�� ����������� - ������ � ������ ����� ������ � ��������
            aMins.push_back(tMins[0]);
            aMins.push_back(tMins[1]);
            inFile.write((char*)&tMins[0], sizeof(int));
            inFile.write((char*)&tMins[1], sizeof(int));
        }
        if (pos == 0) {
            tMins[0] = 0;
            tMins[1] = 0;
            cout << "������� (stop ��� ���������� ������): ";
        }
        else
            cout << "�i���� (stop ��� ���������� ������): ";
        cin >> time;
    }
    inFile.close();
}


vector<int> readAndTranslate(string name) {
    ifstream inFile(name, ios::binary);
    vector<int>arrMins;
    int aMin, m=0;
    cout << "��i�� �����: \n";
    while (inFile.read((char*)&aMin, sizeof(int))) {            //�������� ������� � ����� � �������� �� �� �������
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
    for (int i = 0; i < aMins.size(); i += 2)           //³������ �� ������ ���� ��� ����� � ������
        time -= (aMins[i + 1] - aMins[i]);
    cout << "\n�� ���� � �����i " << time << " ������." << endl;
    cout << "�� " << n << " ��i���i� ����������� " << n * 15 << " ������." << endl;
    time -= n * 15;                                     //���������� 15 �� �� �볺���
    if (time < 0)
        cout << "���� �����������";
    else
        cout << "���� ���������";
}