# Final Project: Hate-Speech Detection 

## Introduction 
For our final project, we have decided to create a Social Media Moderator that would detect potential hate speech in user-generated text. With social media becoming a significant space for contemporary sociopolitical discourse, it felt important to us to create a project that would allow us to decrease discrimination, violence and hate for users. 

## Computational Steps for Final Project 
1. We will need to store and process social media posts to use as input data. The dataset can be created manually by scraping social media sites, or collected from publicly available sources.
2. We will then clean the raw text data. This will involve converting it to lowercase, removing punctuation and preparing it for analysis.
3. We will then extract important elements from the text, such as individual words, and use it to create or use a list of flagged or offensive keywords to compare against posts.
4. We will then develop a rule-based method to detect harmful language by checking if any flagged words appear in the text.
5. Additionally, we want to add sentiment analysis to adapt the model to more subtle or situational cases of hate speech. This would involve analyzing the overall tone of the text using sentiment scoring.
6. We'd combine keyword matches and sentiment score to assign a risk score to each post. If a post's risk score passes a certain threshold, we will label it as potentially harmful, and otherwise mark it as safe.
7. We will output the results to the user, showing the original post along with how our program has classified it, such as risk score or flagged keywords.

## ML Training for Hate Speech Detection
Welcome to our final project for CS32 with the latest updates! Our project is a hate speech detector system that uses machine learning and a browser extension to moderate harmful content in real time. First, we started with an existing and labeled dataset. We cleaned this data and also normalized slang and abbreviations frequently used for hate speech. We also included additional synthetic training examples of both abusive and safe language patterns, so the model could be better at predicting whether it was actual hate speech or just disagreement. Finally, after saving the model, we expose it through a Flask API. The model is then integrated into a browser extension that scans social media posts, sends this text to the backend for classification, and visually blurs harmful content.

## Explanation of our Files ##
'app.py'- creates a Flask server that connects our trained machine learning model to the browser extension. The goal is that the extension sends the extracted text to our Flask server, which will then send the text to our ML training model, resulting in the prediction of hate speech or not

'augment_data.py' - The goal of this script is to improve our training model by creating additional synthetic training examples and appending them to our existing training CSV file.

'content.js' - this script runs inside the browser and scans social media posts, extracting the text from each post and sending it to our Flask server for later classification. It also blurs the text in case it is hate speech.

'manifest.json': this script configures our browser extension, defining its name, version, and required permissions. Is what allows our extension to communicate with the Flask server

'preprocess.py' - Load and clean training data

'processed_data.csv - data cleaned and processed according to what we did in 'preprocess.py.'

'requirements.txt' Python dependencies

'slang_dict.py' normalizes slang and abbreviations that are considered harmful language by converting them into full, explicit forms

test_model.py` - Evaluate model performance

train_baseline.py - Train fast baseline model

train_bert.py - Train high-accuracy BERT model

'warner.txt' original dataset we cleaned and converted into a structured format for machine learning

'manifest.json' is very similar to the other manifest.json script, but now focuses on acting as a bridge between the browser extension and the Python backend, where our machine learning model is

'popup.html' is used to define the user interface of the extension

popup.js: This script should run when the user clicks the button in the extension popup. It should get the tab's URL, send it to the Python backend, and display the response in the pop-up.

## Development Setup
1. We used the GitHub Codespace to write, edit and run code.
3. We installed all the required Python packages using `pip install'. We detail all the packages we installed in the next heading.
4. We uploaded and managed our datasets locally before preprocessing and training models. The raw dataset (warner.txt) was first cleaned and structured using preprocess.py, producing processed_data.csv, which was then used for model training. We also used augment_data.py to generate additional synthetic examples and expand the dataset for better generalization.
5. The Flask backend (app.py) was run locally during development to connect the model with the Chrome extension.
6. The Chrome extension was loaded in Developer Mode. It consisted of: manifest.json for configuration and permissions, content.js for scanninh and extracting text from X, and popup.html and popup.js for the user interface.

## Packages Installed
We installed the following packages over the course of the development of the project. 
1. joblib: used for saving and loading trained machine learning models, allowed us to reuse the model in app.py without having to retrain it every single time
2. flask, from which we further imported Flask, request, jsonify: used for creating the web server, handle incoming data from the extension and convert Python dictionary into JSON Format to send a structured response back to the frontend
3. CORS: used to allow our backend to communicate with our frontend
4. pandas: which is a library that helps us work with structured data, allowed us to load training dataset
5. re: Python's regular expression module
6. from sklearn.model_selection, import train_test_split: used to split datasets into training and testing dataset
7. os: used to interact with the operating system
8. sys: used to provide access to system-specific parameters and functions
9. from sklearn.feature_extraction.text import TfidfVectorizer: used to convert text into numerical features using term frequency-inverse document frequency
10. from sklearn.linear_model import LogisticRegression: used to predict whether text can be classified as hate speech
11. from sklearn.metrics import classification_report, accuracy_score, confusion_matrix: used to evaluate how well our model performs
12. numpty: used for numerical computing


## References and Credits
We want to acknowledge the use of Generative AI, specifically Harvard's AI Sandbox, for this assignment. It assisted us in writing the code as well as the debugging. However, the brainstorming of the project workflow, the comments explaining the code and content in this ReadMe are all our original work. 

In addition, our dataset was taken from the following source. 
1. [Inducing a Lexicon of Abusive Words – a Feature-Based Approach](https://aclanthology.org/N18-1095/) (Wiegand et al., NAACL 2018)



