import blocks
from blocks import Block

def secToMs(sec):
    return sec*1000

'''
b1 = Block(name= "drummer", start = secToMs(60.2), end = secToMs(61), block_type="Sample", audio_file="faded.mp3")
b2 = Block(name= "drummer", start = secToMs(62), end = secToMs(63), block_type="Sample", audio_file="faded.mp3")
b1.play()
b2.play()
b1.play()
'''

b1 = Block(name= "drummer", start = secToMs(50), end = secToMs(51), block_type="Sample", audio_file="faded.mp3")
b2 = Block(name= "drummer2", start = secToMs(62), end = secToMs(63), block_type="Sample", audio_file="faded.mp3")
b1.play()
b2.play()
b1.play()
