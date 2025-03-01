import time
import pygame 
from pydub import AudioSegment
class Block:
    def __init__(self, name, start, end, block_type, audio_file = None, duration = None):
            self.name = name
            self.start = start              # start time (ms)
            self.end = end                  # end time (ms)
            self.block_type = block_type    # type (sample block, empty block)
            if duration is not None:        # duration only applies to empty blocks
                 self.duration = duration
            else: self.duration = 0

            if block_type != "Empty":
                self.audio_sample_file = self.trim_audio_file(start, end, audio_file)
        
    def trim_audio_file(self, start, end, audio_file):
        audio = AudioSegment.from_file(audio_file)
        trimmed_audio = audio[start:end]
        output_file_path = ""
        trimmed_audio.export(output_file_path, format="mp3")

    def loop(self, num_loops):
        for i in range(0, num_loops):
           self.play()
        pass

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_sample_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

        pass
    
