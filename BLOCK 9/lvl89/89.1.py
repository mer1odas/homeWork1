file = open("txt.txt", "r+")
file_sod = file.read()
q = set()
for i in file_sod:
    q.add(i)
# q1 = []
# q2 = []
# # for i in q:
# #     kolichestvo = file_sod.count(i)
# #     if len(q1) < 1:    
# #         q1.append(kolichestvo)
# #         q2.append(i)
# #     else:
# #         q1.append(kolichestvo)
# #         q2.append(i)
# #         if q1[0] > kolichestvo:
# #             q1.remove(q1[1])
# #             q2.remove(q2[1])
# #         else:
# #             q1.remove(q1[0])
# #             q2.remove(q2[0])
q1 = []
for i in q:
    q1.append(file_sod.count(i))
index = q1.index(max(q1))
q2 = list(q)
print(q2[index])