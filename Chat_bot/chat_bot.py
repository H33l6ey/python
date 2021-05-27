import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [
    [
      r"Can i see the book list|what is the book list|How much books do you have|Booklist|"
      ["The books i have are Dune, War of the worlds, Rendezvous with rama, Twenty thousand leagues under the sea,\
      The dispossessed, Blade runner, Foundation, Jurassic park, Starship troopers, The martian chronicles,\
      A hitchhiker's guide to the galaxy, The handmaid's tale, Snow crash, The time machine, Frankenstein,\
      Lost world jurassic park ,Ready player one ,Fahrenheit ,Nineteen eighty four ,Rama ,2001 Space odyssey,\
      Hell house, The haunting of hill house, It,The exorcist ,Ghost house ,Frankenstein ,The shining ,Dracula,\
      House of leaves ,Pet sematary ,Carrie ,At the mountains of madness ,I am legend ,Something wicked this way comes,\
      The road ,The power ,A clockwork orange ,Divergent,The stand,The children of men ,Never let me go,The windup girl,\
      Iron heel , Animal farm , Time machine,ninety eighteen four, Brand new world, The handmaid's taleLater,, Nz frenzy, Across asia on the cheap,\
      London and its environs, Atlas obscura: an explorer's guide to the world's hidden wonders. If you would like to see any specif books just type: Can i see [insert_book_name_here]."]
    ],
    [ 
      r"what are the genre you have|What types of genres do you have|What genres do you have|"
      ["The genres that i have stored are science fiction,horror, dystopian, mystery, guide", "I have science fiction, horror, dystopian,mystery, guide. What category would you like?"]
    ],
    [
      r"can i see all of the science fiction books|what are the science fiction books you have|what science fiction books do you have|"
      ["The science fiction books i have are: Dune, War of the worlds, Rendezvous with rama, Twenty thousand leagues under the sea,\
        The dispossessed, Blade runner, Foundation, Jurassic park, Starship troopers, The martian chronicles ,A hitchhiker's guide to the galaxy,\
        The handmaid's Tale,Snow crash, The time machine, Frankenstein, Lost world jurassic park, Ready player one, Fahrenheit, Nineteen eighty four, Rama, 2001 Space odyssey."]
    ],
    [
      r"can i see all the horror books|what are the horror books you have|what horror books do you have|"
      ["The horror books i have are: The hell house, The haunting of hill house, It, The exorcist,ghost house, frankenstein,the shining, Dracula,\
        House of leaves, Pet sematary, Carrie, St the mountains of madness, I am legend, Something wicked this way comes."]
    ],
    [   
      r"can i see all the dystopian books|what are the dystopian books you have|what dystopian books do you have|"
      ["The dystopian books i have are: The road, The power, A clockwork orange, Divergent, The stand, The children of men, Never let me go, The windup girl, Iron heel, Animal farm, Time machine, Ninety eighteen four, Brand new world, The handmaid's tale"]
    ],
    [
      r"can i see the guide books|what are the guide books you have|what guide books do you have|"
      ["The guide books i have are: Nz frenzy, Across asia on the cheap, London and its environs,Atlas obscura: an explorer's guide to the world's hidden wonders", "I have a few guide books here: Nz frenzy, Across asia on the cheap, London and its environs,Atlas obscura: an explorer's guide to the world's hidden wonders"]
    ],
    [
      r"help"
      ["I am now giving you a sequence of keybinds to use/For"]
    ],
    [
      r"",
      [""]
    ],
    [
      r"",
      [""]
    ],
    [
      r"",
      [""]
    ],
    [
      r"",
      [""]
    ],
    [
      r"",
      [""]
    ],
    [
      r"",
      [""]
    ],
]



def chatbot():
    chat = Chat(set_pairs, reflections) 
    chat.converse()

if __name__ == "__main__":
    chatbot()
