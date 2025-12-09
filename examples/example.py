import sys
sys.path.append("..")

from src.formeler import Formeler


def test_detect():
    api = Formeler("YOUR-API-KEY")
    lang = api.lang_id.detect("Dies ist ein Test")
    print(lang)


def test_batch_detect():
    api = Formeler("YOUR-API-KEY")
    langs = api.lang_id.batch_detect(["This is a test", "Dies ist ein Test"])
    print(langs)


def test_detect_on_premiss():
    api = Formeler("YOUR-API-KEY", "https://formeler.com/api")
    lang = api.lang_id.detect("Dies ist ein Test")
    print(lang)


def main():
    test_detect()
    test_batch_detect()


if __name__ == "__main__":
    main()
