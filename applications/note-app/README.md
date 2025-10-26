# Mood Notes 

**Mood Notes** is a simple and fun web app built with **Django**.  
It allows users to write daily notes about their **mood**, **day**, and **feelings**.  
You can log in, create notes, add reactions, comments, and even upload images to express yourself more.

---

### Features ✨
- User authentication (Sign up, Log in, Log out)  
- Add, edit, and delete notes  
- Add reactions and comments  
- Upload note images  
- Clean and friendly user interface  

---

###  Technologies Used 🛠️
- Python & Django  
- HTML, CSS  
- SQLite (default Django database)

---

###  Project Structure 📁
```
applications/
│
└── note-app/
    ├── main_app/
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_delete_note.py
    │   │   ├── 0003_initial.py
    │   │   ├── 0004_comment.py
    │   │   ├── 0006_photo.py
    │   │   ├── 0007_reaction_note.py
    │   │   └── 0008_note_user.py
    │   │
    │   ├── static/
    │   │   ├── css/
    │   │   │   ├── styles.css
    │   │   │   ├── about.css
    │   │   │   ├── base.css
    │   │   │   ├── form.css
    │   │   │   └── home.css
    │   │   │
    │   │   ├── images/
    │   │   │   ├── mood.jpg
    │   │   │   └── today-s-mood-277365833.webp
    │   │   │
    │   │   └── notes/
    │   │
    │   ├── templates/
    │   │   └── main_app/
    │   │       ├── about.html
    │   │       ├── base.html
    │   │       ├── home.html
    │   │       ├── signup.html
    │   │       ├── note_confirm_delete.html
    │   │       ├── note_form.html
    │   │       ├── reaction_detail.html
    │   │       ├── reaction_form.html
    │   │       ├── reaction_list.html
    │   │       └── notes/
    │   │           ├── detail.html
    │   │           └── index.html
    │   │
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── notes_project/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── db.sqlite3
    ├── manage.py
    ├── Pipfile
    └── Pipfile.lock
```