# 백준 2630
# 색종이 만들기

def count_pieces(paper):
    # Base case : 종이가 한칸이다
    if len(paper) == 1:
        return [1, 0] if paper[0][0] == 0 else [0, 1]

    # 종이를 4등분
    n = len(paper)
    half = n // 2
    q1 = [row[:half] for row in paper[:half]]
    q2 = [row[half:] for row in paper[:half]]
    q3 = [row[:half] for row in paper[half:]]
    q4 = [row[half:] for row in paper[half:]]

    # 각 사분면의 종이를 재귀적으로 센다
    pieces = [0, 0]
    for q in [q1, q2, q3, q4]:
        q_pieces = count_pieces(q)
        pieces[0] += q_pieces[0]
        pieces[1] += q_pieces[1]

    # 결과를 합쳐서 리턴
    if pieces[0] == 0:
        return [0, 1]
    elif pieces[1] == 0:
        return [1, 0]
    else:
        return pieces

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = count_pieces(paper)
print(white)
print(blue)
