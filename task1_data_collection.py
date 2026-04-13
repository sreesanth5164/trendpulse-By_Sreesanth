import requests
import time
import json
import os
from datetime import datetime

# Header (required)
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Store collected stories
collected_data = []

# Count per category
category_counts = {key: 0 for key in categories}

# Step 1: Get top story IDs
try:
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url, headers=headers)
    story_ids = response.json()[:500]
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

# Step 2: Fetch each story
for category, keywords in categories.items():

    print(f"Processing category: {category}")

    for story_id in story_ids:

        # Stop if 25 collected
        if category_counts[category] >= 25:
            break

        try:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            res = requests.get(story_url, headers=headers)
            story = res.json()

            if not story or "title" not in story:
                continue

            title = story["title"].lower()

            # Check keyword match
            if any(keyword in title for keyword in keywords):

                collected_data.append({
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

                category_counts[category] += 1

        except Exception as e:
            print(f"Error fetching story {story_id}: {e}")
            continue

    # Sleep AFTER each category
    time.sleep(2)

# Step 3: Save JSON

# Create data folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# File name with date
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

# Save file
with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)

# Final output
print(f"\nCollected {len(collected_data)} stories.")
print(f"Saved to {filename}")