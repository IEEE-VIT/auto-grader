from src.box_extractor import box_extraction
from src.character_predictor import predict
from src.text_similarity import check_similarity, get_marks

box_extraction("./samples/form.jpg", "./samples/output/")

cos_scores = check_similarity(["sky is blue"], "a grey sky")

print(get_marks(cos_scores, 5, 0.7))
