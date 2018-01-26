# ArcGIS-MultiSpatialJoin
Spatial join on more than one dataset, and based on a common field

## Description

Spatial join is a useful tool for joining one spatial file to another based on spatial attributes, example "within, closest to". However, it gets complicated if you have this situation as I did.

 * You have a polygon dataset that have several regions over an area.
 * You have a point dataset that needs to be spatial join with...
    * another point layer by closest proximity
    * another point layer by closest proximity
    * and so on...
 * Spatial join must be done per region (now that complicates things).

The first step is to intersect all the point layers with the polygon dataset so that the region field names are added to the point layers.

Then use the given script to automate the rest of the geoprocessing.

## Requirements

Python 2.7, arcpy
