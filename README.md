# Smart Search - Semantic Document Search

A web application that allows users to upload documents (PDF, DOCX, TXT) and perform **semantic search** to find relevant content quickly. Built with **Django**, **NumPy**, and simple text embeddings for semantic similarity.

---

## 🔹 Features

- Upload multiple documents in **PDF, DOCX, TXT** formats.
- Automatically extract text from uploaded files.
- Generate embeddings for documents and queries.
- Perform **semantic search** using cosine similarity.
- Display search results with file names and content snippets.
- Simple and clean UI for quick interaction.

---

## 🔹 Tech Stack

- **Backend:** Python 3.14, Django 5.2
- **Frontend:** HTML/CSS (Django Templates)
- **Libraries:**
  - `numpy` – for vector operations
  - `PyPDF2` or `pdfplumber` – for PDF text extraction
  - `python-docx` – for DOCX text extraction
- **Database:** SQLite (default Django DB)

---

## 🔹 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/smart-search-app.git
   cd smart-search-app
2.Create a virtual environment

python -m venv myenv
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # macOS/Linux


3.Install dependencies

pip install -r requirements.txt
pip install pdfplumber python-docx  # For PDF/DOCX support


4.Apply migrations

python manage.py makemigrations
python manage.py migrate


5.Run the development server

python manage.py runserver


6.Access the app
Open your browser at http://127.0.0.1:8000

🔹 Usage

Upload Documents
Go to the Upload page and upload PDF, DOCX, or TXT files. The text will be extracted and stored.

Search Documents
Enter a query in the Search page. Results are ranked by semantic similarity with a snippet preview.

🔹 Project Structure
knowsearch/
├── core/
│   ├── views.py
│   ├── models.py
│   ├── extractor.py
│   └── embedding.py
├── knowsearch/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── upload.html
│   ├── search.html
│   └── home.html
├── media/            # Uploaded files
├── manage.py
└── requirements.txt

🔹 Demo

# KnowSearch - Smart Document Search

A Django-based web app for uploading and searching documents with semantic search.

## Live Demo

Check out the live demo here: [https://smart-search-app-1.onrender.com](https://smart-search-app-1.onrender.com)

---

## Features

- Upload PDF, DOCX, TXT files
- Search documents with semantic embeddings
- View search results with similarity scores

Example search results:

Smart Search
4_Oracle_Database_11g_PLSQL_Fundamentals_PLSQL.pdf (0.498)
documents/requirements.txt (0.309)

🔹 Future Improvements

Replace simple NumPy embeddings with Sentence Transformers for real semantic search.

Add pagination for search results.

Highlight matching keywords in the document snippet.

Deploy using Heroku, Render, or Vercel for public access.

🔹 License

This project is for hackathon participation and personal learning purposes.

🔹 Contact

Developer: Shivayogi

Email: shivayogi3338@gmail.com

GitHub: https://github.com/Shivayogi03/smart-search-app
