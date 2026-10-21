import pas2_text_concordance as api

index = api.concordance("Hello world. Hello again.")
print(index, api.contexts("Hello world. Hello again.", index["hello"], 5))
