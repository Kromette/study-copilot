from studycopilot.embeddings.models import embed
from sklearn.metrics.pairwise import cosine_similarity


a = embed(
    "La glycolyse produit de l'ATP"
)

b = embed(
    "La glycolyse permet de générer de l'énergie cellulaire"
)

c = embed(
    "Les protéines sont constituées d'acides aminés"
)


print(
    cosine_similarity(
        [a],
        [b]
    )[0][0]
)


print(
    cosine_similarity(
        [a],
        [c]
    )[0][0]
)