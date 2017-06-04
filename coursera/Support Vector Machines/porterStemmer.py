@mfunction("stem")
def porterStemmer(inString=None):
    # Applies the Porter Stemming algorithm as presented in the following
    # paper:
    # Porter, 1980, An algorithm for suffix stripping, Program, Vol. 14,
    #   no. 3, pp 130-137

    # Original code modeled after the C version provided at:
    # http://www.tartarus.org/~martin/PorterStemmer/c.txt

    # The main part of the stemming algorithm starts here. b is an array of
    # characters, holding the word to be stemmed. The letters are in b[k0],
    # b[k0+1] ending at b[k]. In fact k0 = 1 in this demo program (since
    # matlab begins indexing by 1 instead of 0). k is readjusted downwards as
    # the stemming progresses. Zero termination is not in fact used in the
    # algorithm.

    # To call this function, use the string to be stemmed as the input
    # argument.  This function returns the stemmed word as a string.

    # Lower-case string
    inString = lower(inString)

    global j
    b = inString
    k = length(b)
    k0 = 1
    j = k



    # With this if statement, strings of length 1 or 2 don't go through the
    # stemming process. Remove this conditional to match the published
    # algorithm.
    stem = b
    if k > 2:
        # Output displays per step are commented out.
        #disp(sprintf('Word to stem: %s', b));
        x = step1ab(b, k, k0)
        #disp(sprintf('Steps 1A and B yield: %s', x{1}));
        x = step1c(x(1), x(2), k0)
        #disp(sprintf('Step 1C yields: %s', x{1}));
        x = step2(x(1), x(2), k0)
        #disp(sprintf('Step 2 yields: %s', x{1}));
        x = step3(x(1), x(2), k0)
        #disp(sprintf('Step 3 yields: %s', x{1}));
        x = step4(x(1), x(2), k0)
        #disp(sprintf('Step 4 yields: %s', x{1}));
        x = step5(x(1), x(2), k0)
        #disp(sprintf('Step 5 yields: %s', x{1}));
        stem = x(1)
        end

        # cons(j) is TRUE <=> b[j] is a consonant.
