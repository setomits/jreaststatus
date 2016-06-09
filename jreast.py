#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html

class JREast:
    URL = 'http://traininfo.jreast.co.jp/train_info/{}.aspx'

    lines = {
        'kanto': ('東海道線', '京浜東北線', '横須賀線', '南武線', '横浜線',
                  '伊東線', '相模線', '鶴見線',

                  '宇都宮線', '高崎線', '京浜東北線', '埼京線', '川越線',
                  '武蔵野線', '上越線', '信越本線', '吾妻線', '烏山線', 
                  '八高線', '日光線', '両毛線',

                  '中央線快速電車', '中央・総武各駅停車', '中央本線',
                  '武蔵野線', '五日市線', '青梅線', '八高線', '小海線',

                  '常磐線', '常磐線快速電車', '常磐線各駅停車', '水郡線', 
                  '水戸線',

                  '総武快速線', '総武本線', '中央・総武各駅停車', '京葉線',
                  '武蔵野線', '内房線', '鹿島線', '久留里線', '外房線',
                  '東金線', '成田線',

                  '山手線',

                  '上野東京ライン', '湘南新宿ライン'),

        'tohoku': ('羽越本線', '奥羽本線', '奥羽本線（山形線）', '常磐線', 
                   '仙山線', '仙石線', '仙石東北ライン', '東北本線',
                   '磐越西線', '左沢線', '石巻線', '大船渡線', 
                   '大船渡線ＢＲＴ', '大湊線', '男鹿線', '釜石線', '北上線', 
                   '気仙沼線', '気仙沼線ＢＲＴ', '五能線', '水郡線',
                   '田沢湖線', '只見線', '津軽線', '八戸線', '花輪線',
                   '磐越東線', '山田線', '米坂線', '陸羽西線', '陸羽東線'),

        'shinetsu': ('羽越本線', '信越本線', '上越線', '篠ノ井線', '中央本線',
                     '白新線', '磐越西線', '飯山線', '越後線', '大糸線', 
                     '小海線', '只見線', '弥彦線', '米坂線')
        }


    def status(self, line):
        self.area = None

        for area in JREast.lines:
            for l in JREast.lines[area]:
                if l == line:
                    self.area = area
                    break

            if self.area:
                break

        m = {'area': self.area, 'line': line, 'status': None}

        if self.area:
            url = JREast.URL.format(self.area)
        else:
            return m

        dom = html.parse(url)

        th = None
        for ele in dom.xpath('//th[@class="text-tit-xlarge"]'):
            if ele.text.strip() == line:
                th = ele
                break
        else:
            return m

        td = th.getnext()
        m['status'] = td.xpath('img')[0].attrib['alt']
        if m['status'] != '平常運転':
            td = td.getnext()
            m['publishedAt'] = td.text.strip()
            td = th.getparent().getnext().xpath('td[@class="cause"]')[0]
            m['detail'] = td.text.strip()
            
        return m


if __name__ == '__main__':
    import pprint

    jr = JREast()

    pprint.pprint(jr.status('山田線'))
    pprint.pprint(jr.status('京葉線'))
