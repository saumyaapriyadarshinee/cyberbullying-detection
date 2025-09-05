import pandas as pd
import re
import nltk

# Download NLTK resources (only the first time)
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Function to clean text
def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    # Remove special characters/numbers
    text = re.sub(r"[^a-z\s]", "", text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)

# Function to load and preprocess dataset
def load_and_preprocess(path):
    df = pd.read_csv(path)
    print("📂 Loaded dataset with shape:", df.shape)
    # Clean the text column
    df["clean_text"] = df["text"].apply(clean_text)
    return df

if __name__ == "__main__":
    dataset_path = "../data/raw/sample_data.csv"
    df = load_and_preprocess(dataset_path)
    print(df.head())
