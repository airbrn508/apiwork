#!/usr/bin/env python3

import pandas
import matplotlib

from asciitree import LeftAligned
from collections import OrderedDict as OD

tree = {
    'asciitree': OD([
        ('sometimes',
            {'you': {}}),
        ('just',
            {'want': OD([
                ('to', {}),
                ('draw', {}),
            ])}),
        ('trees', {}),
        ('in', {
            'your': {
                'terminal': {}
            }
        })
    ])
}

tr = LeftAligned()
print(tr(tree))

