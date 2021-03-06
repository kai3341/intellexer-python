#!/usr/bin/env python3

# mock data
import data
import intellexer

print('Running: named_entity_recognizer')

named_entity_recognizer = intellexer.NamedEntityRecognizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')

response = named_entity_recognizer.url(
	url=data.URL,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
)

print(response.data)

print()

print('Trying to use TEXT:')

response = named_entity_recognizer.text(
	text=data.TEXT,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
)

print(response.data)

print()

print('Trying to use FILE:')

response = named_entity_recognizer.file(
	file=data.FILE1(),
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
)

print(response.data)

print()
