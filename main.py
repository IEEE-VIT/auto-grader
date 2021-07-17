from autograder.box_extractor import box_extraction
from autograder.character_predictor import predict
# from autograder.spelling_corrector import fix_spellings
# from autograder.text_similarity import check_similarity, get_marks

characters = box_extraction("./samples/form_scanned_4.jpg", "./samples/output/")

x = predict(characters)

for i in range(len(x)):
    print(i+1, x[i], sep=": ")

# query = fix_spellings("a blu4 sky")

# cos_scores = check_similarity(["sky is blue"], query)

# print(get_marks(cos_scores, 5, (0.45, 0.85)))
