#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  buckwalter.py
#  A  class to handle buckwalter translateration
#
#  Copyright 2017-2018 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2017-2018	Abdelkrime Aries <kariminfo0@gmail.com>
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

trans_map =	{
		u"\u0627": "A", # alif
		u"\u0628": "b", # ba
		u"\u062A": "t", # ta
		u"\u062B": "v", # tha
		u"\u062C": "j", # jim
		u"\u062D": "H", # Ḥa
		u"\u062E": "x", # kha
		u"\u062F": "d", # dal
		u"\u0630": "*", # dhal
		u"\u0631": "r", # ra
		u"\u0632": "z", # zin
		u"\u0633": "s", # sin
		u"\u0634": "$", # shin
		u"\u0635": "S", # ṣad
		u"\u0636": "D", # Ḍad
		u"\u0637": "T", # Ṭa
		u"\u0638": "Z", # Ẓa
		u"\u0639": "E", # 'Ayn
		u"\u063A": "g", # ghayn
		u"\u0641": "f", # fa
		u"\u0642": "q", # qaf
		u"\u0643": "k", # kaf
		u"\u0644": "l", # lam
		u"\u0645": "m", # mim
		u"\u0646": "n", # nun
		u"\u0647": "h", # ha
		u"\u0648": "w", # waw
		u"\u064A": "y", # ya
		#hamza
		u"\u0621": "'", # lone hamza
		u"\u0623": ">", # hamza on alif
		u"\u0625": "<", # hamza below alif
		u"\u0624": "&", # hamza on waw
		u"\u0626": "}", # hamza on ya
		#alif
		u"\u0622": "|", # madda on alif
		u"\u0671": "{", # alif alwasla
		u"\u0670": "`", # dagger alif
		u"\u0649": "Y", # alif maqsura
		#harakat
		u"\u064E": "a", # fatha
		u"\u064F": "u", # Damma
		u"\u0650": "i", # kasra
		u"\u064B": "F", # fathatayn
		u"\u064C": "N", # dammatayn
		u"\u064D": "K", # kasratayn
		u"\u0651": "~", # shadda
		u"\u0640": "_", # tatwil
		#others
		u"\u0629": "p", # ta marbuta
		u"\u0652": "o", # sukun
}

from lang_trans import MapTrans

class Buckwalter(MapTrans):

	def __init__(self):
		MapTrans.__init__(self, trans_map)

buckwalter = Buckwalter()
