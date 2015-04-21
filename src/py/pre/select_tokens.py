from random         import randrange
from sys            import argv, stdin, stdout

def choose(n, ls):
    """Return a list of n random elements from ls"""
    if len(ls) <= n:
        return ls
    return [ls.pop(randrange(len(ls))) for i in range(n)]

def read_token_stream():
    return [line.strip() for line in stdin]

def log_to_file(path, term_frequency):
    """Log results to file"""
    with open(path, 'w') as log_file:
        for term in term_frequency:
            log_file.write('%d\t%s\n' % (term_frequency[term], term))
        log_file.write('------------------------------\n')
        log_file.write('Total matches:\t%d\n' % sum(term_frequency.values()))
        log_file.write('Hedges found:\t%d\n' % len(term_frequency))

def hedge_freq(tokens):
    """Select n random tokens of each hedge"""
    freq = {}
    for token in tokens:
        hedge = token[:token.index(',')].replace('\"', '')
        if hedge in freq:
            freq[hedge] += 1
        else:
            freq[hedge] = 1
    return freq

def select_tokens(n, path):
    tokens = read_token_stream()
    for choice in choose(n, tokens):
        print choice
    log_to_file(path, hedge_freq(tokens))

if __name__ == '__main__' and len(argv) == 3:
    select_tokens(int(argv[1]), argv[2])
