def get_average_grade(scores):
    grade_ranges = [
        (97, 100, "A+"),
        (93, 96, "A"),
        (90, 92, "A-"),
        (87, 89, "B+"),
        (83, 86, "B"),
        (80, 82, "B-"),
        (77, 79, "C+"),
        (73, 76, "C"),
        (70, 72, "C-"),
        (67, 69, "D+"),
        (63, 66, "D"),
        (60, 62, "D-"),
    ]
    sum_of_scores = sum(scores)
    avg = sum_of_scores // len(scores)
    for low,high,grade in grade_ranges:
        if avg >= low and avg <= high:
            return grade
    else:
        return 'F'