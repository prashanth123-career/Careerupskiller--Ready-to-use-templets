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
st.title("✍️ AI Proposal Writer (Free Version)")
st.markdown("Only 2 free proposals per session. Upgrade for unlimited access.")

service_type = st.selectbox("Service Offered", ["AI Chatbot", "Web Development", "Marketing", "Other"])
client_project = st.text_area("📋 Paste client's project description:")

MAX_FREE = 2

if st.button("Generate My Proposal"):
    if not client_project.strip():
        st.warning("Please paste a project description.")
    elif st.session_state.proposal_count >= MAX_FREE:
        st.error("🚫 You've used 2 free proposals.")
        st.markdown("### 💼 Upgrade for Unlimited Proposals")
        st.markdown("""
        ✅ ₹599/month  
        ✅ Instant smart proposals  
        ✅ Time-saving templates  
        ✅ One-time payment

        """)
        if st.button("🛒 Upgrade Now (₹599)"):
            st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/r/your-link">', unsafe_allow_html=True)
    else:
        with st.spinner("Generating your proposal..."):
            prompt = f"Write a professional freelance proposal for a project about {client_project}. Service: {service_type}."
            output = generator(prompt, max_length=150, do_sample=False)[0]['generated_text']
            st.subheader("✅ Your Proposal")
            st.success(output)

            st.session_state.proposal_count += 1
            st.info(f"🎁 {MAX_FREE - st.session_state.proposal_count} free proposals left")
