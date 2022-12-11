import bs4,requests,openpyxl,os,re
from datetime import date
from datetime import datetime




productname = ''

def GetProductInfo(url):
    req_obj = requests.get(url)
    req_obj.raise_for_status()

    soup_obj = bs4.BeautifulSoup(req_obj.text,'html.parser')
    req_element = soup_obj.select('._30jeq3')

    date_today = date.today()

    name_element = soup_obj.select('.B_NuCI')
    productname = name_element[0].text.strip() 
    os.chdir(r'D:\!scrap\Cost Tracker')
    finalproductname = productname[:25] + '.txt'

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    

    if os.path.exists(finalproductname):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not



    price = re.sub('[₹\,]',"",req_element[0].text.strip())

    info = ((price +',' +str(date_today.day)+'/'+str(date_today.month)+','+ str(current_time) +'\n'))
    file_obj = open(finalproductname, append_write)
    file_obj.write(info)
    
    file_obj.close()
    '''
    wb = openpyxl.Workbook()

    sheet = wb['Sheet']

    sheet['A1'] = (req_element[0].text.strip('₹'))
    sheet['B1'] = (str(date_today))
    sheet['A2'] = (req_element[0].text.strip('₹'))
    sheet['B2'] = (str(date_today))
    os.chdir(r'D:\!scrap☠')
    wb.save('Headphone.xlsx')
    '''

    return info


url = r'https://www.flipkart.com/logitech-g331-leatherette-analog-n-a-au-wired-gaming-headset/p/itm22da5042eaf9a?pid=ACCFXMG2GEYZFHBW&lid=LSTACCFXMG2GEYZFHBW1WYTXV&marketplace=FLIPKART&store=0pm%2Ffcn&srno=b_1_8&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_P9LHWOMXA8fmBDkI3IXFhF3qcuQH8JfUI3ejdNT3La2ipbaOhloXDWyJHoMzKPvBxskcbGqNYjONBHIRj%2F%2FICA%3D%3D&ppt=browse&ppn=browse&ssid=1fx1f4b7v42pnvgg1630179386254'
print(GetProductInfo(url) )