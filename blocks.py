import pygame
import time

class Block:
    def __init__(self, name, start, end, block_type, audio_file = None, duration = None):
            self.name = name
            self.start = start              # start time
            self.end = end                  # end time
            self.block_type = block_type    # type (sample block, empty block)
            if duration is not None:        # duration only applies to empty blocks
                 self.duration = duration
            else: self.duration = 0
            self.audio_sample_file = audio_file

    def loop(self, num_loops):
        for i in range(0,num_loops):
           self.play()

            #TODO: logic to play the track
        pass

    def play(self):
        #TODO: logic to play the track

       
        pass
    
