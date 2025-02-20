API_URL = "http://127.0.0.1:8000/predict/"

st.title("AI Robo-Credit Underwriter (Multi-Agent RL)")

inputs = {k: st.sidebar.slider(k, v[0], v[1], v[2]) for k, v in 
         {"Credit Score": (300, 850, 700), "Income ($)": (20000, 150000, 50000), 
          "Debt-to-Income Ratio": (0.1, 0.9, 0.3), "Age": (21, 70, 35), 
          "Employment Years": (0, 40, 5), "Loan Amount ($)": (5000, 50000, 20000), 
          "Interest Rate (%)": (1, 15, 5)}.items()}

if st.sidebar.button("Submit"):
    payload = {k.lower().replace(" ", "_"): v for k, v in inputs.items()}
    payload["interest_rate"] /= 100
    res = requests.post(API_URL, json=payload).json()

    for key, value in res.items():
        st.success(f"{key}: **{value}**")
