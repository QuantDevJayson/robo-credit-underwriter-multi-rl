from fastapi import FastAPI
import pickle
import numpy as np
from stable_baselines3 import PPO, DQN
from pydantic import BaseModel
from risk_policy import risk_adjusted_approval

# Load Models
with open("credit_model.pkl", "rb") as f:
    model = pickle.load(f)

ppo_agent = PPO.load("ppo_credit_agent")
dqn_agent = DQN.load("dqn_risk_control_agent")  # 

app = FastAPI()

class CreditApplication(BaseModel):
    credit_score: int
    income: float
    debt_to_income: float
    age: int
    employment_years: int
    loan_amount: float
    interest_rate: float

@app.post("/predict/")
def predict_credit_risk(application: CreditApplication):
    features = np.array([[application.credit_score, application.income, application.debt_to_income, 
                          application.age, application.employment_years, application.loan_amount]])

    ml_prediction = model.predict(features)[0]
    ml_confidence = model.predict_proba(features)[0][ml_prediction]

    ppo_action, _ = ppo_agent.predict(features[0])
    dqn_action, _ = dqn_agent.predict(features[0])

    risk_aware_decision = risk_adjusted_approval(1 - ml_confidence, application.loan_amount, application.interest_rate)

    return {
        "ml_decision": "Approved" if ml_prediction == 1 else "Rejected",
        "ml_confidence": round(float(ml_confidence), 2),
        "ppo_decision": "Approved" if ppo_action == 1 else "Rejected",
        "dqn_risk_control": "Approved" if dqn_action == 1 else "Rejected",
        "risk_aware_decision": "Approved" if risk_aware_decision == 1 else "Rejected"
    }
