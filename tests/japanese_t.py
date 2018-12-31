#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  transliteration.py
#  An abstract class  for language transliteration
#
#  Copyright 2018 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2018	Abdelkrime Aries <kariminfo0@gmail.com>
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

from lang_trans.japanese import hepburn, nihonshiki

ORIG = u"じゃしゃしんいっぱい"
HEPBURN = "jashashin'ippai"
HEPBURN_ORIG = u"じゃしゃしにっぱい"
NIHONSHIKI = "zyasyasin'ippai"
NIHONSHIKI_ORIG = u"じゃしゃしにっぱい"

print (("hepburn trans of: " + ORIG))
print (hepburn.trans(ORIG))
print ("")

print ("hepburn untrans of: " + HEPBURN)
print (hepburn.untrans(HEPBURN))
print ("")

print (("nihonshiki trans of: " + ORIG))
print (nihonshiki.trans(ORIG))
print ("")

print ("nihonshiki untrans of: " + NIHONSHIKI)
print (hepburn.untrans(NIHONSHIKI))
print ("")
