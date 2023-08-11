from random import randint
import pandas as pd

df = []
for i in range(6000):
    math = randint(120, 200)
    if math <= 140:
        ukr, eng = randint(120, 160), randint(120, 160)
    elif math <= 170:
        ukr, eng = randint(140, 180), randint(140, 180)
    else:
        ukr, eng = randint(170, 200), randint(170, 200)
    df.append([math, ukr, eng])

df = pd.DataFrame(df)
df.columns = ["math", "ukr", "eng"]

df["rating"] = 0.4 * df['math'] + 0.3 * df['eng'] + 0.3 * df['ukr']
df['benefit'] = 0
for i in range(df.shape[0]):
    if i % 9 == 0:
        df['benefit'][i] = 1

df.to_csv("generated.csv")
