from bs4 import BeautifulSoup
import requests  
import time

print('Tell me what makes an optic bad')
bad_optic=input ('>')
print(f'Filtering out {bad_optic}')
def scrape_optic():
    print('Scraping please wait ...')
    html_text = requests.get('https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html').text
    soup=BeautifulSoup(html_text, 'lxml')
    optics= soup.find_all('tr', class_='grouped-item')
    count=0
    for index, optic in enumerate(optics) :
        optics_delivery=optic.find('span', class_='deliveryTime').text.replace(' ','')
        if "3" in optics_delivery :
            optics_name=optic.find('a', class_='link').text.replace('  ','')
            optics_price=optic.find('span', class_='price').text.replace(' ','')
            more_info = optic.td.a['href']
            if bad_optic not in optics_price:
                    with open(f'optics/{index}.txt', 'w') as f:
                        f.write(f'OPTICS_NAME : {optics_name}')
                        f.write(f'\n OPTICS_PRICE : {optics_price}')
                        f.write(f'\nOPTICS_DELIVERY : "{optics_delivery}')
                        f.write(f'\nMore info : {more_info}' )
                        count+=1
                    print(f'File saved {index}')
                    print(f'{count} files saved')
scrape_optic()
