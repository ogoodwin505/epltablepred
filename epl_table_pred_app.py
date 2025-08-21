import streamlit as st
import requests
import json
import os

# Constants
API_URL = "https://api.football-data.org/v4/competitions/PL/standings"
API_TOKEN = "1ca7105fa42b4e6ba3d6a2e1b9c4d30f"  # Replace with your football-data.org API token
PREDICTIONS_FILE = "predictions.json"
TEAMS = [
    "Manchester City FC",
    "Sunderland AFC",
    "Tottenham Hotspur FC",
    "Liverpool FC",
    "Nottingham Forest FC",
    "Arsenal FC",
    "Leeds United FC",
    "Brighton & Hove Albion FC",
    "Fulham FC",
    "Aston Villa FC",
    "Chelsea FC",
    "Crystal Palace FC",
    "Newcastle United FC",
    "Everton FC",
    "Manchester United FC",
    "AFC Bournemouth",
    "Brentford FC",
    "Burnley FC",
    "West Ham United FC",
    "Wolverhampton Wanderers FC"
]

# Helper functions
def load_predictions():
    if os.path.exists(PREDICTIONS_FILE):
        with open(PREDICTIONS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_predictions(predictions):
    with open(PREDICTIONS_FILE, "w") as f:
        json.dump(predictions, f)

def fetch_current_table():
    headers = {"X-Auth-Token": API_TOKEN}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Extract team names in order
        standings = data["standings"][0]["table"]
        return [team["team"]["name"] for team in standings]
    else:
        st.error("Failed to fetch EPL table. Check your API token.")
        return []

def calculate_score(prediction, current_table):
    score = 0
    for i, team in enumerate(prediction):
        if i < len(current_table) and team == current_table[i]:
            score += 10
    return score

# Streamlit UI
st.title("EPL Table Prediction Game 2025/2026")
st.write("Enter your predicted final EPL table. Scores update as the season progresses!")

# Player name
player = st.text_input("Enter your name:")

# Prediction form
st.write("Rank the teams from 1st to 20th by selecting them in order:")
prediction = st.multiselect(
    "Select teams in your predicted order (top to bottom)",
    options=TEAMS,
    default=[],
    key="prediction_multiselect"
)

if st.button("Submit Prediction"):
    if player and prediction and len(prediction) == 20 and len(set(prediction)) == 20:
        predictions = load_predictions()
        predictions[player] = prediction
        save_predictions(predictions)
        st.success("Prediction saved!")
    else:
        st.error("Please enter your name and select all 20 teams in your predicted order.")

# Fetch current EPL table

# Calculate Scores button
if st.button("Calculate Scores"):
    st.header("Current EPL Table")
    current_table = fetch_current_table()
    if current_table:
        st.write(current_table)

    st.header("Leaderboard")
    predictions = load_predictions()
    leaderboard = []
    for player_name, pred in predictions.items():
        score = calculate_score(pred, current_table)
        leaderboard.append((player_name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    st.table(leaderboard)

    st.caption("10 points for each team in the correct position. Scores update as the table updates.")
