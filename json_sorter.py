# This script sorts the json data and returns a list of the ids of the top-n songs
# according to the function suit in fit_function.py

import json
import pprint
import fit_function as ff

features = [ "valence", "danceability", "energy", "loudness", "speechiness", 
					"instrumentalness"]



def comp(s1, s2):
	sumSq = 0
	for feat in features:
		sumSq += (s1[feat] - s2[feat])*(s1[feat] - s2[feat])
	sumSq /= len(features)



def bestFit(parameters, n):
	with open('dataset.txt') as json_file:
	    data = json.load(json_file)

	data = data[11:]
	songs = []
	ideal = ff.idealSong(parameters)

	for i in range(0,len(data)):
	    data[i] = data[i][0] # getting rid of the extra arrays
	    data[i]['error'] = comp(ideal, data[i])
	    songs.append([data[i]['error'], data[i]['id']])

	songs = sorted(songs)

	for i in range(0, len(songs)):
		songs[i] = songs[i][1]
	songs = list(set(songs))

	top_songs = songs[-n:] # gets 50 songs with highest fitness function
	return top_songs

test = ff.idealSong([0,0,0,0,0,0])