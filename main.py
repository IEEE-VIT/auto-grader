from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict

# from autograder.spelling_corrector import fix_spellings
# from autograder.text_similarity import check_similarity, get_marks

characters, coordinates = box_extraction("./samples/form_scanned_4.jpg", "./samples/output/")
print(coordinates)
pix = 0
for i in range(len(characters)):
    for j in range(len(characters[i])):
        if j != 0:
            pix = pix + 1
    if pix < 20:
        characters.drop(i)


x = predict(characters)

for i in range(len(x)):
    print(i + 1, x[i], sep=": ")

# query = fix_spellings("a blu4 sky")

# cos_scores = check_similarity(["sky is blue"], query)

# print(get_marks(cos_scores, 5, (0.45, 0.85)))
