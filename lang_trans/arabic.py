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
# http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

buckwalter_map =	{
		u"ا": "A", # alif
		u"ب": "b", # ba
		u"ت": "t", # ta
		u"ث": "v", # tha
		u"ج": "j", # jim
		u"ح": "H", # Ḥa
		u"خ": "x", # kha
		u"د": "d", # dal
		u"ذ": "*", # dhal
		u"ر": "r", # ra
		u"ز": "z", # zin
		u"س": "s", # sin
		u"ش": "$", # shin
		u"ص": "S", # ṣad
		u"ض": "D", # Ḍad
		u"ط": "T", # Ṭa
		u"ظ": "Z", # Ẓa
		u"ع": "E", # 'Ayn
		u"غ": "g", # ghayn
		u"ف": "f", # fa
		u"ق": "q", # qaf
		u"ك": "k", # kaf
		u"ل": "l", # lam
		u"م": "m", # mim
		u"ن": "n", # nun
		u"ه": "h", # ha
		u"و": "w", # waw
		u"ي": "y", # ya
		#hamza
		u"ء": "'", # lone hamza
		u"أ": ">", # hamza on alif
		u"إ": "<", # hamza below alif
		u"ؤ": "&", # hamza on waw
		u"ئ": "}", # hamza on ya
		#alif
		u"آ": "|", # madda on alif
		u"ٱ": "{", # alif alwasla
		u"\u0670": "`", # dagger alif
		u"ى": "Y", # alif maqsura
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
		u"ة": "p", # ta marbuta
		u"\u0652": "o", # sukun
}


iso233_map =	{
		u"ا": "ʾ", # alif
		u"ب": "b", # ba
		u"ت": "t", # ta
		u"ث": "ṯ", # tha
		u"ج": "ǧ", # jim
		u"ح": "ḥ", # Ḥa
		u"خ": "ẖ", # kha
		u"د": "d", # dal
		u"ذ": "ḏ", # dhal
		u"ر": "r", # ra
		u"ز": "z", # zin
		u"س": "s", # sin
		u"ش": "š", # shin
		u"ص": "ṣ", # ṣad
		u"ض": "ḍ", # Ḍad
		u"ط": "ṭ", # Ṭa
		u"ظ": "ẓ", # Ẓa
		u"ع": "ʿ", # 'Ayn
		u"غ": "ġ", # ghayn
		u"ف": "f", # fa
		u"ق": "q", # qaf
		u"ك": "k", # kaf
		u"ل": "l", # lam
		u"م": "m", # mim
		u"ن": "n", # nun
		u"ه": "h", # ha
		u"و": "w", # waw
		u"ي": "y", # ya
		#hamza
		u"ء": "ˌ", # lone hamza
		u"أ": "ˈ", # hamza on alif
		u"إ": "ʾ", # hamza below alif
		u"ؤ": "ˈ", # hamza on waw
		u"ئ": "ˈ", # hamza on ya
		#alif
		u"\u0622": "ʾ", # madda on alif
		u"\u0671": "ʾ", # alif alwasla
		u"\u0670": "ʾ", # dagger alif
		u"ى": "ỳ", # alif maqsura
		u"ة": "ẗ", # ta marbuta
}

arabic = [
	u"ث", # tha
	u"ح", # Ḥa
	u"خ", # kha
	u"ذ", # dhal
	u"ش", # shin
	u"ص", # ṣad
	u"ض", # Ḍad
	u"ط", # Ṭa
	u"ظ", # Ẓa
	u"غ", # ghayn
	u"ب", # ba
	u"ت", # ta
	u"ج", # jim
	u"د", # dal
	u"ر", # ra
	u"ز", # zin
	u"س", # sin
	u"ع", # 'Ayn
	u"ف", # fa
	u"ق", # qaf
	u"ك", # kaf
	u"ل", # lam
	u"م", # mim
	u"ن", # nun
	u"ه", # ha
	u"و", # waw
	u"ي", # ya
	u"أ", # hamza on alif
	u"إ", # hamza below alif
	u"ؤ", # hamza on waw
	u"ئ", # hamza on ya
	u"آ", # madda on alif
	u"\u0671", # alif alwasla
	u"\u0670", # dagger alif
	u"ى", # alif maqsura
	u"\u064B", # fathatayn
	u"\u064C", # dammatayn
	u"\u064D", # kasratayn
	u"\u064E", # fatha
	u"\u064F", # Damma
	u"\u0650", # kasra
	u"\u0651", # shadda
	u"\u0640", # tatwil
	u"ة", # ta marbuta
	u"\u0652", # sukun
	u"ء", # lone hamza
	u"ا" # alif
]

arabtex_tab = [
	"_t", # tha
	".h", # Ḥa
	"_h", # kha
	"_d", # dhal
	"^s", # shin
	".s", # ṣad
	".d", # Ḍad
	".t", # Ṭa
	".z", # Ẓa
	".g", # ghayn
	"b", # ba
	"t", # ta
	"j", # jim
	"d", # dal
	"r", # ra
	"z", # zin
	"s", # sin
	"`", # 'Ayn
	"f", # fa
	"q", # qaf
	"k", # kaf
	"l", # lam
	"m", # mim
	"n", # nun
	"h", # ha
	"w", # waw or "U"
	"y", # ya or "I"

	"'", # hamza on alif
	"'i", # hamza below alif
	"'", # hamza on waw
	"'", # hamza on ya

	"'A", # madda on alif
	"|", # alif alwasla <<<<<<
	"_a", # dagger alif <<<<<<
	"_A", # alif maqsura

	"aN", # fathatayn
	"uN", # dammatayn
	"iN", # kasratayn
	"a", # fatha
	"u", # Damma
	"i", # kasra
	"xx", # shadda
	"--", # tatwil

	"T", # ta marbuta
	"\"", # sukun

	"'", # lone hamza
	"A" # alif
  ]

from lang_trans import MapTrans, L2LTrans

class Buckwalter(MapTrans):

	def __init__(self):
		MapTrans.__init__(self, buckwalter_map)

buckwalter = Buckwalter()

class ArabTex(L2LTrans):

	def __init__(self):
		L2LTrans.__init__(self, arabic, arabtex_tab)

arabtex = ArabTex()

class Iso233(MapTrans):

	def __init__(self):
		MapTrans.__init__(self, iso233_map)

iso233 = Iso233()
