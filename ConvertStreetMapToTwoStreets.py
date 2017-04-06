import json
from sys import argv
import numpy as np
import math

def main(infile, outfile):
	np.set_printoptions(precision=12)
	dist = 4*math.sqrt(pow(1.0/111000.0,2))
	data = json.load(open(infile))
	data2 = { "type": "FeatureCollection", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, "features": []}
	for feature in data['features']:
		aFeature = {}
		bFeature = {}
		coords = feature['geometry']['coordinates']
		aFeature['properties'] = bFeature['properties'] = feature['properties']
		aFeature['type'] = bFeature['type'] = feature['type']
		aFeature['geometry'] = { "type": "LineString", "coordinates": []}
		bFeature['geometry'] = { "type": "LineString", "coordinates": []}
		''' 
		See that we don't go above limit when setting second point
		*** Remember also that coordinates is an array of arrays of tuple-lists ***
		'''
		if feature['properties']['fclass'] in ["primary", "secondary", "tertiary", "residential"]: # not sure if we should add "service"
			lineString = coords
			lineStringA = []
			lineStringB = []
			tempLeftLine = [0.0, 0.0]
			tempRightLine = [0.0, 0.0]
			# lineString is an list of coordinates
			while len(lineString) > 1:
				# coords is an element (itself a list of two doubles) of the line
				point1 = np.array(lineString[0])
				point2 = np.array(lineString[1])
				if (np.array_equal(point1, point2)):
					if (len(lineString)>2):
						del lineString[1]
						continue
					else:
						break
				tempLeftLine[0], tempLeftLine[1], tempRightLine[0], tempRightLine[1] = computeFourOrthoganalPointsDistanceAway(point1, point2, dist)
				# Currently the format is not lat long it's long lat and that's just messed up so we convert it here
				lineStringA.append(tempLeftLine[0])
				lineStringB.append(tempRightLine[0])
				del lineString[0]
			lineStringA.append(tempLeftLine[1])  # add the final point
			lineStringB.append(tempRightLine[1]) # add the final point
			aFeature['geometry'] = {"type": "LineString", "coordinates": lineStringA[:]}
			bFeature['geometry'] = {"type": "LineString", "coordinates": lineStringB[:]}
			data2['features'].append(aFeature)
			data2['features'].append(bFeature)
	with open(outfile, 'w') as outfileobj:
		json.dump(data2, outfileobj)


def computeFourOrthoganalPointsDistanceAway(point1, point2, d):
	'''
	coords is a 2D numpy array for calculations
	returns two tuples of two coordinates (list of two doubles)
	'''
	det = (d/np.linalg.norm(point1-point2))*(np.array([point1[1]-point2[1], point2[0]-point1[0]]))
	# Vectorized code
	return (point1+det).tolist(), (point2+det).tolist(),(point1-det).tolist(), (point2-det).tolist()

if __name__ == '__main__':
	infile = argv[1]
	outfile = argv[2]
	main(infile, outfile)
