from random import randrange
from sys    import argv, stdin, stdout

def choose(n, ls):
    """Return a list of n random elements from ls"""
    if len(ls) <= n:
        return ls
    return [ls.pop(randrange(len(ls))) for i in range(n)]

def log_to_file(path, sentences):
    """Log results to file"""
    with open(path, 'w') as log_file:
        for hedge in sorted(sentences.keys()):
            log_file.write('%d\t%s\n' % 
                    (len(sentences[hedge]), hedge.replace('\"', '')))
        log_file.write('-' * 30 + '\n')
        log_file.write('Total matches:\t%d\n' % 
                sum(map(lambda s: len(s), sentences.values())))
        log_file.write('Hedges found:\t%d\n' % len(sentences))

def parse_token(token):
    index = token.index(',')
    return token[:index], token[index + 1:]

def hedge_sentences():
    sentences = {}
    for token in stdin:
        token = token.strip()
        hedge, sentence = parse_token(token)
        if hedge in sentences:
            sentences[hedge].append(sentence)
        else:
            sentences[hedge] = [sentence]
    return sentences

def select_tokens(n, path):
    sentences = hedge_sentences()
    for hedge in sentences:
        for token in choose(n, sentences[hedge]):
            print '%s,%s' % (hedge, token)
    log_to_file(path, sentences)

if __name__ == '__main__' and len(argv) == 3:
    select_tokens(int(argv[1]), argv[2])
