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
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lang_trans.arabic import Buckwalter

ORIG = u'هذا البرنامج يعطينا نطق الحروف'
TRANS = 'h*A AlbrnAmj yETynA nTq AlHrwf'

trans = Buckwalter()

def test_transliterate():
    assert trans.transliterate(ORIG) == TRANS

def test_untransliterate():
    assert trans.untransliterate(TRANS) == ORIG
