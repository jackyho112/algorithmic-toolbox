# Uses python3
import sys

def optimal_weight(W, w):
    results = [
        [0] * W
    ]
    w = sorted(w)

    for index in range(len(w)):
        row = []
        current_weight = w[index]
        for weight in range(1, W + 1):
            if weight >= current_weight:
                remaining_weight = weight - current_weight

                if remaining_weight > 0:
                    row.append(
                        max(
                            current_weight + results[index][remaining_weight - 1],
                            results[index][weight - 1]
                        )
                    )
                else:
                    row.append(current_weight)
            else:
                row.append(results[index][weight - 1])

        results.append(row)

    return results[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
