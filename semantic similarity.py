# Python code to measure similarity between two sentences using cosine similarity. 
import spacy
nlp = spacy.load("en_core_web_sm")
# Sentences
s1 = nlp("The weather is rainy.")
s2 = nlp("It is going to rain outside.")
# Calculate the similarity
print("The similarity is:",s1.similarity(s2))