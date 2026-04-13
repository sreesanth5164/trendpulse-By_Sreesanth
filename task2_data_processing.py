import pandas as pd
import glob
import os

try:
    # Step 1: Find JSON file
    files = glob.glob("data/trends_*.json")
    
    if not files:
        print("No JSON file found in data folder.")
        exit()

    latest_file = max(files, key=os.path.getctime)

    # Load JSON
    df = pd.read_json(latest_file)

    print(f"Loaded {len(df)} stories from {latest_file}")

    # Step 2: Remove duplicates
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # Step 3: Remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # Step 4: Convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Step 5: Remove low-quality stories (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Step 6: Clean whitespace
    df["title"] = df["title"].str.strip()

    # Step 7: Save as CSV
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved {len(df)} rows to {output_file}")

    # Step 8: Summary (stories per category)
    print("\nStories per category:")
    print(df["category"].value_counts())

except Exception as e:
    print("Error:", e)