import numpy as np
from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict

# from autograder.spelling_corrector import fix_spellings
# from autograder.text_similarity import check_similarity, get_marks

charactersAll, coordinates = box_extraction(
    "./samples/form_scanned_2.jpg", "./samples/output/"
)

# print(coordinates)

print(len(charactersAll))

if len(charactersAll) == 380:

    # def csort(e):
    #     return 1000 * e[0] + e[1]

    # charactersAll = np.array([x for _, x in sorted(zip(coordinates, charactersAll))])
    # for c in coordinates:
    #     print(c)

    locations = []
    prev = 0
    print(charactersAll.shape)
    for n in range(10):
        sentence = ""
        characters = charactersAll[38 * n : 38 * (n + 1)]
        for i in range(len(characters)):  # boxes
            pix = 0
            for j in range(len(characters[i])):  # pixels
                debug = characters[i][j]
                if characters[i][j] != 0:
                    pix = pix + 1
            if pix < 30:
                subarray = characters[prev:i].reshape(-1, 28, 28, 1)
                if subarray.shape[0] > 1:
                    # print(subarray.shapes)
                    try:
                        pred = predict(subarray)
                        sentence += "".join(pred) + " "
                    except:
                        print(subarray.shape)
                prev = i + 1

        print(n+1, sentence[::-1])

        # query = fix_spellings(sentence)

        # cos_scores = check_similarity(["sky is blue"], query)

        # print(get_marks(cos_scores, 5, (0.45, 0.85)))

        # [Y],[A],[J],[ ],[ ],[ ],[ ],[ ],[ ],[A],[T]
        # YAJ AT
