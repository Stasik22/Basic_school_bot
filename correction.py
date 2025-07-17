from symspellpy.symspellpy import SymSpell, Verbosity

sym = SymSpell(max_dictionary_edit_distance=2)
sym.load_dictionary("dict.txt", term_index= 0, count_index= 1)

def correction(word):
    suggestion = sym.lookup(word,Verbosity.CLOSEST ,max_edit_distance=2)
    return suggestion[0].term if suggestion else word


