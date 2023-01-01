import src.main as main
import wikipedia


def test_wikiparse_eng():
    search1 = 'Fate'
    search2 = 'Destiny'

    answer = 'Destiny, sometimes referred to as fate ,' \
             ' is a predetermined course of events.' \
             ' It may be conceived as a predetermined future,' \
             ' whether in general or of an individual.'

    page1 = wikipedia.page(search1, auto_suggest=False)
    page2 = wikipedia.page(search2, auto_suggest=False)

    assert main.wikiparse(page1) == answer
    assert main.wikiparse(page2) == answer


def test_wikiparse_rus():
    search1 = 'Часы'
    search2 = 'Ночь'

    answer1 = "Часы́ — прибор для определения текущего времени суток и измерения продолжительности" \
              " временных интервалов в единицах, меньших, чем одни сутки." \
              " Самыми точными часами считаются атомные часы."

    answer2 = "Ночь — промежуток времени от захода Солнца вечером до его восхода утром." \
              " Продолжительность ночи зависит от географической широты места наблюдения и склонения Солнца." \
              " Иногда из понятия ночи исключаются интервалы вечерних" \
              " и утренних гражданских или астрономических сумерек."

    wikipedia.set_lang('ru')
    page1 = wikipedia.page(search1, auto_suggest=False)
    page2 = wikipedia.page(search2, auto_suggest=False)

    assert main.wikiparse(page1) == answer1
    assert main.wikiparse(page2) == answer2


def test_getwiki():
    wp = main.WikiBot().wiki
    wp.set_lang('en')

    search1 = 'aaghggjfjf'
    search2 = 'bot'
    search3 = 'Grand Order'

    answer1 = 'Sorry, I can\'t find anything on the subject😔.'
    answer2 = "Sorry, your query is too ambiguous!\n" \
              "'bot' may refer to:\n"
    answer3 = "Fate/Grand Order  is a free-to-play Japanese mobile game," \
              " developed by Lasengle  using Unity, and published by Aniplex," \
              " a subsidiary of Sony Music Entertainment Japan."

    assert main.getwiki(wp, search1) == answer1
    assert main.getwiki(wp, search2).startswith(answer2)
    assert main.getwiki(wp, search3).startswith(answer3)
