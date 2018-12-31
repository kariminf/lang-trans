#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  transliteration.py
#  An abstract class  for language transliteration
#
#  Copyright 2017 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2017	Abdelkrime Aries <kariminfo0@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lang_trans.arabic import buckwalter, arabtex, iso233

ORIG = u'هذا البرنامج يعطينا نطق الحروف'
BUCKWALTER = 'h*A AlbrnAmj yETynA nTq AlHrwf'
ARABTEX = 'h_dA AlbrnAmj y`.tynA n.tq Al.hrwf'
ISO233 = u'hḏʾ ʾlbrnʾmǧ yʿṭynʾ nṭq ʾlḥrwf'

print "buckwalter trans of: " + ORIG
print buckwalter.trans(ORIG)
print

print "buckwalter untrans of: " + BUCKWALTER
print buckwalter.untrans(BUCKWALTER)
print

print "arabtex trans of: " + ORIG
print arabtex.trans(ORIG)
print

print "arabtex untrans of: " + ARABTEX
print arabtex.untrans(ARABTEX)
print

print "iso233 trans of: " + ORIG
print iso233.trans(ORIG)
print

print "iso233 untrans of: " + ISO233
print iso233.untrans(ISO233)
print
