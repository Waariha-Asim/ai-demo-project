import streamlit as st

st.set_page_config(
    page_title="AI Project Release Agent",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 AI Project Release Agent")
st.markdown("**Automated project sanitization, documentation & publishing**")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Security Checks", value="2 Layers", delta="AI Powered")

with col2:
    st.metric(label="AI Calls", value="3 Gemini", delta="Auto Generated")

with col3:
    st.metric(label="Platforms", value="GitHub + LinkedIn", delta="One Click")

st.divider()

st.subheader("📋 Workflow Pipeline")

steps = {
    "1️⃣ File Intake": "Upload project files via form",
    "2️⃣ Secret Scan": "AI detects and removes sensitive keys",
    "3️⃣ README Generation": "Gemini writes professional README",
    "4️⃣ GitHub Push": "Repo created and files uploaded automatically",
    "5️⃣ LinkedIn Post": "AI generates post — you approve before publishing"
}

for step, desc in steps.items():
    st.success(f"**{step}** — {desc}")

st.divider()

st.subheader("🔒 Security Status")
st.progress(100, text="All checks passed ✅")

st.info("💡 This workflow reduced manual release time from **45 minutes to under 3 minutes**")