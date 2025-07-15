# 🧠 Reddit User Persona Extractor

**Reddit User Persona Extractor** is a Python-based tool that automates the extraction and visualization of **user personas** using public **Reddit posts and comments**.

It analyzes user behavior, builds a structured profile, and generates a clean, scrollable **HTML page** containing both:
- ✨ The extracted persona (age, job, motivations, etc.)
- 📄 Raw scraped Reddit data

---

## 📌 Features

- 🔍 Fetches Reddit posts & comments from given usernames
- 🤖 Automatically extracts key behavioral persona attributes
- 📄 Outputs:
  - `.txt` – raw Reddit content
  - `.json` – structured persona data
  - `.html` – styled user profile page
- 🎨 Beautiful, responsive HTML layout (side-by-side view)
- 🧾 Scrollable right panel showing raw content

---

## 🛠️ Tech Stack

- `Python 3.7+`
- [`PRAW`](https://praw.readthedocs.io/) – Reddit API wrapper
- `HTML + CSS` – responsive & aesthetic layout
- `python-dotenv` – secure `.env` loading
- *(Optional)* GPT-based persona generation

---


#🚀 Getting Started
1. Clone the Repo
bash
Copy code
git clone https://github.com/Sairam-Panuku/reddit-user-persona.git
cd reddit-user-persona
---
2. Install Dependencies

pip install -r requirements.txt
Make sure praw and python-dotenv are included in requirements.txt.
---
3. Setup Reddit API
Create a .env file with your credentials:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=persona-extractor-script
---
4. Run the Script
bash
Copy code
python main.py
Generated outputs will be saved under the outputs/ directory:

.txt → raw data in text_output/

.json → persona info in json_output/

.html → full profile in html_output/
---
📸 Sample Output


💡 Left: Persona profile
📄 Right: Scrollable raw Reddit data
---
🧠 Use Cases
UX Designers building behavior-driven personas

Recruiters reviewing public user footprints

Social scientists analyzing discussion patterns

Developers building user intelligence dashboards
---
📝 Notes
Each user undergoes:

Post/comment scraping

Persona extraction from .txt

HTML profile generation

The layout is responsive and clean

The .env file is ignored by .gitignore for safety
---
🤝 Contributing
Contributions are welcome! Ideas you can try:
---
🌙 Add dark mode

📈 Add comparison between users

🧠 GPT-based advanced persona models

🖨️ Export personas as PDF
---
📄 License
MIT License – use it freely and improve it. Attribution appreciated!
---
💡 Inspiration
Built to help designers, developers, and analysts visualize user personas using social footprints like Reddit.
---
Built with ❤️ by Sairam Panuku

## 📁 Folder Structure

```
reddit-user-persona/
├── .env                      # Reddit credentials (ignored)
├── .gitignore
├── main.py                   # Orchestrates full flow
├── generate_persona.py       # Extracts persona from text
├── generate_html_profile.py  # Creates styled HTML profiles
├── sample_output.png         # Screenshot of final HTML output
├── requirements.txt
├── README.md
└── outputs/
    ├── text_output/          # Raw Reddit content (.txt)
    ├── json_output/          # Persona data (.json)
    └── html_output/          # Final profile pages (.html)

---

