# golden

Tech and startup data extraction in Python.

Extract company summaries, timeline of recent events, key people and more.

```
import golden

search = golden.download('facebook')

golden.summary(search, sentences=3)

golden.timeline(search, events=2)

```
