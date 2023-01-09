from bs4 import BeautifulSoup
from requests import get


url = f"https://remoteok.com/remote-python-jobs"
request = get(url, headers={"User-Agent": "Kimchi"})
if request.status_code != 200:
    print("Can't get jobs.")
else:
    soup = BeautifulSoup(request.text, "html.parser")
    bodys = soup.find_all('td', class_="company position company_and_position")
    for body in bodys:
        title = body.find('h2', itemprop="title")
        company = body.find('h3', itemprop="name")
        
        tooltips= body.find('div', class_="location tooltip")
        print(tooltips)
        anchors = body.find_all('a', itemprop="url", class_="preventLink")
       
        """
        for anchor in anchors:
            link = anchor['href']
            
            jobs_datas= {
                    'company': company.string.replace("\n", " "),
                    'title':title.string.replace("\n", " "),
                    'region': region.string.replace("\n", " "),
                    'pay': pay.string.replace("\n", " "),
                    'link':f"https://remoteok.com/remote-jobs{link}"
                }
            print(jobs_datas)
        """
            

     
      
        
    
    

