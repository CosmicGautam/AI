#TOKENIZATION
import nltk 
#nltk.download()
text = """welcome to nagarjuna college of information technology. it is one of the best college in the world. you will get all facility needed in this college."""
from nltk.tokenize import word_tokenize
print(word_tokenize(text))



#PARSE TREE
import nltk
from nltk.tree import Tree
sentence = "The quick brown fox jumps over the lazy dog."
parse_tree_string = "(S (NP (Det The) (Adj quick) (Adj brown) (N fox)) (VP (V jumps) (PP (P over) (NP (Det the) (Adj lazy) (N dog)))))"
parse_tree = Tree.fromstring(parse_tree_string)
parse_tree.pretty_print()
