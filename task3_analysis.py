import pandas as pd
import numpy as np

try:
    # Step 1: Load data
    df = pd.read_csv("data/trends_clean.csv")

    print(f"Loaded data: {df.shape}\n")

    print("First 5 rows:")
    print(df.head())

    # Average score and comments
    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()

    print(f"\nAverage score   : {avg_score}")
    print(f"Average comments: {avg_comments}")

    # Step 2: NumPy Analysis
   
    scores = df["score"].values

    print("\n--- NumPy Stats ---")

    print(f"Mean score   : {np.mean(scores)}")
    print(f"Median score : {np.median(scores)}")
    print(f"Std deviation: {np.std(scores)}")
    print(f"Max score    : {np.max(scores)}")
    print(f"Min score    : {np.min(scores)}")

    # Category with most stories
    top_category = df["category"].value_counts().idxmax()
    top_count = df["category"].value_counts().max()

    print(f"\nMost stories in: {top_category} ({top_count} stories)")

    # Most commented story
    max_comments_row = df.loc[df["num_comments"].idxmax()]
    print(f'\nMost commented story: "{max_comments_row["title"]}" — {max_comments_row["num_comments"]} comments')

    # Step 3: Add new columns
    # Engagement = num_comments / (score + 1)
    df["engagement"] = df["num_comments"] / (df["score"] + 1)

    # is_popular = score > average score
    df["is_popular"] = df["score"] > avg_score

    # Step 4: Save result
    
    output_file = "data/trends_analysed.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved to {output_file}")

except Exception as e:
    print("Error:", e)
