🌸 Iris Flower Classification - Machine Learning & Streamlit Dashboard
Overview

This project demonstrates machine learning classification on the classic Iris dataset, predicting the species of iris flowers based on their sepal and petal measurements. The project also includes an interactive Streamlit dashboard for live predictions and model performance visualization.

##🚀 Features

1.Live Prediction
    Users can input sepal and petal measurements via sliders.
    Instant prediction of iris species: Setosa, Versicolor, or Virginica.

2.Model Performance Dashboard
    Accuracy Score: Displays the model’s overall prediction accuracy.
    Confusion Matrix: Visualizes correct and incorrect classifications for each species.
    Feature Importance (Permutation): Shows which features (sepal/petal length and width) most influence the model’s predictions.

3.Trained Model
    The trained Random Forest model is saved as a .pkl file for fast loading.
    Label encoding is also saved for consistent predictions.

##🛠️ Technologies & Libraries

Python 3.x
Machine Learning: scikit-learn
Data Handling: pandas, numpy
Visualization: matplotlib, seaborn
Web App: Streamlit
Model Persistence: pickle

📁 Project Structure
iris/
│
├── iris_app.py              # Streamlit dashboard for live prediction & model visualization
├── iris_cleaned.csv         # Cleaned Iris dataset
├── iris_model.pkl           # Trained Random Forest model
├── label_encoder.pkl        # Saved LabelEncoder for species
├── Iris_Classification.ipynb # Notebook for model training & evaluation
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation


##🧪 How It Works
1.Data Preprocessing
    Cleaned the dataset (iris_cleaned.csv), normalized column names.
    Encoded the species labels into numeric form for training.

2.Model Training
    Used Random Forest Classifier.
    Evaluated accuracy and confusion matrix.
    Saved trained model and label encoder using pickle.

3.Dashboard
    Loads trained model and encoder.
    Provides live predictions.
    Displays performance metrics and feature importance interactively.

##📝 Author
    Swetha Suresh
    Email: swethasuresh1905@gmail.com
    GitHub: https://github.com/swethasuresh1903