This is my personal iTerm semantic history script. It handles any text that I command-click on in iTerm2.
It opens paths in PyCharm and bring PyCharm to front

For now, it supports the following constructs:

* karma output like `at Context.<anonymous> (webpack:///frontend_tests/models/test_order_item.js:186:11 <-
  frontend_tests/index.js:32906:23)`

* py.test output


### To Install: ###

1. Fork and clone the repo.
2. Go to Preferences -> Profiles -> Advanced -> Semantic History -> Always run command ... and enter something like:

    /usr/local/bin/python3 ~/Projects/iterm_semantic_history/script.py "\1" "\2" "\5"
    
