#!/bin/python

import shapefile

sf = shapefile.Reader("D:\Semester 5\GIS\Natural Earth/pulau.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#		if not name.startswitch('__'):
#				print name
