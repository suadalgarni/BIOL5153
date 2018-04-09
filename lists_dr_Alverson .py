#!/usr/bin/env python3

# open and read the file
filename = 'blood_on_the_tracks.txt'
infile = open(filename, 'r')

# declare our list
songs = []

# read each line into a list
for line in infile:
    line = line.strip('\n')
    songs.append(line)

# close the file
infile.close()

# count the tracks
track_num = 1

# print the track listing
for track in songs:
    print(str(track_num) + '. ', track)
    track_num += 1
    
# print number of songs
print("There are", len(songs), "songs on", filename)

print(track)
print(line)
