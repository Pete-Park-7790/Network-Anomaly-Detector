import pandas as pd
import joblib
import time

print("\n=== REAL-TIME THREAT SCANNER ===\n")
print("1. Waking up the AI and loading its brain...")

try:
    ai_model = joblib.load('ai_brain.pkl')
    time.sleep(1)
    print("Brain loaded Successfully!!\n")
except FileNotFoundError:
    print("Error: 'ai_brain.pkl' not found. Please run analyzer.py first to train the AI.")
    exit()

print("2. Loading new, unseen network traffic...")
df = pd.read_csv('####TEST FILE####', header=None)
numeric_data = df.select_dtypes(include=['number']).fillna(0)
time.sleep(1)

print("3. Scanning traffic for threats...")
df['Anomaly_Score']= ai_model.predict(numeric_data)
time.sleep(2)

print("4. Filtering results...")
anomalies=df[df['Anomaly_Score'] == -1]
time.sleep(2)
print(f"Done! Out of {len(df)} NEW connections, the AI flagged {len(anomalies)} as suspicious.\n")

print("5. Exporting incident report...")
anomalies.to_csv('live_threats_caught.csv', index=False)
time.sleep(1)
print("Security scan complete. Check 'live_threats_caught.csv' for details.")

