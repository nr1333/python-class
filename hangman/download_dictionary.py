import wget

url = 'https://github.com/C-Erastus/low-level-development/blob/master/hangman-game/dictionary.txt'
dictionary = wget.download(url)
