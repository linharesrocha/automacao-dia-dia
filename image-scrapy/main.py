from urllib.request import urlopen
import pandas as pd
from requests import get
from io import BytesIO
from PIL import Image

data = pd.read_csv('url_check.csv')

height_list = []
width_lsit = []
url_list = []

aux = 1
for url in data['URL']:
    print(str(aux) + '/' + str(len(data['URL'])))
    image_raw = get(url)
    try:
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        height_list.append(height)
        width_lsit.append(width)
        url_list.append(url)
    except:
        height_list.append('ERROR')
        width_lsit.append('ERROR')
        url_list.append(url)
    aux = aux + 1

dicionario = {'largura': width_lsit, 'altura': height_list, 'url': url_list}
data_pronto = pd.DataFrame(dicionario)
print(data_pronto)
data_pronto.to_excel('url_com_dimensao.xlsx', index=False)