Here’s a clean and professional `README.md` for your **Reddit User Persona Extractor** project:

---

```markdown
# 🧠 Reddit User Persona Extractor

This project automates the extraction and visualization of **Reddit user personas** by collecting their public **posts** and **comments**, analyzing their behavioral traits, and presenting them in a **beautiful HTML profile**.

---

## 📌 Features

- 🔍 Fetches public posts & comments from a list of Reddit usernames
- 🤖 Generates user personas based on language analysis
- 📄 Saves:
  - Raw data as `.txt`
  - Extracted persona as `.json`
  - Styled persona page as `.html`
- 🎨 HTML profiles with clean, colorful layouts
- 🧾 Raw Reddit data displayed alongside persona on the same page

---

## 🛠️ Tech Stack

- `Python 3.7+`
- [`PRAW`](https://praw.readthedocs.io/) – Reddit API wrapper
- `OpenAI` (optional if GPT integration is enabled)
- `HTML + CSS` – modern responsive design
- `.env` config using `python-dotenv`

---

## 📂 Project Structure

```

reddit-user-persona/
│
├── main.py                    # Entry point to fetch data & generate profiles
├── generate\_persona.py        # Extracts persona traits from scraped data
├── generate\_html\_profile.py   # Builds HTML profile using persona data
│
├── outputs/
│   ├── text\_output/           # Raw Reddit posts/comments as .txt
│   ├── json\_output/           # Generated persona as .json
│   └── html\_output/           # Beautiful HTML profile
│
├── .env                       # Reddit API credentials (not tracked)
└── README.md                  # This file

````

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/reddit-user-persona.git
cd reddit-user-persona
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

> 📦 Make sure to include `praw`, `python-dotenv` in your `requirements.txt`.

### 3. Set Up Reddit API

Create a `.env` file:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=persona-extractor-script
```

### 4. Run the Script

```bash
python main.py
```

HTML files will be generated inside `outputs/html_output/`.

---

## 🌈 Sample Output

![Example Screenshot](preview.png)

---

## 📘 Notes

* Each user will have:

  * `username.txt` in `outputs/text_output/`
  * `username_persona.json` in `outputs/json_output/`
  * `username_profile.html` in `outputs/html_output/`
* If persona generation uses GPT or LLMs, ensure rate-limiting & key safety.
* Extend `generate_persona.py` to include tone, empathy, or brand preferences.

---

## 🤝 Contribution

PRs are welcome! If you want to add dark mode, GPT integration, or export as PDF – open an issue first.

---

## 📄 License

MIT License. Do what you want. Credit appreciated.

---

## 💡 Inspiration

Inspired by product design workflows that build **personas** to understand user behavior through social signals.

---

> Built with ❤️ by \ Sairam Panuku


