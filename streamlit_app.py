import streamlit_app as st
from analyzer.fetcher import fetch_html
from analyzer.onpage import analyze_onpage
from analyzer.technical import analyze_technical
from analyzer.score import calculate_score
from analyzer.recommendation import generate_recommendations

st.set_page_config(
    page_title="SEO Analyzer",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 SEO Analyzer Tool")
st.write("Enter a website URL to analyze SEO performance and optimization tips.")

url = st.text_input("Website URL", placeholder="https://example.com")

if st.button("Analyze Website"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Analyzing website..."):
            html = fetch_html(url)

            if not html:
                st.error("Unable to fetch the website.")
            else:
                onpage = analyze_onpage(html)
                technical = analyze_technical(url)
                score = calculate_score(onpage, technical)
                recommendations = generate_recommendations(onpage, technical)

                st.success("Analysis Complete")

                st.metric("SEO Score", f"{score}/100")

                st.subheader("📊 On-Page SEO")
                st.json(onpage)

                st.subheader("⚙️ Technical SEO")
                st.json(technical)

                st.subheader("✅ Optimization Recommendations")
                for rec in recommendations:
                    st.write(f"- {rec}")
