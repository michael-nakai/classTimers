import os
from helper_funcs.remove_dupes import remove_dupes


class WhiteMage:

    def __init__(self,
                 start_time=0,
                 burst_filepath=os.path.join('sounds', 'common', 'burst.wav'),
                 blood_filepath=os.path.join('sounds', 'white_mage', 'blood.wav')):

        self.start_time = start_time
        self.burst_filepath = burst_filepath
        self.blood_filepath = blood_filepath
        self.times_list = self.get_times(self.start_time)

    def get_times(self, starttime):
        burst = [(starttime + 7.5) + (x * 120) for x in range(0, 15)]
        blood = [(starttime + 7.5) + (x * 60) for x in range(0, 30)]

        burst = [(self.burst_filepath, x) for x in burst]
        blood = remove_dupes(burst, [(self.blood_filepath, x) for x in blood])

        everything = burst + blood
        everything.sort(key=lambda tup: tup[1])
        return everything





