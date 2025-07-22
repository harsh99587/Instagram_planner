import streamlit as st
import google.generativeai as genai

# Set your API key directly (⚠️ Not secure for public repos)
api_key = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=api_key)

st.set_page_config(page_title="Instagram Content Planner", page_icon="📱")
st.title("📱 Instagram Content Planner using Gemini AI")

niche = st.text_input("🎯 Enter your Niche (e.g., Fitness, Stock Market, Parenting)")

if niche:
    if st.button("Generate Content Topics"):
        with st.spinner("Generating content ideas..."):
            prompt = f"Suggest 10 engaging Instagram content ideas for the '{niche}' niche. Make them useful for reels or carousels."
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            
            st.subheader("📝 Content Topics")
            for i, line in enumerate(response.text.strip().split("\n"), 1):
                clean_line = line.strip().lstrip("0123456789. ").strip("- ")
                if clean_line:
                    st.markdown(f"**{i}.** {clean_line}")
