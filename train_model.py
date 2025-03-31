import pickle
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Veriyi oku
splits = {'train': 'train.csv'}
df = pd.read_csv("hf://datasets/Toygar/turkish-offensive-language-detection/" + splits["train"])

# Metni temizle
df["text"] = df["text"].str.lower()
for i in string.punctuation:
    df['text'] = df['text'].str.replace(i, " ")

# Stopwords listesi
stopwords = ['fakat', 'lakin', 'ancak', 'acaba', 'ama', 'aslında', 'az', 'bazı', 'belki']
for s in stopwords:
    df['text'] = df['text'].str.replace(" " + s + " ", " ")

# Vektörleştirme
cv = CountVectorizer(max_features=1000)
x = cv.fit_transform(df["text"]).toarray()
y = df["label"]

# Veriyi böl
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=19)

# Modeli oluştur ve eğit
rf = RandomForestClassifier(n_estimators=5)
model = rf.fit(x_train, y_train)

# Modeli kaydet
with open("shop/models/text_classification_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("shop/models/vectorizer.pkl", "wb") as vec_file:
    pickle.dump(cv, vec_file)

print("Model başarıyla kaydedildi!")
