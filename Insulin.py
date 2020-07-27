clean_text = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
removed_space = clean_text.replace(" ", "")
print("Total Word count: " + str(len(removed_space)))
print("=====")

lsinsulin_seq_clean = removed_space[0:24]
print("Word count - lsinsulin_seq_clean: " + str(len(lsinsulin_seq_clean)))
print("lsinsulin: " + lsinsulin_seq_clean)
print("=====")

binsulin_seq_clean = removed_space[24:54]
print("Word count - binsulin_seq_clean: " + str(len(binsulin_seq_clean)))
print("binsulin: " + binsulin_seq_clean)

print("=====")
cinsulin_seq_clean = removed_space[54:89]
print("Word count - cinsulin_seq_clean: " + str(len(cinsulin_seq_clean)))
print("cinsulin :" + cinsulin_seq_clean)

print("=====")
ainsulin_seq_clean = removed_space[89:110]
print("Word count - ainsulin_seq_clean: " + str(len(ainsulin_seq_clean)))
print("ainsulin: " + ainsulin_seq_clean)
