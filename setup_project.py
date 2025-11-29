import os

folders = [
    "data/raw", "data/interim", "data/processed",
    "notebooks",
    "src/data", "src/modeling", "src/nlp", "src/api", "src/app", "src/utils",
    "tests", "dashboards", "docker", ".github/workflows"
]

files = [
    "README.md", "requirements.txt", ".gitignore", "LICENSE",
    "src/__init__.py",
    "src/data/load_data.py", "src/data/clean_data.py", "src/data/feature_engineering.py",
    "src/modeling/train_model.py", "src/modeling/evaluate_model.py", "src/modeling/explainability.py",
    "src/nlp/text_cleaning.py", "src/nlp/sentiment_model.py", "src/nlp/intent_classifier.py",
    "src/api/main.py",
    "src/app/streamlit_app.py",
    "src/utils/config.py", "src/utils/helpers.py",
    "tests/test_data.py", "tests/test_model.py", "tests/test_api.py",
    "docker/Dockerfile",
    ".github/workflows/ci.yml"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Projet initialisé avec succès ! 🚀")
