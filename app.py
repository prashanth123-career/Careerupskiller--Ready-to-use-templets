import streamlit as st
from transformers import pipeline
import socket
import uuid

# Page config
st.set_page_config(page_title="AI Proposal Writer", page_icon="✍️", layout="centered")

# Load local T5 model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="t5-small")

generator = load_model()

# Initialize session
if 'proposal_count' not in st.session_state:
    st.session_state.proposal_count = 0
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'user_ip' not in st.session_state:
    try:
        st.session_state.user_ip = socket.gethostbyname(socket.gethostname())
    except:
        st.session_state.user_ip = "unknown"

# UI
st.title("✍️ AI Proposal Writer for Freelancers")
st.markdown("Win more clients with smart, customized proposals powered by AI.")

service_type = st.selectbox("Service Offered", ["AI Chatbot", "Web Development", "Marketing", "Other"])
client_project = st.text_area("📋 Paste the client's project description:")

MAX_FREE = 2

if st.button("Generate My Proposal"):
    if not client_project.strip():
        st.warning("Please paste a project description.")
    elif st.session_state.proposal_count >= MAX_FREE:
        st.error("🚫 You’ve used 2 free proposals.")

        st.markdown("### 💼 Upgrade for Unlimited Proposals")
        st.markdown("""
Choose a plan to unlock unlimited access:
- 🟢 ₹120/month (billed monthly)
- 🟣 ₹999 one-time payment for lifetime access

Get instant access to:
✅ Unlimited smart proposals  
✅ Fast response times  
✅ All future updates  
        """)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔓 Unlock Monthly Access (₹120)", key="monthly"):
                st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/JujI2Kao">', unsafe_allow_html=True)
        with col2:
            if st.button("💼 One-Time Payment (₹999)", key="onetime"):
                st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/KWPswOe9">', unsafe_allow_html=True)

    else:
        with st.spinner("Generating your proposal..."):
            prompt = f"Write a professional freelance proposal for a project about {client_project}. Service: {service_type}."
            output = generator(prompt, max_length=150, do_sample=False)[0]['generated_text']
            st.subheader("✅ Your Proposal")
            st.success(output)

            st.session_state.proposal_count += 1
            st.info(f"🎁 {MAX_FREE - st.session_state.proposal_count} free proposals left")

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

# Testimonials
st.markdown("---")
st.markdown("### What Our Users Say")
st.markdown("""
<div class="testimonial">
    <p><i>“The AI Freelancer Kit helped me double my income in just 3 months!” – Ahmed, Freelancer, UAE</i></p>
</div>
<div class="testimonial">
    <p><i>“The Detailed Career Plan gave me a clear path to follow and free courses to upskill!” – Priya, Student, India</i></p>
</div>
""", unsafe_allow_html=True)

# Custom CSS to hide Streamlit branding and show your footer
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .info-section {
        background: linear-gradient(90deg, #2AB7CA 0%, #1A3550 100%);
        color: white;
        padding: 10px;
        border-radius: 0 0 12px 12px;
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
    }
    .info-section a {
        color: white;
        text-decoration: none;
        margin: 0 8px;
    }
</style>

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
