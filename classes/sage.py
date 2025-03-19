import os
from helper_funcs.remove_dupes import remove_dupes


class Sage:

    def __init__(self,
                 start_time=0,
                 burst_filepath=os.path.join('sounds', 'common', 'burst.wav'),
                 phlegma_filepath=os.path.join('sounds', 'sage', 'phlegma.wav'),
                 psyche_filepath=os.path.join('sounds', 'sage', 'psyche.wav')):

        self.start_time = start_time
        self.burst_filepath = burst_filepath
        self.psyche_filepath = psyche_filepath
        self.phlegma_filepath = phlegma_filepath
        self.times_list = self.get_times(self.start_time)

    def get_times(self, starttime):
        burst = [(starttime + 7.5) + (x * 120) for x in range(0, 15)]
        psyche = [(starttime + 7.5) + (x * 60) for x in range(0, 30)]
        phlegma = [x - 40 for x in burst]
        del phlegma[0]

        burst = [(self.burst_filepath, x) for x in burst]
        psyche = remove_dupes(burst, [(self.psyche_filepath, x) for x in psyche])
        phlegma = remove_dupes(burst, [(self.phlegma_filepath, x) for x in phlegma])

        everything = burst + psyche + phlegma
        everything.sort(key=lambda tup: tup[1])
        return everything





