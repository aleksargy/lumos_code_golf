import streamlit as st
import pandas as pd
import requests
import time

# --- HOLE CHALLENGE DESCRIPTIONS ---
hole_descriptions = {
    1: "Return the nth palindromic prime. (A number that is both a palindrome and a prime.)",
    
    2: "Given a list of (x, y) points, return the slope and intercept (a, b) of the line using linear regression. Use `numpy`, but no `scipy` or `statistics`.",
    
    3: "Return a 5×5 2D list of 0s and 1s forming an 'X' pattern. (1s on both diagonals, 0s elsewhere.)",
    
    4: "Print numbers 1–15 in one line with FizzBuzz rules applied. Output must be space-separated in a single print statement.",
    
    5: "Translate a DNA string into amino acids using 3-letter codons. Return a string of single-letter amino acid codes.",

    6: "[Bonus Round!](https://aiorphoto.com/)",
    
    7: "Return `True` if the computer has internet access. Use only the standard library (e.g. `socket`, `urllib`).",
    
    8: "Return today’s date in YYYY-MM-DD format using as little code as possible.",
        
    9: "Generate a random haiku with the 5-7-5 syllable structure."
}


# --- CONFIGURATION ---
url = "https://script.google.com/macros/s/AKfycbzv2g5JNmgYPUQWcuxpelfGWBPqTPelOGiZdUdfC4SZbF3_1Ko3FV3UFr4Dv2XZ9aNb/exec"

st.set_page_config(page_title="Lumos Code Golf", layout="wide")
st.title("🏌️‍♂️ Lumos Goes Golfing")
st.markdown("Fore! Shortest code wins.")

# --- LOAD DATA ---
try:
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    df["length"] = df["length"].astype(int)
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# --- BEST SUBMISSION PER HOLE ---
best_per_hole = (
    df.groupby(["participant", "hole"])
    .agg({"length": "min"})
    .reset_index()
)

# --- SCOREBOARD ---
scoreboard = (
    best_per_hole.groupby("participant")
    .agg({"length": "sum"})
    .reset_index()
    .rename(columns={"length": "total_score"})
    .sort_values("total_score")
)

st.subheader("🏆 Overall Scores")
st.dataframe(scoreboard.reset_index(drop=True), use_container_width=True)

for hole in range(1, 10):
    with st.expander(f"⛳ Hole {hole}"):
        st.markdown(f"{hole_descriptions.get(hole, 'No description available.')}")

        subset = best_per_hole[best_per_hole["hole"] == hole].sort_values("length")
        st.markdown("**🏆 Submissions:**")
        st.dataframe(subset[["participant", "length"]].reset_index(drop=True), use_container_width=True)


# --- FIXED AUTO-REFRESH EVERY 10 SECONDS ---
time.sleep(20)
st.rerun()

