#!/usr/bin/env python
# A small formatting utility I wrote to incorporate into my TextExpander snippets.
# Copyright (C) 2016  Alan Garcia
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

import re


def timeformat(_time):
    """ Formats the input string [h]hmm[p] to match 'hh:mm AM|PM'. """
    _time = _time.lstrip('0')
    am = re.match(r'^(10|11|12|[1-9]):?([0-5][0-9])$', _time)
    pm = re.match(r'^(10|11|12|[1-9]):?([0-5][0-9]p)$', _time)

    if am and ':' in _time:
        if len(_time) == 4:
            return _time + ' AM'
        if len(_time) == 5:
            return _time + ' AM'
    elif am:
        if len(_time) == 3:
            return _time[0] + ':' + _time[1:] + ' AM'
        if len(_time) == 4:
            return _time[:2] + ':' + _time[2:] + ' AM'

    elif pm and ':' in _time:
        if len(_time) == 5:
            return _time[:4] + ' PM'
        if len(_time) == 6:
            return _time[:5] + ' PM'
    elif pm:
        if len(_time) == 4:
            return _time[0] + ':' + _time[1:3] + ' PM'
        if len(_time) == 5:
            return _time[:2] + ':' + _time[2:4] + ' PM'
    else:
        return None


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        print('usage: ' + argv[0] + ' [h]hmm[p]')
    else:
        print(timeformat(argv[1]))
