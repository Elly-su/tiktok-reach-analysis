# TikTok Reach Analysis Project

🎯 **BSC Data Science - C.A.T 3**

A comprehensive data analysis project exploring TikTok video performance and reach optimization using Python, statistical analysis, and machine learning.

---

## 📊 Project Overview

This project analyzes TikTok video engagement data to understand factors influencing reach and provides actionable insights for content creators, marketers, and businesses.

**Dataset:** 1,000 TikTok videos (Jan-Dec 2024)  
**Analysis Tools:** Python, Pandas, NumPy, Matplotlib, SeabornPlotly, Scikit-learn

---

## 🎓 Learning Objectives

✅ Machine Learning fundamentals and workflow  
✅ Data manipulation with Pandas and NumPy  
✅ Data visualization with Matplotlib, Seaborn, and Plotly  
✅ Statistical hypothesis testing  
✅ Predictive modeling for reach forecasting

---

## 🔍 Research Questions

### H1: Temporal Impact
**Does posting time affect reach?**
- ✅ Yes! Evening hours (6-9 PM) show 50% higher views
- Weekend posts get 30% more engagement

### H2: Engagement Correlation
**How do likes, comments, and shares relate to views?**
- ✅ Strong positive correlations (all p < 0.001)
- Likes show strongest correlation with reach

### H3: Video Duration
**Does video length impact reach?**
- ✅ Yes! Shorter videos (15-30s) perform best
- Optimal length varies by category

### H4: Predictive Modeling
**Can we predict reach using ML?**
- ✅ Yes! Random Forest model achieves R² > 0.70
- Key predictors: Followers, hashtags, posting time

---

## 📁 Project Structure

```
Tiktok Reach Analysis Project/
├── data/
│   └── tiktok_data.csv              # Dataset (1,000 videos)
├── notebooks/
│   ├── tiktok_analysis_part1.ipynb  # Data loading & EDA
│   ├── tiktok_analysis_part2.ipynb  # Hypothesis H1 & H2
│   └── tiktok_analysis_part3.ipynb  # Hypothesis H3, H4 & ML
├── visualizations/                   # Generated charts & plots
│   ├── metrics_distribution.png
│   ├── category_performance.html
│   ├── h1_hourly_reach.png
│   ├── h1_heatmap.png
│   ├── h2_correlation.png
│   ├── h2_scatter.png
│   ├── h3_scatter.html
│   ├── h3_boxplot.png
│   ├── h4_predictions.png
│   └── h4_feature_importance.png
├── models/
│   └── reach_prediction_model.pkl   # Trained ML model
├── generate_dataset.py               # Dataset generator
├── REPORT.md                         # Comprehensive project report
└── README.md                         # This file
```

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter
```

### Running the Analysis

1. **Navigate to project directory:**
```bash
cd "c:\Users\ellio\Tiktok Reach Analysis Project"
```

2. **Generate dataset (already done):**
```bash
python generate_dataset.py
```

3. **Open Jupyter Notebook:**
```bash
cd notebooks
jupyter notebook
```

4. **Run notebooks in order:**
   - `tiktok_analysis_part1.ipynb` - Data loading & EDA
   - `tiktok_analysis_part2.ipynb` - H1 & H2 analysis
   - `tiktok_analysis_part3.ipynb` - H3, H4 & ML modeling

---

## 📈 Key Findings

### 🕐 Best Posting Times
- **Peak Hours:** 6-9 PM (18:00-21:00)
- **Best Days:** Saturday & Sunday
- **Avoid:** Midnight - 6 AM

### 📹 Content Optimization
- **Ideal Length:** 15-30 seconds
- **Top Categories:** Gaming, Comedy, Fashion
- **Hashtags:** Use 3-5 relevant tags

### 🤖 ML Model Performance
- **Best Model:** Random Forest
- **R² Score:** >0.70 (strong predictive power)
- **Top Features:** Followers, hashtags, posting hour

---

## 💡 Recommendations for Content Creators

1. **Post during evening hours (6-9 PM)** for maximum visibility
2. **Keep videos short (15-30s)** for higher engagement
3. **Use 3-5 relevant hashtags** per post
4. **Focus on weekends** when possible
5. **Build your follower base** - strongest reach predictor

---

## 📊 Dataset Features

- **Video Metrics:** Views, Likes, Comments, Shares
- **Content Info:** Category, Length, Hashtags
- **Temporal Data:** Upload time, date, day of week
- **User Stats:** Followers, following, total likes
- **Calculated:** Engagement rates, time periods

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Matplotlib & Seaborn** - Static visualizations
- **Plotly** - Interactive charts
- **SciPy** - Statistical testing
- **Scikit-learn** - Machine learning
- **Jupyter** - Interactive notebooks

---

## 📝 Deliverables

1. ✅ **Jupyter Notebooks** (3 parts) - Complete analysis workflow
2. ✅ **Comprehensive Report** (`REPORT.md`) - Detailed findings
3. ✅ **Visualizations** - 10+ charts and plots
4. ✅ **ML Model** - Trained reach prediction model
5. ✅ **Dataset** - 1,000 videos with 23 features

---

## 📚 Real-World Applications

- **Marketers:** Identify what attracts consumers
- **Businesses:** Understand product reception
- **Content Creators:** Optimize for viral content
- **Social Media Managers:** Data-driven posting strategies

---

## 🎯 Future Enhancements

- Integrate real TikTok API data
- Add audio/music feature analysis
- Implement computer vision for content analysis
- Study viral spread patterns
- Analyze regional engagement differences

---

## 👨‍💻 Author

**[Your Name]**  
BSC Data Science  
December 2024

---

## 📄 License

This project is for educational purposes as part of C.A.T 3 coursework.

---

## 🙏 Acknowledgments

- TikTok for inspiring the analysis
- Python data science community
- Course instructors and peers

---

**For detailed findings, see [REPORT.md](REPORT.md)**
