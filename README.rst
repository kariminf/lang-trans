pyTransliteration
=================

| |Project|
| |License|
| |PyPI|
| |Travis|
| |Codecov|

Python transliteration library (mostly from non-latin scripts, such as
Arabic, Japanese, etc.)

Use
---

Here an example of using Buckwalter transliteration for Arabic:

.. code:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from lang_trans.arabic import buckwalter

    print buckwalter.trans(u'هذا البرنامج يعطينا نطق الحروف')
    print buckwalter.untrans('h*A AlbrnAmj yETynA nTq AlHrwf')

- arabic
  - buckwalter

- japanese
  - hepburn

License
-------

Copyright (C) 2017 Abdelkrime Aries (kariminfo0@gmail.com)

| Licensed under the Apache License, Version 2.0 (the "License");
| you may not use this file except in compliance with the License.
| You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

| Unless required by applicable law or agreed to in writing, software
| distributed under the License is distributed on an "AS IS" BASIS,
| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
  implied.
| See the License for the specific language governing permissions and
| limitations under the License.

.. |Project| image:: https://img.shields.io/badge/Project-pyTransliteration-0BDA51.svg?style=plastic
   :target: https://github.com/kariminf/pytransliteration
.. |License| image:: https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |PyPI| image:: https://img.shields.io/pypi/v/lang-trans.svg?style=plastic
   :target: https://pypi.python.org/pypi/lang-trans
.. |Travis| image:: https://img.shields.io/travis/kariminf/lang-trans.svg?style=plastic
   :target: https://travis-ci.org/kariminf/pytransliteration
.. |Codecov| image:: https://img.shields.io/codecov/c/github/kariminf/lang-trans.svg?style=plastic
   :target: https://codecov.io/gh/kariminf/lang-trans
