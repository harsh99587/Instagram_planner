import streamlit as st
import google.generativeai as genai

# --- CONFIGURE GEMINI ---
GEMINI_API_KEY = "AIzaSyBUQqvP5o0Wf-25-Bi7Kb83soMi2Bm4vhU"  # 🔒 Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# --- STREAMLIT UI ---
st.set_page_config(page_title="Instagram Content Planner", page_icon="📱")
st.title("📱 Instagram Content Planner using Gemini AI")

st.markdown("Enter your niche and get AI-generated content ideas for Reels or Carousels.")

# --- NICHE INPUT ---
niche = st.text_input("🎯 Enter your Niche (e.g., Fitness, Parenting, Finance)")

# --- GENERATE TOPICS ---
if niche and st.button("Generate Content Topics"):
    with st.spinner("Generating content ideas..."):
        prompt = f"Suggest 10 engaging Instagram content ideas for the '{niche}' niche. Each idea should be suitable for either Reels or Carousels, and explain how it can be used effectively."

        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(prompt)

        # Format and display output
        st.subheader("📝 Content Topics")
        for i, line in enumerate(response.text.strip().split("\n"), 1):
            line = line.strip()
            if line and not line.startswith(str(i) + "."):
                line = f"{i}. {line}"
            st.markdown(f"**{line}**")
