# robo-credit-underwriter-multi-rl

### Optimized AI Robo-Credit Underwriter with Multi-Agent RL & Risk-Aware Learning

**Outline:** <br>
This project implements an AI-powered credit underwriting system that leverages machine learning (ML) and reinforcement learning (RL) to optimize loan approval decisions while managing risk. It includes:<br>

(i) ML-Based Credit Risk Prediction (Random Forest)<br>
(ii) Reinforcement Learning Agents (PPO & DQN) for dynamic decision-making<br>
(iii) FastAPI Server for real-time loan application processing<br>
(iv) Risk-Aware Decision Model for enhanced financial risk management<br>

#### Model Training Details 

**a) ML Model (Credit Scoring)** <br>
- Algorithm: Random Forest<br>
- Features Used: Credit Score, Income, Debt-to-Income Ratio, Age, Employment Years, Loan Amount<br>
- Output: Approval Decision (1 = Approved, 0 = Rejected)<br>

**b) Reinforcement Learning Agents** <br>
- PPO (Proximal Policy Optimization) → Focuses on optimizing long-term rewards<br>
- DQN (Deep Q-Networks) → Handles risk control in loan approvals<br>
- Custom OpenAI Gym Environment simulates credit applications<br>

**c) Risk-Aware Decision Policy** <br>
- Combines ML & RL to make more informed approval decisions<br>
- Incorporates Risk Factors such as loan amount & interest rates<br>
- Prevents High-Risk Lending through reinforcement learning penalties<br>

#### Running the FastAPI Server
After training the models, start the API:  uvicorn api:app --reload

**Future Enhancements** <br>
✅ Expand dataset with real-world financial data <br>
✅ Improve model interpretability with SHAP values<br>
✅ Deploy on AWS/GCP with real-time transaction processing<br>

----------------------------------------------------------------------------

**Tech Stack:**
- *ML*: Scikit-Learn (Random Forest)<br>
- *RL*: Stable-Baselines3 (PPO, DQN)<br>
- *API*: FastAPI<br>
- *Backtesting & Simulation*: OpenAI Gym<br>

----------------------------------------------------------------------------

🚀 Ready to transform credit underwriting with AI? Let's go! 🎯
