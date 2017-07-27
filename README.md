# pyTransliteration

[![Project](https://img.shields.io/badge/Project-pyTransliteration-0BDA51.svg?style=plastic)](https://github.com/kariminf/pytransliteration)
[![Version](https://img.shields.io/badge/Version-0.1.0-0BDA51.svg?style=plastic)](https://github.com/kariminf/pytransliteration/releases)
[![License](https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic)](http://www.apache.org/licenses/LICENSE-2.0)
[![Travis](https://img.shields.io/travis/kariminf/ArArud.svg?style=plastic)](https://travis-ci.org/kariminf/pytransliteration)

Python transliteration library (mostly from non-latin scripts, such as Arabic, Japanese, etc.)

## Use

Here an example of using Buckwalter transliteration for Arabic:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lang_trans.arabic.buckwalter import Buckwalter

trans = Buckwalter()

print trans.transliterate(u'هذا البرنامج يعطينا نطق الحروف')
print trans.untransliterate('h*A AlbrnAmj yETynA nTq AlHrwf')
```


## License

Copyright (C) 2017 Abdelkrime Aries (kariminfo0@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
