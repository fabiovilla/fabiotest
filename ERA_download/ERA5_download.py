# CODICE DA USARE PER IL DOWNLOAD (da sito copernicus):
# import cdsapi
#   client = cdsapi.Client()
#   dataset = "<DATASET-SHORT-NAME>"
#   request = {
#       <SELECTION-REQUEST>
#   }
#   target = "<TARGET-FILE>"
#   client.retrieve(dataset, request, target)


import cdsapi

try:  

    ## DATASET TEMPERATURE ORARIE
    # dataset = "reanalysis-era5-single-levels"
    # request = {
    #     "product_type": [
    #         "reanalysis",
    #         "ensemble_mean"
    #     ],
    #     "variable": ["2m_temperature"],
    #     "year": ["2019"],
    #     "month": ["01", "02", "03","04", "05", "06","07", "08", "09","10", "11", "12"],
    #     "day": [
    #         "01", "02", "03","04", "05", "06","07", "08", "09","10", "11", "12","13", "14", "15","16", "17", "18","19", "20", "21","22", "23", "24",
    #         "25", "26", "27","28", "29", "30","31"
    #     ],
    #     "time": [
    #         "00:00", "01:00", "02:00","03:00", "04:00", "05:00","06:00", "07:00", "08:00","09:00", "10:00", "11:00","12:00", "13:00", "14:00","15:00",
    #         "16:00", "17:00","18:00", "19:00", "20:00","21:00", "22:00", "23:00"
    #     ],
    #     "data_format": "netcdf",
    #     "download_format": "zip",
    #     "area": [47, 6, 40, 17]
    # }


#     # DATASET TEMPERATURE GIORNALIERE
#     dataset = "derived-era5-land-daily-statistics"
#     request = {
#         "variable": [
#             "2m_temperature"
# #            "soil_temperature_level_1"
#         ],
#         "year": "2019",
#         "month": ["01", "02", "03","04", "05", "06","07", "08", "09","10", "11", "12"],
#         "day": [
#             "01", "02", "03","04", "05", "06","07", "08", "09","10", "11", "12","13", "14", "15","16", "17", "18","19", "20", "21","22", "23", "24",
#             "25", "26", "27","28", "29", "30","31"
#         ],
#         "data_format": "netcdf",
#         #"download_format": "zip",
#         "area": [47, 6, 40, 17],
#         "daily_statistic": "daily_mean",
#         "time_zone": "utc+00:00",
#         "frequency": "1_hourly"
#     }

###   ERA5 post-processed daily statistics on single levels from 1940 to present   ###

    dataset = "derived-era5-single-levels-daily-statistics"
    request = {
        "product_type": "reanalysis",
        "variable": ["total_precipitation"],
        "year": "2020",
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "day": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12",
            "13", "14", "15",
            "16", "17", "18",
            "19", "20", "21",
            "22", "23", "24",
            "25", "26", "27",
            "28", "29", "30",
            "31"
        ],
        #"data_format": "netcdf",
        #"download_format": "zip",
        "daily_statistic": "daily_sum",
        "time_zone": "utc+01:00",
        "frequency": "1_hourly",
        "area": [47, 6, 40, 17]
    }


    client = cdsapi.Client()
    target = r'C:\imageo Dropbox\fabio villa\LAVORO_FABIO\SVILUPPO_FABIO\ERA5_DOWNLOAD\download_2020_daily_tot_prec.nc'
    response = client.retrieve(dataset, request, target)
    #client.retrieve(dataset, request).download()

except Exception as errore:
  print(errore)