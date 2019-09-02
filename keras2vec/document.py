class Document:
    def __init__(self, doc_id, labels, text):
        self.doc_id = doc_id
        self.labels = labels
        self.text = text.split(' ')
        self.windows = None

    def gen_windows(self, window_size, pad_word=''):
        """Generate a sliding window, of size window_size, for the given document
        Args:
            window_size (int): the size of the window, must be an odd number!
            pad_word (string): the word to pad indexes beyond the document, defaults to ''
        """

        self.windows = []
        if window_size%2 != 1:
            raise ValueError("Parameter window_size must be an odd number.")

        win_half = (window_size - 1)//2
        num_words = len(self.text)

        for ix in range(num_words):
            curr_window = []
            for w_ix in range(ix - win_half, ix + win_half + 1):
                if w_ix < 0 or w_ix >= num_words:
                    curr_window.append(pad_word)
                else:
                    curr_window.append(self.text[w_ix])

            self.windows.append(curr_window)
