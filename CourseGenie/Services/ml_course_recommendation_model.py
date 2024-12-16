# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Create the Dataset
data = {
    "profile": [
        # Matching profiles for each course
        "AI beginner exploring fundamentals",  # AI Fundamentals+
        "Understanding AI basics for beginners",
        "Starting with AI principles and core concepts",
        "Learning AI applications from scratch",
        "Analyzing data trends and AI insights",  # AI Data+
        "Mining knowledge with AI tools",
        "Building AI-based data analytics pipelines",
        "AI-powered data analysis for businesses",
        "Exploring generative AI techniques",  # AI Gen+
        "Understanding AI models like GPT",
        "Creating content with generative AI",
        "AI-driven creativity and solutions",
        "Learning machine learning and deep learning models",  # AI Deep+
        "Mastering neural networks and ML algorithms",
        "Building deep learning projects",
        "Exploring supervised and unsupervised learning",
        "Ensuring ethical and responsible AI practices",  # AI Responsible+
        "Implementing fairness and bias detection in AI",
        "Developing safe and responsible AI systems",
        "Learning ethical AI frameworks",
        # Non-matching examples
        "Designing web applications with React",
        "Building blockchain solutions",
        "Learning cloud infrastructure",
        "Becoming a cybersecurity specialist",
    ],
    "related_course": [
        # Labels for matching profiles
        "AI Fundamentals+",
        "AI Fundamentals+",
        "AI Fundamentals+",
        "AI Fundamentals+",
        "AI Data+",
        "AI Data+",
        "AI Data+",
        "AI Data+",
        "AI Gen+",
        "AI Gen+",
        "AI Gen+",
        "AI Gen+",
        "AI Deep+",
        "AI Deep+",
        "AI Deep+",
        "AI Deep+",
        "AI Responsible+",
        "AI Responsible+",
        "AI Responsible+",
        "AI Responsible+",
        # Non-matching profiles (optional for diversity)
        "None",
        "None",
        "None",
        "None",
    ],
}

df = pd.DataFrame(data)

# Step 2: Preprocess Data
X = df["profile"]  # Features (text data)
y = df["related_course"]  # Labels (course names)

# Convert Text to Numerical Features using TF-IDF
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Encode Course Labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y_encoded, test_size=0.2, random_state=42
)

# Step 4: Train the Model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("\nClassification Report:")
# print(
#     classification_report(
#         y_test,
#         y_pred,
#         labels=list(range(len(label_encoder.classes_))),  # All encoded labels
#         target_names=label_encoder.classes_,
#     )
# )

# new_profiles = [
#     "Learning ethical AI development",
#     "Building deep learning models and neural networks",
#     "Analyzing business data with AI tools",
#     "Exploring generative AI for creative solutions",
#     "Experienced AI professional focused on the fundamentals of Artificial Intelligence, building foundational models and training AI systems.",
# ]
# new_profiles_tfidf = vectorizer.transform(new_profiles)
# predictions = model.predict(new_profiles_tfidf)
# predicted_courses = label_encoder.inverse_transform(predictions)


# for profile, course in zip(new_profiles, predicted_courses):
#     print(f"Profile: {profile} -> Recommended Course: {course}")


def predict_course(
    profile_text, vectorizer=vectorizer, model=model, label_encoder=label_encoder
):
    # Transform the input text using the fitted TF-IDF vectorizer
    profile_tfidf = vectorizer.transform([profile_text])

    # Predict the label using the trained model
    prediction = model.predict(profile_tfidf)

    # Decode the predicted label back to the course name
    predicted_course = label_encoder.inverse_transform(prediction)[0]

    return predicted_course


# Example Usage
profile_text = "Building deep learning models and neural networks"
recommended_course = predict_course(profile_text)
print(f"Profile: {profile_text} -> Recommended Course: {recommended_course}")
