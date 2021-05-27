import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [
     [
      r"Can i see the book list|what is the book list|How much books do you have|Booklist",
      ["The books i have are Dune, War of the worlds, Rendezvous with rama, Twenty thousand leagues under the sea,\
      The dispossessed, Blade runner, Foundation, Jurassic park, Starship troopers, The martian chronicles,\
      A hitchhiker's guide to the galaxy, The handmaid's tale, Snow crash, The time machine, Frankenstein,\
      Lost world jurassic park ,Ready player one ,Fahrenheit ,Nineteen eighty four ,Rama ,2001 Space odyssey,\
      Hell house, The haunting of hill house, It,The exorcist ,Ghost house, The shining ,Dracula,\
      House of leaves ,Pet sematary ,Carrie ,At the mountains of madness ,I am legend ,Something wicked this way comes,\
      The road ,The power ,A clockwork orange ,Divergent,The stand,The children of men ,Never let me go,The windup girl,\
      Iron heel , Animal farm, ninety eighteen four, Brand new world. If you would like to see any specif books just type: Can i see [insert_book_name_here]."]
    ],

    [ 
      r"What are the genre you have|What types of genres do you have|What genres do you have|Genres",
      ["The genres that i have stored are science fiction,horror, dystopian, mystery, guide", "I have science fiction, horror, dystopian,mystery, guide. What category would you like?"]
    ],
    [
      r"Can i see all of the science fiction books|What are the science fiction books you have|What science fiction books do you have|Science fiction book",
      ["The science fiction books i have are: Dune, War of the worlds, Rendezvous with rama, Twenty thousand leagues under the sea,\
        The dispossessed, Blade runner, Foundation, Jurassic park, Starship troopers, The martian chronicles ,A hitchhiker's guide to the galaxy,\
        The handmaid's Tale,Snow crash, The time machine, Frankenstein, Lost world jurassic park, Ready player one, Fahrenheit, Nineteen eighty four, Rama, 2001 Space odyssey."]
    ],
    [
      r"Can i see all the horror books|What are the horror books you have|What horror books do you have|Horror book",
      ["The horror books i have are: The hell house, The haunting of hill house, It, The exorcist,ghost house, frankenstein,the shining, Dracula,\
        House of leaves, Pet sematary, Carrie, St the mountains of madness, I am legend, Something wicked this way comes."]
    ],
    [   
      r"Can i see all the dystopian books|What are the dystopian books you have|What dystopian books do you have|Dystopian book",
      ["The dystopian books i have are: The road, The power, A clockwork orange, Divergent, The stand, The children of men, Never let me go, The windup girl, Iron heel, Animal farm, Time machine, Ninety eighteen four, Brand new world, The handmaid's tale"]
    ],
    [
      r"help",
      ["I am now giving you a sequence of keybinds to use/For"]
    ],
    [
      r"Dune",
      [""]
    ],
     [
      r"The War of the Worlds",
      [""]
    ],
     [
      r"Rendezvous with Rama",
      [""]
    ],
     [
      r"Twenty Thousand Leagues Under the Seas",
      [""]
    ],
     [
      r"The Dispossessed",
      [""]
    ],
     [
      r"Blade Runner",
      [""]
    ],
     [
      r"Foundation (Asimov novel)",
      [""]
    ],
     [
      r"Jurassic Park",
      [""]
    ],
     [
      r"Starship Troopers",
      [""]
    ],
     [
      r"The Martian Chronicles",
      [""]
    ],
     [
      r"The Hitchhiker's Guide to the Galaxy",
      [""]
    ],
     [
      r"The Handmaid's Tale",
      [""]
    ],
     [
      r"Snow Crash",
      [""]
    ],  
    [
      r"The Time Machine",
      [""]
    ], 
    [
      r"Frankenstein",
      [""]
    ], 
    [
      r"The Lost World ",
      [""]
    ], 
    [
      r"Ready Player One",
      [""]
    ], 
    [
      r"Fahrenheit 451",
      [""]
    ], 
    [
      r"Nineteen Eighty-Four",
      [""]
    ], 
    [
      r"Rendezvous with Rama",
      [""]
    ], 
     [
      r"2001: A Space Odyssey ",
      [""]
    ], 
     [
      r"Hell House",
      [""]
    ], 
     [
      r"The Haunting of Hill House",
      [""]
    ], 
     [
      r"It",
      [""]
    ], 
     [
      r"The Exorcist",
      [""]
    ], 
     [
      r"Ghost House",
      [""]
    ], 
     [
      r"The Shining",
      [""]
    ], 
     [
      r"Dracula",
      [""]
    ], 
     [
      r"House of Leaves",
      [""]
    ], 
     [
      r"Pet Sematary",
      [""]
    ], 
     [
      r"Carrie",
      [""]
    ], 
     [
      r"At the Mountains of Madness",
      [""]
    ], 
    [
      r"Something Wicked This Way Comes",
      [""]
    ], 
    [
      r"The Road",
      [""]
    ], 
    [
      r"The Power",
      [""]
    ], 
    [
      r"A Clockwork Orange ",
      [""]
    ], 
    [
      r"Divergent",
      [""]
    ], 
    [
      r"The Stand",
      [""]
    ], 
    [
      r"Children of Men",
      [""]
    ], 
    [
      r"Never Let Me Go",
      [""]
    ], 
    [
      r"The Windup Girl",
      [""]
    ], 
    [
      r"The Iron Heel",
      [""]
    ], 
    [
      r"Animal Farm",
      [""]
    ], 
    [
      r"Nineteen Eighty-Four",
      [""]
    ], 
    [
      r"Brave New World",
      [""]
    ], 
]

#This fuction claers the terminal of some information keeeping it rudimentary and simple
def clear_screen():
  import os
  os.system("cls")

#
def chatbot():
  chat = Chat(set_pairs, reflections) 
  chat.converse()

#This fuction simpley displays a text welcoming the user and explains the basics of the code.
def display_welcome_message():
  print('###################################')
  print("# Welcome to the Library chatbot #")
  print('###################################')
  print('To start please enter the required statement eg: Booklist/Genres if you need any help then just type the word help, to exit type down Exit. ')



if __name__ == "__main__":
  clear_screen()
  display_welcome_message()
  chatbot()
