# GNSS-Data-Downloader
It is python package for downloading naviation(n) and observation(o) files for various IGS stations with specific days.
## Tutorial
- Download the `gnss_data_downloader.py` file from here and put it in a directory where you want to download your n.Z and o.Z files.
- Use jupyter notebook or normal python, and import this as `import gnss_data_downloader as gnss`.
- Two functions are available `gnss.downloadGnssData` to downlaod all data between two days of the year and `gnss.downloadGnssDataSpecificDays` to downlaod data for some specific days of the year.
To downlaod data for some specific days in a year with some specific stations. Use the code given below.
```python
import gnss_data_downloader as gnss
year = 2024
specific_days = [100,101,102,103]
stations = ['iisc','lck4','hyde']
gnss.downloadGnssDataSpecificDays(year,specific_days,stations)
```
The days should be as day of the year. In future I'll update it as normal date to add more flexibility.
To downlaod data for days in a range in a year with some specific stations. Use the code given below.
```python
import gnss_data_downloader as gnss
year = 2024
start_day = 1
end_day = 100
stations = ['iisc','lck4','hyde']
gnss.downloadGnssData(year,start_day,end_day,stations)
```
