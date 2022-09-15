# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 06:19:05 2022

@author: Takodachi
"""

from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)

import torch
torch.cuda.is_available()