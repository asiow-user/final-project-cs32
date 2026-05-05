# ML Training for Hate Speech Detection
Welcome to our final project for CS32! Our project is a hate speech detector system that uses machine learning and a browser extension to moderate harmful content in real time. First, we started with an existing and labeled dataset. We cleaned this data and also normalized slang and abbreviations frequently used for hate speech. We also included additional synthetic training examples of both abusive and safe language patterns, so the model could be better at predicting whether it was actual hate speech or just disagreement. Finally, after saving the model, we expose it through a Flask API. The model is then integrated into a browser extension that scans social media posts, sends this text to the backend for classification, and visually blurs harmful content. Finally, we would like to point out that we have used AI (ChatGPT) to guide us on how to build the machine learning and the extension portion of our final project. The in-class knowledge was limited to the scope of this project, and using AI to help us with those more complex tasks, while understanding why we were using it was of great help.

## Explanation of our Files
- 'app.py'- creates a Flask server that connects our trained machine learning model to the browser extension. The goal is that the extension sends the extracted text to our Flask server, which will then send the text to our ML training model, resulting in the prediction of hate speech or not
- 'augment_data.py' - The goal of this script is to improve our training model by creating additional synthetic training examples and appending them to our existing training CSV file.
- 'content.js' - this script runs inside the browser and scans social media posts, extracting the text from each post and sending it to our Flask server for later classification. It also blurs the text in case it is hate speech.
- 'manifest.json': this script configures our browser extension, defining its name, version, and required permissions. Is what allows our extension to communicate with the Flask server
- `preprocess.py` - Load and clean training data
- 'processed_data.csv - data cleaned and processed according to what we did in 'preprocess.py.'
- 'requirements.txt' Python dependencies
- 'slang_dict.py' normalizes slang, abbreviations that are considered harmful language by converting them into full, explicit forms
- test_model.py` - Evaluate model performance
- `train_baseline.py` - Train fast baseline model
- `train_bert.py` - Train high-accuracy BERT model
- 'warner.txt' original dataset we cleaned and converted into a structured format for machine learning
- 'manifest.json' is very similar to the other manifest.json script, but now focuses on acting as a bridge between the browser extension and the Python backend, where our machine learning model is
- 'popup.html' used to define the user interface of the extension.
- popup.js: This script should run when the user clicks the button in the extension popup. It should get the tab's URL, send it to the Python backend, and display the response in the popup.
- 'content.js' 
