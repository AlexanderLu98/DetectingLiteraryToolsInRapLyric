import sentencepiece as spm

# Train the SentencePiece model
spm.SentencePieceTrainer.Train('--input=rap_lyrics.txt --model_prefix=rap_lyrics --vocab_size=100')

# Load the trained model with a SentencePieceProcessor
sp = spm.SentencePieceProcessor()
sp.load('rap_lyrics.model')

# Tokenize a rap lyric
rap_lyric = "Your rap lyrics here"
subword_tokens = sp.encode_as_pieces(rap_lyric)

# Print the subword tokens
print(subword_tokens)
