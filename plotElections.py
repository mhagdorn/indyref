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

import pylab
import numpy

scotland = numpy.loadtxt('election_sct.data',dtype=float)
rUK = numpy.loadtxt('election_ruk.data',dtype=float)

plotAll = False

if plotAll:
    pylab.subplot(3, 1, 1)
pylab.plot(rUK[:,0],rUK[:,4],'b.-')
pylab.plot(rUK[:,0],rUK[:,6],'r.-')
pylab.plot(rUK[:,0],rUK[:,8],'k.-')
pylab.plot(rUK[:,0],0.5*numpy.sum(rUK[:,4::2],axis=1),'g.-')

pylab.plot(rUK[:,0],rUK[:,4]+scotland[:,4],'b.:')
pylab.plot(rUK[:,0],rUK[:,6]+scotland[:,6],'r.:')
pylab.plot(rUK[:,0],rUK[:,8]+scotland[:,8],'k.:')
pylab.plot(rUK[:,0],0.5*(numpy.sum(rUK[:,4::2],axis=1)+
                         numpy.sum(scotland[:,4::2],axis=1)),'g.:')
pylab.ylabel('seats')

if plotAll:
    pylab.subplot(3,1,2)
    nSeatsRUK = numpy.sum(rUK[:,4::2],axis=1)
    pylab.plot(rUK[:,0],100*rUK[:,4]/nSeatsRUK,'b.-')
    pylab.plot(rUK[:,0],100*rUK[:,6]/nSeatsRUK,'r.-')
    pylab.plot(rUK[:,0],100*rUK[:,8]/nSeatsRUK,'k.-')

    nSeatsSCO = numpy.sum(scotland[:,4::2],axis=1)
    pylab.plot(scotland[:,0],100*scotland[:,4]/nSeatsSCO,'b.:')
    pylab.plot(scotland[:,0],100*scotland[:,6]/nSeatsSCO,'r.:')
    pylab.plot(scotland[:,0],100*scotland[:,8]/nSeatsSCO,'k.:')
    pylab.ylabel('percentage of seats')


    pylab.subplot(3,1,3)
    pylab.plot(rUK[:,0],rUK[:,3]/rUK[:,2]*100,'b.-')
    pylab.plot(rUK[:,0],rUK[:,5]/rUK[:,2]*100,'r.-')
    pylab.plot(rUK[:,0],rUK[:,7]/rUK[:,2]*100,'k.-')

    pylab.plot(scotland[:,0],scotland[:,3]/scotland[:,2]*100,'b.:')
    pylab.plot(scotland[:,0],scotland[:,5]/scotland[:,2]*100,'r.:')
    pylab.plot(scotland[:,0],scotland[:,7]/scotland[:,2]*100,'k.:')
    pylab.ylabel('percentage of votes')

    #pylab.subplot(3, 1, 3)
    #pylab.plot(scotland[:,0],scotland[:,2]/scotland[:,1]*100,color='b')
    #pylab.plot(rUK[:,0],rUK[:,2]/rUK[:,1]*100,color='r')
    #pylab.ylabel('participation [%]')

pylab.xlabel('election year')

if True:
    pylab.savefig('elections.png')
else:
    pylab.show()
