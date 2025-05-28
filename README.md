# Music Sampler

A Flask-based web application for creating, managing, and sequencing audio samples. Upload audio files, create sample blocks, and compose music using a simple text-based notation system.

## Features

- **Audio Upload**: Upload MP3 files to use as source material
- **Block Creation**: Create audio blocks by specifying start/end times from uploaded files
- **Empty Blocks**: Create silent blocks for spacing and timing
- **Text-Based Composition**: Write music sequences using simple text notation
- **Real-time Playback**: Play individual blocks or complete compositions
- **Loop Support**: Create repeating patterns with loop notation
- **Multi-track Mixing**: Layer multiple tracks simultaneously

## Installation

### Prerequisites

- Python 3.7+
- Flask
- pygame
- pydub
- werkzeug

### Setup

1. Clone or download the project files
2. Install required dependencies:
```bash
pip install flask pygame pydub werkzeug
```
3. Run the application:
```bash
python app.py
```
4. Open your browser and navigate to `http://localhost:5000/upload`

## Usage

### 1. Upload Audio Files

1. Go to the `/upload` page
2. Select an MP3 file and click "Upload"
3. Your file will be stored in the `uploads/` directory

### 2. Create Blocks

Create audio blocks by filling out the block creation form:

- **Block Name**: Unique identifier for your block
- **Start Time**: Start time in seconds
- **End Time**: End time in seconds  
- **Block Type**: Choose "Sample" for audio or "Empty" for silence
- **Audio File**: Select from uploaded files (required for Sample blocks)
- **Duration**: Duration for Empty blocks (in seconds)

### 3. Compose Music

Use the text area to write your composition using block names:

#### Basic Syntax
```
block1 block2 block3
```

#### Multi-track (each line is a separate track)
```
drums bass drums bass
strings strings lead strings
```

#### Loop Notation
```
loop(4,drums,bass)
```
This plays "drums" and "bass" 4 times in sequence.

#### Empty Blocks
```
empty(2)
```
Creates a 2-second silence.

#### Example Composition
```
drums empty(1) drums bass
strings loop(2,lead,strings) 
bass bass drums empty(0.5) bass
```

### 4. Play Music

- **Play Individual Blocks**: Use the dropdown to select and play any created block
- **Play Composition**: Enter your composition text and click "Play Mixed" to hear the full arrangement

## Block Types

### Sample Block
- Contains audio data from an uploaded file
- Defined by start and end times
- Automatically trims audio to specified duration

### Empty Block  
- Creates silence for timing and spacing
- Defined by duration only
- Useful for creating rhythmic patterns

## Technical Details

### Audio Processing
- Uses `pydub` for audio manipulation and mixing
- Supports MP3 format input and output
- Handles audio trimming, concatenation, and overlay operations

### Playback
- Uses `pygame` for real-time audio playback
- Supports both individual block and mixed composition playback

### Data Persistence
- Blocks are saved to `blocks.json` 
- Maintains block definitions between sessions
- Uploaded files stored in `uploads/` directory

## Limitations

- Currently supports MP3 format only
- Web interface playback may have browser compatibility issues
- No built-in audio visualization
- Limited to simple text-based composition syntax

## Future Enhancements

- Support for additional audio formats (WAV, FLAC, etc.)
- Visual waveform editor
- MIDI export functionality
- More advanced loop and timing controls
- Real-time recording capabilities
- Effect processing (reverb, delay, etc.)

## Contributing

Feel free to submit issues and enhancement requests. :)
