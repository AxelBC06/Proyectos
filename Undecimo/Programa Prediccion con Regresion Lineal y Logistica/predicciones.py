import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LogisticRegression


def Predicción_de_Temperatura_en_Cultivos():
    x = np.array([
        [30,8,1],
        [50,6,2],
        [40,7,1],
        [60,10,3],
        [55,5,2],
        [45,9,1],
        [35,4,3],
        [65,11,2],
        [70,12,1],
        [50,8,3],
    ])

    y = np.array([24,22,23,26,21,25,20,28,29,24])

    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    regresion = SGDRegressor(max_iter=10000)
    regresion.fit(x_norm, y)

    x_predict = np.array([
        [40,8,1],
        [60,10,2],
        [50,7,3],
        ])

    x_predict_norm = norm.transform(x_predict)
    y_pred = regresion.predict(x_predict_norm)

    for i, w in enumerate(y_pred):
        print(f"La temperatura optima numero {i +1} es de: {w:.0f}°C ")
    print(y_pred)
def Clasificación_de_Enfermedades_Respiratorias():
    x = np.array([
        [5,30],
        [20,45],
        [15,50],
        [8,28],
        [30,60],
        [2,25],
        [12,40],
        [18,55],
        [4,35],
        [25,65]
    ])
    y = np.array([0,1,1,0,1,0,1,1,0,1])

    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    log = LogisticRegression()
    log.fit(x_norm, y)

    x_predict = ([
        [10, 40],
        [22, 55],
        [6,30],
    ])
    x_predict_norm = norm.transform(x_predict)
    probabilidades = log.predict_proba(x_predict_norm)
    for i, w in enumerate(probabilidades[:,1]):
        if w >= 0.6:
            print(f"la persona numero {i+1} tiene un riesgo con una probabilidad del {w * 100:.2f}%")
        else:
            print(f"la persona numero {i+1} no tiene ningun riesgo")    

    print(probabilidades)

Predicción_de_Temperatura_en_Cultivos()
Clasificación_de_Enfermedades_Respiratorias()