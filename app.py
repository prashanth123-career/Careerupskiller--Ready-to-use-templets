import streamlit as st
from transformers import pipeline
import uuid

# --- Page Setup ---
st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

# --- Load Stable, Compatible Model ---
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small", max_length=512)

generator = load_model()

# --- Session Setup ---
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- Default Project Descriptions ---
default_projects = {
    "AI Chatbot": "I need an AI chatbot that can assist customers on my website, answer product-related questions, and provide support 24/7. It should handle both text and voice inputs and integrate with WhatsApp.",
    "Web Development": "I need a responsive website for my business that includes a homepage, about section, services page, contact form, and blog. The website should be mobile-friendly, SEO optimized, and fast-loading.",
    "Marketing": "I need a social media marketing expert to manage and grow my business presence on platforms like Instagram, Facebook, and LinkedIn. The goal is to increase brand awareness, engagement, and lead generation. The strategy should include content creation, scheduling posts, running paid ad campaigns, and monthly performance reports.",
    "UI/UX Design": "I need a user-friendly mobile app design with modern visuals and a seamless user experience.",
    "Data Analytics": "I want to build a dashboard that shows real-time insights into my sales and customer behavior.",
    "Other": ""
}

# --- UI ---
st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Create smart, ready-to-send freelance proposals in seconds with AI.")

# --- Select Service ---
service_options = list(default_projects.keys())
selected_service = st.selectbox("🛠 Service Offered", service_options)

# Custom Service
custom_service = ""
if selected_service == "Other":
    custom_service = st.text_input("Please specify your service:")
    final_service = custom_service.strip() if custom_service.strip() else "Custom Service"
else:
    final_service = selected_service

# Project Description
project_input = st.text_area("📋 Paste the client's project description (or leave blank to use our template):")

# Use default if blank
if not project_input.strip() and selected_service != "Other":
    project_input = default_projects[selected_service]

# --- Generate Proposal ---
if st.button("Generate My Proposal"):
    if not final_service.strip():
        st.warning("⚠️ Please specify your service.")
    else:
        with st.spinner("Creating your smart proposal..."):
            prompt = f"""
Act as a professional freelancer on Upwork. Write a complete freelance proposal for the following service and project:

Service: {final_service}
Client's Project Description: {project_input}

Include:
- Greeting
- A strong intro about you
- Your understanding of their problem
- What you’ll deliver
- How you’ll help
- A nice closing with a call to action

Make the proposal clear, friendly, and ready to copy-paste into Upwork or Fiverr.
"""
            try:
                result = generator(prompt)[0]['generated_text']
                st.subheader("✅ Your Custom Proposal")
                st.success(result)
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")

# --- Promo Section ---
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
st.caption("🚀 Powered by CareerUpskillers | Helping Freelancers Win Clients with AI")
