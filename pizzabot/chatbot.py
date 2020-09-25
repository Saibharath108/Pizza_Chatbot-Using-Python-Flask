from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('YOYOBot')
 # Training with Personal Ques & Ans 
#conversation = [
#    "Hello",
#    "Hi there!",
#    "How are you doing?",
#    "I'm doing great.",
#    "That is good to hear",
#    "Thank you.",
#    "You're welcome."
#]

#trainer = ListTrainer(chatbot)
#trainer.train(conversation)
#'chatterbot.corpus.english'
# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    './data/veg.yml',
    './data/nonveg.yml',
    './data/vegnonvegitem.yml',
    './data/conform.yml',
    './data/conformorder.yml',
    './data/nonconform.yml',
    './data/checkstatus.yml'
) 