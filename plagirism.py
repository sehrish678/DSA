import re
import string 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """Preprocess text by removing punctuation, converting to lowercase, and removing stop words."""
    stop_words = set(["a", "an", "the", "is", "in", "on", "and", "or", "for", "to", "with", "of", "by"])
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove stop words
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def n_gram_similarity(doc1, doc2, n=3):
    """Calculate n-gram similarity between two documents."""
    def generate_ngrams(text, n):
        tokens = text.split()
        return set([' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)])

    ngrams1 = generate_ngrams(doc1, n)
    ngrams2 = generate_ngrams(doc2, n)

    intersection = len(ngrams1.intersection(ngrams2))
    union = len(ngrams1.union(ngrams2))
    return intersection / union if union > 0 else 0

def cosine_similarity_text(doc1, doc2):
    """Calculate cosine similarity between two documents."""
    vectorizer = CountVectorizer().fit_transform([doc1, doc2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0, 1]

def detect_plagiarism(documents):
    """Detect plagiarism in a list of documents."""
    results = []
    for i in range(len(documents)):
        for j in range(i + 1, len(documents)):
            doc1 = preprocess_text(documents[i])
            doc2 = preprocess_text(documents[j])
            ngram_score = n_gram_similarity(doc1, doc2)
            cosine_score = cosine_similarity_text(doc1, doc2)
            results.append({
                'Document 1': f'Document {i+1}',
                'Document 2': f'Document {j+1}',
                'N-gram Similarity': ngram_score,
                'Cosine Similarity': cosine_score
            })
    return results

# Example usage
documents = [
    "Plagiarism is the act of using someone else's work without proper credit.",
    "Using someone else's work without giving credit is considered plagiarism.",
    "Plagiarism detection systems help identify similar text in documents.",
    "This text is unrelated and talks about machine learning systems."
]

results = detect_plagiarism(documents)
# Print results
for result in results:
  print(result)
