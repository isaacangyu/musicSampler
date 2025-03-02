from blocks import Block

# take in a string and return list of list of blocks (tracks)
def parse(user_input: str, block_map: dict) -> list[list[Block]]:
   
    lines = user_input.split('\n')
    print(lines)
    tracks = [[] for _ in range(len(lines))]
    for line_idx in range(0, len(lines)):
        line = lines[line_idx]
        words = line.strip().split(' ')
        for word in words:
            if word[:4] == "loop":  # Ex: loop(5, drums, strings, bass)
                loop_inside = word[5:-1]
                loop_elements = loop_inside.split(';')[1:]
                print(loop_inside)
                num_iterations = int(loop_inside[0])

                for j in range(num_iterations):
                    for elem in loop_elements:
                        tracks[line_idx].append(block_map[elem])
            elif word[:5] == "empty":
                tracks[line_idx].append(Block("Empty", -1, -1, "Empty", duration=int(word[6:-1])*1000))
            else:   
                tracks[line_idx].append(block_map[word])
    return tracks

def secToMs(sec):
    return sec*1000

b1 = Block(name= "drummer", start = secToMs(60.2), end = secToMs(61), block_type="Sample", audio_file="faded.mp3")
b2 = Block(name= "strings", start = secToMs(60.2), end = secToMs(61), block_type="Sample", audio_file="faded.mp3")
b3 = Block(name= "base", start = secToMs(60.2), end = secToMs(61), block_type="Sample", audio_file="faded.mp3")

print(parse("drummer strings base base loop(2;strings;base) \n empty(2) base", {"drummer":b1 , "strings": b2, "base":b3}))

                
            




'''def merge:'''
    