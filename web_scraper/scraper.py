import requests, json
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
  res = requests.get(URL)
  soup = BeautifulSoup(res.content, 'html.parser')

  results = soup.find_all('a', title="Wikipedia:Citation needed")
  return len(results)

def get_citations_needed_report(URL):
  res = requests.get(URL)
  soup = BeautifulSoup(res.content, 'html.parser')

  results = soup.find_all('a', title="Wikipedia:Citation needed")
  
  all_citations = []
  counter = 0
  for result in results:
      result_dict = {'title':'', 'citation number':''}
      title_before_stripping = result.find('span')
      counter += 1
      if title_before_stripping:
          title = title_before_stripping.get_text().strip()
          result_dict['title'] = title
          result_dict['citation number'] = counter
          all_citations.append(result_dict)

  with open('all_results.json', 'w') as f:
      content = json.dumps(all_citations)
      f.write(content)

  return content

if __name__ == '__main__':
  URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
  count = get_citations_needed_count(URL)
  report = get_citations_needed_report(URL)
  # print(count)
  print(report)

