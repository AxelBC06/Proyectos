import pymysql
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor, LogisticRegression

def diabetes():
    try:
        db = pymysql.connect(
        host= "localhost",
        user= "root",
        passwd= "1234",
        database="diabetes",
        port= 3307
        )
        print("conexion exitosa")
    except Exception as e:
        print("error al conectar:", e)

    cursor = db.cursor()

    query = """

    SELECT p.edad, p.genero, h.imc, h.nivel_glucosa, h.presion_arterial, h.grosor_piel,h.insulina, h.diabetes
    from pacientes as p inner join historialmedico as h on p.id = h.paciente_id

    """
    cursor.execute(query)
    datos = cursor.fetchall()
    # print(datos)
    datos_s = np.array(datos)

    X = np.array(datos_s[:, 0:7])
    y = np.array(datos_s[:, -1])
    for i in X:
        if i[1] == "Masculino":
            i[1]=1
        else:
            i[1]=0
    X = X.astype(float)
    y = y.astype(float)

    print(X)
    print(y)
    norm = StandardScaler()
    x_norm = norm.fit_transform(X)

    log = LogisticRegression()
    log.fit(x_norm, y)

    x_p = np.array([
        [48,  1, 33.0, 170, 85, 37, 0],
        [32, 0,  24.0, 105, 72, 26, 85],
        [55, 1,  29.0, 140, 80, 32, 0],
        [27, 0, 21.0, 95,  68, 22, 75],
    ])
    x_p_n = norm.transform(x_p)
    y_norm = log.predict_proba(x_p_n)
    print(y_norm)
    print("---------------------------------------------------------------------------------------")
    for i, w in enumerate(y_norm[:, 1]):  
     if w >= 0.4:
        print(f"La persona número {i + 1} tiene riesgo con una probabilidad del {w * 100:.2f}%")
     else:
        print(f"La persona número {i + 1} no tiene riesgo")
        print("---------------------------------------------------------------------------------------")
def paquetes():
    try:
        db = pymysql.connect(
        host= "localhost",
        user= "root",
        passwd= "1234",
        database="transporte_logistica",
        port= 3307
        )
        print("conexion exitosa")
    except Exception as e:
        print("error al conectar:", e)

    cursor = db.cursor()

    query = """
    SELECT distancia_km, peso_kg, volumen_m3, tipo_vehiculo_id, trafico_id,condiciones_climaticas_id, tiempo_entrega_min
    FROM paquetes
    """

    cursor.execute(query)

    datos = cursor.fetchall()


    X = []
    y = []
    for i in datos:
        distancia = i[0]
        peso = i[1]
        volumen = i[2]
        tipo_vehiculo = i[3]
        trafico_id = i[4]
        condiciones_climaticas_id = i[5]
        tiempo = i[6]
        X.append([distancia, peso, volumen, tipo_vehiculo, trafico_id, condiciones_climaticas_id])
        y.append(tiempo)

    # print(X)
    # print(y)
    X_a = np.array(X)
    y_a = np.array(y)

    norm = StandardScaler()
    X_norm = norm.fit_transform(X_a)

    regresion = SGDRegressor(max_iter=1000)
    regresion.fit(X_norm,y_a)

    x_p = np.array ([
        [70, 6, 0.6, 2, 2, 2],
        [55, 5.5, 0.55, 2, 2, 2],
        [95, 9.5, 0.95, 3, 3, 3],
        [35, 3.5, 0.35, 1, 2, 1],
        [85, 8.5, 0.85, 2, 3, 2],
        [15, 1.5, 0.15, 1, 1, 1],
        [65, 6.5, 0.65, 2, 2, 2],
        [105, 10.5, 1.05, 3, 3, 3],
        [45, 4.5, 0.45, 1, 2, 1],
        [75, 7.5, 0.75, 2, 3, 2]
        
    ])
    x_p_n = norm.transform(x_p)

    y_pred = regresion.predict(x_p_n)

    print(y_pred)
    moto = """

    SELECT id, nombre FROM tipos_vehiculo

    """
    cursor.execute(moto)

    dm = cursor.fetchall()

    traf = """

    SELECT id, nivel from niveles_trafico

    """
    cursor.execute(traf)

    df = cursor.fetchall()

    condi = """

        SELECT id, condicion FROM condiciones_climaticas

    """
    cursor.execute(condi)
    dc = cursor.fetchall()
    print(y_pred)
    print(dc)
    xd = -1
    print("Predicciones De Tiempo de Entrega")
    print("----------------------------------")
    for w, k in enumerate(x_p):
     xd = xd + 1
    
     print(f"{w + 1}.Paquete {w+1}: {k[0]} km, {k[1]} kg, {k[2]} m³, Tipo de Vehiculo: {dm[int(k[3]-1)][1]}, Nivel de trafico: {df[int(k[4]-1)][1]}, Condicion climatica: {dc[int(k[5]-1)][1]}, Tiempo estimado:{y_pred[xd]:.2f} minutos ")

menu = 0
while menu <= 2:
   menu = int(input("seleccione la prediccion que desea realizar: \n1-Transporte logistica\n2-Diabetes\n3-Salir\nSu opcion ---->"))
   if menu == 1:
      paquetes()
   if menu == 2:
      diabetes()  
   if menu == 3:
      print("Gracias por usar el programa xdlol")
  

