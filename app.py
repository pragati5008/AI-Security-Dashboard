import plotly.express as px
from analysis_history import add_record, get_history
import pandas as pd
import streamlit as st

from url_features import extract_features
from risk_engine import calculate_risk

st.set_page_config(
    page_title="AI Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Security Dashboard")

st.markdown("---")

url = st.text_input("🔗 Enter URL")

if st.button("Analyze URL"):

    features = extract_features(url)

    risk_score = calculate_risk(features)
    add_record(url, risk_score)

    st.subheader("Risk Analysis")

    st.progress(risk_score / 100)

    st.metric("Risk Score", f"{risk_score}%")

    if risk_score < 30:
        st.success("✅ Low Risk")

    elif risk_score < 70:
        st.warning("⚠️ Medium Risk")

    else:
        st.error("🚨 High Risk")

    st.subheader("Extracted Features")

    st.json(features)
    st.markdown("---")

st.subheader("Analysis History")

history = get_history()
total_urls = len(history)

total_threats = len(
    [item for item in history if item["Risk Score"] >= 40]
)
col1, col2 = st.columns(2)

with col1:
    st.metric("URLs Analyzed", total_urls)

with col2:
    st.metric("Threats Detected", total_threats)

if history:
    st.dataframe(pd.DataFrame(history))
if history:

    safe_count = len(
        [item for item in history if item["Risk Score"] < 40]
    )

    threat_count = len(
        [item for item in history if item["Risk Score"] >= 40]
    )

    fig = px.pie(
        names=["Safe", "Threat"],
        values=[safe_count, threat_count],
        title="Safe vs Threat URLs"
    )

    st.plotly_chart(fig, use_container_width=True)
if history:

    csv = pd.DataFrame(history).to_csv(index=False)

    st.download_button(
        label="📥 Download Security Report",
        data=csv,
        file_name="security_report.csv",
        mime="text/csv"
    )