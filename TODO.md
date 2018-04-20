## Goal
Create a function that returns 'blocks' of processed twitter data distilled
into a feature vector / class vector based on some time interval across our
given dataset:

```[Sentiment Score, Retweet Score, Change in Price]```

Now we have a new dataset that uses two feature values to predict a target
value, which is easily fed to one of our many algorithms from this semester.
This can be expounded upon by making further insights on the data: 

- lag / lead time in change of market values vs. 'block' time in twitter data
- gathering large samples of cryptocurrency values and taking the second
  derivative of the approx. function rather than just the first
- having mismatched sizes on the time interval of tweets vs. crypto change
