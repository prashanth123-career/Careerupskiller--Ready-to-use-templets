import streamlit as st
from transformers import pipeline
import uuid

# Page config
st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

# Load smarter proposal-writing model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)

generator = load_model()

# Session management
if 'proposal_count' not in st.session_state:
    st.session_state.proposal_count = 0
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

MAX_FREE = 2

# Default sample project briefs by service
default_projects = {
    "AI Chatbot": "I need an AI chatbot that can assist customers on my website, answer product-related questions, and provide support 24/7. It should handle both text and voice inputs, and integrate with WhatsApp.",
    "Web Development": "I need a responsive website for my business that includes a homepage, about section, services page, contact form, and blog. The website should be mobile-friendly, SEO optimized, and fast-loading.",
    "Marketing": "I need a digital marketing strategy for my product launch, including SEO, email marketing, and paid ads to drive conversions.",
    "UI/UX Design": "I want a user-friendly mobile app interface focused on smooth navigation and aesthetic appeal for both iOS and Android platforms.",
    "Data Analytics": "I need a dashboard that visualizes customer data, sales performance, and helps track key business KPIs in real-time.",
    "Other": ""
}

# --- UI ---
st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Win more clients with smart, customized proposals powered by AI.")

# Select service
services = list(default_projects.keys())
selected_service = st.selectbox("Service Offered", services)

# If "Other", allow custom input
custom_service = ""
if selected_service == "Other":
    custom_service = st.text_input("Enter your custom service name:")
    final_service = custom_service.strip() or "Custom Service"
else:
    final_service = selected_service

# Project description input or autofill
project_input = st.text_area("📋 Paste the client's project description (or leave blank to use default):")

if not project_input.strip() and selected_service != "Other":
    project_input = default_projects[selected_service]

# --- Proposal Generation ---
if st.button("Generate My Proposal"):
    if not final_service.strip():
        st.warning("Please enter a service name.")
    elif st.session_state.proposal_count >= MAX_FREE:
        st.error("🚫 You’ve used 2 free proposals.")
        st.markdown("### 💼 Upgrade for Unlimited Proposals")
        st.markdown("""
- 🟢 ₹120/month (billed monthly)  
- 🟣 ₹999 one-time payment for lifetime access  
        """)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔓 Monthly Access (₹120)", key="monthly"):
                st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/JujI2Kao">', unsafe_allow_html=True)
        with col2:
            if st.button("💼 Lifetime Access (₹999)", key="onetime"):
                st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/KWPswOe9">', unsafe_allow_html=True)
    else:
        with st.spinner("Generating your proposal..."):
            prompt = f"Write a detailed and professional freelance proposal for the following project:\n\nService: {final_service}\nProject Description: {project_input}"
            try:
                output = generator(prompt, do_sample=False)[0]['generated_text']
                st.subheader("✅ Your Proposal")
                st.success(output.strip())
                st.session_state.proposal_count += 1
                st.info(f"🎁 {MAX_FREE - st.session_state.proposal_count} free proposals left.")
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")

# --- Promo Section ---
st.markdown("---")
st.markdown("### 🚀 Boost Your Freelance Career")
st.markdown("""
Get the **AI Freelancer Kit** and **Detailed Career Plan** at amazing prices:

- ₹499 for the AI Freelancer Kit (ready-to-use templates)
- ₹199 for Career Counseling (jobs, salaries, skills)

Get access now and grow your freelance journey!
""")

col1, col2 = st.columns(2)
with col1:
    if st.button("🛠 AI Freelancer Kit (₹499)", key="freelancer_kit"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/t37swnF">', unsafe_allow_html=True)
with col2:
    if st.button("📊 Career Plan (₹199)", key="career_plan"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/FAsUJ9k">', unsafe_allow_html=True)
