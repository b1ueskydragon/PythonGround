"""
File includes like:

yyyy-mm-dd hh:mm:ss,000 DEBUG [ajp-nio-9000-exec-00] [1234][5678] report.ReportSiteUnitController (ClassName.java:000) MSGA　MSGB
"""
import re
import solutions.mypath as my
from collections import OrderedDict

r = re.compile("(\[)([0-9]+)(\])")
POS = 4
IDPOS = 1
PATH = my.REPORT_FILE


def read_file():
    datum = []
    file = open(PATH, 'r', encoding='UTF-8')

    for line in file:
        if line is '\n':
            continue
        id = line.split(' ')[POS]

        datum.append(r.match(id).groups()[IDPOS])

    file.close()

    return datum


datum = read_file()
table = {}

for data in datum:
    if data in table:
        table.update({data: table[data] + 1})
    else:
        table.update({data: 1})

print(table)

# Sort by a value (count of id)
print(sorted(table.items(), key=lambda x: x[1]))
