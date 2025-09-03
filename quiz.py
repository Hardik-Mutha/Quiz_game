import random
 # shuffle options (careful, need to adjust answer index too)






quiz_questions = [
    {
        "question": "what is the capital of india?",
        "options": ["mumbai", "new delhi", "kolkata", "chennai"],
        "answer": 2
    },
    {
        "question": "who is known as the 'father of computer'?",
        "options": ["alan turing", "charles babbage", "thomas edison", "bill gates"],
        "answer": 2
    },
    {
        "question": "which planet is known as the 'red planet'?",
        "options": ["earth", "venus", "mars", "jupiter"],
        "answer": 3
    },
    {
        "question": "water boils at what temperature (at sea level)?",
        "options": ["50c", "100c", "150c", "200c"],
        "answer": 2
    },
    {
        "question": "what is 15 × 6?",
        "options": ["60", "75", "90", "120"],
        "answer": 3
    },
    {
        "question": "the square root of 144 is:",
        "options": ["10", "11", "12", "13"],
        "answer": 3
    },
    {
        "question": "what does 'http' stand for?",
        "options": [
            "hypertext transfer protocol",
            "hightext transfer program",
            "hypertext transmission process",
            "hyper transfer text protocol"
        ],
        "answer": 1
    },
    {
        "question": "which company developed the programming language 'python'?",
        "options": ["microsoft", "google", "cwi", "ibm"],
        "answer": 3
    },
    {
        "question": "who is the main character in the cartoon 'pokemon'?",
        "options": ["ash ketchum", "ben 10", "goku", "naruto"],
        "answer": 1
    },
    {
        "question": "which is the largest ocean in the world?",
        "options": ["atlantic ocean", "arctic ocean", "indian ocean", "pacific ocean"],
        "answer": 4
    }
]
random.shuffle(quiz_questions)  # shuffle questions

score = 0
for q_no, question in enumerate(quiz_questions, start=1):
    print(f"Q{q_no}: {question["question"]}")

    # Correct option text store karo
    correct_option = question["options"][question["answer"] - 1]

    # Options shuffle karo
    shuffled_options = question["options"][:]
    random.shuffle(shuffled_options)

    # Naya correct answer index nikalna
    new_answer_index = shuffled_options.index(correct_option) + 1

    for i, option in enumerate(shuffled_options, start=1):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your option no.: "))

    if user_answer == new_answer_index:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")
        print("Correct Answer is:", correct_option)

    print("Your Score:", score)
    print("-" * 30)

print("🎯 Your Total Score:", score)