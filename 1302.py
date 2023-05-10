# 1302 베스트셀러
books = dict()
for _ in range(int(input())):
    book = input()
    if book not in books:
        books[book] = 0
    else:
        books[book] += 1
bstsllr = max(books.values())
tmp = []
for book in books:
    if bstsllr == books[book]:
        tmp.append(book)
tmp.sort()
print(tmp[0])