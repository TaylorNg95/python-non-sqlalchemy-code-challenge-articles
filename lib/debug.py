#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    charles_dickens = Author('Charles Dickens')
    mary_baker_eddy = Author('Mark Baker Eddy')
    mark_twain = Author('Mark Twain')

    sports_illustrated = Magazine('Sports Ill', 'Sports')
    economist = Magazine('Economist', 'Business')
    ny_times = Magazine('NY Times', 'Business')

    moby_dick_article = Article(charles_dickens, economist, 'The Great Moby Dick')
    christian_science_article = Article(mary_baker_eddy, sports_illustrated, 'The Sport of Christian Science')
    buddha_article = Article(mary_baker_eddy, economist, 'The Business of Buddha')
    hindu_article = Article(mary_baker_eddy, economist, 'The Business of Hindu')
    devout_article = Article(mary_baker_eddy, economist, 'The Business of Being Devout')

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
