# Author: Joysankar Majumdar, 2024, BHU, Varanasi

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
        matching_files = [file for file in files if (file.startswith(station) and (file.endswith('o.Z') or file.endswith('n.Z') or file.endswith('o.gz') or file.endswith('n.gz')))]
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
        matching_files = [file for file in files if (file.startswith(station) and (file.endswith('o.Z') or file.endswith('n.Z') or file.endswith('o.gz') or file.endswith('n.gz')))]
        for file in matching_files:
          with open(file, 'wb') as local_file:
              print(f"Downloading {file}...")
              ftp.retrbinary(f"RETR {file}", local_file.write)
      ftp.cwd('..')

    ftp.quit()

def unzipZfiles():
    import patoolib
    os.chdir('.')
    for filename in os.listdir():
        if filename.endswith('.Z'):
            patoolib.extract_archive(filename, outdir='.')
            os.remove(filename)
            print(f"Extracted and deleted: {filename}")


def unzipgzfiles():
    import patoolib
    os.chdir('.')
    for filename in os.listdir():
        if filename.endswith('.gz'):
            patoolib.extract_archive(filename, outdir='.')
            os.remove(filename)
            print(f"Extracted and deleted: {filename}")
