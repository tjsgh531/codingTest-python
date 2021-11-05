import collections
import itertools

def solution(orders, course):
    answer = []

    for set_num in course:
        all_course_combination = []
        for order in orders:
            all_course_combination += itertools.combinations(sorted(order),set_num);
        
        most_order = collections.Counter(all_course_combination).most_common();
        answer += [ "".join(list(value)) for value, num in most_order if num > 1 and num == most_order[0][1] ]

    return sorted(answer)       