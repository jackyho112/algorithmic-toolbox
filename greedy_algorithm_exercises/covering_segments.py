# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda x: x[1])
    points = [segments[0][1]]
    reached = 0
    current_segment = segments[0]

    while reached != len(segments):
        current_segment = segments[reached]
        if current_segment[0] <= points[-1] and points[-1] <= current_segment[1]:
            reached += 1
        else:
            points.append(current_segment[1])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
