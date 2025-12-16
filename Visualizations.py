"""
Visualization generator for TikTok Reach Analysis
Creates key visualizations from the dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

# Load data
df = pd.read_csv(r'data\tiktok_data.csv')

print(f"Loaded {len(df)} videos")

# 1. Views Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Views'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Views', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Distribution of Video Views', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/views_distribution.png', dpi=300, bbox_inches='tight')
print("Created views_distribution.png")
plt.close()

# 2. Hourly Reach
hourly_reach = df.groupby('Upload_Hour')['Views'].mean().round(0)
plt.figure(figsize=(12, 6))
plt.bar(hourly_reach.index, hourly_reach.values, color='coral', alpha=0.7, edgecolor='black')
plt.plot(hourly_reach.index, hourly_reach.values, color='darkred', marker='o', linewidth=2, markersize=6)
plt.xlabel('Hour of Day', fontsize=12, fontweight='bold')
plt.ylabel('Average Views', fontsize=12, fontweight='bold')
plt.title('Average Video Reach by Hour of Day', fontsize=14, fontweight='bold')
plt.xticks(range(0, 24))
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/hourly_reach.png', dpi=300, bbox_inches='tight')
print("Created hourly_reach.png")
plt.close()

# 3. Category Performance
category_stats = df.groupby('Category')['Views'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
bars = plt.barh(category_stats.index, category_stats.values, color='teal', alpha=0.7, edgecolor='black')
plt.xlabel('Average Views', fontsize=12, fontweight='bold')
plt.ylabel('Category', fontsize=12, fontweight='bold')
plt.title('Average Views by Content Category', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/category_performance.png', dpi=300, bbox_inches='tight')
print("Created category_performance.png")
plt.close()

# 4. Engagement Correlation
engagement_cols = ['Views', 'Likes', 'Comments', 'Shares']
corr_matrix = df[engagement_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            square=True, linewidths=2, cbar_kws={'shrink': 0.8})
plt.title('Engagement Metrics Correlation', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/correlation_matrix.png', dpi=300, bbox_inches='tight')
print("Created correlation_matrix.png")
plt.close()

print("\nAll visualizations created successfully!")
print("Saved to: visualizations/")
