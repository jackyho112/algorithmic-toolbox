# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    items = []
    filled_capacity = 0
    total_value = 0

    for index, weight in enumerate(weights):
        value = values[index]
        items.append({
            'value_per_weight': value / weight,
            'weight': weight,
            'total_value': value
        })

    items.sort(key=lambda x: x['value_per_weight'], reverse=True)

    for item in items:
        if (filled_capacity + item['weight'])  < capacity:
            total_value += item['total_value']
            filled_capacity += item['weight']
        else:
            return (total_value + (capacity - filled_capacity) * item['value_per_weight'])

    return total_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
