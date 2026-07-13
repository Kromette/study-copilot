from studycopilot.retrieval.search import search
import time


start=time.time()

results = search(
    "What are the functions of amino acids?"
)


for result in results:

    print("----------------")
    print(
        f"Citation: {result.citation}"
    )
    print(
        f"Score: {result.score}"
    )

    print(
        f"Page: {result.page}"
    )

    print(
        result.text[:300]
    )

duration=time.time()-start

print(
f"Retrieval latency: {duration:.3f}s"
)