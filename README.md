This is my personal iTerm semantic history script. It handles any text that I command-click on in iTerm2.

Functions so far:

* Open URLs in default browser
* Open paths in PyCharm and bring PyCharm to front
* Adjust paths if they start with /vagrant/
* Remove cruft from paths printed by flake8

Probably most of these specific things will be useless or wrong for your setup -- but they might give you some ideas for your own script.

### To Install: ###

1. Fork and clone the repo.
2. Go to Preferences -> Profiles -> Advanced -> Semantic History -> Always run command ... and enter something like:

		python ~/iterm_semantic_history/script.py "\1" "\2" "\3" "\4" "\5"
    
