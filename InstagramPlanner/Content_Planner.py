import streamlit as st
import google.generativeai as genai
import re

# ===== 🔐 Set your Gemini API key here (keep it secret!) =====
api_key = "AIzaSyBUQqvP5o0Wf-25-Bi7Kb83soMi2Bm4vhU"  # Replace this with your actual key

# Configure Gemini
genai.configure(api_key=api_key)

# Load the Gemini model (Flash is cheaper/faster, Pro is deeper)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# ===== 🌟 Streamlit UI =====
st.title("📱 Instagram Content Planner using Gemini AI")
st.markdown("Generate content topic ideas for Reels or Carousels based on your niche.")

# User input
niche = st.text_input("🎯 Enter your niche (e.g., Fitness, Parenting, Stock Market)")

if niche:
    if st.button("🚀 Generate Content Topics"):
        with st.spinner("Thinking..."):
            prompt = f"Suggest 10 engaging Instagram content ideas for the '{niche}' niche. Make them useful for Reels or Carousels, and avoid long introductions or headings."

            response = model.generate_content(prompt)

            # ===== 🧹 Clean the response =====
            # Remove Gemini's intro paragraph
            response_text = re.split(r"\n1\.", response.text, maxsplit=1)
            if len(response_text) > 1:
                cleaned_text = "1." + response_text[1]  # Add back "1."
            else:
                cleaned_text = response.text

            # Extract only the numbered content blocks
            matches = re.findall(r"\d+\.\s+(.*?)(?=\n\d+\.|\Z)", cleaned_text.strip(), re.DOTALL)
            topics = [re.sub(r'\s+', ' ', topic.strip()) for topic in matches if topic.strip()]

            # ===== 📝 Display the cleaned topics =====
            if topics:
                st.subheader("📝 Content Topics")
                for i, topic in enumerate(topics, 1):
                    st.markdown(f"**{i}.** {topic}")
            else:
                st.warning("⚠️ Couldn’t parse any content topics from the response.")
