# -*- coding: utf-8 -*-
# @Author: aung
# @Date:   2016-04-28 16:00:58
# @Last Modified by:   aung
# @Last Modified time: 2016-04-28 16:03:45

class Borg:
    __shared_state = {}    
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()
    rm4 = Borg()
    print('rm3 id: {0}'.format(id(rm3)))
    print('rm4 id: {0}'.format(id(rm4)))

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))
    print('rm4: {0}'.format(rm4))
