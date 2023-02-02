import pandas as pd
import numpy as np
pd.read_csv('https://data.cityofnewyork.us/resource/erm2-nwe9.csv?$query=select unique_key, created_date, closed_date, complaint_type, descriptor, location_type, incident_zip, bbl, borough, latitude, longitude limit 50 ').to_csv('311.csv', index=False, sep=',')

