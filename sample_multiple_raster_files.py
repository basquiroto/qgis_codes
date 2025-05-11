# layer with the points to sample the raster data.
point_lyr = QgsProject.instance().mapLayersByName('point_lyr')[0]

# name of the raster layers
rst_lst = ['29253se', 'Orto-RGB_SH-22-X-B-II-3-SE-F', 'imagem_google_20250426']

for index, raster_name in enumerate(rst_lst):
	raster_lyr = QgsProject.instance().mapLayersByName(raster_name)[0]
	print(index)
	
	if index == 0:
		params = {'COLUMN_PREFIX':'SAMPLE_',
		'INPUT' : point_lyr,
		'OUTPUT' : 'TEMPORARY_OUTPUT',
		'RASTERCOPY' : raster_lyr}

		result = processing.run('native:rastersampling', params)
		result_lyr = result['OUTPUT']
		
	else:
		params = {'COLUMN_PREFIX':'SAMPLE_',
		'INPUT' : result_lyr,
		'OUTPUT' : 'TEMPORARY_OUTPUT',
		'RASTERCOPY' : raster_lyr}

	result = processing.run('native:rastersampling', params)
	result_lyr = result['OUTPUT']

QgsProject.instance().addMapLayer(result_lyr)

"""
If there are columns with empty/null values, run this function in the field calculator to extract the first non-null value.
coalesce( "SAMPLE_1" , "SAMPLE_1_2" , "SAMPLE_1_3" , "SAMPLE_1_4" , "SAMPLE_1_5" , "SAMPLE_1_6" , "SAMPLE_1_7" , "SAMPLE_1_8" , "SAMPLE_1_9" , "SAMPLE_1_10" , "SAMPLE_1_11" , "SAMPLE_1_12" , "SAMPLE_1_13" , "SAMPLE_1_14" , "SAMPLE_1_15" , "SAMPLE_1_16" , "SAMPLE_1_17" , "SAMPLE_1_18" , "SAMPLE_1_19" , "SAMPLE_1_20" , "SAMPLE_1_21", "SAMPLE_1_22", "SAMPLE_1_23", "SAMPLE_1_24", "SAMPLE_1_25", "SAMPLE_1_26", "SAMPLE_1_27", "SAMPLE_1_28", "SAMPLE_1_29", "SAMPLE_1_30", "SAMPLE_1_31", "SAMPLE_1_32", "SAMPLE_1_33", "SAMPLE_1_34", "SAMPLE_1_35", "SAMPLE_1_36", "SAMPLE_1_37", "SAMPLE_1_38", "SAMPLE_1_39", "SAMPLE_1_40", "SAMPLE_1_41", "SAMPLE_1_42", "SAMPLE_1_43", "SAMPLE_1_44" )
"""