import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ==========================================
# 1. LOAD THE DATASET
# ==========================================
# For demonstration, here is a synthetic dataset.
# In your actual task, you will load your CSV file here.
# Example: df = pd.read_csv('phishing_dataset.csv')

data = {
    'email_text': [
        "URGENT: Your account has been compromised. Click http://secure-update-now.com to reset.",
        "Hey Sarah, are we still on for the marketing meeting at 2 PM?",
        "Congratulations! You've won a $1,000 Walmart gift card. Reply with your SSN to claim.",
        "Please find the attached invoice for last month's freelance work.",
        "Security Alert: Verify your banking details immediately at www.bank-verify-login.xyz",
        "Can you send over the final draft of the presentation by EOD?",
        "Free Bitcoin! Click here to double your crypto instantly!",
        "Thanks for the coffee today, let's catch up again next week."
    ],
    'label': ['Phishing', 'Safe', 'Phishing', 'Safe', 'Phishing', 'Safe', 'Phishing', 'Safe']
}

df = pd.DataFrame(data)

# Separate features (X) and target labels (y)
# Replace 'email_text' and 'label' with your actual dataset column names
X = df['email_text']
y = df['label']

# ==========================================
# 2. SPLIT THE DATA
# ==========================================
# Split the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. BUILD THE MACHINE LEARNING PIPELINE
# ==========================================
# A Pipeline links feature extraction and the classifier together.
# TfidfVectorizer: Extracts features (keywords, URLs) by converting text to word frequency weights.
# MultinomialNB: A Naive Bayes classifier, which is an industry standard for text/spam classification.

model_pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')), 
    ('classifier', MultinomialNB())
])

# ==========================================
# 4. TRAIN THE MODEL
# ==========================================
print("Training the model...")
model_pipeline.fit(X_train, y_train)

# ==========================================
# 5. PREDICT AND EVALUATE
# ==========================================
# Make predictions on the test set
y_pred = model_pipeline.predict(X_test)

# Calculate and display the Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n--- Model Evaluation ---")
print(f"Accuracy: {accuracy * 100:.2f}%\n")

# Generate the Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=model_pipeline.classes_)

# ==========================================
# 6. DISPLAY CONFUSION MATRIX
# ==========================================
# Visualize the confusion matrix for a professional expected outcome
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model_pipeline.classes_)
disp.plot(cmap=plt.cm.Blues)

plt.title("Phishing Detection Confusion Matrix")
plt.show()