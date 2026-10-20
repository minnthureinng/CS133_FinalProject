# Student submission for Milestone 0
"""
DATASET: Formula 1 World Championship (1950 - 2024)
SOURCE: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020
DESCRIPTION: Results of every Formula 1 race from 1950 to 2024 (1,125 races),
including each driver's starting grid position, finishing position, team,
circuit, and reason for finishing or retiring. Used to answer: how much does
qualifying (starting) position decide the race?
The dataset has 14 linked CSV files; the main table is results.csv, joined
to races, drivers, constructors, circuits, and status by ID columns.

DATA DICTIONARY (results.csv - main table):
- resultId: Unique ID for each result
- raceId: Race ID (links to races.csv)
- driverId: Driver ID (links to drivers.csv)
- constructorId: Team ID (links to constructors.csv)
- number: Car number
- grid: Starting position (1 = pole, 0 = pit lane start)
- position: Finishing position (blank if not classified)
- positionText: Finishing position or code (R = retired, D = disqualified,
                W = withdrew, F = failed to qualify, N = not classified)
- positionOrder: Final order including non-finishers
- points: Championship points earned
- laps: Laps completed
- time: Winner's race time or gap to winner (e.g. "+5.478")
- milliseconds: Race time in milliseconds
- fastestLap: Lap number of driver's fastest lap
- rank: Rank of driver's fastest lap in the race
- fastestLapTime: Fastest lap time (e.g. "1:27.452")
- fastestLapSpeed: Average speed on fastest lap (km/h)
- statusId: Finish/retirement reason (links to status.csv, e.g. Finished,
            Engine, Collision, +1 Lap)

Supporting tables:
- races.csv: raceId, year, round, circuitId, name, date, time, session dates
- circuits.csv: circuitId, name, location, country, lat, lng, alt
- drivers.csv: driverId, forename, surname, code, number, dob, nationality
- constructors.csv: constructorId, name, nationality
- qualifying.csv: raceId, driverId, position, q1, q2, q3 lap times (1994+)
- status.csv: statusId, status description

INITIAL QUALITY AUDIT (results.csv):
- Rows: 26,759
- Columns: 18
- Missing values (stored as "\\N" in the file):
  - position: 10,953 missing (40.9%) -> drivers who did not finish
  - time / milliseconds: 19,079 missing (71.3%) -> only for lead-lap cars
  - fastestLap / fastestLapTime / fastestLapSpeed: 18,507 missing (69.2%)
    -> only recorded from 2004 onwards
  - rank: 18,249 missing (68.2%)
  - number: 6 missing (0.02%)
- Data types: 15 numeric, 3 object
- Duplicates: 0 duplicate rows (91 cases of the same driver twice in one race,
  which is real: 1950s drivers sometimes shared or switched cars)
- Outliers / problems:
  - grid = 0 for 1,638 results (6.1%): pit-lane starts, not real positions
  - Times stored as text ("1:27.452") and need converting to seconds
  - Only 28.7% of results have status "Finished"
  - Pit stops (2011+) include 517 stops over 60 seconds (max 3,069 s) caused
    by red flags; lap times include 708 laps over 5 minutes
  - Coverage differs: results go back to 1950, qualifying 1994, pit stops 2011
- Other tables: 14 files, about 701,000 rows in total; lap_times.csv is the
  largest (589,081 rows)
"""
