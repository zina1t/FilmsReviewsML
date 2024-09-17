from django.shortcuts import render
from django.http import JsonResponse
from .forms import ReviewForm
import joblib

# Load pre-trained models
vectorizer = joblib.load('/workspaces/FilmsReviewsML/tfidf_vectorizer.pkl')
model = joblib.load('/workspaces/FilmsReviewsML/logistic_regression_model.pkl')

def predict_sentiment(review_text):
    # Transform review using the vectorizer
    review_transformed = vectorizer.transform([review_text])
    
    # Predict sentiment using the loaded ML model
    sentiment = model.predict(review_transformed)[0]
    
    # Map prediction to sentiment and rating
    if sentiment == 1:
        rating = 8  # Example: positive reviews get a higher rating
        sentiment_label = 'positive'
    else:
        rating = 3  # Example: negative reviews get a lower rating
        sentiment_label = 'negative'
    
    return sentiment_label, rating

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data['review']
            sentiment, rating = predict_sentiment(review)
            
            # Return the result as a JSON response
            return JsonResponse({
                'review': review,
                'sentiment': sentiment,
                'rating': rating
            })
    else:
        form = ReviewForm()
    
    return render(request, 'review/submit_review.html', {'form': form})
