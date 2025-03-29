import streamlit as st
import openai

# Streamlit page config
st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

# Load OpenAI API key
openai.api_key = st.secrets["API_KEY"]

# App Header
st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Win more clients with smart, customized proposals powered by AI.")

# Service Selection
service_type = st.selectbox("What service are you offering?", [
    "AI Chatbot", "Web Development", "Data Analysis", "Social Media Marketing", "Other"
])

# Project Description Input
client_project = st.text_area("📋 Paste the client’s project description from Upwork/Fiverr:")

# Generate Proposal Button
if st.button("Generate My Proposal"):
    if not client_project.strip():
        st.warning("Please paste a project description first.")
    else:
        with st.spinner("Writing your proposal..."):
            prompt = f"""
You are an expert freelancer. Based on the following client project description, write a professional, personalized proposal tailored for {service_type}. Make it friendly, confident, and persuasive. Mention relevant skills, suggest how you'll solve their problem, and include a short CTA at the end.

Client Project:
\"\"\"{client_project}\"\"\"
"""
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.7
            )
            proposal = response.choices[0].message.content.strip()
            st.subheader("✅ Your Proposal")
            st.success(proposal)

# Upsell Section
st.markdown("---")
st.markdown("### 🔥 Want Ready-to-Use Proposal Templates?")
st.markdown("""
Boost your chances with our ₹499 Proposal Kit:
- 50+ Copy-Paste Proposals for AI, Web Dev, and more
- Price Calculator & Bonus Freelancer Checklist
- PDF + Google Docs format

👉 Perfect for Upwork, Fiverr, Freelancer.com

""")
if st.button("🛒 Get the Proposal Kit (₹499)"):
    st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/r/yourpaymentlink">', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ by CareerUpskillers")
