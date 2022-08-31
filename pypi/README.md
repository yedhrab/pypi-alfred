# PyPI Client

Search pypi for query and get result list

## ⭐️ Examaple Usage

```python
async with PyPICilent() as client:
    results = await client.search("yemreak")
    assert len(results) > 0
```

```python      
[
    Result(
        name='ypackage',
        version='3.0.4',
        created='Jan 17, 2022',
        description=
        "Yunus Emre Ak ~ YEmreAk (@yedhrab)'ın google drive direkt link oluşturmagitbook entegrasyonu, google arama motoru sonuçlarını filtreleme ile ilgili çalışmaları",
        url='https://pypi.org//project/ypackage/'
    ),
    Result(
        name='yinstabot',
        version='2.5.3',
        created='Nov 6, 2019',
        description='Instagram bot',
        url='https://pypi.org//project/yinstabot/'
    )
]
```

## 🪪 License

```
Copyright 2022 Yunus Emre Ak ~ YEmreAk.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
