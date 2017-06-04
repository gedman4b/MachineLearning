# GETVOCABLIST reads the fixed vocabulary list in vocab.txt and returns a
# cell array of the words
#   vocabList = GETVOCABLIST() reads the fixed vocabulary list in vocab.txt 
#   and returns a cell array of the words in vocabList.


#% Read the fixed vocabulary list
fid = fopen(mstring('vocab.txt'))

# Store all dictionary words in cell array vocab{}
n = 1899# Total number of words in the dictionary

# For ease of implementation, we use a struct to map the strings => integers
# In practice, you'll want to use some form of hashmap
vocabList = cell(n, 1)
for i in mslice[1:n]:
    # Word Index (can ignore since it will be = i)
    fscanf(fid, mstring('%d'), 1)
    # Actual Word
    vocabList(i).lvalue = fscanf(fid, mstring('%s'), 1)
    end
    fclose(fid)

end
