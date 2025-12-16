"""
TikTok Dataset Generator
Generates a synthetic TikTok dataset with realistic engagement patterns for educational analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_VIDEOS = 1000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 15)

# Categories and their typical engagement rates
CATEGORIES = {
    'Dance': {'avg_engagement': 0.08, 'variance': 0.03},
    'Comedy': {'avg_engagement': 0.10, 'variance': 0.04},
    'Tutorial': {'avg_engagement': 0.06, 'variance': 0.02},
    'Cooking': {'avg_engagement': 0.07, 'variance': 0.025},
    'Fashion': {'avg_engagement': 0.09, 'variance': 0.035},
    'Gaming': {'avg_engagement': 0.11, 'variance': 0.045},
    'Music': {'avg_engagement': 0.08, 'variance': 0.03},
    'Fitness': {'avg_engagement': 0.07, 'variance': 0.025},
}

# Hashtags per category
HASHTAGS = {
    'Dance': ['#dance', '#viral', '#fyp', '#trending', '#dancechallenge'],
    'Comedy': ['#funny', '#comedy', '#viral', '#fyp', '#lol'],
    'Tutorial': ['#tutorial', '#howto', '#learn', '#education', '#tips'],
    'Cooking': ['#cooking', '#recipe', '#food', '#foodie', '#chef'],
    'Fashion': ['#fashion', '#style', '#outfit', '#ootd', '#trending'],
    'Gaming': ['#gaming', '#gamer', '#gameplay', '#twitch', '#streamer'],
    'Music': ['#music', '#song', '#cover', '#singing', '#artist'],
    'Fitness': ['#fitness', '#workout', '#gym', '#health', '#fitfam'],
}

def generate_video_data():
    """Generate synthetic TikTok video data"""
    
    data = []
    
    for video_id in range(1, NUM_VIDEOS + 1):
        # Random category
        category = random.choice(list(CATEGORIES.keys()))
        
        # Random upload date and time
        random_date = START_DATE + timedelta(
            seconds=random.randint(0, int((END_DATE - START_DATE).total_seconds()))
        )
        upload_hour = random_date.hour
        upload_day = random_date.strftime('%A')
        
        # Video duration (15-180 seconds)
        video_length = random.choice([15, 20, 30, 45, 60, 90, 120, 180])
        
        # Base views (influenced by time of day)
        # Peak hours: 6-9 PM (18-21)
        time_multiplier = 1.0
        if 18 <= upload_hour <= 21:
            time_multiplier = 1.5  # 50% more views during peak hours
        elif 12 <= upload_hour <= 17 or 22 <= upload_hour <= 23:
            time_multiplier = 1.2  # 20% more views during moderate hours
        elif 0 <= upload_hour <= 6:
            time_multiplier = 0.7  # 30% fewer views during late night/early morning
        
        # Weekend boost
        weekend_multiplier = 1.3 if upload_day in ['Saturday', 'Sunday'] else 1.0
        
        # Base views with realistic distribution
        base_views = np.random.lognormal(mean=10, sigma=1.5) * time_multiplier * weekend_multiplier
        views = int(base_views)
        
        # Engagement metrics based on category
        engagement_rate = np.random.normal(
            CATEGORIES[category]['avg_engagement'],
            CATEGORIES[category]['variance']
        )
        engagement_rate = max(0.01, min(0.20, engagement_rate))  # Clamp between 1% and 20%
        
        total_engagement = int(views * engagement_rate)
        
        # Distribution of engagement (likes are most common, then shares, then comments)
        likes = int(total_engagement * np.random.uniform(0.60, 0.75))
        shares = int(total_engagement * np.random.uniform(0.15, 0.25))
        comments = int(total_engagement * np.random.uniform(0.10, 0.20))
        
        # Hashtags (1-5 hashtags per video)
        num_hashtags = random.randint(1, 5)
        hashtags = random.sample(HASHTAGS[category], min(num_hashtags, len(HASHTAGS[category])))
        hashtag_str = ' '.join(hashtags)
        
        # User stats
        user_followers = int(np.random.lognormal(mean=7, sigma=1.5))
        user_following = int(np.random.uniform(100, user_followers * 0.8))
        user_total_likes = int(user_followers * np.random.uniform(5, 20))
        
        # Video title
        video_titles = {
            'Dance': [f"Dance Challenge #{video_id}", f"Viral Dance Moves", f"New Dance Trend"],
            'Comedy': [f"Funny Moment #{video_id}", f"Comedy Skit", f"This Made Me Laugh"],
            'Tutorial': [f"How to Tutorial #{video_id}", f"Easy Guide", f"Learn This Trick"],
            'Cooking': [f"Recipe #{video_id}", f"Cooking Tutorial", f"Easy Recipe"],
            'Fashion': [f"Outfit Inspo #{video_id}", f"Fashion Haul", f"Style Tips"],
            'Gaming': [f"Gaming Highlight #{video_id}", f"Epic Gameplay", f"Game Review"],
            'Music': [f"Music Cover #{video_id}", f"Original Song", f"Singing"],
            'Fitness': [f"Workout Routine #{video_id}", f"Fitness Tips", f"Get Fit"],
        }
        video_title = random.choice(video_titles[category])
        
        data.append({
            'Video_ID': video_id,
            'User_ID': random.randint(1, NUM_VIDEOS // 2),
            'Username': f'user{random.randint(1, NUM_VIDEOS // 2)}',
            'Video_Title': video_title,
            'Category': category,
            'Likes': likes,
            'Comments': comments,
            'Shares': shares,
            'Views': views,
            'Upload_Date': random_date.strftime('%Y-%m-%d'),
            'Upload_DateTime': random_date.strftime('%Y-%m-%d %H:%M:%S'),
            'Upload_Hour': upload_hour,
            'Upload_Day': upload_day,
            'Video_Length': video_length,
            'Hashtags': hashtag_str,
            'Hashtag_Count': num_hashtags,
            'User_Followers': user_followers,
            'User_Following': user_following,
            'User_Total_Likes': user_total_likes,
        })
    
    return pd.DataFrame(data)

# Generate the dataset
print("Generating synthetic TikTok dataset...")
df = generate_video_data()

# Add calculated features
df['Engagement_Rate'] = (df['Likes'] + df['Comments'] + df['Shares']) / df['Views']
df['Like_Rate'] = df['Likes'] / df['Views']
df['Comment_Rate'] = df['Comments'] / df['Views']
df['Share_Rate'] = df['Shares'] / df['Views']

# Save to CSV
output_path = r'c:\Users\ellio\Tiktok Reach Analysis Project\data\tiktok_data.csv'
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully!")
print(f"   Total videos: {len(df)}")
print(f"   Date range: {df['Upload_Date'].min()} to {df['Upload_Date'].max()}")
print(f"   Categories: {', '.join(df['Category'].unique())}")
print(f"   Saved to: {output_path}")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nBasic statistics:")
print(df[['Views', 'Likes', 'Comments', 'Shares', 'Video_Length']].describe())
