import pandas as pd
from sklearn.ensemble import IsolationForest
import time
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

print("=== AI TRAINING FACILITY ===\n")
print("\n1.Loading the Dataset....\n")
df = pd.read_csv('traffic.txt', header=None)
time.sleep(1)
print(f"Successfully loaded {len(df)} network records\n")

print("2.Here is a peek of you data....\n")
time.sleep(1.5)
print(df.head())


print("\n3.Preparing data for AI....\n")
time.sleep(1)
numeric_data = df.select_dtypes(include=['number'])
numeric_data = numeric_data.fillna(0)

print("4.Waking up the AI (Isolation Forest)....\n")
ai_model= IsolationForest(contamination=0.05, random_state=42)
time.sleep(1)

print("Training the AI....\n")
df['Anomaly_Score'] = ai_model.fit_predict(numeric_data)
time.sleep(1)

print("Filtering results....\n")
anomalies = df[df['Anomaly_Score'] == -1]
time.sleep(1)

print(f"5.Done!! Out of {len(df)}, the AI flagged {len(anomalies)} as suspicious.\n")
time.sleep(2)

print("6. SAVING THE AI'S BRAIN...\n")
joblib.dump(ai_model, 'ai_brain.pkl')
time.sleep(1)
print("Success! 'ai_brain.pkl' has been generated. The AI is ready for deployment.")




