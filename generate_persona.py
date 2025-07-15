import os
import re
import json
from collections import Counter


def extract_persona_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract posts and comments
    posts = re.findall(r"\[Post \d+\](.*?)Score: \d+", content, re.DOTALL)
    comments = re.findall(r"\[Comment \d+\](.*?)Score: \d+", content, re.DOTALL)
    all_text = ' '.join(posts + comments).lower()

    # Extract details
    location = re.search(r"(?:(?:from|in|moving to|relocating to)\s)([a-zA-Z ]+)", all_text)
    age = re.search(r"(\d{2}) ?yrs? old", all_text)
    job = re.search(r"(?:working at|join(?:ed|ing)?|i'?m a) ([a-zA-Z ]+)", all_text)
    company = re.search(r"(?:infosys|tcs|cts|cognizant|accenture|ey|deloitte|capgemini|zoho|hcl)", all_text)

    subreddits = re.findall(r"Subreddit: ([a-zA-Z_]+)", content)
    top_subreddits = Counter(subreddits).most_common(5)

    motivations = []
    if "salary" in all_text or "hike" in all_text:
        motivations.append("Salary growth")
    if "airport lounge" in all_text:
        motivations.append("Comfort & lifestyle")
    if "move" in all_text or "relocate" in all_text:
        motivations.append("Better opportunities")

    frustrations = []
    if "confusing" in all_text:
        frustrations.append("Confusing policies")
    if "not sure" in all_text or "no clarity" in all_text:
        frustrations.append("Lack of information")

    # Default values
    persona = {
        "name": file_path.split("/")[-1].replace(".txt", "").replace("_", " ").title(),
        "username": os.path.basename(file_path).replace(".txt", ""),
        "quote": "I want to make financially wise decisions while living comfortably.",
        "age": age.group(1) if age else "Not mentioned",
        "occupation": job.group(1).strip().title() if job else "Unknown",
        "company": company.group(0).title() if company else "",
        "location": location.group(1).strip().title() if location else "Unknown",
        "interests": [sr for sr, _ in top_subreddits],
        "motivations": motivations,
        "frustrations": frustrations,
        "goals": ["Career growth", "Work-life balance"],
        "preferences": ["Online communities", "Peer opinions", "Anonymity"],
        "personality": ["Introvert", "Thinking", "Judging", "Sensing"],
    }

    return persona


def generate_persona_from_file(file_path):
    data = extract_persona_data(file_path)
    summary = f"""
"{data['quote']}"
Username: u/{data['username']}

AGE: {data['age']}
OCCUPATION: {data['occupation']} {f'at {data["company"]}' if data['company'] else ''}
LOCATION: {data['location']}
TIER: Early Adopter
ARCHETYPE: The Realist

INTERESTED SUBREDDITS: {', '.join(data['interests'])}

MOTIVATIONS:
- {chr(10).join(data['motivations']) if data['motivations'] else 'Not clear'}

FRUSTRATIONS:
- {chr(10).join(data['frustrations']) if data['frustrations'] else 'Not clear'}

PERSONALITY:
- {chr(10).join(data['personality'])}
    """.strip()

    # Save JSON for HTML use
    json_path = file_path.replace(".txt", "_persona.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return summary


if __name__ == '__main__':
    # Test run
    test_user_file = "outputs/Any_Track_1781.txt"
    summary = generate_persona_from_file(test_user_file)
    print(summary)
