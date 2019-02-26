import requests
import lxml.html as lh
import pandas as pd


def get_won_rate():
    m_exchange_rate_url = 'https://www.mizuhobank.co.jp/market/cash.html'

    # Create a handle, page (response), to handle the contents of the website
    page = requests.get(m_exchange_rate_url)

    # Store the contents of the website under doc
    doc = lh.fromstring(page.content)

    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    col = []
    i = 0

    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        print('%d:"%s"' % (i, name))
        col.append((name, []))


get_won_rate()
