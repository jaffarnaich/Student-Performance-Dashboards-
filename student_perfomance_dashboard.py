#🎓 Student Performance Dashboard Challenge 2025

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# ---------------------------------------------------------------
# 1️⃣ LOAD DATA
# ---------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("StudentsPerformance.csv")
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df["avg_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)
    return df

# ---------------------------------------------------------------
# STREAMLIT PAGE SETTINGS
# ---------------------------------------------------------------
st.set_page_config(page_title="🎓 Student Performance Dashboard", layout="wide")
st.title("🎓 Student Performance Dashboard 2025")
st.markdown("""
### Transform Data into Visual Stories 🎨📊  
Analyze student performance trends and discover key insights interactively.
""")

# ---------------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------------
df = load_data()

# ---------------------------------------------------------------
# 2️⃣ CHOOSE THEME
# ---------------------------------------------------------------
st.sidebar.header("🎨 Dashboard Settings")
theme = st.sidebar.selectbox("Select Theme", ["whitegrid", "darkgrid", "ticks", "dark"])
sns.set_theme(style=theme)
st.sidebar.success(f"Theme Applied: {theme}")

# ---------------------------------------------------------------
# SHOW DATA PREVIEW
# ---------------------------------------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# ---------------------------------------------------------------
# 3️⃣ VISUAL 1 – Score Distribution
# ---------------------------------------------------------------
st.subheader("📈 Score Distribution")
subject = st.selectbox("Select Subject", ["math_score", "reading_score", "writing_score"])

fig1, ax1 = plt.subplots()
sns.histplot(df[subject], bins=10, kde=True, color="skyblue", ax=ax1)
ax1.set_title(f"📊 Distribution of {subject.replace('_',' ').title()}")
st.pyplot(fig1)

# ---------------------------------------------------------------
# 4️⃣ VISUAL 2 – Compare Performance by Gender
# ---------------------------------------------------------------
st.subheader("👩‍🎓 Performance by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(x="gender", y="avg_score", data=df, palette="pastel", ax=ax2)
ax2.set_title("💁‍♂️ Average Score by Gender")
st.pyplot(fig2)

# ---------------------------------------------------------------
# 5️⃣ VISUAL 3 – Effect of Test Preparation Course
# ---------------------------------------------------------------
st.subheader("📘 Test Preparation Course Effect")
fig3, ax3 = plt.subplots()
sns.barplot(x="test_preparation_course", y="avg_score", data=df, palette="muted", ax=ax3)
ax3.set_title("📗 Impact of Test Preparation on Scores")
st.pyplot(fig3)

# ---------------------------------------------------------------
# 6️⃣ VISUAL 4 – Correlation Heatmap
# ---------------------------------------------------------------
st.subheader("🔥 Correlation Heatmap")
corr = df[["math_score", "reading_score", "writing_score", "avg_score"]].corr()
fig4, ax4 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
ax4.set_title("🔥 Correlation Between Scores")
st.pyplot(fig4)

# ---------------------------------------------------------------
# 7️⃣ FINAL DASHBOARD – Arrange All Visuals in Subplots
# ---------------------------------------------------------------
st.subheader("🧩 Combined Dashboard View")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.histplot(df["math_score"], kde=True, color="lightblue", ax=axes[0, 0])
axes[0, 0].set_title("Math Score Distribution")

sns.boxplot(x="gender", y="avg_score", data=df, ax=axes[0, 1], palette="pastel")
axes[0, 1].set_title("Performance by Gender")

sns.barplot(x="test_preparation_course", y="avg_score", data=df, ax=axes[1, 0], palette="muted")
axes[1, 0].set_title("Test Preparation Course Effect")

sns.heatmap(corr, annot=True, cmap="viridis", ax=axes[1, 1])
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
st.pyplot(fig)

# ---------------------------------------------------------------
# 💡 BONUS CHALLENGES (Extra Points)
# ---------------------------------------------------------------

# 🟢 Interactivity – Dropdowns and sidebar controls (already added)
st.sidebar.header("Controls")
score_filter = st.sidebar.slider("Filter by Minimum Average Score", 0, 100, 50)
filtered_df = df[df["avg_score"] >= score_filter]

st.sidebar.info(f"Showing students with avg_score ≥ {score_filter}")
st.dataframe(filtered_df)

# 🟡 Export – Save Dashboard as Image (PNG)
if st.button("💾 Export Dashboard as PNG"):
    fig.savefig("student_dashboard.png")
    st.success("✅ Dashboard saved as student_dashboard.png")

# 🔵 Storytelling – Summarize Insights
st.markdown("---")
st.header("💬 Storytelling & Insights")
st.write("""
- Students who **completed test preparation** generally performed better across all subjects.  
- There is a **strong correlation** between reading and writing scores.  
- Math scores show **more variation** compared to reading and writing.  
- Gender performance difference is minor, showing **balanced performance** overall.
""")


# ---------------------------------------------------------------
# 🏆 LEADERBOARD & BADGES SECTION
# ---------------------------------------------------------------
st.markdown("---")
st.header("🏆 Leaderboard & Badges")

leaderboard_data = {
    "Name": ["Jaffar", "Sara", "Ahmed", "Fatima", "Ali"],
    "Average Score": [92, 89, 87, 84, 80],
    "Badge": ["🥇 Data Artist", "🥈 Insight Master", "🥉 Code Picasso", "⭐ Analyst", "🎯 Learner"]
}
leaderboard_df = pd.DataFrame(leaderboard_data)
st.dataframe(leaderboard_df)

top_student = leaderboard_df.iloc[0]
st.success(f"🏅 **Top Performer:** {top_student['Name']} — {top_student['Badge']} with {top_student['Average Score']}%")

# ---------------------------------------------------------------
# 🎯 CREDITS & MOTIVATION
# ---------------------------------------------------------------
st.markdown("---")
st.markdown("""
### 🎯 Credits & Motivation
            
👨‍💻 Created by **JAFFAR HUSSAIN**  
📅 Challenge 2025 — *Student Performance Dashboard*
""")
