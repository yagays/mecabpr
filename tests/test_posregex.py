from mecabpr import MeCabPosRegex


def test_sentnece_01():
    mpr = MeCabPosRegex()
    sentence = "あらゆる現実をすべて自分のほうへねじ曲げたのだ。"

    # あらゆる現実をすべて自分のほうへねじ曲げたのだ。
    # あらゆる        連体詞,*,*,*,*,*,あらゆる,アラユル,アラユル
    # 現実    名詞,一般,*,*,*,*,現実,ゲンジツ,ゲンジツ
    # を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
    # すべて  名詞,副詞可能,*,*,*,*,すべて,スベテ,スベテ
    # 自分    名詞,一般,*,*,*,*,自分,ジブン,ジブン
    # の      助詞,連体化,*,*,*,*,の,ノ,ノ
    # ほう    名詞,非自立,一般,*,*,*,ほう,ホウ,ホー
    # へ      助詞,格助詞,一般,*,*,*,へ,ヘ,エ
    # ねじ曲げ        動詞,自立,*,*,一段,連用形,ねじ曲げる,ネジマゲ,ネジマゲ
    # た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
    # の      名詞,非自立,一般,*,*,*,の,ノ,ノ
    # だ      助動詞,*,*,*,特殊・ダ,基本形,だ,ダ,ダ
    # 。      記号,句点,*,*,*,*,。,。,。

    assert mpr.findall(sentence, "名詞") == [['現実'], ['すべて'], ['自分'], ['ほう'], ['の']]
    assert mpr.findall(sentence, "連体詞") == [['あらゆる']]
    assert mpr.findall(sentence, "記号") == [['。']]
    assert mpr.findall(sentence, "助詞") == [['を'], ['の'], ['へ']]
    assert mpr.findall(sentence, "助動詞") == [['た'], ['だ']]
    assert mpr.findall(sentence, "連体詞") == [['あらゆる']]
    assert mpr.findall(sentence, "動詞") == [['ねじ曲げ']]
    assert mpr.findall(sentence, "その他") == []
    assert mpr.findall(sentence, "フィラー") == []
    assert mpr.findall(sentence, "感動詞") == []
    assert mpr.findall(sentence, "形容詞") == []
    assert mpr.findall(sentence, "接続詞") == []
    assert mpr.findall(sentence, "接頭詞") == []
    assert mpr.findall(sentence, "副詞") == []

    assert mpr.findall(sentence, "名詞助詞") == [['現実', 'を'], ['自分', 'の'], ['ほう', 'へ']]

    assert mpr.findall(sentence, "名詞?助詞") == [['現実', 'を'], ['自分', 'の'], ['ほう', 'へ']]
    assert mpr.findall(sentence, "名詞*助詞") == [['現実', 'を'], ['すべて', '自分', 'の'], ['ほう', 'へ']]

    assert mpr.findall(sentence, "名詞{2}") == [['すべて', '自分']]
    assert mpr.findall(sentence, "名詞{1,2}") == [['現実'], ['すべて', '自分'], ['ほう'], ['の']]

    assert mpr.findall(sentence, "(名詞助詞){2}") == [['自分', 'の', 'ほう', 'へ']]
    assert mpr.findall(sentence, "(名詞助詞){1,2}") == [['現実', 'を'], ['自分', 'の', 'ほう', 'へ']]

    assert mpr.findall(sentence, "(名詞|動詞)") == [['現実'], ['すべて'], ['自分'], ['ほう'], ['ねじ曲げ'], ['の']]

    assert mpr.findall(sentence, "^連体詞") == [['あらゆる']]
    assert mpr.findall(sentence, "^名詞") == []

    assert mpr.findall(sentence, "記号$") == [['。']]
    assert mpr.findall(sentence, "名詞$") == []

    assert mpr.findall(sentence, "名詞-一般") == [['現実'], ['自分']]
    assert mpr.findall(sentence, "名詞-非自立") == [['ほう'], ['の']]
    assert mpr.findall(sentence, "名詞-数") == []
    assert mpr.findall(sentence, "名詞-接尾") == []
    assert mpr.findall(sentence, "名詞-固有名詞") == []

    assert mpr.findall(sentence, "動詞-自立") == [['ねじ曲げ']]
    assert mpr.findall(sentence, "動詞-非自立") == []

    assert mpr.findall(sentence, "名詞-一般助詞") == [['現実', 'を'], ['自分', 'の']]
    assert mpr.findall(sentence, "(名詞-一般)(助詞)") == [['現実', 'を'], ['自分', 'の']]

    assert mpr.findall(sentence, "名詞-副詞可能名詞-一般助詞") == [['すべて', '自分', 'の']]

    assert mpr.findall(sentence, ".*") == [['あらゆる', '現実', 'を', 'すべて',
                                            '自分', 'の', 'ほう', 'へ', 'ねじ曲げ', 'た', 'の', 'だ', '。']]


def test_sentnece_01_raw():
    mpr = MeCabPosRegex()
    sentence = "あらゆる現実をすべて自分のほうへねじ曲げたのだ。"

    assert mpr.findall(sentence, "名詞", raw=True) == [['現実\t名詞,一般,*,*,*,*,現実,ゲンジツ,ゲンジツ'],
                                                     ['すべて\t名詞,副詞可能,*,*,*,*,すべて,スベテ,スベテ'],
                                                     ['自分\t名詞,一般,*,*,*,*,自分,ジブン,ジブン'],
                                                     ['ほう\t名詞,非自立,一般,*,*,*,ほう,ホウ,ホー'],
                                                     ['の\t名詞,非自立,一般,*,*,*,の,ノ,ノ']]

    assert mpr.findall(sentence, "名詞名詞", raw=True) == [['すべて\t名詞,副詞可能,*,*,*,*,すべて,スベテ,スベテ',
                                                        '自分\t名詞,一般,*,*,*,*,自分,ジブン,ジブン']]


def test_neologd():
    mpr = MeCabPosRegex()
    mpr_neologd = MeCabPosRegex("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    assert mpr.findall("8月3日", "名詞") == [['8'], ['月'], ['3'], ['日']]
    assert mpr_neologd.findall("8月3日", "名詞") == [['8月3日']]
