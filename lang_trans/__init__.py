#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  transliteration.py
#  An abstract class  for language transliteration
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


import sys
import abc

if sys.version_info >= (3, 4):
	ABC = abc.ABC
else:
	ABC = abc.ABCMeta('ABC', (), {})


class Trans(ABC):

	def __init__(self):
		pass

	def trans(self, word):
		return self.transliterate(word)

	@abc.abstractmethod
	def transliterate(self, word):
		return word

	def untrans(self, word):
		return self.untransliterate(word)

	@abc.abstractmethod
	def untransliterate(self, word):
		return word

class MapTrans(Trans):

	def __init__(self, the_map):
		self.the_map = the_map

	def transliterate(self, word):
		res = ""
		if len(word) < len(self.the_map):
			for char in word:
				res += self.the_map.get(char, char)
		else:
			res = word
			for k,v in self.the_map.items():
				res = res.replace(k, v)

		return res

	def untransliterate(self, word):
		res = word
		for k,v in self.the_map.items():
			res = res.replace(v, k)

		return res


class L2LTrans(Trans):

	def __init__(self, src, dst):
		self.src = src
		self.dst = dst

	def transliterate(self, word):
		res = word
		for i, v in enumerate(self.src):
			res = res.replace(v, self.dst[i])
		return res

	def untransliterate(self, word):
		res = word
		for i, v in enumerate(self.dst):
			res = res.replace(v, self.src[i])
		return res
