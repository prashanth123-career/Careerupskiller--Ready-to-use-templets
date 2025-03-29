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
# --- Promotional Section ---
st.markdown("""
<div class="promo-section">
    <h2>Unlock Your Freelancer Success: Use AI Tools, Strategic Plans, and Free Learning Resources for a Career Transformation! 🚀✨</h2>
    <p>Discover More and Share Your Dreams!</p>
    <h3>3 Steps to Enhance Your Freelance Journey:</h3>
    <ul>
        <li>1. Use our AI Freelancer Kit for ready-to-use templates and tools.</li>
        <li>2. Get our Detailed Career Plan for market insights and strategies.</li>
        <li>3. Leverage our free video links to expand your skills.</li>
    </ul>
    <p><strong>Free Ready-to-Use Chatbot Script Included!</strong></p>
    <p>Join 3,000+ happy buyers around the globe! Get a ₹10,000 worth AI Starter Tool for just ₹499 and receive free AI career counseling. For detailed career counseling, pay only ₹199 to get market insights, skills to upskill, salary comparisons, and companies to apply to.</p>
    <p>Follow the kit and start earning – don’t only rely on jobs as it’s uncertain! Just spend 8 hours on a weekend and start a new earning stream. Half of our students have quit their jobs within six months of purchasing!</p>
</div>
""", unsafe_allow_html=True)

# Purchase Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Purchase AI Freelancer Kit (₹499)", key="emailpromo_freelancer"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/t37swnF">', unsafe_allow_html=True)
with col2:
    if st.button("Purchase Detailed Career Plan (₹199)", key="emailpromo_career"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/FAsUJ9k">', unsafe_allow_html=True)
st.markdown("### What Our Users Say")
st.markdown("""
<div class="testimonial">
    <p><i>“The AI Freelancer Kit helped me double my income in just 3 months!” – Ahmed, Freelancer, UAE</i></p>
</div>
<div class="testimonial">
    <p><i>“The Detailed Career Plan gave me a clear path to follow and free courses to upskill!” – Priya, Student, India</i></p>
</div>
""", unsafe_allow_html=True)
# Footer with Branding, Privacy, and Social Links
# Custom CSS to hide Streamlit elements and show branding
st.markdown("""
<style>
    /* Hide default Streamlit header and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom top branding section */
    .info-section {
        background: linear-gradient(90deg, #2AB7CA 0%, #1A3550 100%);
        color: white;
        padding: 10px;
        border-radius: 0 0 12px 12px;
        text-align: center;
        margin-bottom: 20px;
        font-size: 14px;
    }
    .info-section a {
        color: white;
        text-decoration: none;
        margin: 0 8px;
    }
</style>

<!-- Top Branding Bar -->
<div class="info-section">
    © 2025 CareerUpskillers |
    <a href="https://www.careerupskillers.com/about-1">About Us</a> |
    <a href="https://www.careerupskillers.com/about-1">Privacy</a> |
    <a href="https://wa.me/917892116728">Call/WhatsApp</a> |
    <a href="https://www.youtube.com/@Careerupskillers">YouTube</a> |
    <a href="https://www.facebook.com/share/18gUeR73H6/">Facebook</a> |
    <a href="https://www.linkedin.com/company/careerupskillers/">LinkedIn</a> |
    <a href="https://www.instagram.com/careerupskillers?igsh=YWNmOGMwejBrb24z">Instagram</a>
</div>
""", unsafe_allow_html=True)


