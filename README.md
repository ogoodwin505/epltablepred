# EPL Predictions League Scorer

A simple Python app to run and score an **EPL predictions league**.  
Users submit their predicted Premier League tables, and the app compares them against the actual final standings (fetched via an API) to award points and determine who made the best prediction.

## Features

- Accepts user-submitted predictions
- Fetches the actual EPL table via API
- Compares predictions against real standings
- Scores predictions based on accuracy (e.g. exact positions, close positions, etc.)
- Outputs results in JSON (`predictions.json`)
- Lightweight and easy to run locally

## Requirements

- Python 3.7+
- Internet access (to fetch EPL table data via API)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ogoodwin505/epltablepred.git
   cd epltablepred
