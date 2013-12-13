require 'lda'
lda = Lda::Lda.new
corpus = Lda::Corpus.new('lda/data-file.dat')
lda.corpus = corpus
lda.em("random")

to_classify_file = File.readlines("positive-control_.txt")[0].split(',')
lda.load_vocabulary("positive-control_.txt")
lda.print_topics(20)