# Godspeed You! Black Emperor Movement Extractor

This is a simple script to extract the movements from the song titles of the band Godspeed You! Black Emperor.

The movements in the file `lps.json` are extracted from the wikipedia page of each LP.

## Requirements

- Python 3.9 or greater (due to type-hints)
- FFmpeg
- Original CDs of each album

## Usage

By default this script will read the filenames of each album declared in the json file and will dump the movements in the same folder.

This script is meant to be used with FLAC sources 

```bash
git clone https://github.com/JorgeRuizDev/gybe-movement-extractor.git

python split.py
```

## License
MIT

## JSON Example
```json
{
  "1998. F♯ A♯ ∞ [2000, PCD-23058]": {
    "01. 'The Dead Flag Blues'.flac": {
      "The Dead Flag Blues (Intro)": "6:37",
      "Slow Moving Trains and The Cowboy...": "7:50",
      "The Dead Flag Blues (Outro)": "2:00"
    },
    "02. 'East Hastings'.flac": {
      "Nothing's Alrite in Our Life... and The Dead Flag Blues (Reprise)": "1:35",
      "The Sad Mafioso...": "10:44",
      "Drugs in Tokyo and Black Helicopter": "5:41"
    },
    "03. 'Providence'.flac": {
      "Divorce & Fever...": "2:45",
      "Dead Metheny...": "8:07",
      "Kicking Horse on Brokenhill": "5:53",
      "String Loop Manufactured During Downpour...": "4:37",
      "Silence": "3:30",
      "J.L.H. Outro": "4:08"
    }
  }
}
```