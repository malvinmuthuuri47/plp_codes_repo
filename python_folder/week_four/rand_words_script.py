import os
import random

WORDS = [
	"the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
    "hello", "world", "python", "code", "random", "sentence", "generate",
    "text", "data", "example", "words", "list"
]

def random_sentence_bytes(num_bytes):
	"""Generate a random sentence of words with apporximately num_bytes in UTF-8 encoding"""
	sentence = ""

	# Keep adding words until we reach or slightly exceed the target byte length
	while len(sentence.encode('utf-8')) < num_bytes:
		word = random.choice(WORDS)
		if sentence:
			sentence += " " # add space between words
		sentence += word

	# Trim last word if it overshoots
	while len(sentence.encode('utf-8')) > num_bytes:
		sentence = sentence.rsplit(" ", 1)[0]	# remove last word

	# capitalise first letter and add a period if there's space
	if sentence:
		sentence = sentence[0].upper() + sentence[1:]
		if len(sentence.encode('utf-8')) + 1 <= num_bytes:
			sentence += '.'

	return sentence


def write_random_sentences(filename, sentence_count, bytes_per_sentence):
	with open(filename, 'w', encoding='utf-8') as f:
		for _ in range(sentence_count):
			sentence = random_sentence_bytes(bytes_per_sentence)
			f.write(sentence + '\n')

write_random_sentences("rand_sentences.txt", 600, 50)
print("rand_sentences.txt created successfully")
