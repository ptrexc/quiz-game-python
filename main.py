def new_game():
    answer_list = []
    answer_increment = 0
    score = 0
    for i in question:
        print(i)
        for j in answer[answer_increment]:
            print(j)
        answer_increment += 1
        answer_input = input("Your Answer ? (A, B, C, D) ").upper()
        answer_list.append(answer_input)
        score += check_answer(question.get(i), answer_input)
        display_answer(answer_list)
    print(f"Your score is {score*25}%")
    print()
    play_again_prompt = input("Want to play again? (Y/N)").upper()
    print()
    play_again(play_again_prompt)


def check_answer(question_inp, answer_inp):
    if answer_inp == question_inp:
        return 1
    else:
        return 0


def display_answer(answer_show):
    print(f"Answer", end=" ")
    for i in question:
        print(question.get(i), end=" ")
    print()
    print(f"Your Answer", end=" ")
    for j in answer_show:
        print(j, end=" ")
    print()


def play_again(play_again_prompt):
    if play_again_prompt == "Y":
        new_game()
    else:
        print("Thanks for playing")
        print("Byeee!!!")


question = {
    "Who is the most perfect waifu? ": "A",
    "What is shape of earth?": "C",
    "Which anime who have pirate theme?": "D",
    "The most beautiful country? ": "D"
}

answer = [
    ["A. Yukino", "B. Nino", "C. Robin", "D. Shinobu"],
    ["A. Plane", "B. Triangle", "C. Rounded", "D. Rectangle"],
    ["A. Oregairu", "B. Demon Slayer", "C. Gotoubun no hanayome", "D. One Piece"],
    ["A. Switzerland", "B. Finland", "C. United Kingdom", "D All of them"]
]

if __name__ == '__main__':
    new_game()
