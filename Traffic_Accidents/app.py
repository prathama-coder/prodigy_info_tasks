import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Traffic Accident Analysis Dashboard",
    page_icon="🚦",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("traffic_accidents.csv")
    return df

df = load_data()

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("""
<h1 style='text-align:center;color:#00BFFF;'>
🚦 Traffic Accident Analysis Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:gray;'>
Weather • Road Conditions • Injury Severity • Contributing Factors
</h4>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.header("Filters")

weather_options = sorted(
    df["weather_condition"].astype(str).unique()
)

selected_weather = st.sidebar.multiselect(
    "Weather Condition",
    weather_options,
    default=["CLEAR"] if "CLEAR" in weather_options else weather_options[:3]
)

filtered_df = df[
    df["weather_condition"].astype(str).isin(selected_weather)
]

# -------------------------------------------------
# KPI SECTION
# -------------------------------------------------
st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Accidents",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Weather Types",
        filtered_df["weather_condition"].nunique()
    )

with col3:
    st.metric(
        "Crash Causes",
        filtered_df["prim_contributory_cause"].nunique()
    )

with col4:
    st.metric(
        "Road Conditions",
        filtered_df["roadway_surface_cond"].nunique()
    )

st.divider()

# -------------------------------------------------
# WEATHER CONDITIONS
# -------------------------------------------------
st.subheader("🌦 Weather Conditions")

weather_counts = (
    filtered_df["weather_condition"]
    .value_counts()
    .head(10)
    .reset_index()
)

weather_counts.columns = ["Weather", "Count"]

fig1 = px.bar(
    weather_counts,
    x="Weather",
    y="Count",
    color="Count",
    title="Top Weather Conditions During Accidents"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# ROAD CONDITIONS
# -------------------------------------------------
st.subheader("🛣 Road Surface Conditions")

road_counts = (
    filtered_df["roadway_surface_cond"]
    .value_counts()
    .head(10)
    .reset_index()
)

road_counts.columns = ["Road Condition", "Count"]

fig2 = px.bar(
    road_counts,
    x="Road Condition",
    y="Count",
    color="Count",
    title="Road Surface Conditions"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# ACCIDENTS BY HOUR
# -------------------------------------------------
st.subheader("⏰ Accidents by Hour")

fig3 = px.histogram(
    filtered_df,
    x="crash_hour",
    nbins=24,
    title="Accident Distribution by Hour"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------
# ACCIDENTS BY DAY
# -------------------------------------------------
st.subheader("📅 Accidents by Day of Week")

day_counts = (
    filtered_df["crash_day_of_week"]
    .value_counts()
    .sort_index()
    .reset_index()
)

day_counts.columns = ["Day", "Count"]

fig4 = px.line(
    day_counts,
    x="Day",
    y="Count",
    markers=True,
    title="Accidents Across Week"
)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------
# ACCIDENTS BY MONTH
# -------------------------------------------------
st.subheader("🗓 Accidents by Month")

month_counts = (
    filtered_df["crash_month"]
    .value_counts()
    .sort_index()
    .reset_index()
)

month_counts.columns = ["Month", "Count"]

fig5 = px.bar(
    month_counts,
    x="Month",
    y="Count",
    color="Count",
    title="Monthly Accident Distribution"
)

st.plotly_chart(fig5, use_container_width=True)

# -------------------------------------------------
# TOP CAUSES
# -------------------------------------------------
st.subheader("⚠ Top Contributing Factors")

cause_counts = (
    filtered_df["prim_contributory_cause"]
    .value_counts()
    .head(10)
    .reset_index()
)

cause_counts.columns = ["Cause", "Count"]

fig6 = px.bar(
    cause_counts,
    x="Cause",
    y="Count",
    color="Count",
    title="Top 10 Causes of Accidents"
)

st.plotly_chart(fig6, use_container_width=True)

# -------------------------------------------------
# CRASH TYPES
# -------------------------------------------------
st.subheader("🚗 Most Common Crash Types")

crash_counts = (
    filtered_df["crash_type"]
    .value_counts()
    .head(10)
    .reset_index()
)

crash_counts.columns = ["Crash Type", "Count"]

fig7 = px.bar(
    crash_counts,
    x="Crash Type",
    y="Count",
    color="Count",
    title="Most Common Crash Types"
)

st.plotly_chart(fig7, use_container_width=True)

# -------------------------------------------------
# INJURY SEVERITY
# -------------------------------------------------
st.subheader("🚑 Injury Severity Distribution")

injury_counts = (
    filtered_df["most_severe_injury"]
    .value_counts()
    .reset_index()
)

injury_counts.columns = ["Injury", "Count"]

fig8 = px.pie(
    injury_counts,
    names="Injury",
    values="Count",
    title="Injury Severity Distribution"
)

st.plotly_chart(fig8, use_container_width=True)

# -------------------------------------------------
# INSIGHTS
# -------------------------------------------------
st.subheader("📌 Key Insights")

st.success(
    f"Most Common Weather Condition: {filtered_df['weather_condition'].mode()[0]}"
)

st.info(
    f"Peak Accident Hour: {filtered_df['crash_hour'].mode()[0]}:00"
)

st.warning(
    f"Leading Accident Cause: {filtered_df['prim_contributory_cause'].mode()[0]}"
)

# -------------------------------------------------
# DOWNLOAD BUTTON
# -------------------------------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_accidents.csv",
    mime="text/csv"
)

# -------------------------------------------------
# DATASET PREVIEW
# -------------------------------------------------
with st.expander("📁 View Dataset"):

    st.dataframe(filtered_df.head(50))

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("""
---
### 👩‍💻 Project Information

**Project:** Traffic Accident Analysis Dashboard

**Tools Used**
- Python
- Pandas
- Plotly
- Streamlit

**Objective**
Analyze accident patterns based on:
- Weather Conditions
- Road Conditions
- Time of Day
- Contributing Factors

Built for Data Analytics Portfolio & GitHub Showcase.
""")