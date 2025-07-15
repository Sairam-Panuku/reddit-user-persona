import os
import json

def generate_html(username, persona_data, html_path):
    def format_tags(tags, color="#81d4fa"):
        if not tags:
            return '<p class="muted">Not specified</p>'
        return '<div class="tag-group">' + ''.join(
            f'<span class="tag" style="background:{color}">{tag}</span>' for tag in tags
        ) + '</div>'

    raw_text_path = f"outputs/text_output/{username}.txt"
    try:
        with open(raw_text_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except:
        raw_text = "Raw text not available."

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Persona: {persona_data.get('username', username)}</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #e0f7fa, #e1f5fe);
            margin: 0;
            padding: 2rem;
            color: #2c3e50;
        }}
        .container {{
            display: flex;
            gap: 2rem;
            flex-wrap: wrap;
        }}
        .card {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        }}
        .left {{
            flex: 1;
            min-width: 400px;
            max-width: 700px;
        }}
        .right {{
            flex: 1;
            min-width: 400px;
            max-height: 90vh;
            overflow-y: auto;
        }}
        h1 {{
            margin-bottom: 0.3rem;
            font-size: 2rem;
            color: #00796b;
        }}
        h2 {{
            font-size: 1.1rem;
            color: #4a148c;
            margin-top: 1.4rem;
            margin-bottom: 0.6rem;
        }}
        blockquote {{
            font-style: italic;
            color: #555;
            margin: 0.5rem 0 1.2rem;
            padding-left: 1rem;
            border-left: 4px solid #00bfa5;
        }}
        .tag {{
            display: inline-block;
            background: #b2ebf2;
            color: #004d40;
            padding: 0.4rem 0.9rem;
            border-radius: 20px;
            margin: 0.3rem 0.4rem 0 0;
            font-size: 0.85rem;
        }}
        .muted {{
            color: #999;
            font-style: italic;
        }}
        .tag-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.3rem;
        }}
        .demographics p {{
            margin: 0.4rem 0;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.2rem;
            margin-top: 1.2rem;
        }}
        .grid-section {{
            background: #f3e5f5;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #d1c4e9;
        }}
        .scroll-box {{
            background: #f9fbe7;
            padding: 1rem;
            border: 1px solid #c5e1a5;
            border-radius: 12px;
            overflow-y: auto;
        }}
        .scroll-box pre {{
            white-space: pre-wrap;
            font-size: 0.95rem;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- LEFT PANEL -->
        <div class="card left">
            <h1>{persona_data.get('name', username)}</h1>
            <blockquote>"{persona_data.get('quote', 'No quote provided.')}"</blockquote>
            <p><strong>Username:</strong> u/{username}</p>

            <div class="demographics">
                <h2>🧠 Demographics</h2>
                <p><strong>Age:</strong> {persona_data.get('age', 'Not mentioned')}</p>
                <p><strong>Occupation:</strong> {persona_data.get('occupation', 'Unknown')}</p>
                <p><strong>Company:</strong> {persona_data.get('company', 'N/A')}</p>
                <p><strong>Location:</strong> {persona_data.get('location', 'Unknown')}</p>
            </div>

            <div class="grid">
                <div class="grid-section">
                    <h2>🌱 Motivations</h2>
                    {format_tags(persona_data.get('motivations'), "#a7ffeb")}
                </div>
                <div class="grid-section">
                    <h2>😤 Frustrations</h2>
                    {format_tags(persona_data.get('frustrations'), "#ffccbc")}
                </div>
                <div class="grid-section">
                    <h2>🎯 Goals</h2>
                    {format_tags(persona_data.get('goals'), "#ffe082")}
                </div>
                <div class="grid-section">
                    <h2>💡 Preferences</h2>
                    {format_tags(persona_data.get('preferences'), "#b2ebf2")}
                </div>
                <div class="grid-section">
                    <h2>📌 Top Interests</h2>
                    {format_tags(persona_data.get('interests'), "#c5cae9")}
                </div>
                <div class="grid-section">
                    <h2>📍 Personality</h2>
                    {format_tags(persona_data.get('personality', ['Introvert', 'Thinking', 'Judging', 'Sensing']), "#dcedc8")}
                </div>
            </div>
        </div>

        <!-- RIGHT PANEL -->
        <div class="card right">
            <h2>🧾 Raw Reddit Data</h2>
            <div class="scroll-box">
                <pre>{raw_text}</pre>
            </div>
        </div>
    </div>
</body>
</html>
    """

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Styled HTML saved to {html_path}")
