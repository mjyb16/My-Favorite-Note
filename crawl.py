import re # mp3 file extraction
import os # cmd calls
import urllib.request # file requests

def copyMp3(url, path):
	handle = urllib.request.urlopen(url)
	with open(path, 'wb') as f: f.write(handle.read())

def mp3FromUrl(url):
	html = str(urllib.request.urlopen(url).read())
	return re.findall(r'http:\/\/piano-transcriptions\.narod\.ru\/audio\/[^\.]+\.mp3', html)

def makeArtist(name, path, func):
	url = 'http://piano-play.com/' + name + '.html'
	fNames = mp3FromUrl(url)
	
	os.system('mkdir ' + path)
	os.system('mkdir ' + path + name) # make artist directory
	print('Copying into directory ' + path + name)
	
	for fUrl in fNames:
		fName = fUrl.split('/')[-1]
		fPath = path + name + '/' + fName
		copyMp3(fUrl, fPath)

		func(fName, fPath) # deals with file appropriately
