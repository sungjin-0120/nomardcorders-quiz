from bs4 import BeautifulSoup
from requests import get


url = f"https://remoteok.com/remote-python-jobs"
request = get(url, headers={"User-Agent": "Kimchi"})
if request.status_code != 200:
    print("Can't get jobs.")
else:
    soup = BeautifulSoup(request.text, "html.parser")
    
    

