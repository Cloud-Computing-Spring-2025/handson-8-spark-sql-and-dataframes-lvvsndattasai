from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, avg, sum, when

spark = SparkSession.builder.appName("SocialMediaAnalysis").getOrCreate()

# Load CSV files
posts = spark.read.option("header", "true").option("inferSchema", "true").csv("posts.csv")
users = spark.read.option("header", "true").option("inferSchema", "true").csv("users.csv")

# Task 1: Hashtag Trends
hashtags_df = posts.select(explode(split(col("Hashtags"), ",")).alias("Hashtag"))
hashtag_counts = hashtags_df.groupBy("Hashtag").count().orderBy(col("count").desc())
hashtag_counts.limit(10).write.csv("outputs/top_hashtags", header=True, mode="overwrite")

# Task 2: Engagement by Age Group
joined_df = posts.join(users, on="UserID")
engagement_df = joined_df.groupBy("AgeGroup").agg(
    avg("Likes").alias("AvgLikes"),
    avg("Retweets").alias("AvgRetweets")
).orderBy(col("AvgLikes").desc())
engagement_df.write.csv("outputs/engagement_by_age", header=True, mode="overwrite")

# Task 3: Sentiment vs Engagement
sentiment_df = posts.withColumn("Sentiment",
    when(col("SentimentScore") > 0.2, "Positive")
    .when(col("SentimentScore") < -0.2, "Negative")
    .otherwise("Neutral")
)
sentiment_engagement = sentiment_df.groupBy("Sentiment").agg(
    avg("Likes").alias("AvgLikes"),
    avg("Retweets").alias("AvgRetweets")
).orderBy("Sentiment")
sentiment_engagement.write.csv("outputs/sentiment_vs_engagement", header=True, mode="overwrite")

# Task 4: Top Verified Users by Reach
verified = users.filter(col("Verified") == True)
joined_verified = posts.join(verified, on="UserID")
reach_df = joined_verified.withColumn("Reach", col("Likes") + col("Retweets"))
top_verified = reach_df.groupBy("Username").agg(
    sum("Reach").alias("TotalReach")
).orderBy(col("TotalReach").desc()).limit(5)
top_verified.write.csv("outputs/top_verified_users", header=True, mode="overwrite")

spark.stop()

