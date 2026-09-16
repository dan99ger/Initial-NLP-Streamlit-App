from transformers import pipeline

# 1. تحميل نموذج جاهز لتحليل المشاعر
classifier = pipeline("sentiment-analysis")

# 2. نص للتجربة
texts = [
    "I absolutely love working with Machine Learning and AI!",
    "The deployment process was very confusing and frustrating."
]

# 3. تشغيل النموذج ورؤية النتائج
results = classifier(texts)

for text, result in zip(texts, results):
    print(f"\nText: {text}")
    print(f"Label: {result['label']} | Score: {result['score']:.4f}")