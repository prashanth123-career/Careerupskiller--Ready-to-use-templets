import streamlit as st
from transformers import pipeline
import uuid

st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="tiiuae/falcon-1b-instruct", max_length=512, do_sample=True)

generator = load_model()

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

default_projects = {
    "AI Chatbot": "I need an AI chatbot that can assist customers on my website, answer product-related questions, and provide support 24/7. It should handle both text and voice inputs and integrate with WhatsApp.",
    "Web Development": "I need a responsive website for my business that includes a homepage, about section, services page, contact form, and blog. The website should be mobile-friendly, SEO optimized, and fast-loading.",
    "Marketing": "I need a social media marketing expert to manage and grow my business presence on platforms like Instagram, Facebook, and LinkedIn. The strategy should include content creation, scheduling posts, running paid ad campaigns, and monthly performance reports.",
    "UI/UX Design": "I need a user-friendly mobile app design with modern visuals and a seamless user experience.",
    "Data Analytics": "I want to build a dashboard that shows real-time insights into my sales and customer behavior.",
    "Other": ""
}

st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Create smart, ready-to-send freelance proposals in seconds with AI.")

service_options = list(default_projects.keys())
selected_service = st.selectbox("🛠 Service Offered", service_options)

custom_service = ""
if selected_service == "Other":
    custom_service = st.text_input("Please specify your service:")
    final_service = custom_service.strip() if custom_service.strip() else "Custom Service"
else:
    final_service = selected_service

project_input = st.text_area("📋 Paste the client's project description (or leave blank to use our template):")

if not project_input.strip() and selected_service != "Other":
    project_input = default_projects[selected_service]

if st.button("Generate My Proposal"):
    if not final_service.strip():
        st.warning("⚠️ Please specify your service.")
    else:
        with st.spinner("Creating your smart proposal..."):
            prompt = f"""Write a professional freelance proposal for the following service and project.

Service: {final_service}
Project Description: {project_input}

Include: greeting, brief intro about you, your understanding of their problem, your solution, deliverables, and a friendly closing.
"""
            try:
                result = generator(prompt, max_new_tokens=300)[0]['generated_text']
                cleaned = result.replace(prompt, "").strip()
                st.subheader("✅ Your Custom Proposal")
                st.success(cleaned)
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")
