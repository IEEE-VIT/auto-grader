from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict
from autograder.spelling_corrector import fix_spellings
from autograder.text_similarity import check_similarity, get_marks


def auto_grade(defined_answers, image_location, output_location):
    characters_all, coordinates = box_extraction(image_location, output_location)
    if len(characters_all) == 380:

        # def csort(e):
        #     return 1000 * e[0] + e[1]

        # charactersAll = np.array([x for _, x in sorted(zip(coordinates, charactersAll))])
        # for c in coordinates:
        #     print(c)

        locations = []
        prev = 0
        print(characters_all.shape)
        for n in range(10):
            sentence = ""
            characters = characters_all[38 * n : 38 * (n + 1)]
            for i in range(len(characters)):  # boxes
                pix = 0
                for j in range(len(characters[i])):  # pixels
                    debug = characters[i][j]
                    if characters[i][j] != 0:
                        pix = pix + 1
                if pix < 30:
                    subarray = characters[prev:i].reshape(-1, 28, 28, 1)
                    if subarray.shape[0] > 1:
                        try:
                            pred = predict(subarray)
                            sentence += "".join(pred) + " "
                        except:
                            print(subarray.shape)
                    prev = i + 1

            print(n + 1, sentence[::-1])

            new_words = []
            for answer in defined_answers[n]:
                words = answer.split()
                for word in words:
                    new_words.append(word)

            query = fix_spellings(sentence[::-1], new_words)

            if query != "":
                print(query)
                cos_scores = check_similarity(defined_answers[n], query)
                print("Marks: ", "%.2f" % get_marks(cos_scores, 5, (0.45, 0.85)))
            else:
                print("Marks: ", "0.00")


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
