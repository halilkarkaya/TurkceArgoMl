from django.shortcuts import render
import pickle
import os

def ml(request):
    skor = None
    sonuc = None

    if request.method == "POST":
        # Model ve Vektörleştirici yolları
        model_path = os.path.join("models", "text_classification_model.pkl")
        vectorizer_path = os.path.join("models", "vectorizer.pkl")

        # Modeli yükle
        if os.path.exists(model_path) and os.path.exists(vectorizer_path):
            with open(model_path, "rb") as model_file:
                model = pickle.load(model_file)

            with open(vectorizer_path, "rb") as vectorizer_file:
                vectorizer = pickle.load(vectorizer_file)

            mesaj = request.POST.get("mesaj", "")
            if mesaj:
                mesaj_vector = vectorizer.transform([mesaj]).toarray()
                sonuc = model.predict(mesaj_vector)[0]
                skor = model.predict_proba(mesaj_vector).max() * 100

    return render(request, "ml.html", {"sonuc": sonuc, "skor": skor})





