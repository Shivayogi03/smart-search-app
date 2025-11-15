from django.shortcuts import render, redirect
from .models import Document
from .extractor import extract_text
from .embedding import embed, load_vector
from numpy import dot
from numpy.linalg import norm
import json

# Cosine similarity function
def cosine_score(q, d):
    return dot(q, d) / (norm(q) * norm(d) + 1e-10)


def upload_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        text = extract_text(file)  # Extract text from uploaded file
        embedding = embed(text)

        # Convert list to bytes before saving
        embedding_bytes = json.dumps(embedding).encode()

        Document.objects.create(file=file, text=text, embedding=embedding_bytes)
        return redirect('search')

    return render(request, 'upload.html')


def search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        docs = Document.objects.all()
        query_vec = embed(query)

        scored = []
        for doc in docs:
            doc_vec = load_vector(doc.embedding)  # Converts bytes → np.array
            similarity = cosine_score(query_vec, doc_vec)
            scored.append((doc, similarity))

        # Sort by highest similarity
        results = sorted(scored, key=lambda x: x[1], reverse=True)

    return render(request, 'search.html', {
        'query': query,
        'results': results
    })


def home(request):
    return render(request, 'home.html')
