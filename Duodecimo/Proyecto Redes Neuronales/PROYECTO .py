import tensorflow as tf
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import cifar10
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Flatten
import os

train_data = tf.keras.preprocessing.image_dataset_from_directory(
    "C:/Users/CTPLAB5/Downloads/dataset/train",
    image_size=(224, 224),
    batch_size=32
)

print(train_data)

X = []
y = []

for x_batch, y_batch in train_data:
    X.append(x_batch.numpy())
    y.append(y_batch.numpy())

X = np.concatenate(X)
y = np.concatenate(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,   # 20% para test
    random_state=42
)

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])
modelo1 = Sequential([
    data_augmentation,  

    tf.keras.layers.Rescaling(1./255, input_shape=(224,224,3)),

    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.BatchNormalization(), 
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(3)
])
modelo1.compile(
        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        optimizer = tf.keras.optimizers.Adam(0.0001)
    )

modelo1.fit(X_train, y_train, epochs=50)



prediccion_modelo1 = modelo1.predict(X_test)
prediccion_modelo1 = tf.nn.softmax(prediccion_modelo1)
aciertos = 0
for i in range(len(y_test)):
    if np.argmax(prediccion_modelo1[i]) == y_test[i]:
        aciertos += 1 
precision_modelo = (aciertos / len(y_test)) *100
print(f"La precisión del modelo es de {precision_modelo:.2f}%")


idx = 0
img = X_test[idx]            
label_real = y_test[idx]    


img_input = np.expand_dims(img, axis=0)  


pred = modelo1.predict(img_input)
pred_clase = np.argmax(tf.nn.softmax(pred))


plt.imshow(img.astype("uint8"))  
plt.title(f"Real: {label_real} - Predicción: {pred_clase}")
plt.axis("off")
plt.show()


clases = ["clase1", "clase2", "clase3"]

def cargar_imagen(ruta):
    img = tf.keras.utils.load_img(ruta, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) 
    return img_array

carpeta = "C:/Users/CTPLAB5/Downloads/ndataset/nuevas_imagenes"

for archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, archivo)

    try:
        img = cargar_imagen(ruta)
        img_input = np.expand_dims(img, axis=0)

        pred = modelo1.predict(img_input)
        pred = tf.nn.softmax(pred)

        clase_predicha = np.argmax(pred)
        confianza = np.max(pred)

        plt.imshow(img.astype("uint8"))
        plt.title(f"{archivo} → {clases[clase_predicha]} ({confianza*100:.2f}%)")
        plt.axis("off")
        plt.show()

    except Exception as e:
        print(f"Error con {archivo}: {e}")
print(X.shape)
print(y.shape)

