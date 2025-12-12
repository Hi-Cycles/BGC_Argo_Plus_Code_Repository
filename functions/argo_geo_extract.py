import xarray as xr
import numpy as np
from multiprocessing import Pool


def argo_prof_lat_lon_extract(argo_path, file, var_select, basin_select, lat_lims=None, lon_lims=None):
    try:
        argo_n = xr.load_dataset(argo_path+file)
        argo_n = argo_n.set_coords(('PRES_ADJUSTED','LATITUDE','LONGITUDE','JULD'))
    except:
        print(file + ' failed to load')
        return


    var_list = list(argo_n.data_vars)

    for var in var_select:
        if var not in var_list: 
            # print('Skipping')
            continue
            
        if basin_select != 'Global': # filter argo_n using lat/lon limits
            prof_index = ((argo_n.LATITUDE >= lat_lims[0]) & (argo_n.LATITUDE <= lat_lims[1]) & 
                                    (argo_n.LONGITUDE >= lon_lims[0]) & (argo_n.LONGITUDE <= lon_lims[1]))
            if np.sum(prof_index)==0:
                continue
            argo_n = argo_n.isel(N_PROF=prof_index)
                                    
        var_trimmed = argo_n[var].where(~np.isnan(argo_n[var]), drop=True)
        
        wmo_n = argo_n.PLATFORM_NUMBER.values.astype(int)[0]

        prof_loc = xr.Dataset()
        prof_loc['wmo']=(['N_PROF'],np.repeat(wmo_n,len(var_trimmed)))

        prof_loc['LATITUDE'] = (['N_PROF'], var_trimmed.LATITUDE.data)
        prof_loc['LONGITUDE'] = (['N_PROF'], var_trimmed.LONGITUDE.data)
        prof_loc['juld'] = (['N_PROF'],var_trimmed.JULD.data)

        # # append all files into one long xarray
    return