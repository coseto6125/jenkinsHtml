# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-09-02 23:58:53
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-09-03 03:04:02

from html import unescape
from datetime import timezone, datetime


class HTML:
    def __init__(self, Header, tableStyles={}, trStyles={}, thStyles={}):
        trStyles = HTML._styleConverter(trStyles)
        thStyles = HTML._styleConverter(thStyles)
        self.rows = []
        header = ''.join(f'\n<th {thStyles} >{th}</th>' for th in Header)
        self.header = f'<tr {trStyles} >{header}\n</tr>'
        self.tableStyles = HTML._styleConverter(tableStyles)

    @staticmethod
    def _styleConverter(styleDict: dict):
        if styleDict == {}:
            return ''
        styles = ''.join(f'{style}: {value};' for [
                         style, value] in styleDict.items())
        return f'style="{styles}"'

    def addRow(self, row, trStyles={}, tdStyles={}):
        trStyles = HTML._styleConverter(trStyles)
        tdStyles = HTML._styleConverter(tdStyles)
        temp_row = f'\n<tr {trStyles} >'
        for idx, td in enumerate(row):
            if idx == 6:
                td = f'<a href="{td}">click</a>'
            temp_row += f'\n<td {tdStyles} >{td}</td>'
        temp_row += '\n</tr>'
        self.rows.append(temp_row)

    def __str__(self):
        tFormat = "%Y-%m-%d %I:%M:%S %p"
        theTime = datetime.now()
        utcTime = theTime.astimezone(timezone.utc).strftime(tFormat)
        gmt8 = datetime.strftime(theTime, tFormat)
        content = (
            f'<h1 style="text-align: center;"> [{gmt8} -- GMT+8]    [{utcTime} -- utc]</h1>\n'
            f'<table {self.tableStyles}>\n'
            f'{self.header}'
            f'{"".join(self.rows)}'
            '</table>'
        )
        return content


def dictionaryToHTMLTable(dict: dict):
    """
    convert dict to html table
    """
    border = lambda x: f';border: {x}px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px'
    html = HTML(Header=dict.keys(),
                tableStyles={'margin': f'3px auto{border(2)};width: 80%'},
                trStyles={'background-color': f'#99F2E6{border(1)}'},
                thStyles={'color': f'black{border(1)};font-size:32px'})
    for i, row in enumerate(zip(*dict.values())):
        # print(row)
        BGC, TC = ('#FFACBB', 'DarkGreen') if i % 2 == 0 else (
            '#AAB6FB', 'Navy')
        html.addRow(row, trStyles={f'background-color': f'{BGC}{border(1)};color:{TC};font-size:26px'},
                    tdStyles={'padding': f'1rem{border(1)};color:{TC};font-size:26px'})
    return html


if __name__ == '__main__':
    myDict = {
        'GameName': ('value11', 'value12', 'value13'),
        'Skip %': ['value21', 'value22', 'value23'],
        'Know %': ['value31', 'value32', 'value33'],
        'Fail %': ['value41', 'value42', 'value43'],
        'Pass %': ['value51', 'value52', 'value53'],
        'Pass+Know': ['value61', 'value62', 'value63'],
        'Link': ['value71', 'value72', 'value73']
    }
    loadDescriptions = '''
    &lt;h1 style="text-align: center">Update time: 2022/09/02 18:44&lt;/h1>
    &lt;table style="margin: 3px auto;border: 2px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;width: 85%;" >
    &lt;tr style="background-color: #99F2E6;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >GameName&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Skip %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Know %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Fail %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Pass %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Pass+Know&lt;/th>
    &lt;/tr>

    &lt;tr style="background-color: #FFACBB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value11&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value21&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value31&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;/tr>
    &lt;tr style="background-color: #AAB6FB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value12&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value22&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value32&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;/tr>
    &lt;tr style="background-color: #FFACBB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value13&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value23&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value33&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;/tr>
    &lt;/table>
    &lt;h1 style="text-align: center">Update time: 2022/09/02 18:44&lt;/h1>
    &lt;table style="margin: 3px auto;border: 2px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;width: 85%;" >
    &lt;tr style="background-color: #99F2E6;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >GameName&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Skip %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Know %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Fail %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Pass %&lt;/th>
    &lt;th style="color: black;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;" >Pass+Know&lt;/th>
    &lt;/tr>

    &lt;tr style="background-color: #FFACBB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value11&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value21&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value31&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value41&lt;/td>
    &lt;/tr>
    &lt;tr style="background-color: #AAB6FB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value12&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value22&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value32&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value42&lt;/td>
    &lt;/tr>
    &lt;tr style="background-color: #FFACBB;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value13&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value23&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value33&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;td style="padding: 1rem;border: 1px solid #FED7DD; border-collapse: collapse;text-align: center;padding: 15px;color:#FFFEE1;" >value43&lt;/td>
    &lt;/tr>
    &lt;/table>
    '''

    # print(unescape(loadDescriptions))
    print(dictionaryToHTMLTable(myDict))
