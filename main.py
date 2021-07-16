from src.box_extractor import box_extraction
from src.character_predictor import predict
from src.spelling_corrector import fix_spellings
from src.text_similarity import check_similarity, get_marks

box_extraction("./samples/form.jpg", "./samples/output/")

query = fix_spellings("a blu4 sky")

cos_scores = check_similarity(["sky is blue"], query)

print(get_marks(cos_scores, 5, (0.45, 0.85)))
