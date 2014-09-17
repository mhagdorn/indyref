# Copyright Magnus Hagdorn, 2014
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import BeautifulSoup
import requests
import numpy

def getNumVotes(s):
    return int(s.replace(',',''))
def getPercentage(s):
    return float(s)
def getSeats(s):
    return int(s)
transform = [getNumVotes,getPercentage,getSeats]

def getDataRaw(year,country):
    results = {}

    r  = requests.get('http://electionresources.org/uk/house.php?election=%d&country=%s'%(year,country))
    
    soup = BeautifulSoup.BeautifulSoup(r.text)

    results['participation'] = []
    table = soup.findAll('table')[-1]
    for row in table.findAll('tr'):
        rawData = row.findAll('td')
        if len(rawData) == 4:
            data = []
            for d in rawData:
                data.append(d.getText().replace('&nbsp;',''))
            if data[0] == 'Electors':
                results['participation'].append( getNumVotes(data[1]))
            elif data[0] == 'Total Votes':
                results['participation'].append( getNumVotes(data[1]))
                results['participation'].append( getPercentage(data[2][:-1]))
            else:
                p = data[0]
                if p=='Conservative (including Speaker)':
                    p='Conservative'
                results[p] = []
                for i in range(3):
                    results[p].append(transform[i](data[1+i]))
    return results

def getData(year,country):
    d = getDataRaw(year,country)
    data = numpy.zeros(8,int)
    data[0] = d['participation'][0]
    data[1] = d['participation'][1]
    if 'Conservative' in d:
        data[2] = d['Conservative'][0]
        data[3] = d['Conservative'][2]
    if 'Labour' in d:
        data[4] = d['Labour'][0]
        data[5] = d['Labour'][2]
    for p in d:
        if p not in ['Conservative','Labour','participation']:
            data[6]+=d[p][0]
            data[7]+=d[p][2]
    return data


years = [2010,2005,2001,1997,1992,1987,1983]
years.sort()
countries = ['ENG','WLS','NIR']

with open('election_sct.data','w') as out:
    out.write('#year electorate votes Conservative Labour Other\n')
    for y in years:
        print y,'sct'
        d = getData(y,'SCT')
        out.write('%d'%y)
        for i in range(8):
            out.write(' %d'%d[i])
        out.write('\n')

with open('election_ruk.data','w') as out:
    out.write('#year electorate votes Conservative Labour Other\n')
    for y in years:
        d = numpy.zeros(8,int)
        for c in countries:
            print y,c
            d += getData(y,c)
        out.write('%d'%y)
        for i in range(8):
            out.write(' %d'%d[i])
        out.write('\n')
