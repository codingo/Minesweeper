![Minesweeper Logo](https://github.com/codingo/codingo.github.io/blob/master/assets/minesweeper_banner.png)
A Burpsuite plugin (BApp) to aid in the detection of scripts being loaded from over 14000+ malicious cryptocurrency mining domains (cryptojacking).

[![BApp Store](https://img.shields.io/badge/BApp-Published-orange.svg)](https://portswigger.net/bappstore/f317b96ea38b46fab74b13decc7116cc)
[![License](https://img.shields.io/badge/license-GPL3-_red.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Python 3.2|3.6](https://img.shields.io/badge/python-3.2|3.6-green.svg)](https://www.python.org/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/codingo/Minesweeper/issues)
[![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_)

# Summary
Minesweeper will passively scan in-scope items looking for matches against more than 14000+ known cryptojacking domains within the source of pages. When discovered, an alert similar to the following will be raised:

![Minesweeper Alert](https://github.com/codingo/codingo.github.io/blob/master/assets/minesweeper_example_request.png)

# Manually Updating Sources
As this is the first build of Minesweeper lists are currently built based on [CoinBlockerLists](https://github.com/ZeroDot1/CoinBlockerLists). As the project matures more sources will be added, as well as direct code checks. Since CoinBlockerLists updates quite frequently code is included to allow you to manually update your source list from the CoinBlockerLists github project.

If you don't wish to wait for the next build of the plugin and want to update your own sources you can use the following in the root of your cloned project:

```bash
$ ./lib/update_sources.py
```

This should produce an output similar to the following on a successful update:

![Minesweeper Update](https://github.com/codingo/codingo.github.io/blob/master/assets/minesweeper_sources_update.png)
