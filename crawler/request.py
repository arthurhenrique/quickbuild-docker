import requests

link_qb = 'http://127.0.0.1:8810/{}'

s = requests.Session()

s.get(url=link_qb.format(''), 
      # verify=True
      )

headers = {
    'Host': link_qb.format(''),
    'Connection': 'keep-alive',
    'Content-Length': '51',
    'Cache-Control': 'max-age=0',
    'Origin': link_qb.format(''),
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': link_qb.format('signin'),
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6,fr;q=0.5'
}

cookies = s.cookies

a = s.post(url=link_qb.format('signin?13-1.IFormSubmitListener-form'),
                  # verify=True,
                  headers=headers,
                  cookies=cookies,
                  data='id65_hf_0=&userName=admin&password=admin')

b = s.get(url=link_qb.format('my'))

'admin' in b.content.__str__()