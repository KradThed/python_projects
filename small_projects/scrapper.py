import requests 
import lxml.html as html1

html = requests.get('https://store.steampowered.com/explore/new/')
doc = html1.fromstring(html.content)

"""  Grab information from ENG version steam"""
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0] # will return a list of all the divs in the HTML page
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()') # e titles of all of the games in the “Popular New Releases” tab.
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()') # TODO doesnt work with UAH
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]') 
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []

for div in tags_divs:
    tags.append(div.text_content())

tags = [tag.split(', ') for tag in tags]



"""extracting the tab_item_details div.
The XPath in line 5 is a bit different. Here we have [contains(@class,
"platform_img")] instead of simply having [@class="platform_img"]. The reason is that [@class="platform_img"] returns those spans which only have the
platform_img class associated with them.
"""

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)


output = []
for info in zip(titles,prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)


print(output)