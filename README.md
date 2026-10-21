Part C: Theory Questions

1. What is supervised machine learning?
Supervised learning is when we train a model using labeled data. The data has inputs(X) and correct outputs(y). The model learns the relationship between them so it can predict the output.For example, in this project,we gave hours studied and exam scores.

2. What is unsupervised machine learning?
Unsupervised learning is when we train a model using data with no labels where it finds hidden patterns, groups by itself. Example, in our customer project, we only gave spending and visits and the model had to find the 3 customer groups on its own.

3. Explain the difference between supervised and unsupervised learning.
- Supervised has labeled data (X and y) while unsupervised has only X.

- Supervised goal is to predict like we have done in the exam score while unsupervised goal is to group patterns.

- In supervised we can check accuracy while in unsupervised we check clusters.

- Supervised example is linear Regression while Unsupervised example is K-Means.

4. Why is Linear Regression considered supervised learning?
Because it learns from labeled data. We give it both the input (study hours) and the correct answer (exam score). It learns the line that best fits this labeled data to predict future scores.

5. Why is K-Means considered unsupervised learning?
Because it does not get any correct labels. We only give it customer data (spending, visits). It finds the clusters by grouping customers who are similar to each other without being told which group is correct.

6. What is the difference between fit() and predict()?
- fit() is for training. The model learns from the data. e.g. model.fit(x, y) or model.fit(scaled_data).
- predict() is for predicting.After training, we use it to predict new values e.g model.predict([[6]]) to predict score for 6 hours.

7. Give two real-world applications of supervised learning and two of unsupervised learning.
Supervised:
- Email spam detection - predicting if an email is spam or not.

- Student pass prediction - predicting if a student will pass or fail from hours studied.


Unsupervised:
- YouTube videos - grouping similar articles into topics e.g politics, sports, entertainment without being told the topic. Like YouTube grouping videos you watch.


- Music grouping - Music platforms e.g Spotify grouping similar songs into playlists without labels. It finds hidden patterns.