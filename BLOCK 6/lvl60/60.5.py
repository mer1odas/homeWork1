a = "faiufah"
q = ["a", "o", "e", "i", "u", "y"]
slog = []
for i in a:
    if i in q:
        slog.append(a[0 : a.find(i) + 1])
        a = a[a.find(i) + 1 : len(a)]
        if len(a) < 2 and not(a[len(a) - 1] in q):
            slog[len(slog) - 1] = slog[len(slog) - 1] + a
        print(a)
print(slog)
