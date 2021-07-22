from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict

# from autograder.spelling_corrector import fix_spellings
# from autograder.text_similarity import check_similarity, get_marks

characters, coordinates = box_extraction(
    "./samples/form_scanned_4.jpg", "./samples/output/"
)

if len(characters) == 380:

    # def csort(e):
    #     return 1000 * e[0] + e[1]

    # coordinates.sort(key=csort)
    # for c in coordinates:
    #     print(c)

    prev = 0
    sentence = ""
    for i in range(len(characters)):  # boxes
        pix = 0
        for j in range(len(characters[i])):  # pixels
            debug = characters[i][j]
            if characters[i][j] != 0:
                pix = pix + 1
        if pix < 200:
            print("A  ", len(characters[prev:i]))
            if len(characters[prev:i]) != 0:
                sentence += "".join(predict(characters[prev:i])) + " "
                # print(predict(characters[prev:i]))
            prev = i

    print(sentence)

    # x = predict(characters)

    # for i in range(len(x)):
    #     print(i + 1, x[i], sep=": ")

    # query = fix_spellings("a blu4 sky")

    # cos_scores = check_similarity(["sky is blue"], query)

    # print(get_marks(cos_scores, 5, (0.45, 0.85)))

    # [Y],[A],[J],[ ],[ ],[ ],[ ],[ ],[ ],[A],[T]
    # YAJ AT
