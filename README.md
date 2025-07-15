Here’s your full, updated, **polished `README.md`** file, ready to drop into your GitHub repository — including fixed image embedding, improved formatting, and a clean layout that looks great both in VS Code and on GitHub.

---

```markdown
# 🧠 Reddit User Persona Extractor

This project automates the extraction and visualization of **Reddit user personas** by collecting their public **posts** and **comments**, analyzing behavioral traits, and presenting them in a clean, beautiful **HTML profile**.

---

## 📌 Features

- 🔍 Fetches Reddit posts & comments from given usernames
- 🤖 Generates a summarized **user persona** (age, job, motivations, etc.)
- 🗂️ Outputs:
  - ✅ `.txt` – raw Reddit content
  - ✅ `.json` – structured persona data
  - ✅ `.html` – styled persona profile
- 🎨 Responsive, scrollable HTML layout
- 🧾 Right panel includes raw scraped data

---

## 🛠️ Tech Stack

- `Python 3.7+`
- [`PRAW`](https://praw.readthedocs.io/) – Reddit API wrapper
- `HTML + CSS` – responsive & aesthetic layout
- `dotenv` – for secure credential loading
- *(Optional)* GPT-based persona generation

---

## 📁 Folder Structure

```

reddit-user-persona/
├── .env                      # Reddit credentials (ignored)
├── .gitignore
├── main.py                   # Orchestrates full flow
├── generate\_persona.py       # Extracts persona from text
├── generate\_html\_profile.py  # Creates styled HTML profiles
├── sample\_output.png         # Screenshot of final HTML output
├── requirements.txt
├── README.md
└── outputs/
├── text\_output/          # Raw Reddit content (.txt)
├── json\_output/          # Persona data (.json)
└── html\_output/          # Final profile pages (.html)

````

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Sairam-Panuku/reddit-user-persona.git
cd reddit-user-persona
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ✅ Ensure `praw`, `python-dotenv` are included in `requirements.txt`.

### 3. Setup Reddit API Keys

Create a file named `.env` with the following format:

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

Generated files will appear in the `outputs/` folder:

* 🔹 `text_output/` – raw data (`username.txt`)
* 🔹 `json_output/` – extracted persona (`username_persona.json`)
* 🔹 `html_output/` – final profile (`username_profile.html`)

---

## 📸 Sample Output

Here’s how the final persona profile looks in HTML:

![Reddit User Persona Screenshot](sample_output.png)

> Left side: Clean persona data
> Right side: Scrollable raw Reddit content

---

## 🧠 Example Use Cases

* UX Designers creating behavioral personas
* Recruiters analyzing public profiles
* Social scientists & behavioral analysts
* Devs building portfolio-style personality pages

---

## 📝 Notes

* ✍️ Each Reddit user entry goes through:

  1. Data scraping
  2. Persona extraction from `.txt`
  3. HTML generation
* ✨ HTML layout is clean, responsive, and scrollable
* 🛡️ `.env` is **ignored via `.gitignore`**

---

## 🤝 Contribution

Pull requests are welcome! Suggested improvements:

* 🌙 Dark mode toggle
* 🧠 GPT-4 integration for richer persona modeling
* 🖨️ Export to PDF
* 📊 Persona comparison charts

---

## 📄 License

MIT License. Feel free to use and improve. Attribution appreciated 💙

---

## 💡 Inspiration

Inspired by the need to **understand user behavior through public signals** and make user profiles more visual and structured for design, hiring, and research purposes.

---

> Built with ❤️ by [Sairam Panuku](https://github.com/Sairam-Panuku)

```

---

