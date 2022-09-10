import os
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""
    root = ET.fromstring(content)
    tag_list = []
    print(root.attrib)
    for child in root.iter("category"):
        tag_list.append(child.text)
    c = Counter(tag_list)
    return c.most_common(n)


print(get_pybites_top_tags())


"""
<rss>
    <channel>
        <item>
            <title>twitter digest 2017 week 26</title>
            <link>https://pybit.es/twitter_digest_201726.html</link>
            <description>&lt;p&gt;every weekend we share a curated list of 15 cool things (mostly python) that we found / tweeted throughout the week.&lt;/p&gt;</description>
            <dc:creator xmlns:dc="http://purl.org/dc/elements/1.1/">pybites</dc:creator>
            <pubdate>sun, 02 jul 2017 17:52:00 +0200</pubdate>
            <guid ispermalink="false">tag:pybit.es,2017-07-02:/twitter_digest_201726.html</guid>
            <category>twitter</category>
            <category>news</category>
            <category>tips</category>
            <category>python</category>
            <category>code</category>
            <category>siri</category>
            <category>voice</category>
            <category>pgcli</category>
            <category>mycli</category>
            <category>matplotlib</category>
            <category>data science</category>
            <category>macos</category>
            <category>mongodb</category>
            <category>pymongo</category>
            <category>training</category>
            <category>flask</category>
            <category>pydata</category>
            <category>type checking</category>
            <category>django</category>
            <category>vim</category>
            <category>constructors</category>
            <category>kubernetes</category>
        </item>
    </channel>
</rss>
"""
