# Creating a JSON structure with the provided classic science fiction movies information
import json

classic_sci_fi_movies = [
    {"title": "Blade Runner", "year": 1982, "director": "Ridley Scott", "plot": "In a dystopian future, a blade runner must pursue and terminate four replicants who stole a ship in space and have returned to Earth to find their creator."},
    {"title": "2001: A Space Odyssey", "year": 1968, "director": "Stanley Kubrick", "plot": "The film follows a voyage to Jupiter with the sentient computer HAL after the discovery of a mysterious monolith affecting human evolution."},
    {"title": "Metropolis", "year": 1927, "director": "Fritz Lang", "plot": "In a futuristic city sharply divided between the working class and the city planners, the son of the city's mastermind falls in love with a working-class prophet who predicts the coming of a savior to mediate their differences."},
    {"title": "The Day the Earth Stood Still", "year": 1951, "director": "Robert Wise", "plot": "An alien lands and tells the people of Earth that they must live peacefully or be destroyed as a danger to other planets."},
    {"title": "Forbidden Planet", "year": 1956, "director": "Fred M. Wilcox", "plot": "A starship crew goes to investigate the silence of a planet's colony only to find two survivors and a deadly secret that one of them has."},
    {"title": "A Clockwork Orange", "year": 1971, "director": "Stanley Kubrick", "plot": "In the future, a sadistic gang leader is imprisoned and volunteers for a conduct-aversion experiment, but it doesn't go as planned."},
    {"title": "Solaris", "year": 1972, "director": "Andrei Tarkovsky", "plot": "A psychologist is sent to a station orbiting a distant planet in order to discover what has caused the crew to go insane."},
    {"title": "Alien", "year": 1979, "director": "Ridley Scott", "plot": "The crew of a commercial spacecraft encounter a deadly lifeform after investigating an unknown transmission."},
    {"title": "The War of the Worlds", "year": 1953, "director": "Byron Haskin", "plot": "Earth is invaded by Martians with unbeatable weapons and a cruel sense of humor."},
    {"title": "The Time Machine", "year": 1960, "director": "George Pal", "plot": "A man's quest for knowledge turns into a desperate race through time after he invents a machine that can transport him through time."}
]

# Specify the file path for the JSON file
file_path = 'classic_sci_fi_movies.json'

# Writing the data to a JSON file
with open(file_path, 'w') as file:
    json.dump(classic_sci_fi_movies, file, indent=4)
