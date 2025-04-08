import streamlit as st
from transformers import pipeline
import uuid

# --- Page Setup ---
st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

# --- Load Proposal Generation Model ---
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)

generator = load_model()

# --- Session State ---
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- Default Project Descriptions ---
default_projects = {
    "AI Chatbot": "I need an AI chatbot that can assist customers on my website, answer product-related questions, and provide support 24/7. It should handle both text and voice inputs and integrate with WhatsApp.",
    "Web Development": "I need a responsive website for my business that includes a homepage, about section, services page, contact form, and blog. The website should be mobile-friendly, SEO optimized, and fast-loading.",
    "Marketing": "I need a digital marketing strategy for my product launch, including social media ads, SEO, and email campaigns.",
    "UI/UX Design": "I need a user-friendly mobile app design with modern visuals and a seamless user experience.",
    "Data Analytics": "I want to build a dashboard that shows real-time insights into my sales and customer behavior.",
    "Other": ""
}

# --- UI Layout ---
st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Win more clients with smart, customized proposals powered by AI.")

# --- Service Selection ---
service_options = list(default_projects.keys())
selected_service = st.selectbox("🛠 Service Offered", service_options)

# Custom Service Input if "Other"
custom_service = ""
if selected_service == "Other":
    custom_service = st.text_input("Please specify your service:")
    final_service = custom_service.strip() if custom_service.strip() else "Custom Service"
else:
    final_service = selected_service

# --- Project Description Input ---
project_input = st.text_area("📋 Paste the client's project description (or leave blank to use our template):")

# Auto-fill with default if blank
if not project_input.strip() and selected_service != "Other":
    project_input = default_projects[selected_service]

# --- Generate Proposal ---
if st.button("Generate My Proposal"):
    if not final_service.strip():
        st.warning("⚠️ Please specify your service.")
    else:
        with st.spinner("Generating your smart proposal..."):
            prompt = f"""Write a detailed freelance proposal for the following project:

Service: {final_service}
Project Description: {project_input}
"""
            try:
                result = generator(prompt)[0]['generated_text']
                st.subheader("✅ Your Custom Proposal")
                st.success(result)
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")

# --- Promotional Section ---
st.markdown("---")
st.markdown("### 🚀 Boost Your Freelance Career")
st.markdown("""
Get the **AI Freelancer Kit** and **Detailed Career Plan** at amazing prices:

- ₹499 for the AI Freelancer Kit (ready-to-use templates)
- ₹199 for Career Counseling (jobs, salaries, skills)

Start today and change your future!
""")

col1, col2 = st.columns(2)
with col1:
    if st.button("🛠 AI Freelancer Kit (₹499)", key="freelancer_kit"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/t37swnF">', unsafe_allow_html=True)
with col2:
    if st.button("📊 Career Plan (₹199)", key="career_plan"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/FAsUJ9k">', unsafe_allow_html=True)

# --- Testimonials ---
st.markdown("---")
st.markdown("### ❤️ What Our Users Say")
st.markdown("""
<div class="testimonial">
    <p><i>“The AI Freelancer Kit helped me double my income in just 3 months!” – Ahmed, Freelancer, UAE</i></p>
</div>
<div class="testimonial">
    <p><i>“The Detailed Career Plan gave me a clear path to follow and free courses to upskill!” – Priya, Student, India</i></p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("🚀 Powered by CareerUpskillers | Transforming Freelancers into Winners")
