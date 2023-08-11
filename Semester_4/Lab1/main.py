import pandas as pd
import matplotlib.pyplot as plt


def formatNegative(val):
    if type(val) == str:
        if val[1:].isdigit():
            return int("-" + val[1:])
        return None
    return val


# Обрані дані у форматі таблиці
migrationData = pd.read_excel("kpv_reg_0122_ue.xls", skiprows=[0, 1, 2, 4])
print("Завантажені дані:\n\n", migrationData.head())

# Первинна обробка: знак мінус у від'ємних значеннях заданий не дефісом, а тире
for i in migrationData:
    if i != "Область":
        for j in range(len(migrationData[i])):
            val = formatNegative(migrationData[i][j])
            migrationData[i][j] = val

# Статистика
print("Математичне сподівання:\n", migrationData.mean())
print("\nМедіана:\n", migrationData.median())
print("\nМода:\n", migrationData.mode().iloc[0])
print("\nДисперсія:\n", migrationData.var())
print("\nСередньоквадратичне відхилення:\n", migrationData.std())

# Візуалізація
migrationData.plot(x="Область", y="Кількість прибулих", kind="bar")
plt.tight_layout()
migrationData.plot(x="Область", y="Кількість вибулих", kind="bar")
plt.tight_layout()
migrationData.plot(x="Область", y="Міграційний приріст", kind="bar")
plt.legend()
plt.tight_layout()
plt.show()

# пункт колекції Series i DataFrame
# Series з індексами за замовчуванням - кількість прибулих - і виведення Series
print("\nSeries з індексами за замовчуванням:\n")
arrived = pd.Series(migrationData["Кількість прибулих"])
print(arrived.head())

# створення Series з однаковими значеннями і звернення до елементів за індексом
sameValues = pd.Series(arrived[0], range(3))
print("\nSeries з однаковими значеннями:\n\n", sameValues.head())

# обчислення описових статистик для Series
print("\nCount: ", arrived.count())
print("Mean: ", arrived.mean())
print("Min: ", arrived.min())
print("Max: ", arrived.max())
print("Std: ", arrived.std())
print("\nDESCRIBE:\n", arrived.describe())

# Series з нестандартними індексами
arrivedInd = pd.Series(list(migrationData["Кількість прибулих"]), index=list(migrationData["Область"]))
print("\nSeries з нестандартними індексами:\n", arrivedInd.head())

# Series зі словника і звернення за нестандартним індексом
serDict = {migrationData["Область"][i]: migrationData["Кількість прибулих"][i] for i in range(25)}
print("\nСтворений словник: ", serDict)
arrivedDict = pd.Series(serDict)
print("Series зі словника:\n", arrivedDict.head())
print("arrivedDict[\"Вінницька\"] =", arrivedDict["Вінницька"])
print("arrivedDict.Вінницька =", arrivedDict.Вінницька)
print("arrivedDict.values =", arrivedDict.values)

# Series з рядковими елементами
strSer = pd.Series(migrationData["Область"])
print("\nSeries з рядковими елементами:\n", strSer.head())
print("\nМістять літеру 'с':\n", strSer.str.contains("с").head())
print("\nМетод upper:\n", strSer.str.upper().head())

# DataFrame на базі словника
frDict = {i: [migrationData[i][j] for j in range(5)] for i in migrationData if i != "Область"}
print("\nСтворений словник:", frDict)
dictFrame = pd.DataFrame(frDict)
print("\nDataFrame зі словника:\n", dictFrame.head())

# Налаштування індексів DataFrame з використанням атрибута index
dictFrame.index = list(migrationData["Область"])[:5]
print("\nІндекси з атрибутом index:\n",dictFrame.head())

# Вибір рядків з використанням атрибутів loc і iloc - окремі рядки, сегменти і підмножини
print("\n", dictFrame.loc["Вінницька"])

print("\n", dictFrame.iloc[0])

print("\n", dictFrame.loc["Вінницька":"Дніпропетровська"])

print("\n", dictFrame.iloc[0:3])

print("\n", dictFrame.loc[["Вінницька", "Дніпропетровська"]])

print("\n", dictFrame.iloc[[0, 2]])

print("\n", dictFrame.loc["Вінницька":"Дніпропетровська", ["Кількість прибулих", "Міграційний приріст"]])

print("\n", dictFrame.iloc[0:3, [0, 2]])

# Логічне індексування
print(dictFrame[dictFrame >= 1000])

print(dictFrame[(dictFrame >= 0) & (dictFrame <= 400)])

# Звернення до конкретного осередку DataFrame по рядку і стовпцю
print(dictFrame.at["Вінницька", "Міграційний приріст"])
print(dictFrame.iat[0, 2])

dictFrame.at["Вінницька", "Міграційний приріст"] = 100
print(dictFrame.iat[0, 2])

dictFrame.iat[0, 2] = 75
print(dictFrame.iat[0, 2])

# Описова статистика
print(dictFrame.describe())

print(dictFrame.mean())

# Транспонування DataFrame
print(dictFrame.T.head())
print(dictFrame.T.describe())

# Сортування
print("\nЗа рядками за спаданням:\n",dictFrame.sort_index(ascending=False))
print("\nЗа стовпцями за зростанням:\n",dictFrame.sort_index(axis=1))
print("\nЗа зростанням значень стовпців у Вінницькій області:\n",dictFrame.sort_values(by="Вінницька", axis=1))

print("\nПерший рядок за спаданням:\n",dictFrame.iloc[0].sort_values(ascending=False))
