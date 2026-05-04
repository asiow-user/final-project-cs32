# ML Training for Hate Speech Detection
Welcome to our final project for CS32! Our project is a hate speech detector system that uses machine learning and a browser extension to moderate harmful content in real time. First, we started with an existing and labeled dataset. We cleaned this data and also normalized slang and abbreviations frequently used for hate speech. We also included additional synthetic training examples of both abusive and safe language patterns, so the model could be better at predicting what actual hate speech or just disagreement. Finally, after saving the model, we expose it through a Flask API. The model is then integrated into a browser extension that scans social media posts, sends this text to the backend for classification, and visually blurs harmful content.

## Explanation of our Files
- 'app.py'- creates a Flask server that connects our trained machine learning model to the browser extension. The goal is that the extension sends the extracted text to our flask server, which will then send the text to our ML training model, resulting in the prediction of hate speech or not
- 'augment_data.py' -  the goal of this script is to improve our training model by creating additional sythetic training examples and appending them to our existing training CSV file.
- 'content.js' - this script runs inside the browser and scans social media posts, extracting the text from each post and sending it to our flask server for later classification. It also blurs the text in case it is hate speech.
- 'manifest.json': this script configures our browser extension, defining its name, version and required permissons. Is what allows our extesion to communicate with the flask server
- `preprocess.py` - Load and clean training data
- `train_baseline.py` - Train fast baseline model
- `train_bert.py` - Train high-accuracy BERT model
- `test_model.py` - Evaluate model performance
- `requirements.txt` - Python dependencies
- 
