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

import sys
import abc

if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (), {})

class Transliteration(ABC):

	def __init__(self):
		pass

	@abc.abstractmethod
	def transliterate(self, word):
		return word

	@abc.abstractmethod
	def untransliterate(self, word):
		return word
