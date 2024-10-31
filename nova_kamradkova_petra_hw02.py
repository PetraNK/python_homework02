import json
import csv

# Decade calculator
def get_decade(year):
    return (year // 10) * 10

# Functions for loading and processing data from one file to another
def netflix_data_reader(input, output):
    data = []

    with open(input, mode='r', encoding='utf-8') as netflix_data:
        netflixTable = csv.DictReader(netflix_data, delimiter='\t')

        for row in netflixTable:
            # Column selection by rows
            # selecting only the following data: title, list of directors, list of actors, list of genres, year of release
            title = row["PRIMARYTITLE"]
            directors = row["DIRECTOR"].split(',') if row["DIRECTOR"] else []
            cast = row["CAST"].split(',') if row["CAST"] else []
            genres = row["GENRES"].split(',') if row["GENRES"] else []
            start_year = int(row["STARTYEAR"])
            decade = get_decade(start_year)
            
            # Dictionary creating
            item = {
                "title": title.strip(),
                "directors": [d.strip() for d in directors] if directors else [],
                "cast": [c.strip() for c in cast] if cast else [],
                "genres": [g.strip() for g in genres],
                "decade": decade
            }

            # List filling with obtained data
            data.append(item)
    
    # Save the resulting list to JSON file
    with open(output, mode='w', encoding='utf-8') as netflix_json:
        json.dump(data, netflix_json, ensure_ascii=False, indent=4)


# Variables:
input = 'netflix_titles.tsv'
output = 'hw02_output.json'

# Function call:
netflix_data_reader(input, output)