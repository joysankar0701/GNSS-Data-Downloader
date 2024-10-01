from ftplib import FTP
import glob
import os

def downloadGnssData(year: int, day_start: int, day_end: int, station_names: list[str]):
    ftp_server = 'gssc.esa.int'
    ftp_user = 'anonymous'

    path = f'cddis\gnss\data\daily\{year}'

    ftp = FTP(ftp_server)
    ftp.login(user=ftp_user)
    ftp.cwd(path)
    for i in range(day_start, day_end+1):
      day = f'{i:03}'
      ftp.cwd( f'{day}')
      files = ftp.nlst()
      for station in station_names:
        matching_files = [file for file in files if (file.startswith(station) and (file.endswith('o.Z') or file.endswith('n.Z')))]
        for file in matching_files:
          with open(file, 'wb') as local_file:
              print(f"Downloading {file}...")
              ftp.retrbinary(f"RETR {file}", local_file.write)
      ftp.cwd('..')

    ftp.quit()
    
def downloadGnssDataSpecificDays(year: int, days: list[int], station_names: list[str]):
    ftp_server = 'gssc.esa.int'
    ftp_user = 'anonymous'

    path = f'cddis\gnss\data\daily\{year}'

    ftp = FTP(ftp_server)
    ftp.login(user=ftp_user)
    ftp.cwd(path)
    for i in days:
      day = f'{i:03}'
      ftp.cwd( f'{day}')
      files = ftp.nlst()
      for station in station_names:
        matching_files = [file for file in files if (file.startswith(station) and (file.endswith('o.Z') or file.endswith('n.Z')))]
        for file in matching_files:
          with open(file, 'wb') as local_file:
              print(f"Downloading {file}...")
              ftp.retrbinary(f"RETR {file}", local_file.write)
      ftp.cwd('..')

    ftp.quit()
