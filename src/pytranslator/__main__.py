from . import translator
import fileinput

trans = translator.Translator()
if __name__ == '__main__':
    for line in fileinput.input():
        # line = "Còn đợi Merge với confirm nữa là xong"
        print(line)
        print(trans.translate(line))
