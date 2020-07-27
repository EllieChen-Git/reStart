clean_text = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"

removed_space = clean_text.replace(" ", "")
# Use .replace() method to remove spaces in 'clean_text': https://www.w3schools.com/python/ref_string_replace.asp
print("Total Word count: " + str(len(removed_space)))
# Use .len() function to return the length of 'removed_space': https://www.w3schools.com/python/ref_func_len.asp
# Use .str() function to convert numbers to strings: https://www.w3schools.com/python/ref_func_str.asp
print("=====")
# Just a seperater to make the output looks nicer

lsinsulin_seq_clean = removed_space[0:24]
# Split string into sub-strings [beginningIndex:endingIndex] (where 'beginningIndex' is included but 'endingIndex' is not included): https://www.w3schools.com/python/gloss_python_string_slice.asp
# Note: Programming languages count from 0. 
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