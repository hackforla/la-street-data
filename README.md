# la-street-data
Datasets about LA streets

OSM_BSS_AND_PPD.geojson Intersection of Preferential Parking Districts and BSS street sweeping routes
OSM_BSS_NOT_PPD.geojson BSS sweeping routes that do not overlap PPDs 
Both geojson files contain the following:
--
Street sweeping rules for each street.
___
	Has: 
		Road Names
		Route Numbers
		Sweeping Times
		Boundries
		LineStrings for coordinaties

---
ParserForStreetSweeping.py
Parser for Street Sweeping Routes...
input: Non-uniformly formatted csv from BSS data on data.lacity.gov
---
ConvertStreetMapToTwoStreets.py
Converter for OSM_BSS_* Files to geojson files containing two streets for every street (user configurable to restrict to specified types of streets from OSM)
input above geojson files
output: set of two street lines projected d distance away from initial OSM street lines
---
Caution: CRS84 projections are from QGIS and do not overlay perfectly on coordinates for streets that Google maps uses.
