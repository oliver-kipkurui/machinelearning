from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

customers = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],  
    [3000, 4]
]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(customers)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(scaled_data)

labels = model.labels_

for i, cluster in enumerate(labels, start=1):
    print(f"Customer {i} belongs to cluster {cluster}")

print("\n--- Total customers in each cluster ---")
unique, counts = np.unique(labels, return_counts=True)
for cluster_id, count in zip(unique, counts):
    print(f"Cluster {cluster_id}: {count} customers")

# Bonus
plt.scatter([c[0] for c in customers], [c[1] for c in customers], c=labels, cmap='Set1', s=100)
plt.xlabel('Monthly Spending (KES)')
plt.ylabel('Monthly Visits')
plt.title('Customer Segmentation')
plt.savefig('unsupervised_result.png')
#plt.show()