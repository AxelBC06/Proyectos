import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor, LogisticRegression
def Predicción_de_ventas_de_un_Producto():
    # Datos de entrenamiento (características X y valores reales Y)
    x = np.array([
        [10, 20, 7],
        [15, 25, 8],
        [20, 15, 6],
        [25, 30, 9],
        [30, 35, 10],
        [12, 22, 7],
        [18, 27, 8],
        [14, 23, 7],
        [19, 29, 9],
        [22, 32, 9],
    ])
    y = np.array([200, 250, 300, 400, 210, 280, 230, 290, 340, 360])

    # Normalización de los datos
    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    # Entrenamiento del modelo de regresión
    regresion = SGDRegressor(max_iter=10000)
    regresion.fit(x_norm, y)

    # Nuevos datos a predecir
    x_predict = np.array([
        [12, 23, 8],
        [22, 17, 9],
        [8, 9, 6],
    ])
    x_predict_norm = norm.transform(x_predict)

    # Predicción
    y_norm = regresion.predict(x_predict_norm)

    # Resultados
    print("Las ventas mensuales son las siguientes:")
    print("---------------------------------------------------------------------------------------")
    for i, w in enumerate(y_norm):
        print(f"Mes número {i + 1} tuvo: {w:.0f} ventas mensuales")
    print("---------------------------------------------------------------------------------------")



def Predicción_de_Consumo_de_combustible():
    x = np.array([
        [100, 5, 3, 1],
        [150, 10, 5, 2],
        [200, 7, 2, 1],
        [250, 12, 1, 2],
        [300, 15, 4, 3],
        [120, 4, 2, 1],
        [180, 9, 3, 2],
        [220, 11, 6, 3],
        [140, 6, 5, 1],
        [160, 8, 4, 2],
    ])
    y = np.array([10, 15, 12, 18, 20, 8, 14, 22, 11, 13])

    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    regresion = SGDRegressor(max_iter=10000)
    regresion.fit(x_norm, y)

    x_predict = np.array([
        [120, 6, 2, 1],
        [220, 11, 3, 2],
        [180, 8, 4, 3],
    ])
    x_predict_norm = norm.transform(x_predict)
    y_norm = regresion.predict(x_predict_norm)

    print("---------------------------------------------------------------------------------------")
    print("El consumo de combustible de los vehículos de la empresa es el siguiente:")
    for i, w in enumerate(y_norm):
        print(f"Vehículo número {i + 1} consume {w:.2f} galones de combustible")
    print("---------------------------------------------------------------------------------------")


def Predicción_de_Diabetes():
    x = np.array([
        [22.5, 90],
        [30.1, 150],
        [28.4, 110],
        [24.6, 85],
        [32.0, 160],
        [26.5, 120],
        [21.8, 95],
        [29.3, 140],
        [25.1, 100],
        [31.7, 155],
    ])
    y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])  # 1 = Riesgo de diabetes, 0 = Sin riesgo

    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    log = LogisticRegression()
    log.fit(x_norm, y)

    x_predict = np.array([
        [26.0, 130],
        [33.0, 175],
        [24.0, 90],
        [31.0, 150],
    ])
    x_predict_norm = norm.transform(x_predict)
    y_norm = log.predict_proba(x_predict_norm)

    print("---------------------------------------------------------------------------------------")
    for i, w in enumerate(y_norm[:, 1]):  # Probabilidad de tener diabetes
        if w >= 0.4:
            print(f"La persona número {i + 1} tiene riesgo con una probabilidad del {w * 100:.2f}%")
        else:
            print(f"La persona número {i + 1} no tiene riesgo")
    print("---------------------------------------------------------------------------------------")


def Predicción_de_Enfermedades_Cardiovasculares():
    x = np.array([
        [45, 180],
        [50, 210],
        [38, 190],
        [60, 240],
        [30, 170],
        [55, 230],
        [47, 200],
        [65, 250],
        [40, 195],
        [58, 220],
    ])
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # 1 = Riesgo, 0 = Sin riesgo

    norm = StandardScaler()
    x_norm = norm.fit_transform(x)

    log = LogisticRegression()
    log.fit(x_norm, y)

    x_predict = np.array([
        [36, 190],
        [62, 245],
        [54, 210],
        [48, 195],
    ])
    x_predict_norm = norm.transform(x_predict)
    y_norm = log.predict_proba(x_predict_norm)

    print("---------------------------------------------------------------------------------------")
    for i, w in enumerate(y_norm[:, 1]):
        if w >= 0.4:
            print(f"La persona número {i + 1} tiene riesgo con una probabilidad del {w * 100:.2f}%")
        else:
            print(f"La persona número {i + 1} no tiene riesgo")
    print("---------------------------------------------------------------------------------------")
# -------------------------------------------------------------
#  menu xd
# -------------------------------------------------------------
menu = 0
while menu <= 4:
    menu = int(input("""
*** Menú ***
Seleccione el número de la predicción que desea visualizar:
1 - Predicción de ventas de un Producto
2 - Predicción de Consumo de combustible
3 - Predicción de Diabetes
4 - Predicción de Enfermedades Cardiovasculares
5 - Salir
Su opción -----> """))

    if menu == 1:
        Predicción_de_ventas_de_un_Producto()
    elif menu == 2:
        Predicción_de_Consumo_de_combustible()
    elif menu == 3:
        Predicción_de_Diabetes()
    elif menu == 4:
        Predicción_de_Enfermedades_Cardiovasculares()
    elif menu == 5:
        print("Gracias por utilizar mi programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")












    


