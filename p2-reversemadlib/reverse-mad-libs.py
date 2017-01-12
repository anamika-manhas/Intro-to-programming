# String and its Answers to be filled in beginner level
beginner_answer = ["python" , "udacity" , "programming" , "2", "fun"]
stringBeginner = "\nHello Gamer!!! My name is Anamika Manhas. This game uses  __1__ \
 programming language which I have learned from www. __2__ .com. I am pursuing intro to __3__\
 nanodegree. This is my stage __4__ submission. I hope you will have __5__ ."

# String and its Answers to be filled in intermediate level
intermediate_answer = ["west" , "jack" , "rowling" , "deathly", "albus"]
stringIntermediate = "Harry Potter and the Cursed Child is a two-part __1__ End stage play \
 written by __2__ Thorne based on an original new story by Thorne, J.K. __3__  and John Tiffany.\
 The story is set nineteen years after the events of Harry Potter and the __4__ Hallows and \
 follows Harry Potter, now a Ministry of Magic employee, and his younger son __5__ Severus Potter."

# String and its Answers to be filled in proficient level
proficient_answer = ["google" , "online" , "sundar" , "sergey"]
stringProficient = "__1__ is an American multinational technology company specializing in Internet-related \
 services and products that include __2__ advertising technologies, search, cloud computing, and software.\
 The CEO of this company is __3__ pichai.The founders of this company are Larry Page and __4__ Brin."

# String and its Answers to be filled in experienced level
experienced_answer = ["jammu" , "kashmir" , " tawi" , "municipal"]
stringExperienced = "__1__ is the largest city in the Jammu Division and the winter capital of state of Jammu \
and __2__ . It is situated on the banks of the __3__ River. It is administered by a __4__ corporation."

# String and its Answers to be filled in expert level
expert_answer = ["computer" , "data" , "cable" , "wireless" ]
stringExpert = "A __1__ network or data network is a telecommunications network which allows computers to exchange\
 data. In computer networks, networked computing devices exchange __2__ with each other using a data link. The \
 connections between nodes are established using either __3__ media or __4__ media."


def run(answer , quiz_string):
        '''
        This is the main function which executes the level.
        It takes the question as string argument and its answers as list type
        argument. This function executes til the player has completed his
        level.
        '''
        i = 0
        while(i < len(answer)):

                blank = raw_input("What should go in blank " + str(i + 1) + " ? ")

                '''
                the conditions check if the word typed by the user is in the answer
                list .
                '''
                if(word_in_pos(blank , answer) != None and i == answer.index(blank)):

                        # the following replaces the blank with the correct answer filled
                        quiz_string = quiz_string.split()
            # j is used to store index from where the blank starts
                        j = quiz_string.index("__" + str(i + 1) + "__")
                        word = quiz_string[j]
                        word = word.replace("__" + str(i + 1) + "__" , blank)
                        quiz_string[j] = word

                        # it now iterates to next blank
                        i += 1
                        print "\nThat's Correct!\n"
                        quiz_string = " ".join(quiz_string)
                        print quiz_string + "\n"

                else:
                        print("\nSorry! Wrong Answer. Please try again")

        print "Congratulations you cleared the level !!\n"
        return


def word_in_pos(word, answers):

        '''
        It checks if a word filled by the player is present in the answer
        list or not. It returns the word itself.
        '''

        for pos in answers:
                if pos == word:
                        return pos
        return None


def main():

        '''
        It is the main block or function of the game.
        '''

        play = "yes"


        while(play == "yes"):
                string_multiplier = 23
                print "\n" + " " * string_multiplier + "Welcome to Reverse Mad-libs !!"
                print "\nPress \n 1 for beginner \n 2 for intermediate \n 3 for \
proficient\n 4 for experienced \n 5 for expert"

                level = raw_input("\nEnter your Choice : ")

                level_Selector(level)

                play = raw_input("Do You want to play again ? (yes/no) ")
                if(play == "no"):
                        print "ThankYou for playing :)"


'''
    This function selects the level as per the user choice
'''

def level_Selector(level):
    # this will return the beginner level
    if(level == '1'):
        print stringBeginner + "\n"
        run(beginner_answer, stringBeginner)

    # this will return the intermediate level
    elif(level == '2'):
        print stringIntermediate + "\n"
        run(intermediate_answer, stringIntermediate)

    # this will return the proficient level
    elif(level == "3"):
        print stringProficient + "\n"
        run(proficient_answer, stringProficient)

    # this will return the experienced level
    elif(level == "4"):
        print stringExperienced + "\n"
        run(experienced_answer, stringExperienced)

    # this will return the expert level
    elif(level == "5"):
        print stringExpert + "\n"
        run(expert_answer, stringExpert)

    else:
        level = raw_input("\nSorry Wrong choice! Please type in your Expertise Level : ")
        level_Selector(level)

# to initialize the main function

if __name__ == "__main__":
        main()
