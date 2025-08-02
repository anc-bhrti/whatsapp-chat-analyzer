# 📊 WhatsApp Chat Analyzer

Analyze your WhatsApp group or personal chat exports with insightful visualizations and statistics using Python, Pandas, and Streamlit.

<img width="1907" height="1028" alt="image" src="https://github.com/user-attachments/assets/1271814f-f5c8-43bf-8f93-38ac2b715b81" />

---

## 🔍 Features

- 📅 Extracts and visualizes message frequency over time (daily/monthly)
- 🗣️ Identifies most active users in group chats
- ⌚ Peak chat hours and busiest days
- 📈 Word frequency & emoji usage stats
- 🧹 Cleans and structures raw WhatsApp `.txt` chat exports
- 📤 Easy drag-and-drop UI using **Streamlit**

---

## 🚀 Live Demo

> 💡https://whatsapp-chat-analyzer-64zvgx7twrhb8nbyjisjuy.streamlit.app/


---

## 🛠️ Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/anc-bhrti/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
python -m venv .venv
.venv\Scripts\activate  # For Windows
pip install -r requirements.txt
````

---

## ▶️ Run the App

```bash
streamlit run app.py
```

> Upload your exported WhatsApp chat `.txt` file (no media).

---

## 📁 Project Structure

```
whatsapp-chat-analyzer/
│
├── app.py                 # Streamlit app UI
├── analyzer.py            # Core chat parsing and analysis logic
├── utils.py               # Helper functions
├── sample_chat.txt        # Example chat file
├── requirements.txt       # Required Python packages
└── README.md              # This file
```

---

## 🔒 Data Privacy

This app runs **locally on your machine** — your data is never uploaded or stored elsewhere.

---

## 📌 Future Scope

* Sentiment analysis of chats using NLP
* Chat topic modeling (e.g., using LDA)
* Group vs personal chat differentiation
* Export reports as PDF or CSV

---

## 🧑‍💻 Author

**Anchal Bharti**
[GitHub](https://github.com/anc-bhrti) • [LinkedIn](https://www.linkedin.com/in/anchal-bharti-5a20b6287/)
*Contributions welcome!*

---

## 📄 License

MIT License. See `LICENSE` for more info.

```

---

Let me know:
- Your preferred screenshot (or I’ll add a placeholder).
- If you want this in **LaTeX** format for a report too.
- If the project is hosted, I can update the `Live Demo` section.

Would you like me to generate a `requirements.txt` or explain how to deploy on **Streamlit Cloud** next?
```
