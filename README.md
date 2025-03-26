# 🚀 Spark SQL & DataFrames: Social Media Sentiment & Engagement Analysis

This project uses **Apache Spark SQL and DataFrames** to analyze social media activity data — including user posts, hashtags, sentiment scores, and user profiles — to extract valuable insights related to audience engagement and content performance.

---

## 📊 Dataset

Two datasets were used:

### `posts.csv`
Contains user-generated content and post performance.
| Column           | Type     | Description                                           |
|------------------|----------|-------------------------------------------------------|
| PostID           | Integer  | Unique ID of the post                                |
| UserID           | Integer  | ID of the user who posted                            |
| Content          | String   | Text content of the post                             |
| Timestamp        | String   | Time the post was made                               |
| Likes            | Integer  | Number of likes                                      |
| Retweets         | Integer  | Number of retweets                                   |
| Hashtags         | String   | Comma-separated hashtags                             |
| SentimentScore   | Float    | Ranges from -1 (negative) to 1 (positive) sentiment  |

### `users.csv`
Contains user demographics.
| Column    | Type    | Description                      |
|-----------|---------|----------------------------------|
| UserID    | Integer | Unique user ID                   |
| Username  | String  | User handle                      |
| AgeGroup  | String  | Teen, Adult, or Senior           |
| Country   | String  | Country of the user              |
| Verified  | Boolean | Whether the user is verified     |

---

## ✅ Tasks Completed

### 1️⃣ Trending Hashtags (`top_hashtags`)
- Extracted hashtags from posts
- Counted frequency of each
- Returned Top 10 hashtags

📁 Output: `outputs/top_hashtags/`

---

### 2️⃣ Engagement by Age Group (`engagement_by_age`)
- Joined user + post data
- Calculated average likes & retweets for each age group

📁 Output: `outputs/engagement_by_age/`

---

### 3️⃣ Sentiment vs. Engagement (`sentiment_vs_engagement`)
- Categorized posts into Positive, Neutral, or Negative
- Calculated avg. likes & retweets per sentiment group

📁 Output: `outputs/sentiment_vs_engagement/`

---

### 4️⃣ Top Verified Influencers (`top_verified_users`)
- Filtered verified users
- Calculated total reach = Likes + Retweets
- Displayed top 5 influential verified users

📁 Output: `outputs/top_verified_users/`

---

## ⚙️ How to Run

### 🐳 Using Docker + Spark

```bash
docker run -it --rm -v "$PWD":/app -w /app bitnami/spark /bin/bash
spark-submit src/analysis.py


PROJECT STRUCTURE 

├── posts.csv
├── users.csv
├── outputs/
│   ├── top_hashtags/
│   ├── engagement_by_age/
│   ├── sentiment_vs_engagement/
│   └── top_verified_users/
└── src/
    └── analysis.py
