# golden

Tech and startup data extraction in Python.

Extract company summaries, timeline of recent events, key people and more.

1/ Clone repository
```
git clone git@github.com:terrosdesigns/golden.git
```

2/ Extract key tech and startup data !

```python
>>> import golden
>>> search = golden.download('Apple')

>>> golden.summary(search, sentences=1)
# Apple Inc. is a public company designing and selling personal computers, smartphones, consumer electronics, and software. Its headquarters is located in Cupertino, California and it was founded in 1976.﻿Apple Inc. is a California-based electronics company with a focus producing on consumer devices.

>>> events = golden.timeline(search, events=1)
>>> for event in events:
>>>     print(event["date"], " : ", event["subtitle"], "\n", event["content"])
# March 25, 2019  :  Apple Card
# On March 25, 2019 during their keynote event Apple, in partnership with Goldman Sachs and Mastercard, announced Apple Card. A credit card by Apple with no fees—no annual, cash-advance, over-the-limit, international, or late fees— thats gives Apple users the ability to sign up for Apple Card using the Apple Wallet application.

```
