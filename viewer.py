#pip install laspy
#pip install PDAL
import numpy as np
import laspy
import json
import pdal

# 파일 경로
file_path = 'C:\\Users\\c1203\\Downloads\\DJI_20230802124203_0001_Zenmuse-L1-mission_sbet.out'

with open(file_path, 'r') as file:
    content = file.read()
    
print(content)
