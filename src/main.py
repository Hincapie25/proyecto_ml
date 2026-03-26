import pandas as pd
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score

# Crear carpeta outputs si no existe
os.makedirs("outputs", exist_ok=True)

# =========================
# 📊 Cargar datos
# =========================
df = pd.read_csv("data/sdss_sample.csv")

# =========================
# 🤖 CLASIFICACIÓN (KNN)
# =========================
X = df[['u','g','r','i','z']]
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# =========================
# 📈 REGRESIÓN
# =========================
X_reg = df[['u','g','r','i','z']]
y_reg = df['redshift']

reg_model = LinearRegression()
reg_model.fit(X_reg, y_reg)

y_pred_reg = reg_model.predict(X_reg)

mse = mean_squared_error(y_reg, y_pred_reg)
r2 = r2_score(y_reg, y_pred_reg)

# =========================
# 🔵 CLUSTERING
# =========================
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_reg)

df['cluster'] = clusters

# =========================
# 📊 GRÁFICA
# =========================
plt.figure()
plt.scatter(df['u'], df['g'], c=df['cluster'])
plt.title("Clusters")
plt.xlabel("u")
plt.ylabel("g")
plt.savefig("outputs/clusters.png")

# =========================
# 💾 GUARDAR MÉTRICAS
# =========================
with open("outputs/metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy}\n")
    f.write(f"Matriz de Confusión:\n{conf_matrix}\n\n")
    f.write(f"MSE: {mse}\n")
    f.write(f"R2: {r2}\n")

print("✅ Proceso terminado correctamente")
print("📁 Resultados guardados en /outputs")