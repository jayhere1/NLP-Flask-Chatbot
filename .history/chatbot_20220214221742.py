from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
CB = ChatBot(
    "Buddy",
    read_only=True,
    preprocessors=[
        "chatterbot.preprocessors.clean_whitespace",
        "chatterbot.preprocessors.unescape_html",
        "chatterbot.preprocessors.convert_to_ascii",
    ],
)
# Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train("chatterbot.corpus.english")
