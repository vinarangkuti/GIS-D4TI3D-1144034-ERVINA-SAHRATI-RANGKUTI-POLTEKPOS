>**GEOGRAPHIC INFORMATION SYSTEM PROJECT - MEETING 5**
------------------------------------------------------

	
	In the use of Geographic Information Systems, there are many among us who do not know how to use the data in geospatial data. At the 5th meeting of the Geographic Information System, I'll explain how to create geospatial data in shapefile import and incorporate variablenya using python programming language and also how to use classes and methods in python.
	
Creating a Geospatial Data
1. Import shapefiles
2. Enter the variable, eg a variable to shapefile.writer ()
a = shapefile.writer ()
So, make geospatial data formats No 2, namely:
1. shp => a.point (x, y)
a.poly [(x, y), (v, w)]
2. .dbf => a.field ( 'name.field', 'c', '40')
a.record ( 'bdg')
Geospatial data is stored using a method a.save ( 'file.shp').
Meaning of the method in the writer:
- Point (x, y): insert data in the form of paint into shp and all data must be formatted ESRI.1
- Poly [(a, b), (c, d)]: polygon-shaped insert geospatial data (back to the starting point) or polyline (not back to point early).
- Field ( 'name', 'c', '40'): it means making the polygon attribute table 'name' with varchar data type with a length of 40. This method can be repeated and can be done for krbuthan new field again.
- Record ( 'Bandung'): Filling table which only one field with the value 'Bandung'.
- Save ( 'nama.file'): save file to save the file.


	






