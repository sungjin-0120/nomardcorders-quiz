from requests import get
from bs4 import BeautifulSoup



base_url = "https://weworkremotely.com/remote-jobs/search?term="
response = get(f"{base_url}{keyword}")
if response.status_code != 200:
    print("can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = (soup.find_all('section', class_="jobs"))
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, position, location = anchor.find_all('span', class_="company")
            print(company)
            title = anchor.find('span', class_="title")
            jobs_data = {
            
                'link': f"https://weworkremotely.com{link}",
                'company': company.string.replace(","," "),
                'position': position.string.replace(","," "),
                'location': location.string.replace(","," "),
                'title': title.string
            }
        
