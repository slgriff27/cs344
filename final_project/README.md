# Amazon Electronics Reviews Classification

Amazon Electronics Reviews Classification is an application for classifying electronics reviews as positive, neutral, or negative.

## Installation

In order to run this file, you must have keras, pandas, sklearn, tokenizer, numpy, and matplotlib installed.

## Usage

The first file, movieReviews.ipynb, is a fully functional version of a sentiment analysis based on chapter 3.5 in the book Deep Learning with Python. You may simply run each code block in this one without any further instructions.

The second file, AmazonReviews.ipynb, is not fully functional. You will only be able to run the first few code blocks before you get to vectorizing the data. From then on out, it will not work since the dataset could not be trimmed down to 10,000 most frequently used words. As for loading the dataset from the internet, there are two ways you can do it. One is keeping the code as is in the first code block and pulling it from the internet. The other option would be to download the file onto your local machine from http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz. This may or may not go faster when you run the program.
