import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="مُحلل النصوص الذكي", page_icon="🧠")

st.title("🧠 مُحلل النصوص الذكي (Sentiment Analyzer)")
st.write("يقوم هذا التطبيق بتحليل مشاعر النصوص باللغة الإنجليزية وتحديد مستوى الثقة باستعمال Hugging Face.")

st.divider()

user_input = st.text_area(
    "أدخل النص باللغة الإنجليزية للتحليل:", 
    value="Machine Learning and AI are transforming the tech industry rapidly!",
    height=140
)

if st.button("🚀 تحليل النص الآن", use_container_width=True):
    if user_input.strip():
        with st.spinner("جاري تحليل النص..."):
            try:
                # استخدام نموذج تحليل المشاعر المباشر
                classifier = pipeline("sentiment-analysis")
                result = classifier(user_input)[0]
                
                label = result['label']
                score = result['score']
                
                st.divider()
                if label == "POSITIVE":
                    st.success(f"🎉 **النتيجة:** إيجابي ({label}) | **نسبة الثقة:** {score*100:.2f}%")
                else:
                    st.error(f"⚠️ **النتيجة:** سلبي ({label}) | **نسبة الثقة:** {score*100:.2f}%")
            except Exception as e:
                st.error(f"حدث خطأ أثناء المعالجة: {e}")
    else:
        st.warning("يرجى كتابة نص أولاً.")