# Final Project: Hate-Speech Detection 

## Introduction 
For our final project, we have decided to create a Social Media Moderator that would detect potential hate speech in user-generated text. With social media becoming a significant space for contemporary sociopolitical discourse, it felt important to us to create a project that would allow us to decrease discrimination, violence and hate for users. 

## Computational Steps for Final Project 
1. We will need to store and process social media posts to use as input data. The dataset can be created manually by scraping social media sites, or collected from publicly available sources.
2. We will then clean the rawe text data. This will involve converting it to lowercase, removing punctuation and preparing it for analysis.
3. We will then extract important elements from the text, such as individual words, and use it to create or use a list of flagged or offensive keywords to compare against posts.
4. We will then develop a rule-based method to detect harmful language by checking if any flagged words appear in the text.
5. Additionally, we want to add sentiment analysis to adapt the model to more subtle or situational cases of hate speech. This would involve analyzing the overall tone of the text using sentiment scoring.
6. We'd combine keyword matches and sentiment score to assign a risk score to each post. If a post's risk score passes a certain threshold, we will label it as potentially harmful, and otherwise mark it as safe.
7. We will output the results to the user, showing the original post along with how our program has classified it, such as risk score or flagged keywords. 
