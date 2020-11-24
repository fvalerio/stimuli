# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:52:15 2020

@author: vr4
"""

import matlab.engine
import time

eng = matlab.engine.start_matlab()
eng.tcpip_test(nargout=0)

t = time.time()
eng.quit()
elapse = time.time() - t
print(elapse)