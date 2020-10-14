#!/usr/local/bin/python3
import sys


from test import test

epoch = 9

#test('./real_weights/CRAFT_clr_' + repr(epoch) + '.pth')
test('./real_weights_false/CRAFT_clr_' + repr(epoch) + '.pth')         #! modified saving directory
