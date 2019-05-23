# My Favorite Note
SteelHacks 2019

## Note: 
1. This code assumes the user will create a folder called /music_partition (in the original usage, a symbolic link to a separate partition) used to store music data. Any references in the code to /music_partition refer to this folder, and can be renamed to suit the user.
2. The "Getting CSVs" code obtains the music for one artist (default = Ray Charles). This code can be run repeatedly with modifications to get as many artists' music as desired or modified to obatin all artists' music. 

## Description:
This project was created during the 2019 SteelHacks hackathon at the University of Pittsburgh. It takes an input of a jazz musician's name, and returns the most common key/quality, average BPM, and average danceability score based on the songs available on http://piano-play.com/transcriptions.html. 

## Dependencies: 
-- Eel framework, https://github.com/ChrisKnott/Eel

-- Essentia library, https://essentia.upf.edu/documentation/

-- Pandas library for python

## Contributions: 
Lizzie Seward: HTML and Javascript front end (found in testing.html)

Gennadi Ryan: Data aquisition, storage, and analysis (found in crawl.py, Getting CSVs.ipynb, and Importing Music.ipynb)

Michael Barth: Data cleaning/analysis (found in SteelHacks.ipynb), Eel implementation (found in SteelHacks.ipynb and testing.html)

Jeffrey Tang: Supporting research

SteelHacks staff: Assisted with Eel implementation
