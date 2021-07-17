from sentence_transformers import SentenceTransformer
import scipy

model = SentenceTransformer("bert-base-nli-mean-tokens")


def check_similarity(sentences, query):
    sentences_embeddings = model.encode(sentences)
    queries = [query]
    query_embeddings = model.encode(queries)

    number_top_matches = len(sentences)

    print("Semantic Search Results")

    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist(
            [query_embedding], sentences_embeddings, "cosine"
        )[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        print("\n\n======================\n\n")
        print("Query:", query)
        print(f"\nSimilar {number_top_matches} sentence(s) in corpus:")

        cos_scores = []

        for idx, distance in results[0:number_top_matches]:
            print(sentences[idx].strip(), "(Cosine Score: %.4f)" % (1 - distance))
            cos_scores.append(1 - distance)
        return cos_scores


def get_marks(cos_scores, max_marks, bias):
    max_cos_score = max(cos_scores)
    marks_obtained = max(
        [
            ((max_cos_score - bias[0]) / (1 - bias[0])) * max_marks
            if max_cos_score < bias[1]
            else max_marks,
            0,
        ]
    )
    print("Marks: ", "%.2f" % marks_obtained, "/", "%.2f" % max_marks)
    return marks_obtained
