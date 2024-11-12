import string
import re
import os

import itertools

vowel = ['a', 'e', 'o', 'i', 'u']
punctuation = [' ', '-', '_', '-', '·']
r_punctuation = ['.', ' ', '_']
common_letter_replace_dic = {'b':'p','i':'1,l',"l":'i,1',"o":'0','c':'k','k':'c','p':'b','m':'n','n':'m','s':'5'}

prefix_list = []
file_name = os.getcwd() + os.path.sep + "prefix.txt"
file_obj = open(file_name,"r")
try:
    for line in file_obj:
        prefix_list.append(line.rstrip("\n"))
finally:
    file_obj.close()

class DeformationMethod:
    """generate appname or packagename variants"""

    def __init__(self, ori_name):
        self.ori_name = ori_name
        self.variant_dic = {}
        self.length = len(self.ori_name)

    def appname_deformation(self):
        self.vowel_character_deletion()
        self.vowel_character_insertion()
        self.vowel_character_substitution()
        self.double_character_deletion()
        self.double_character_insertion()
        self.common_misspelling_mistakes_substition()
        self.puncatuation_deletion()
        self.puncatuation_substitution()
        self.add_suffix_variants()
        self.add_character_variants()
        self.add_symbol_variants()
        self.add_emoji_variants()
        self.string_rearrangement_for_app_name()
        # self.add_case_variants()
        if (self.ori_name in self.variant_dic.keys()) or (self.ori_name.lower() in self.variant_dic.keys()):   #
            self.variant_dic.pop(self.ori_name)
        # if (self.ori_name in self.variant_dic.keys()) :  # self.add_case_variants()
        #     self.variant_dic.pop(self.ori_name)

    # def packagename_deformation(self):
    #     self.vowel_character_deletion()
    #     self.vowel_character_insertion()
    #     self.vowel_character_substitution()
    #     self.double_character_deletion()
    #     self.double_character_insertion()
    #     self.common_misspelling_mistakes_substition()
    #     self.puncatuation_deletion()
    #     self.puncatuation_substitution()
    #     # self.string_rearrangement()
    #     if (self.ori_name in self.variant_dic.keys()) or (self.ori_name.lower() in self.variant_dic.keys()):
    #         self.variant_dic.pop(self.ori_name)

    def vowel_character_insertion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                for r_letter in vowel:
                    word = self.ori_name.lower()
                    word = word[0:i] + r_letter + word[i:]
                    self.variant_dic[word] = 'vowel_character_insertion'

    def vowel_character_deletion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                word = word[0:i] + word[i+1:]
                self.variant_dic[word] = 'vowel_character_deletion'

    def vowel_character_substitution(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                for r_letter in vowel:
                    word = self.ori_name.lower()
                    if r_letter != word[i]:
                        word = word[0:i] + r_letter + word[i+1:]
                        self.variant_dic[word] = 'vowel_character_substitution'

    def double_character_insertion(self):
        for i in range(0,self.length-1):
            word = self.ori_name.lower()
            if word[i] == word[i + 1]:
                word = word[0:i] + word[i] + word[i:]
                self.variant_dic[word] = 'double_character_insertion'

    def double_character_deletion(self):
        for i in range(0,self.length-1):
            word = self.ori_name.lower()
            if word[i] == word[i + 1]:
                word = word[0:i] + word[i+1:]
                self.variant_dic[word] = 'double_character_deletion'
                word = word[0:i] + word[i + 1:]
                self.variant_dic[word] = 'double_character_deletion'

    def puncatuation_substitution(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in punctuation:
                for r_letter in punctuation:
                    word = self.ori_name.lower()
                    if r_letter != word[i]:
                        word = word[0:i] + r_letter +word[i+1:]
                        self.variant_dic[word] = 'puncatuation_substitution'
                        word = self.ori_name.lower()
                        word = word.replace(" ", r_letter)
                        word = word.replace("_", r_letter)
                        word = word.replace(".", r_letter)
                        word = word.replace("·", r_letter)
                        word = word.replace("-", r_letter)
                        self.variant_dic[word] = 'puncatuation_substitution'

    def puncatuation_deletion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in punctuation:
                word = word[0:i] + word[i + 1:]
                self.variant_dic[word] = 'puncatuation_deletion'
        word = self.ori_name.lower()
        word = word.replace(" ", "")
        word = word.replace("_", "")
        word = word.replace(".", "")
        word = word.replace("·", "")
        word = word.replace("-", "")
        self.variant_dic[word] = 'puncatuation_deletion'

    def common_misspelling_mistakes_substition(self):
        for i in range(0, self.length):
            for key in common_letter_replace_dic.keys():
                word = self.ori_name.lower()
                if word[i] == key:
                    letter = word[i]
                    values = common_letter_replace_dic.get(key)
                    if ',' in values:
                        value = values.split(',')
                        for val in value:
                            word = self.ori_name.lower()
                            word = word[0:i] + val + word[i + 1:]
                            self.variant_dic[word] = 'misspelling_mistakes_substition'
                            word = word.replace(letter,val)
                            self.variant_dic[word] = 'misspelling_mistakes_substition'
                    else:
                        word = word[0:i] + values + word[i + 1:]
                        self.variant_dic[word] = 'misspelling_mistakes_substition'
                        word = word.replace(letter, values)
                        self.variant_dic[word] = 'misspelling_mistakes_substition'

    # def string_rearrangement_for_app_name(self):
    #     # 使用正则表达式分隔字符串，支持空格、·、-
    #     word_list = re.split(r'[ \-·]+', self.ori_name)
    #     length = len(word_list)
    #     number = list(range(length))  # 生成单词的索引列表

    #     # 确定排列的起始长度
    #     start = max(1, length - 2)

    #     # 生成排列组合
    #     for le in range(start, length):
    #         numberlist = list(itertools.permutations(number, le + 1))
    #         for numberls in numberlist:
    #             newword = ' '.join(word_list[num] for num in numberls)  # 按顺序拼接单词
    #             self.variant_dic[newword] = 'string_rearrangement'

    def string_rearrangement_for_app_name(self):
    # 使用正则表达式分隔字符串，支持空格、·、-
        word_list = re.split(r'[ \-·]+', self.ori_name)
        
        # 移除空字符串，以防连续分隔符导致空字符串出现在列表中
        word_list = [word for word in word_list if word]
        
        length = len(word_list)
        number = list(range(length))  # 生成单词的索引列表

        # 只生成与原始字符串同等长度的排列组合
        numberlist = list(itertools.permutations(number, length))
        for numberls in numberlist:
            newword = ' '.join(word_list[num] for num in numberls)  # 按顺序拼接单词
            self.variant_dic[newword] = 'string_rearrangement'

    def add_suffix_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["pro", "AI", "v1", "v2", "updated", "plus"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'word_expansion'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'word_expansion'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'word_expansion'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'word_expansion'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'word_expansion'
            variant = f"{self.ori_name}·{suffix}"
            self.variant_dic[variant] = 'word_expansion'


    def add_symbol_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["+", "#", "$", "~", "-", "·", ".", "_"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            variant = f"{self.ori_name}·{suffix}"
            self.variant_dic[variant] = 'symbol_expansion'
            

    def add_character_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["1", "2", "Ⅰ", "Ⅱ"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'string_expansion'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'string_expansion'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'string_expansion'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'string_expansion'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'string_expansion'
            variant = f"{self.ori_name}·{suffix}"
            self.variant_dic[variant] = 'string_expansion'
    
    def add_emoji_variants(self):
        suffixes = [
        "🚀", "👍", "🎉", "⭐", "🔥", "🔥", "🎁", "🔔", "🌟", "💡", "📈", "💪", "✨", "✅", "🥇", "💥", 
        "📣", "🏆", "👏", "🎈", "🛠", "📝", "💬", "🤖", "📚", "🔍", "💭", "⏳", "🧠", "🎓", "🌍", 
        "💼", "⚙️", "🔑", "🌐", "📊", "🖥", "📌", "🎯", "📆", "💰", "💬", "🔗", "📌", "🧩", "🚧", "🌱", "💎"
        ]
        
        for suffix in suffixes:
            # suffix_emoji = f'U+{ord(suffix):X}'
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'
            variant = f"{self.ori_name}·{suffix}"
            self.variant_dic[variant] = 'Emoji_expansion'

    def add_case_variants(self):
        """Generate case variations for the original name, handling both single and multi-word names and removing duplicates."""
        
        # 检查名称是否为单个单词还是多个单词
        words = self.ori_name.split()
        print(self.ori_name)

        # 如果是单个单词
        if len(words) == 1:
            single_word_lower = self.ori_name.lower()
            single_word_upper = self.ori_name.upper()
            single_word_title = self.ori_name.capitalize()
            
            # 添加变体：全小写、全大写和首字母大写
            self.variant_dic[single_word_lower] = 'case_variation'
            self.variant_dic[single_word_upper] = 'case_variation'
            self.variant_dic[single_word_title] = 'case_variation'

        # 如果是多个单词
        else:
            # 将整个名称转换为所需的三种格式
            multi_word_lower = ' '.join(word.lower() for word in words)
            multi_word_upper = ' '.join(word.upper() for word in words)
            multi_word_title = ' '.join(word.capitalize() for word in words)
            
            # 添加变体：全小写、全大写和每个单词首字母大写
            self.variant_dic[multi_word_lower] = 'case_variation'
            self.variant_dic[multi_word_upper] = 'case_variation'
            self.variant_dic[multi_word_title] = 'case_variation'

        # 删除与原始名称相同的变体
        if self.ori_name in self.variant_dic:
            del self.variant_dic[self.ori_name]