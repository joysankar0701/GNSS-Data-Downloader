# GNSS-Data-Downloader
It is python package for downloading naviation(n) and observation(o) files for various IGS stations with specific days.
## Tutorial
- Download the `gnss_data_downloader.py` file from here and put it in a directory where you want to download your n.Z or n.gz and o.Z or o.gz files.
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
The files will be in .Z format, so you can manually extract the files or use the code written below.
To use this you need to install `patool` library. To install it, use
```bash
pip install patool
```
Then you can run this code below -
```python
import gnss_data_downloader as gnss
gnss.unzipZfiles()
gnss.unzipgzfiles()
```
This function will extract all the .Z or .gz files to get the raw data in the directory and after extracting it will remove the .Z or .gz files as well.
## Reference
If you are using this code to download the IGS data then acknowledge me (Joysankar Majumdar).
