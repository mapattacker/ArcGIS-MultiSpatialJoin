import arcpy
import os


# get list of unique values from field
def unique(table, field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        listset = set([row[0] for row in cursor]) # remove duplicates
        return list(listset)

table = "C:\Users\fake\Documents\ArcGIS\singapore.gdb\main"
field = 'field_name'
listset = unique(table, field)



# for each value in list, create definition query based on each field value
workspace = "C:\Users\siyang\Documents\ArcGIS\\nearest.gdb"
for num, i in enumerate(listset, 1):
    # where clause for definition query for each layer
    where = "field_name = '{}'".format(i)

    # input names
    pa_main = os.path.join(workspace,"main")
    community = os.path.join(workspace,"near1")
    resident = os.path.join(workspace,"near2")
    
    # output layer names
    main_lyr = "main_lyr{}".format(num)
    near1_lyr = "near1_lyr{}".format(num)
    near2_lyr = "near2_lyr{}".format(num)


    # create definition queries
    arcpy.MakeFeatureLayer_management(pa_main, pa_lyr, 
                                        where_clause=where)
    arcpy.MakeFeatureLayer_management(community, cc_lyr, 
                                        where_clause=where)
    arcpy.MakeFeatureLayer_management(resident, rc_lyr, 
                                        where_clause=where)

    # spatial join pa & cc (in memory)
    arcpy.SpatialJoin_analysis(main_lyr, near1_lyr, 'in_memory/join1',
                                match_option='CLOSEST')

    # spatial join pa & rc
    i = i.replace(' ', '_')
    arcpy.SpatialJoin_analysis('in_memory/join1', near2_lyr, 
                                os.path.join(workspace, 'output_{}'.format(i)),
                                match_option='CLOSEST')

    # remove in memory dataset
    arcpy.Delete_management("in_memory/join1")
    print i, 'done'

