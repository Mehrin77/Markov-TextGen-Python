# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name: Mehrin Khan
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""
[a] What was in the file you analyzed?   -->  Chess Mate
    + Feel free to include it (up to you).

[b] How many words did it have?  -->     __528________
    Use word_count.

[c] How many characters did it have?  -->       _2984_______

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->       {'i': 18,
 'like': 3,
 'poptarts': 3,
 'and': 19,
 '42': 1,
 'spam': 3,
 'will': 2,
 'get': 2,
 'for': 5,
 'the': 21,
 'holidays': 1,
 'chessmate': 1,
 'chess': 20,
 'is': 3,
 'more': 1,
 'than': 1,
 'simply': 1,
 'a': 15,
 'hobby': 1,
 'me': 13,
 'it': 5,
 'also': 1,
 'makes': 1,
 'feel': 1,
 'excited': 1,
 'nostalgic': 1,
 'that': 4,
 'means': 2,
 'lot': 1,
 'to': 10,
 'always': 2,
 'hold': 1,
 'special': 1,
 'place': 1,
 'in': 17,
 'my': 12,
 'heart': 1,
 'has': 2,
 'been': 4,
 'crucial': 1,
 'part': 1,
 'of': 10,
 'growth': 1,
 'both': 2,
 'professionally': 1,
 'personally': 1,
 'vaguely': 1,
 'remember': 1,
 'granny': 1,
 'dad': 1,
 'playing': 4,
 'when': 5,
 'was': 8,
 'just': 1,
 'one': 4,
 'half': 1,
 'years': 2,
 'old': 2,
 'ive': 2,
 'loved': 1,
 'with': 5,
 'pieces': 3,
 'even': 5,
 'young': 2,
 'child': 1,
 'but': 4,
 'never': 2,
 'very': 2,
 'good': 1,
 'at': 4,
 'since': 1,
 'four': 1,
 'father': 3,
 'first': 2,
 'taught': 3,
 'how': 6,
 'play': 2,
 'we': 5,
 'have': 3,
 'used': 1,
 'game': 7,
 'as': 5,
 'communication': 1,
 'between': 1,
 'daughter': 1,
 'so': 1,
 'interested': 2,
 'this': 1,
 'planning': 1,
 'thinking': 1,
 'lost': 2,
 'myself': 2,
 'got': 1,
 'older': 1,
 'passion': 1,
 'only': 2,
 'heightened': 1,
 'entire': 2,
 'family': 1,
 'enjoyed': 1,
 'children': 2,
 'are': 1,
 'fiercely': 1,
 'competitive': 1,
 'about': 1,
 'now': 1,
 'would': 2,
 'develop': 1,
 'creative': 1,
 'strategic': 1,
 'plans': 1,
 'discussed': 1,
 'them': 2,
 'another': 1,
 'give': 2,
 'up': 2,
 'anything': 1,
 'his': 2,
 '': 1,
 'not': 6,
 'strategies': 2,
 'unquestionably': 1,
 'assisted': 1,
 'enhancing': 1,
 'cognitive': 1,
 'capabilities': 1,
 'level': 1,
 'patience': 1,
 'life': 4,
 'stepping': 1,
 'stone': 1,
 'towards': 1,
 'becoming': 1,
 'person': 2,
 'am': 1,
 'today': 1,
 'people': 1,
 'bangladesh': 1,
 'consistently': 1,
 'reminded': 1,
 'women': 1,
 'do': 3,
 'because': 2,
 'all': 1,
 'countrys': 1,
 'grandmasters': 1,
 'men': 1,
 'girl': 2,
 'elementary': 1,
 'school': 2,
 'who': 2,
 'learned': 1,
 'early': 1,
 'on': 2,
 'defy': 1,
 'expectations': 1,
 'succeed': 1,
 'against': 1,
 'odds': 1,
 'male': 1,
 'classmates': 1,
 'laughed': 1,
 'they': 2,
 'were': 2,
 'competing': 2,
 'end': 1,
 'ones': 1,
 'went': 1,
 'middle': 1,
 'became': 1,
 'ever': 1,
 'female': 1,
 'champion': 1,
 'over': 2,
 'two': 1,
 'hundred': 1,
 'boys': 1,
 'breaking': 1,
 'gender': 1,
 'stereotype': 1,
 'made': 1,
 'realize': 1,
 'if': 1,
 'believe': 2,
 'something': 1,
 'then': 2,
 'no': 1,
 'society': 2,
 'or': 2,
 'can': 5,
 'stop': 1,
 'value': 2,
 'perseverance': 1,
 'from': 1,________
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  -->
    - ...relative to a generic distribution of "all text"
 
    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.
    chess came up 20 times, how 6 times and life 4 times. 

[f] Other thoughts/insights?!
So the text is about chess and 
    life or how chess is inccporated in life


"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """Takes a text string and converts it to a dictionary of word transitions."""
    words = text.split()
    d = {}
    prev_word = '$' # Previous word is initially set to the sentence-start $ sign
    
    for word in words:
        if not word[0].isalnum():  #checks the alphanumeric
            # Word starts with punctuation, so ignore it and start new sentence
            prev_word = '$'
            continue
        if prev_word not in d:
            d[prev_word] = [word] # First occurrence of previous word, create new list
        else:
            d[prev_word].append(word) # Add word to list of next words for previous word
        if word[-1] in '.?!':
            # Word ends in sentence-ending punctuation, so start new sentence
            prev_word = '$'
        else:
            prev_word = word # Update previous word to current word
    
    return d


#
# Function #2   (generateText)
#
import random
def generateText(d, N):
    """generateText(d, n) will accept a dictionary of word transitions 
    d (generated in your createDictionary function, above) and a positive integer, n. 
    Then, generateText should print a string of n words
    """
    nextWord = random.choice (d['$'])       #(list(d.values())[0]) #calls the list anmd the firdt word [0]
    print()  # start by printing a newline

    for i in range(N):
        if not nextWord[-1].isalnum() or i==0:  #checks if its alpha numeric 

        #first if statement check if last word is not in the alphabet or if i==0
            #call random statement on line 426
            nextWord= random.choice(d['$'])
        
        else:
            if nextWord not in d:
                nextWord= random.choice(d['$'])
            else: 
                nextWord = random.choice (d[nextWord])


            print(nextWord, end = ' ')  # Using end = ' ' stops it from going to the next line

    print()                  # Final print, newline
            # if word isnt in the list of dictionary words 
            #call random statement on line 426
            #else
                # random on specific word in dictionary
         # Next word -- will be replaced (alas)
#delete poptarts 
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
    

    print()                  # Final print, newline


#
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
#
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!

Chess-Mate

Chess is more than simply a hobby for me; it also makes me feel excited and 
nostalgic. That means a lot to me and will always hold a special place in my 
heart. Chess has been a crucial part of my growth both professionally and personally.
 I vaguely remember my granny and my dad playing chess when I was just one and 
 a half years old. I've always loved playing with chess pieces, even when I was 
 a young child, but I've never been very good at it. Since I was four years old, 
 when my father first taught me how to play chess, we have used the game as a 
 means of communication between father and daughter. And I was so interested in 
 this game of planning and thinking that I lost myself in it. As I got older, my 
 passion for the game of chess only heightened. 

Chess was the one game that my entire family enjoyed playing as children, 
and we are fiercely competitive about it now. We would develop creative and
 strategic plans, but we never discussed them with one another. My  father would
  give up anything for his children , but not his chess strategies. 
  Chess unquestionably assisted me in enhancing both my cognitive capabilities 
  and my level of patience. My entire life, the game of chess has been a stepping
   stone towards becoming the person I am today. People in Bangladesh have 
   consistently reminded me that women do not play chess because all of the 
   country's chess grandmasters have been men. Because I was the only girl in 
   elementary school who was interested in playing chess, I learned early on how
    to defy expectations and succeed against the odds. Even my male classmates
     laughed at me when they were competing with me, but in the end they were the
      ones who lost the game. When I went to middle school I became the first 
      ever female chess champion competing with over two hundred boys. Breaking
       the gender stereotype made me realize if I believe in something then no
        society or person can not stop me. 

Chess taught me to believe in myself and the  value of perseverance.
 As a young girl from a conservative society I faced many challenges and
  chess was one thing giving a sense of direction. I incorporated the strategies 
  of chess in real life. Like how in chess even at the deadend we still try to 
  find loopholes or do not get discouraged even after our king is checked several
   times. These taught me not to give up in life and look for alternatives.
    Then how every piece in chess adds a unique value to the game. Even a pawn
     can become a queen, and a knight can be the knight in shining armor as 
     can jump over the pieces. It is very interesting to me how such small
      observations can teach life skills.  The pieces in chess do not compete 
      with each other, rather focus on how to utilize them in their abilities at
       its best.
