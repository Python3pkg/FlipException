# FlipException
_uoᴉʇdǝɔxƎdᴉꞁᖵ ǝsᴉɐɹ_

The best way to flip an exception out of rage.

![PyPi status](https://img.shields.io/pypi/status/flipexception.svg)
[![PyPI version](https://badge.fury.io/py/flipexception.svg)](https://badge.fury.io/py/flipexception)
[![Build Status](https://travis-ci.org/xeBuz/FlipException.svg?branch=master)](https://travis-ci.org/xeBuz/FlipException)
[![Code Climate](https://codeclimate.com/github/xeBuz/FlipException/badges/gpa.svg)](https://codeclimate.com/github/xeBuz/FlipException)


## Installation
```bash
pip install flipexception
```


## Usage

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipException


try:
    raise FlipException("Oops, something happens")
except Exception, e:
    print str(e)
```

```
(╯°□°）╯︵ suǝddɐɥ ƃuᴉɥʇǝɯos 'sdoO
```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipException
    
try:
    raise FlipException()
except FlipException, e:
    print str(e)
```

```
(╯°□°）╯︵ ┻━┻
```


