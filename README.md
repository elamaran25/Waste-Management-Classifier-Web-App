

# ♻️ Waste Management Classification Web App  

This project is a **Django-based web application** that classifies waste into categories such as **Organic** and **Recyclable** using a fine-tuned **Deep Learning model (TensorFlow/Keras)**.  
It is designed to promote **sustainable waste management practices** by enabling quick classification through image uploads.  

---

## 🚀 Tech Stack  

- **Backend**: Django (Python Framework)  
- **Frontend**: HTML, CSS, JavaScript  
- **Machine Learning**: TensorFlow, Keras, NumPy, Pillow  
- **Database**: SQLite (default, can be extended to MySQL/PostgreSQL)  

---

## ⚙️ Features  

✅ Upload an image of waste and get classification results (Organic / Recyclable)  
✅ Fine-tuned deep learning model for accuracy  
✅ Simple, user-friendly web interface  
✅ Database integration for storing uploaded results  
✅ **Real-time camera-based waste classification** 

---

## 📂 Project Structure  

```

classifier/
│-- Waste\_classifier/       # Main app containing ML model integration
│-- db.sqlite3              # Database
│-- manage.py               # Django project entry point
│-- requirements.txt        # Dependencies

````

---

## 📦 Installation  

Clone this repository:  

```bash
git clone https://github.com/elamaran25/waste-management-classifier.git
cd waste-management-classifier
````

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser at 👉 `http://127.0.0.1:8000/`

---

## 🖼️ Model

The trained waste classification model is stored in:

```
Waste_classifier/model/waste_classifier.h5
```

It is loaded during runtime to classify images into **Organic** or **Recyclable**.

---

## 🛠️ Future Enhancements

* Multi-class waste classification (Plastic, Metal, E-Waste, etc.)
* Mobile app integration using Flutter
* Dashboard for analytics & monitoring waste patterns

---

## 👨‍💻 Author

**Elamaran V**
📍 Final Year B.Tech Artificial Intelligence & Data Science
🎓 Vel Tech High Tech Dr. Rangarajan Dr. Sakunthala Engineering College
🔗 [GitHub](https://github.com/elamaran25) | [LinkedIn](https://www.linkedin.com/in/elamaran25)

---

---

Would you like me to also include **sample screenshots (placeholders)** in the README (like UI home page, upload form, classification result), so it looks more attractive on GitHub?
```
