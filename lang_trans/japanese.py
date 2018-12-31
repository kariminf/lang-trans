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

loneUnTrans = {
	"ku": "く",
	"su": "す",
	"nu": "ぬ",
	"fu": "ふ",
	"hu": "ふ",
	"mu": "む",
	"yu": "ゆ",
	"ru": "る",
	"gu": "ぐ",
	"zu": "ず",
	"du": "づ",
	"bu": "ぶ",
	"pu": "ぷ"
}


from lang_trans import L2LTrans
import re


def post_trans(word):
	res = re.sub(ur"ix", "", word)
	return re.sub(ur"(っ+)(.)", lambda m: (m.group(2) * (1 + len(m.group(1)))), res)

def tsu_replace_call(m):
	c = m.group(1)
	try:
		"aeuio".index(c) # if no exception
		return m.group()
	except ValueError:
		rep_char = u"っ"
		if c == "n":
			rep_char = u"ん"
		nbr = len(m.group())/len(c) - 1
		return (rep_char * nbr) + c

def tsu_replace(word):
	return re.sub(r"(sh|ch|.)\1+", tsu_replace_call, word)

def xya2jap_call(m):
	res = m.group()
	try:
		i = trans_tab.index(m.group(1) + "i") # can generate ValueError
		res = hiragana[i]
		i = trans_tab.index("xy" + m.group(2)) # can generate ValueError
		res += hiragana[i]
		return res
	except ValueError:
		return res

def xya2jap(word):
	return re.sub(r"(sh|ch|.)y([aeuio])", xya2jap_call, word)

def post_untrans_call(m):
	key = m.group()
	more_than_one = (len(m.group()) > 1)
	if more_than_one:
		if key == u"tう":
			return "つ"
		key = key[:-1]
	key += "u"
	res = ""
	if key in loneUnTrans:
		res = loneUnTrans[key]
	if more_than_one:
		res += "う"
	return res

def post_untrans(word):
	return re.sub(ur"[a-z][う]?", post_untrans_call, word)

class Hepburn(L2LTrans):

	def __init__(self):
		L2LTrans.__init__(self, hiragana, trans_tab)

	@staticmethod
	def pre_trans(word):
		return re.sub(ur"([しちじぢ])([ゃぇゅょ])", lambda m: (
		(trans_tab[hiragana.index(m.group(1))] + trans_tab[hiragana.index(m.group(2))]).replace("ixy", "")
		), word)

	def transliterate(self, word):
		res = Hepburn.pre_trans(word)
		res = L2LTrans.transliterate(self, res)
		return post_trans(res)

	@staticmethod
	def pre_untrans(word):
		res = tsu_replace(word)
		res = re.sub(r"(sh|ch|j)([aeuo])", xya2jap_call, res)
		return xya2jap(res)

	def untransliterate(self, word):
		res = Hepburn.pre_untrans(word)
		res = L2LTrans.untransliterate(self, res)
		return post_untrans(res)


hepburn = Hepburn()
