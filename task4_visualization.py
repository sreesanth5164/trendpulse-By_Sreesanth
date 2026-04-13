import pandas as pd
import matplotlib.pyplot as plt
import os

try:
    
    df = pd.read_csv("data/trends_analysed.csv")

    
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # Chart 1: Top 10 Stories
    top = df.sort_values(by="score", ascending=False).head(10)

    titles = []
    for t in top["title"]:
        if len(t) > 50:
            titles.append(t[:50] + "...")
        else:
            titles.append(t)

    plt.figure()
    plt.barh(titles, top["score"])
    plt.title("Top 10 Stories by Score")
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.gca().invert_yaxis()
    plt.savefig("outputs/chart1_top_stories.png")
    plt.show()

    # Chart 2: Category Count
    counts = df["category"].value_counts()

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("outputs/chart2_categories.png")
    plt.show()

    
    # Chart 3: Scatter Plot
    
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure()
    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
    plt.title("Score vs Comments")
    plt.xlabel("Score")
    plt.ylabel("Comments")
    plt.legend()
    plt.savefig("outputs/chart3_scatter.png")
    plt.show()

 
    # Dashboard (bonus)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))

    # Chart 1
    axs[0].barh(titles, top["score"])
    axs[0].set_title("Top Stories")

    # Chart 2
    axs[1].bar(counts.index, counts.values)
    axs[1].set_title("Categories")

    # Chart 3
    axs[2].scatter(popular["score"], popular["num_comments"])
    axs[2].set_title("Score vs Comments")

    fig.suptitle("TrendPulse Dashboard")
    plt.savefig("outputs/dashboard.png")
    plt.show()

    print("Charts saved in outputs folder")

except Exception as e:
    print("Error:", e)