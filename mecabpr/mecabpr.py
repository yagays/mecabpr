import re
import MeCab

from .pos_dictionary import pos2id


class MeCabPosRegex:
    def __init__(self, mecab_option=""):
        self.tagger = MeCab.Tagger(mecab_option)
        self.tagger.parse("")

    def get_all_possible_pos(self):
        return sorted(pos2id.keys(), key=lambda x: len(x))

    def convert_string(self, pos_raw_list):
        pos_list = ["-".join(t[1:5]) for t in pos_raw_list]
        return "".join([pos2id[p] for p in pos_list])

    def convert_pattern(self, string, dic):
        for i, j in pos2id.items():
            string = string.replace(i, "({})".format(j))
        return string

    def findall(self, string, pattern, raw=False):
        pos_raw = [t for t in self.tagger.parse(string).split("\n") if "\t" in t]
        pos_raw_list = [re.split(r',|\t', t) for t in pos_raw]

        # convert string into id sequence
        pos_seq = self.convert_string(pos_raw_list)

        # convert pattern into id sequence
        reg_pattern = self.convert_pattern(pattern, pos2id)

        # specify output format
        if raw:
            tokens = pos_raw
        else:
            tokens = [t[0] for t in pos_raw_list]

        output = []
        for m in re.finditer(reg_pattern, pos_seq):
            start = int(m.start() / 4)
            end = int(start + len(m.group()) / 4)
            if not len(m.group()):
                continue

            output.append(tokens[start:end])
        return output

    def extract_nouns(self, string):
        return ["".join(t) for t in self.findall(string, "名詞")]

    def extract_noun_phrase(self, string):
        return ["".join(t) for t in self.findall(string, "名詞*")]

    def extract_verbs(self, string):
        return ["".join(t) for t in self.findall(string, "動詞")]
