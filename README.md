# A Python based Chatbot using NLTK

### To install virtual environment

```
python -m venv venv
mkdir venv
source venv/bin/activate
```

### Downloading and installing NLTK

Install NLTK run 
```pip install nltk```

Test installation: run python then type import nltk
For platform-specific instructions, read here.

### Installing NLTK Packages

import NLTK and run nltk.download().
This will open the NLTK downloader from where you can choose the corpora and models to download. You can also download all packages at once.

### Term Frequency

It is a scoring of the frequency of the word in the current document.
```
TF = (Number of times term t appears in a document)/(Number of terms in the document)
```

### Inverse Document Frequency: is a scoring of how rare the word is across documents.

```
IDF = 1+log(N/n), where, N is the number of documents 
and n is the number of documents a term t has appeared in.
```
Tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus

Example:

Consider a document containing 100 words wherein the word ‘phone’ appears 5 times.
The term frequency (i.e., tf) for phone is then (5 / 100) = 0.05. 

Now, assume we have 10 million documents and the word phone appears in one thousand of these. Then, the inverse document frequency (i.e., IDF) is calculated as 

log(10,000,000 / 1,000) = 4

Thus, the Tf-IDF weight is the product of these quantities: 0.05 * 4 = 0.20.

Tf-IDF can be implemented in scikit learn as:

```
from sklearn.feature_extraction.text import TfidfVectorizer
```

### Cosine Similarity

TF-IDF is a transformation applied to texts to get two real-valued vectors in vector space. We can then obtain the Cosine similarity of any pair of vectors by taking their dot product and dividing that by the product of their norms. That yields the cosine of the angle between the vectors. Cosine similarity is a measure of similarity between two non-zero vectors. Using this formula we can find out the similarity between any two documents d1 and d2.

```
Cosine Similarity (d1, d2) =  Dot product(d1, d2) / ||d1|| * ||d2||
where d1,d2 are two non zero vectors.
```

### Corpus

For our example,we will be using the Wikipedia page for chatbots as our corpus. Copy the contents from the page and place it in a text file named ‘chatbot.txt’. However, you can use any corpus of your choice.

### Conclusion

Though it is a very simple bot with hardly any cognitive skills, its a good way to get into NLP and get to know about chatbots.Though ‘ROBO’ responds to user input. Thank you.

