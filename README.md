# lang-trans

[![License](https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic)](http://www.apache.org/licenses/LICENSE-2.0)
[![PyPI](https://img.shields.io/pypi/v/lang-trans.svg?style=plastic)](https://pypi.python.org/pypi/lang-trans)
[![Downloads](https://img.shields.io/pypi/dm/lang-trans.svg?style=plastic)](https://pypi.org/project/lang-trans/)
[![Python version](https://img.shields.io/pypi/pyversions/lang-trans.svg?style=plastic)](https://pypi.org/project/lang-trans/)
[![Travis](https://img.shields.io/travis/kariminf/lang-trans.svg?style=plastic)](https://travis-ci.org/kariminf/lang-trans)
[![Codecov](https://img.shields.io/codecov/c/github/kariminf/lang-trans.svg?style=plastic)](https://codecov.io/gh/kariminf/lang-trans)

Python transliteration library (mostly from non-latin scripts, such as Arabic, Japanese, etc.)

## Use

Here an example of using Buckwalter transliteration for Arabic:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lang_trans.arabic import buckwalter

print buckwalter.transliterate(u'هذا البرنامج يعطينا نطق الحروف')
print buckwalter.untransliterate('h*A AlbrnAmj yETynA nTq AlHrwf')
```

abbreviated methods:
- transliterate(text): trans(text)
- untransliterate(text): untrans(text)

## Available transliterators

- arabic
    - buckwalter
    - arabtex
    - iso233

- japanese
    - hepburn
    - nihonshiki
    - kunreishiki

## Similar projects


## License

Copyright (C) 2017-2018 Abdelkrime Aries (kariminfo0@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
