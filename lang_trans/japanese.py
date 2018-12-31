#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  buckwalter.py
#  A  class to handle hepburn translateration
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

hiragana = [
    u"が",
    u"ぎ",
    u"ぐ",
    u"げ",
    u"ご",
    u"ざ",
    u"じ",
    u"じ",
    u"ず",
    u"ぜ",
    u"ぞ",
    u"だ",
    u"ぢ",
    u"ぢ",
    u"づ",
    u"で",
    u"ど",
    u"ば",
    u"び",
    u"ぶ",
    u"べ",
    u"ぼ",
    u"ぱ",
    u"ぴ",
    u"ぷ",
    u"ぺ",
    u"ぽ",
    u"ふぁ",
    u"ふぉ",
    u"ふぃ",
    u"か",
    u"き",
    u"く",
    u"け",
    u"こ",
    u"た",
    u"ち",
    u"つ",
    u"て",
    u"と",
    u"さ",
    u"し",
    u"し",
    u"す",
    u"せ",
    u"そ",
    u"な",
    u"に",
    u"ぬ",
    u"ね",
    u"の",
    u"は",
    u"ひ",
    u"ふ",
    u"へ",
    u"ほ",
    u"ま",
    u"み",
    u"む",
    u"め",
    u"も",
    u"や",
    u"ゆ",
    u"よ",
    u"ら",
    u"り",
    u"る",
    u"れ",
    u"ろ",
    u"わ",
    u"を",
    u"あ",
    u"い",
    u"う",
    u"え",
    u"お",
    u"ん",
    u"ゃ",
    u"ぇ",
    u"ゅ",
    u"ぃ",
    u"ょ"
]
trans_tab = [ # https://en.wikipedia.org/wiki/Hepburn_romanization
    "ga",
    "gi",
    "gu",
    "ge",
    "go",
    "za",
    "ji",
    "zi",
    "zu",
    "ze",
    "zo",
    "da",
    "ji",
    "di",
    "zu",
    "de",
    "do",
    "ba",
    "bi",
    "bu",
    "be",
    "bo",
    "pa",
    "pi",
    "pu",
    "pe",
    "po",
    "fa",
    "fo",
    "fi",
    "ka",
    "ki",
    "ku",
    "ke",
    "ko",
    "ta",
    "chi",
    "tsu",
    "te",
    "to",
    "sa",
    "shi",
    "si",
    "su",
    "se",
    "so",
    "na",
    "ni",
    "nu",
    "ne",
    "no",
    "ha",
    "hi",
    "fu",
    "he",
    "ho",
    "ma",
    "mi",
    "mu",
    "me",
    "mo",
    "ya",
    "yu",
    "yo",
    "ra",
    "ri",
    "ru",
    "re",
    "ro",
    "wa",
    "wo",
    "a",
    "i",
    "u",
    "e",
    "o",
    "n",
    "xya",
    "xye",
    "xyu",
    "xyi",
    "xyo"
]


from lang_trans import Transliteration

class Hepburn(Transliterator):

	def __init__(self):
		pass

	def transliterate(self, word):
		res = ""
		if len(word) < len(trans):
			for char in word:
				res += trans.get(char, char)
		else:
			res = word
			for k,v in trans.items():
				res = res.replace(k, v)

		return res

	def untransliterate(self, word):
		res = word
		for k,v in trans.items():
			res = res.replace(v, k)

		return res

hepburn = Hepburn()
