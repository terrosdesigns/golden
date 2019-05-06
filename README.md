# golden

Tech and startup data extraction in Python.

Extract company summaries, timeline of recent events, key people and more.

1/ Clone repository
```
git clone git@github.com:terrosdesigns/golden.git
```

2/ Extract key tech and startup data !

```python
>>> from golden import golden
>>> search = golden.download('Apple')

>>> golden.title(search)
# 'Apple (company)'

>>> golden.summary(search)
# Apple Inc. is a public company designing and selling personal computers, smartphones, consumer electronics, and software. Its headquarters is located in Cupertino, California and it was founded in 1976.﻿Apple Inc. is a California-based electronics company with a focus producing on consumer devices.

>>> golden.content(search, sentences=3)
#'﻿Apple Inc. is a California-based electronics company with a focus producing on consumer devices. ﻿Products﻿Products and devices produced by Apple Inc. include iPad, iPhone, AirPods,Apple Watch, HomePod, and MacBook.﻿ Each product can give users access to one or more forms of media or technology including television, music, data storage, and computer applications.The products run on the Mac operating system, which has special features thare not available on non-Mac systems. Furthermore, the devices use continuity, which allows for all the devices owned by a user to beconnected.﻿﻿﻿The company also produces software as a service and media options.'

>>> events = golden.timeline(search, events=1)
>>> for event in events:
>>>     print(event["date"], " : ", event["subtitle"], "\n", event["content"])
# March 25, 2019  :  Apple Card
# On March 25, 2019 during their keynote event Apple, in partnership with Goldman Sachs and Mastercard, announced Apple Card. A credit card by Apple with no fees—no annual, cash-advance, over-the-limit, international, or late fees— thats gives Apple users the ability to sign up for Apple Card using the Apple Wallet application.

>>> other_search = golden.download("jetpack aviation")
>>> people = golden.people(other_search)
>>> for p in people:
>>>     print(p["name"], p["role"])
# Boris Jarry Employee
# Daniel Schwarzbaum Employee
# David Mayman Founder, CEO, Test Pilot, Project Manager
# Nelson Tyler Founder, Principle Designer
# Sergey Samchik Employee

>>> ceo = golden.people(other_search, "CEO")
>>> print(ceo)
# David Mayman : Founder, CEO, Test Pilot, Project Manager
```


TO DO

Add new queries :
- Commpany Url
- Products
- Country

Improve suggestion while querying

Hide html output when downloading a new page

Improve content query output:
- Sentences nb query parameter doesn't always work
