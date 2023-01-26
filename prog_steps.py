from gtts import gTTS
import os
from pydub import audio_segment
import numpy as np
import pandas as pd


def get_filepaths(index: int) -> dict:
    project_dir = os.getcwd()
    fp = {'et_fast': os.path.join(project_dir, f'{index}_et_slow.mp3'),
          'et_slow': os.path.join(project_dir, f'{index}_et_slow.mp3'),
          'en_fast': os.path.join(project_dir, f'{index}_en_fast.mp3'),
          'en_slow': os.path.join(project_dir, f'{index}_en_slow.mp3'),
          'et2en': os.path.join(project_dir, 'Estonian2English'),
          'en2et': os.path.join(project_dir, 'English2Estonian'),
          }
    return fp


def save(d_subset: dict):  # reads words in Eng and Est, saves to individual mp3s, loads for merge
    for i, lil_d in d_subset.items():
        fp = get_filepaths(i)
        for k, v in lil_d.items():
            out_en_slow = gTTS(text=k, lang='en', slow=True)
            out_en_slow.save(fp['en slow'])
            out_en_fast = gTTS(text=k, lang='en', slow=False)
            out_en_fast.save(fp['en fast'])
            out_et_slow = gTTS(text=v, lang='et', slow=True)
            out_et_slow.save(fp['et slow'])
            out_et_fast = gTTS(text=v, lang='et', slow=False)
            out_et_fast.save(fp['et fast'])


def load(aseg: audio_segment.AudioSegment, index: int):
    fp = get_filepaths(index)
    out = {'et fast': aseg.from_mp3(fp['et fast']),
           'et slow': aseg.from_mp3(fp['et slow']),
           'en fast': aseg.from_mp3(fp['en fast']),
           'en slow': aseg.from_mp3(fp['en slow']),
           }
    return out


def merge(loaded: dict, merged:dict, silence: audio_segment.AudioSegment, index: int, start: int, finish: int):
    """Merges individual mp3s to blocks of 50"""
    fp = get_filepaths(index)
    if index == 0:
        et2en = et_slow + et_fast + silence + en_slow
        en2et = en_slow + silence + et_slow + et_fast
    else:
        et2en = merged['et2en'] + et_slow + et_fast + silence + en_slow
        en2et = merged['en2et'] + en_slow + silence + et_slow + et_fast
    loaded['et2en'].export(os.path.join(fp['et2en'], f'Estonian2English{start}-{finish}.mp3'), format='mp3')
    loaded['en2et'].export(os.path(fp['en2et'], f'English2Estonian{start}-{finish}.mp3'), format='mp3')
    return {'et2en': et2en, 'en2et': en2et}


def cleanup():
    # delete individual sound files in evn folder in previous index range
    dum = 0


if __name__ == "__main__":
    d = {
        1: {'be': 'olema'},
        2: {'and': 'ja'},
        3: {'of': 'kohta'},
        4: {'in': 'sisse'},
        5: {'to': 'et'},
    }
    s = pd.Series(d)
    aseg = audio_segment.AudioSegment
    silence = aseg.silent(duraion=2000)
    # loop to lump groups of 50 words, all below code goes in there so start and finish get updated each time
    batch_size = 50
    i0 = 0
    i1 = np.clip(len(d) - batch_size, i0+1, len(d))
    for x in range(i0, i1, batch_size):
        start = x
        finish = np.clip(x + batch_size, 0, len(d))
        d_subset = s.iloc[start:finish].to_dict()
        save(d_subset)
        for index in range(start, finish, 1):
            loaded = load(aseg, index)
            merged = merge(loaded, merged, silence, index, start, finish)
