# Minesweeper
[![License](https://img.shields.io/badge/license-GPL3-_red.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Python 3.2|3.6](https://img.shields.io/badge/python-3.2|3.6-green.svg)](https://www.python.org/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_)

A Burpsuite plugin to aid in the detection of malicious crypto currency mining Scripts (cryptojacking).

# Sumnmary
Minesweeper will passively scan in-scope items looking for matches against more than 3000 known cryptojacking domains within the source of pages. When discovered, an alert similar to the following will be raised:

![Minesweeper Alert](https://github.com/codingo/codingo.github.io/blob/master/assets/MinesweeperExampleRequest.PNG)
