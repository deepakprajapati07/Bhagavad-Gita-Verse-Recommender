import streamlit as st
from processing import recommend

st.title("Bhagavad Gita Verse Recommender System")
user_input = st.text_area("Enter some text/keywords (in english only for best results)", "")

options = {
    'English': 'eng',
    'Hindi': 'hin'
}
lang = st.radio(
    "Choose the output language",
    list(options.keys())
)

if st.button('Recommend'):
    recommended_data = recommend(user_input, output_lang=options[lang])

    # Display recommended data
    if recommended_data:
        st.header("Recommended Verses")
        for data in recommended_data:
            st.subheader(f"{data['chapter']}, {data['verse']}")
            st.markdown(f"<div style='background-color: #2B2B2B; color: yellow; padding: 10px; border-radius: 5px; margin-bottom: 10px'>{data['shlokha']}</div>", unsafe_allow_html=True)
            if data['lang'] == 'eng':
                st.markdown("**English Translation**")
                st.write(f"{data['eng_translation']}")
                st.markdown("**English Meaning**")
                st.write(f"{data['eng_meaning']}")
            elif data['lang'] == 'hin':
                st.markdown("**Hindi Translation**")
                st.write(f"{data['hin_translation']}")
                st.markdown("**Hindi Meaning**")
                st.write(f"{data['hin_meaning']}")
            st.markdown("---")
