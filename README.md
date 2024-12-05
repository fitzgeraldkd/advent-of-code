# Advent of Code

Here's my repo for my [Advent of Code](https://adventofcode.com/) solutions. I'm currently migrating my old repo over to this one now that I have a clearer idea of how I want to structure everything.

## Setup

Install required packages with:
```bash
pip install -r requirements.txt
```

A directory for a new puzzle can be created by running (this example sets up the directory for year 2015 day 1):
```bash
./init.sh 2015 1
```

## Testing

The tests for all puzzles can be run with:

```bash
python -m unittest
```

Or a specifiy year or day can be run with:
```bash
python -m unittest discover solutions.year_2015
python -m unittest discover solutions.year_2015.day_01
```

## Progress

|        | 2015  | 2016  | 2017  | 2018  | 2019  | 2020  | 2021  | 2022  | 2023  | 2024  |
| :----: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Day 1  | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | 🟢 🟢 |
| Day 2  | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | 🟢 🟢 |
| Day 3  | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | 🟢 🟢 |
| Day 4  | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | 🟢 🟢 |
| Day 5  | 🟢 🟢 | 🟢 🟡 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 6  | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 7  | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 8  | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 9  | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 10 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 11 | 🟢 🟢 | 🟡 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 12 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 13 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 14 | 🟢 🟢 | 🟢 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟡 | ⚪️ ⚪️ |
| Day 15 | 🟢 🔵 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 16 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ |
| Day 17 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 18 | 🟢 🟢 | 🟢 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 19 | 🟢 🟢 | 🟢 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 20 | 🟡 🟡 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 21 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 22 | 🟡 🟡 | 🟢 🟠 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 23 | 🟢 🟢 | 🟢 🟡 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 24 | 🟡 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |
| Day 25 | 🟢 🟢 | 🟢 🟢 | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ | ⚪️ ⚪️ |

Key:
- 🟢: Solved
- 🔵: Solved, but with notes on possible optimizations or needs testing
- 🟡: Solved, but inefficient (> 15 seconds to execute)
- 🟠: Solved, with manual intervention
- 🔴: Unsolved / stuck
- ⚪️: Not started
