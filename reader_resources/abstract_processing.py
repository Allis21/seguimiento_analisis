"""
 This module contains a class used to handle and process abstracts extracted from
 the bibtex articles
"""
import re
import time

from tabulate import tabulate
from reader_resources.algorithms_execution import AlgorithmsExecution
from collections import Counter

class AbstractProcessing:
    """
    Class for article abstract processing
    """

    def __init__(self):
        self.keywords = ["abstraction", "algorithm", "coding", "creativity",
                         "logic", "conditionals", "loops",
                         "motivation", "persistence", "block", "mobile",
                         "application", "programming", "robotic", "scratch"]
        self.keywords_appereances = []

    def count_keyword_frequencies(self, abstracts):
        """
        Count the frequency of keywords in the abstracts and print them in a table.
        """
        text = " ".join(abstracts).lower()
        frequencies = Counter()
        
        for keyword in self.keywords:
            frequencies[keyword] = len(re.findall(rf"\b{keyword}\b", text))
        
        self.keywords_appereances = sorted(
            list(frequencies.items()), key=lambda x: (-x[1], x[0])
        )

        # Imprimir tabla usando tabulate
        headers = ["Término", "Frecuencia"]
        print(tabulate(self.keywords_appereances, headers=headers, tablefmt="fancy_grid"))

        AlgorithmsExecution.execute_algorithms(
            abstracts[:3000], 'KEYWORDS'
        )
        


    @staticmethod
    def separate_white_spaces(abstract):
        """
        This method separates the words contained in the article abstract
        string into a string array
        """
        words = re.split(r'[,\s]+', abstract.strip())
        return words

    