#!/usr/bin/env python3

'''
	25.07.2023
	Robert Folkenberg Siro
	Nuclear Eng. & Thermal Physics, NRNU MEPhI
	Geospatial (Optical Multispectral & Hyperspectral RS), The Technical University of Kenya 2019
'''

import numpy, matplotlib.pyplot, rasterio, earthpy.plot;
import earthpy.spatial;
from rasterio.plot import plotting_extent;

dir = './data/landsat/';
commn_ext = dir+'LC08_L1TP_170061_20190215_20200829_02_T1_B';
file_lst = [];
for x in range(3, 6):
	file_lst.append(commn_ext+str(x)+'.TIF');
file_lst.sort(reverse=True);

raster_arr, raster_profile = earthpy.spatial.stack(file_lst,\
out_path=dir+'stack_543.tiff');
raster_ext = plotting_extent(raster_arr[0],\
raster_profile["transform"]);
fig, ax = matplotlib.pyplot.subplots(figsize=(7, 7))
earthpy.plot.plot_rgb(raster_arr, ax=ax, extent=raster_ext,\
stretch=True, str_clip=1, title=" COLOR INFRARED BAND COMBINATION");
matplotlib.pyplot.savefig('./output/color.infrared.png')
matplotlib.pyplot.show()

'''
file_lst = numpy.array(file_lst);
band_ref = rasterio.open(file_lst[0], 'r');
met = band_ref.meta.copy().update({'count': 3, 'nodata': -9999});
with rasterio.open("../data/raster/landsat/2019/outputs/stack_234.TIF", 'w', **met) as output:
	for item, bandx in enumerate(file_lst, start=1):
		output.write(bandx, item);

def open_tif(PATH):
	return rioxarray.open_rasterio(PATH,masked=True).squeeze();
tif_lst = [];
for item, bandx in enumerate(file_lst):
	tif_lst.append(open_tif(bandx));
	tif_lst[item]['BAND']=item+1;
arr_val = xarray.concat(tif_lst, dim='BAND').values;
print (arr_val)

'''
