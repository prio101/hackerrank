def solution(A, B, P):
    found_indices = []
    for str in B:
        if(str.find(P)):
            found_indices.append(str.find(P))
    
    print(found_indices)


if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    C = input().strip()

    solution(A, B, C)
    print(solution)