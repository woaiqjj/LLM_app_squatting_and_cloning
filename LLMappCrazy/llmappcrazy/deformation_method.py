import string
import os

import itertools

vowel = ['a', 'e', 'o', 'i', 'u']
punctuation = [' ', '-', '_']
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
        if (self.ori_name in self.variant_dic.keys()) or (self.ori_name.lower() in self.variant_dic.keys()):
            self.variant_dic.pop(self.ori_name)

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

    def add_suffix_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["tutor", "master", "assistant", "pro", "AI"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'

    def add_symbol_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["+", "#", "$", "~"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'

    def add_character_variants(self):
        """Add suffixes or emojis to the original name to generate variants."""
        # , "\ud83d\ude80", "\ud83d\udc4d", "\ud83c\udf89"
        suffixes = ["1", "2", "Ⅰ", "Ⅱ"]
        for suffix in suffixes:
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
    
    def add_emoji_variants(self):
        suffixes = [
        "🚀", "👍", "🎉", "⭐", "🔥", "🎁", "🔔", "🌟", "💡", "📈", "💪", "✨", "✅", "🥇", "💥", 
        "📣", "🏆", "👏", "🎈", "🛠", "📝", "💬", "🤖", "📚", "🔍", "💭", "⏳", "🧠", "🎓", "🌍", 
        "💼", "⚙️", "🔑", "🌐", "📊", "🖥", "📌", "🎯", "📆", "💰", "💬", "🔗", "📌", "🧩", "🚧", "🌱"
        ]
        
        for suffix in suffixes:
            # suffix_emoji = f'U+{ord(suffix):X}'
            variant = f"{self.ori_name}{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name} {suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}-{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}_{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'
            variant = f"{self.ori_name}.{suffix}"
            self.variant_dic[variant] = 'add_suffix_variants'