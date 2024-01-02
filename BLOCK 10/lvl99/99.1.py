text = "dfusg hhd 9h g fujh j goji0trj ihg ji hg hi ji0 ji0h trhj0  ij0h rj0h rij0 rji0 hr ij0 rj 0j j0reh0jej90 hej09 j09hejhj-9e j9- eh j-oehjk9- j hejoi-hjo-he je-j j- hj-o"
text1 = ""
q1 = 0
q = 69
for i in range(len(text) // 70):
    while not(text[q]) == " ":
        q -= 1
    text1 = text1 + text[q1 + 1 : q + 1] + "\n"
    q1 = q
    q += 70
text1 = text1 + text[q1 + 1 : len(text)]
print(text1)