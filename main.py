from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict

# from autograder.spelling_corrector import fix_spellings
# from autograder.text_similarity import check_similarity, get_marks


def auto_grade(defined_answers, image_location, output_location):
    answers, coordinates = box_extraction(image_location, output_location)
    if len(answers) == 380:

        locations = []
        prev = 0
        print(
            answers.shape
        )  # 16 cells x 2 rows x 10 answers = 360 boxes x (28 x 28) pixels
        for n in range(10):  # all questions
            sentence = ""
            answer = answers[38 * n : 38 * (n + 1)]  # individual answer(2 rows)
            for i in range(38):  # boxes of a answer
                box = answer[i]
                sum_pix = 0
                for pixel in box:  #  pixel of the box
                    if pixel != 0:
                        sum_pix = sum_pix + 1
                # do nothing when char is detected in the box, counter i will increase. When and empty
                # box is detected after some character boxes, pix < 30
                if sum_pix < 30 or i == 37:
                    word_array = answer[prev:i].reshape(-1, 28, 28, 1)
                    if word_array.shape[0] > 1:
                        try:
                            pred = predict(word_array)
                            if i < 16:
                                sentence = sentence + "".join(pred) + " "
                            else:
                                sentence = "".join(pred) + " " + sentence
                        except:
                            print(word_array.shape)
                    prev = i + 1

            print(n + 1, sentence[::-1])

            # new_words = []
            # for answer in defined_answers[n]:
            #     words = answer.split()
            #     for word in words:
            #         new_words.append(word)

            # query = fix_spellings(sentence[::-1], new_words)

            # if query != "":
            #     print(query)
            #     cos_scores = check_similarity(defined_answers[n], query)
            #     print("Marks: ", "%.2f" % get_marks(cos_scores, 5, (0.45, 0.85)))
            # else:
            #     print("Marks: ", "0.00")


defined_answers = [
    ["Yajat Malhotra", "Yajat"],
    ["Anshul Agrawala", "Anshul"],
    ["Avyay Casheekar", "Avyay"],
    ["Hello world", "Hi world"],
    ["Hello world"],
    ["Hello world"],
    ["Hello world"],
    ["Hello world"],
    ["Hello world"],
    ["Hello world"],
]

auto_grade(defined_answers, "./samples/form_scanned_2.jpg", "./samples/output/")
