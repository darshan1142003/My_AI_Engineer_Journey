import numpy as np
marks=np.array([[15,12,16],
                [12,16,18],
                [18,18,19],
                [20,17,16],
                [15,12,11]])

total=marks.sum(axis=1)
average=marks.mean(axis=1)
topper= np.argmax(total)

for i in range(5):
    print("Student", i + 1, "Total:", total[i])
    print("Student", i + 1, "Average:", average[i])
    print()

print("Topper: Student", topper + 1)

