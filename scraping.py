from bs4 import BeautifulSoup
import requests  
import time
import json

print('Tell me what makes an optic bad')
bad_optic=input ('>')
print(f'Filtering out {bad_optic}')
data=[]
def scrape_optic():
    print('Scraping data from OptoSigma...')
    #Accessing the first page => The list of all optics
    first_page = requests.get('https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html').text
    first_soup=BeautifulSoup(first_page, 'html.parser')
    optics= first_soup.find_all('tr', class_='grouped-item')
    count=0
    for index, optic in enumerate(optics) :
        optics_delivery=optic.find('span', class_='deliveryTime').text.replace(' ','')
        #An example of filtering optics to scrape by delivery time
        if bad_optic not in optics_delivery :
            item={}
            item['name']=optic.find('a', class_='link').text.replace('  ','')
            item['price']=optic.find('span', class_='price').text.replace(' ','')
            item['delivery']=optic.find('span', class_='deliveryTime').text.replace(' ','')
            # Another way to find a specific tag byt going through the tag tree
            item['link'] = optic.td.a['href']
            #Accessing the second page through item['link'] => More info about each optic
            second_page=requests.get(item['link']).text
            second_soup=BeautifulSoup(second_page, 'html.parser')
            #Getting general description & type of Optic
            item['description']=second_soup.find('div', class_="product attribute short_description").text
            item['sku']=second_soup.find('div', class_="value").text
            item['types']=second_soup.find('div', class_="product attribute description").text.replace('\u25e6', '')
            #Finding the table that contains the attributes we're looking for
            more_info= second_soup.find('table', class_='data table additional-attributes')
            #Going through the rows one by one
            item['weight']=more_info.find('tr',class_="clearfix Weight").text.replace(' ','')
            item['standard_coating_available']=more_info.find('tr',class_="clearfix standard coatings available").text.replace(' ','')
            item['Focal length']=more_info.find('tr',class_="clearfix focal length").text.replace(' ','')
            item['Material']=more_info.find('tr',class_="clearfix material").text.replace(' ','')
            item['Diameter']=more_info.find('tr',class_="clearfix diameter φd").text.replace('\u03c6',' ')
            item['Design Wavelength']=more_info.find('tr',class_="clearfix design wavelength").text.replace(' ','')
            item['Refractive index n<sub>e</sub>']=more_info.find('tr',class_="clearfix refractive index n<sub>e</sub>").text.replace(' ','')
            item['Coating']=more_info.find('tr',class_="clearfix coating").text.replace(' ','')
            item['Clear aperture']=more_info.find('tr',class_="clearfix clear aperture").text.replace(' ','')
            # item['Surface Quality (Scratch-Dig)']=more_info.find('tr',class_="clearfix surface quality (scratch-dig)").text.replace(' ','')
            item['Wavelength range of Antireflection Coating']=more_info.find('tr',class_="clearfix wavelength range of antireflection coating").text.replace(' ','')
            item['Edge thickness te']=more_info.find('tr',class_="clearfix edge thickness te").text.replace(' ','')
            item['Center thickness tc']=more_info.find('tr',class_="clearfix center thickness tc").text.replace(' ','')
            item['Back focal length fb']=more_info.find('tr',class_="clearfix back focal length fb").text.replace(' ','')
            item['Radius of curvature r']=more_info.find('tr',class_="clearfix radius of curvature r").text.replace(' ','')
            # item['Centration']=more_info.find('tr',class_="clearfix centration").text.replace('%\n\n','')
            #Saving all the info in data
            data.append(item)
            print(f'Item n° {index} saved')
            count+=1
    print(f'{count} items saved')
    #Writing in JSON file
    with open("optics.json", "w") as writeJSON:
        json.dump(data, writeJSON, ensure_ascii=False)
scrape_optic()
