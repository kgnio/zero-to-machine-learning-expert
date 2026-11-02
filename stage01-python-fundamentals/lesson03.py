
scores = [85, 42, 76, 35, 95]

passing_score = 50

for score in scores:
    if score >= passing_score:
        print(f"{score}: PASS")
    else:
        print(f"{score}: FAIL")
