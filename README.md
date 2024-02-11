Auto detect the language and translate it to another language

# install
```
pip install -e .
```

# run
```
cat  tests/example.txt | python3 -m pytranslator
```

# how to use
```
from pytranslator import translator
trans = translator.Translator(to_language = "en")
trans.translate("Còn đợi Merge với confirm nữa là xong")
```
The default cache file is: ~/.cache3/default.sqlite3