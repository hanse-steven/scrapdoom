import requests
from lxml import etree

r_get = requests.get('https://thebulletin.org/doomsday-clock/')
html = etree.HTML(r_get.text)

elements = html.xpath('//span[@class="fl-heading-text"]')
element = etree.tostring(elements[1], pretty_print=True, encoding='unicode')
element = element.split('</em>')[1].replace('</span>', '')

print(element)