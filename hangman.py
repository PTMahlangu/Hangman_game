import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    try:
        return input('Guess the missing letter: ')
    except EOFError:
        pass 


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    print(word)
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    guess_word =[]
    word_as_list = list(word.strip())
    alphebet =  word_as_list[random.randint(0, len(word_as_list)-1)]
    char_position = word_as_list.index(alphebet)

    for i in range(len(word_as_list)-1):
        guess_word.append('_')
    guess_word.insert(char_position,alphebet)
    word_ =''.join(guess_word)
    return  word_


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):

    if (char in original_word) and (char not in answer_word) or (original_word.count(char)>1):
        return True
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    answer_word = list(answer_word)
    if char in original_word.strip() :
        for i in range(len(original_word)):
            if char == original_word[i]:
                answer_word[i] = original_word[i]
    answer_word = ''.join(answer_word)
    return answer_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    number_guesses = 5 -number_guesses
    if number_guesses == 1:
        print('/----\n|\n|\n|\n|\n_______')
    elif number_guesses == 2:
        print('/----\n|   0\n|\n|\n|\n_______')
    elif number_guesses == 3:
        print('/----\n|   0\n|  /|\\\n|\n|\n_______')
    elif number_guesses == 4:
        print('/----\n|   0\n|  /|\\\n|   |\n|\n_______')
    elif number_guesses == 5:
        print('/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______')

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    number_guesses = 5
    print("Guess the word: "+answer)
    while number_guesses > 0 and (word !=answer):
        guess = get_user_input()
        if guess == 'exit' or guess == 'quit':
            print('Bye!')
            break
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_guesses =number_guesses-1
            do_wrong_answer(answer, number_guesses)
            if number_guesses == 0:
                print('Sorry, you are out of guesses. The word was: '+word)

                

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        words_file = ask_file_name()
        words = read_file(words_file)
    else:
        words = read_file(sys.argv[1])

    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)

