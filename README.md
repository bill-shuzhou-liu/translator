The python code to auto detect the language and transalte it to English

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
trans = translator.Translator(to_language = "fr")
trans.translate("Còn đợi Merge với confirm nữa là xong")
```
The default cache file is: ~/.cache3/default.sqlite3