import streamlit as st
import pandas as pd
import requests

# Load data (from Google Sheet JSON endpoint)
url = "https://api.sheety.co/2caf3187832c60cabf5169409f671a57/codeGolfLeaderboard/sheet1"
data = requests.get(url).json()["scores"]

df = pd.DataFrame(data)
df["length"] = df["length"].astype(int)

st.title("🏆 Code Golf Leaderboard")
st.markdown("Live submissions from participants")

# Leaderboard view
leaderboard = (
    df.groupby(["participant", "hole"])
    .agg({"length": "min"})
    .reset_index()
    .sort_values(by="length")
)

for hole in sorted(df["hole"].unique()):
    st.subheader(f"⛳ Hole {hole}")
    subset = leaderboard[leaderboard["hole"] == hole]
    st.table(subset[["participant", "length"]])
