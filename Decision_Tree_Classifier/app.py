import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Bank Marketing Intelligence Dashboard",
    page_icon="🏦",
    layout="wide"
)

model = joblib.load("bank_marketing_decision_tree.pkl")

st.markdown("""
<style>
.main {padding-top:1rem;}
.title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
}
.subtitle {
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🏦 Bank Marketing Intelligence Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Decision Tree Classifier | UCI Bank Marketing Dataset</p>', unsafe_allow_html=True)

st.divider()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Model Accuracy","89.5%")
c2.metric("Features","16")
c3.metric("Algorithm","Decision Tree")
c4.metric("Dataset","UCI Bank")

st.sidebar.header("📋 Customer Information")

age = st.sidebar.number_input("Age",18,100,30)

job = st.sidebar.selectbox("Job",[
"admin.","blue-collar","entrepreneur","housemaid",
"management","retired","self-employed","services",
"student","technician","unemployed","unknown"
])

marital = st.sidebar.selectbox("Marital Status",
["divorced","married","single"])

education = st.sidebar.selectbox("Education",
["primary","secondary","tertiary","unknown"])

default = st.sidebar.selectbox("Credit Default",
["no","yes"])

housing = st.sidebar.selectbox("Housing Loan",
["no","yes"])

loan = st.sidebar.selectbox("Personal Loan",
["no","yes"])

balance = st.sidebar.number_input("Account Balance",value=1000)

st.sidebar.header("📞 Campaign Information")

contact = st.sidebar.selectbox("Contact Type",
["cellular","telephone","unknown"])

month = st.sidebar.selectbox("Month",
["apr","aug","dec","feb","jan","jul","jun","mar","may","nov","oct","sep"])

day = st.sidebar.number_input("Day of Contact",1,31,15)
duration = st.sidebar.number_input("Call Duration (seconds)",value=200)
campaign = st.sidebar.number_input("Campaign Contacts",value=1)
pdays = st.sidebar.number_input("Days Since Previous Contact",value=-1)
previous = st.sidebar.number_input("Previous Contacts",value=0)

poutcome = st.sidebar.selectbox(
    "Previous Campaign Outcome",
    ["failure","other","success","unknown"]
)

job_map={"admin.":0,"blue-collar":1,"entrepreneur":2,"housemaid":3,"management":4,"retired":5,"self-employed":6,"services":7,"student":8,"technician":9,"unemployed":10,"unknown":11}
marital_map={"divorced":0,"married":1,"single":2}
education_map={"primary":0,"secondary":1,"tertiary":2,"unknown":3}
yes_no_map={"no":0,"yes":1}
contact_map={"cellular":0,"telephone":1,"unknown":2}
month_map={"apr":0,"aug":1,"dec":2,"feb":3,"jan":4,"jul":5,"jun":6,"mar":7,"may":8,"nov":9,"oct":10,"sep":11}
poutcome_map={"failure":0,"other":1,"success":2,"unknown":3}

feature_importance = pd.DataFrame({
    "Feature":[
        "age","job","marital","education","default","balance","housing",
        "loan","contact","day","month","duration","campaign","pdays",
        "previous","poutcome"
    ],
    "Importance":model.feature_importances_
}).sort_values(by="Importance", ascending=False)

st.subheader("Customer Subscription Prediction")

if st.button("🔍 Predict Subscription", use_container_width=True):

    input_df = pd.DataFrame({
        'age':[age],
        'job':[job_map[job]],
        'marital':[marital_map[marital]],
        'education':[education_map[education]],
        'default':[yes_no_map[default]],
        'balance':[balance],
        'housing':[yes_no_map[housing]],
        'loan':[yes_no_map[loan]],
        'contact':[contact_map[contact]],
        'day':[day],
        'month':[month_map[month]],
        'duration':[duration],
        'campaign':[campaign],
        'pdays':[pdays],
        'previous':[previous],
        'poutcome':[poutcome_map[poutcome]]
    })

    prediction = model.predict(input_df)[0]

    confidence = 100
    if hasattr(model, "predict_proba"):
        confidence = max(model.predict_proba(input_df)[0]) * 100

    st.divider()
    st.subheader("🎯 Prediction Result")

    rc1, rc2 = st.columns([2,1])

    with rc1:
        if prediction == 1:
            st.success("✅ Customer is likely to subscribe.")
        else:
            st.error("❌ Customer is unlikely to subscribe.")

    with rc2:
        st.metric("Confidence", f"{confidence:.2f}%")

    st.divider()

    st.subheader("📋 Customer Summary")

    summary = pd.DataFrame({
        "Attribute":["Age","Job","Marital","Education","Balance"],
        "Value":[age,job,marital,education,balance]
    })

    st.dataframe(summary, use_container_width=True)

st.divider()

st.subheader("📊 Top Features Influencing Prediction")
st.bar_chart(feature_importance.set_index("Feature"))

st.divider()

st.subheader("📌 Project Information")

st.markdown("""
**Model:** Decision Tree Classifier

**Dataset:** UCI Bank Marketing Dataset

**Objective:** Predict whether a customer will subscribe to a term deposit.

**Technologies Used**
- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib
""")

st.divider()
st.caption("Developed by Prathama Debnath | B.Tech AIML | SRM University")
