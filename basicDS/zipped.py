details = input().split()
num_subjects = int(details.pop())
num_students = int(details.pop())
zipped = []

for _ in range(num_subjects):
    scores = input().split()
    scores = [float(i) for i in scores]
    zipped += list(zip(range(num_students), scores))

scores = [0] * len(scores)
for (student_index, score) in zipped:
    scores[student_index] += score

for score in scores:
    print(score/num_subjects)
    