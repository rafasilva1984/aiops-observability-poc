
from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

# Sample data simulation
data = pd.DataFrame({
    "cpu_usage": [10, 12, 13, 11, 90, 95, 10, 12],
    "memory_usage": [30, 32, 31, 29, 85, 87, 32, 31]
})

model = IsolationForest(contamination=0.1)
model.fit(data)

predictions = model.predict(data)
data["anomaly"] = predictions

print(data)

# Save the model
joblib.dump(model, "model.joblib")
