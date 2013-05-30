#!/usr/bin/env python
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Define devices supported by the orangutan framework here.
# More information on orangutan: https://github.com/wlach/orangutan

from actions import TAP_ACTION
from actions import getRandomSleep
from utils import countWithDesc


class OrangutanDevice(object):
    '''An OrangutanDevice assumes that a compiled orangutan binary has been "adb push"ed to the
    device. See https://github.com/wlach/orangutan for more details.'''
    def setMaxHorizPixels(self, hpx):
        '''Sets the maximum horizontal pixels.'''
        self.hpx = hpx
    def getMaxHorizPixels(self):
        '''Gets the maximum horizontal pixels.'''
        return self.hpx
    def setMaxVertPixels(self, vpx):
        '''Sets the maximum vertical pixels.'''
        self.vpx = vpx
    def getMaxVertPixels(self):
        '''Gets the maximum vertical pixels.'''
        return self.vpx
    def setButtonVertPixelOffset(self, offset):
        '''Sets the number of pixels offset for the phone button(s).'''
        self.offset = offset
    def getButtonVertPixelOffset(self):
        '''Gets the number of pixels offset for the phone button(s).'''
        return self.offset
    def setHomeKeyLocation(self, homeKeyLoc):
        '''Sets the location of the home key.'''
        # See bug 838267, a bug on supporting the HOME key for the orangutan library
        assert isinstance(homeKeyLoc, list), 'Must be a list because we concatenate this later.'
        self.homeKeyLoc = homeKeyLoc
    def getHomeKeyLocation(self):
        '''Gets the location of the home key.'''
        return self.homeKeyLoc
    def getHomeKeyTap(self, rnd, count):
        '''Trigger a tap on the home key.'''
        return ' '.join([countWithDesc(count, 'Home key tap') + TAP_ACTION] +
                            [str(x) for x in self.getHomeKeyLocation()] +
                            ['1', str(rnd.randint(50, 1000))]
                        )
    def getHomeKeyLongPress(self, rnd, count):
        '''Trigger a long press on the home key, defined as >= 2 seconds.'''
        return ' '.join([countWithDesc(count, 'Home key long press') + TAP_ACTION] +
                            [str(x) for x in self.getHomeKeyLocation()] +
                            ['1', str(rnd.randint(2000, 10000))]
                        )
    def getAppSwitcherXButtonLocation(self):
        '''Gets the location of the X button in the app switcher.'''
        return [int(0.1 * self.hpx), int(0.15 * (self.vpx - self.offset))]
    def getForceCloseApp(self, rnd, count):
        '''Force close an application.'''
        return ' '.join([countWithDesc(count, 'Force close an application')] +
                            [self.getHomeKeyLongPress(rnd, count) + ' ; '] +
                            [getRandomSleep(rnd) + ' ; '] +
                            [TAP_ACTION] +
                            [str(x) for x in self.getAppSwitcherXButtonLocation()] +
                            ['1', str(rnd.randint(50, 1000))]
                        )


class Unagi(OrangutanDevice):
    '''Unagi devices were available for dogfooding.'''
    def __init__(self):
        '''Unagi devices have 320x520 resolution.'''
        super(Unagi, self).__init__()
        self.setMaxHorizPixels(320)
        self.setMaxVertPixels(520)
        self.setButtonVertPixelOffset(40)
        self.setHomeKeyLocation([44, 515])

if __name__ == '__main__':
    pass
