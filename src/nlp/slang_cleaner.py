import re

# Dictionary for common slang/abbreviations
SLANG_DICT = {
    "plz": "please",
    "krde": "kar do",
    "drop krde": "chod do",
    "clg": "college",
    "pg": "pg",
    "leja": "le ja",
    "lejao": "le jao",
    "chhoddo": "chod do",
    "mujhe": "mujhe",
    "school": "school",
    "bhai": "bhai",
    "bro": "bhai",
    "jaa": "ja",
    "chal": "chalo",
    "mein": "main",
    "aa": "a",
    "ja": "ja",
    "pls": "please"
}

def clean_slang(text: str) -> str:
    # Lowercase and remove extra spaces
    text = text.lower().strip()

    # Replace slang/shortcuts
    for slang, proper in SLANG_DICT.items():
        text = re.sub(rf"\b{re.escape(slang)}\b", proper, text)

    # Handle basic patterns (optional: more rules can be added here)
    text = text.replace("please bhai", "कृपया भाई")
    text = text.replace("bhai please", "भाई कृपया")
    text = text.replace("please", "कृपया")
    text = text.replace("mujhe", "मुझे")
    text = text.replace("le ja", "ले जाओ")
    text = text.replace("chod do", "छोड़ दो")
    text = text.replace("college", "कॉलेज")
    text = text.replace("pg", "पीजी")
    text = text.replace("school", "स्कूल")
    text = text.replace("chalo", "चलो")

    return text
