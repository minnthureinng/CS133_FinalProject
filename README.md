# CS133_FinalProject
F1 Pole Position Analysis 
# Pole Position Power: How Much Does Qualifying Decide a Formula 1 Race?

## Author
- Minn Thurein Naung @ minnthureinng (https://github.com/minnthureinng/CS133_FinalProject)

## Project Description
This project analyzes every Formula 1 World Championship race from 1950 to 2024 to measure how much a driver's starting position decides the race result. I use the Formula 1 World Championship dataset from Kaggle: 14 related tables covering 1,125 races, 861 drivers, 212 teams, and 77 circuits. My main question is how often the driver starting on pole position wins, and whether that advantage differs by circuit (for example, tight street tracks like Monaco versus high-speed tracks like Monza) and across eras of the sport. In an early look at the data, the pole sitter won 481 of 1,136 races (42.3%), so starting first helps a lot but does not guarantee a win. I will clean and join the data, test these differences with statistics, and present my findings through static charts, a map of circuits, and an interactive dashboard.

## Project Outline/Plan

### Interface Plan
**Jupyter notebooks** in this repository walk through each stage (data cleaning, statistical tests, and static charts) with explanations next to the code.

### Data Collection and Storage Plan
- **Source:** [Formula 1 World Championship (1950 - 2024) https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020 
- **Main tables for my question:**
- `results.csv` (start and finish position for each driver in each race),
- `races.csv` (season, date, circuit),
- `circuits.csv` (location, latitude/longitude),
- `drivers.csv`, `constructors.csv`, `qualifying.csv`, and `status.csv` (why a car finished or retired)
  
- **Storage:** The raw CSVs go in `data/raw/` and are not changed. Cleaned tables are saved to `data/processed/`. Because the raw files are large and publicly available, they are listed in `.gitignore`, and users download them from Kaggle by following the steps below.
- **Cleaning steps I have already identified (Milestone 0 audit):**
  - Convert the `\N` placeholders (160,076 cells) to real missing values.
  - Convert lap times and gaps stored as text (e.g. `"1:26.572"`) into seconds.
  - Handle the 1,638 results with grid position 0 (pit-lane starts).
  - Group non-finishers using `statusId` instead of dropping them.
  - Note that qualifying data only starts in 1994 and pit stops in 2011.
  - Flag red-flag outliers in lap and pit times.
- **Joining:** Tables are linked using `raceId`, `driverId`, `constructorId`, `circuitId`, and `statusId`, which gives one analysis table with one row per driver per race.

### Data Analysis and Visualization Plan
- **Descriptive statistics:** Win rate, podium rate, and average finishing position by starting position, with breakdowns by circuit, decade, and team.
- **Statistical tests:**
  - **Chi-square test:** Is finishing on the podium independent of starting in the top 3?
  - **ANOVA:** Does the pole sitter's win rate differ across eras (e.g. 1950s-70s, 1980s-90s, 2000s, 2010s-20s)?
  - **Correlation (Spearman):** How strongly do grid position and finishing position move together, and is this relationship getting stronger over time?
- **Static visualizations (at least 5, colorblind-friendly palette):**
  1. Bar chart: win rate by starting position.
  2. Line chart: pole-to-win rate by decade.
  3. Heatmap: grid position vs. finishing position.
  4. Ranked bar chart: circuits where pole matters most and least.
  5. Stacked bar chart: reasons for retirement over time (reliability).
- **Interactive visualization:** The Plotly dashboard described in the Interface Plan.
- **Optional machine learning:** A model that predicts whether a driver finishes on the podium from grid position, team, circuit, and season, compared against a simple baseline.
- **Bias and limitations:** Rule changes over 75 years (points systems, qualifying formats, grid sizes) make some comparisons across eras unfair. Early seasons have less complete data, and team dominance can be mixed up with the effect of pole position.
