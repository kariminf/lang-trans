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
    "が",
    "ぎ",
    "ぐ",
    "げ",
    "ご",
    "ざ",
    "じ",
    "じ",
    "ず",
    "ぜ",
    "ぞ",
    "だ",
    "ぢ",
    "ぢ",
    "づ",
    "で",
    "ど",
    "ば",
    "び",
    "ぶ",
    "べ",
    "ぼ",
    "ぱ",
    "ぴ",
    "ぷ",
    "ぺ",
    "ぽ",
    "ふぁ",
    "ふぉ",
    "ふぃ",
    "か",
    "き",
    "く",
    "け",
    "こ",
    "た",
    "ち",
    "つ",
    "て",
    "と",
    "さ",
    "し",
    "し",
    "す",
    "せ",
    "そ",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ひ",
    "ふ",
    "へ",
    "ほ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "や",
    "ゆ",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "わ",
    "を",
    "あ",
    "い",
    "う",
    "え",
    "お",
    "ん",
    "ゃ",
    "ぇ",
    "ゅ",
    "ぃ",
    "ょ"
  ]

hepburn = [
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
  ];


from lang_trans import Transliteration

class Hepburn(Transliteration):

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
