import random
from hyperion_decision_engine.prediction_engine import predict_future_cpu

print("\n🔵 AURUM Autonomous Financial Risk System Started...\n")

# ----------------------------------
# STEP 1 — Simulated Financial Inputs
# ----------------------------------
transaction_volume = random.randint(50, 500)
login_attempts = random.randint(10, 100)
network_activity = random.randint(100, 1000)

print(f"📊 Incoming Data → Transactions:{transaction_volume}, Logins:{login_attempts}, Network:{network_activity}")

# ----------------------------------
# STEP 2 — Helios-style Detection
# ----------------------------------
anomaly_detected = transaction_volume > 400 or login_attempts > 80

if anomaly_detected:
    print("🚨 Helios Detection Engine: Anomaly Detected!")
else:
    print("✅ Helios Detection Engine: System Normal")

# ----------------------------------
# STEP 3 — Hyperion Prediction
# ----------------------------------
predicted_cpu = predict_future_cpu()
if predicted_cpu is None:
    predicted_cpu = 50

print(f"🔮 Predicted System Stress Level: {predicted_cpu}")

# ----------------------------------
# STEP 4 — AURUM Risk Engine (Unified)
# ----------------------------------
risk_score = 0

if anomaly_detected:
    risk_score += 40

risk_score += predicted_cpu * 0.5
risk_score += (transaction_volume / 10)

print(f"⚖️ Final Financial Risk Score: {risk_score:.2f}")

# ----------------------------------
# STEP 5 — Autonomous Decision Engine
# ----------------------------------
if risk_score > 120:
    decision = "FREEZE SUSPICIOUS TRANSACTIONS"
elif risk_score > 80:
    decision = "TRIGGER ALERT & MONITOR"
else:
    decision = "SYSTEM NORMAL"

print(f"🧠 Decision Engine: {decision}")

# ----------------------------------
# STEP 6 — Action Execution
# ----------------------------------
if "FREEZE" in decision:
    print("⚡ Action: Transactions Temporarily Frozen")
elif "ALERT" in decision:
    print("📢 Action: Admin Alert Sent")
else:
    print("🟢 Action: No intervention needed")

print("\n🟢 AURUM Cycle Complete.\n")
