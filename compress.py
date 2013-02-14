# compress.py
# taken from http://rosettacode.org/wiki/LZW_compression#Python

##fname = "flintstones.txt"

infile = open("montypython.txt", 'r')
outfile = open("results.txt", 'w')


def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
##    return result

    return(dictionary)

 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}
 
    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result
 


lines = infile.readlines()
count = 0
for line in lines:
    compressed = compress(line)
##    print(compressed)
    count += len(compressed)
    
print(count)



##        outfile.write(n)
    
# How to use:
##decompressed = decompress(compressed)

##
##with open (fname, 'a') as f:
##    for line in f:
##  
        

##        words = line.split()
##        num_lines += 1
##        num_words += len(words)
##        num_chars += len(line)

