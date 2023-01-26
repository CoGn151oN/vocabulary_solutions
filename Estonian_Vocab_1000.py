from googletrans import Translator
from gtts import gTTS
from pydub.audio_segment import AudioSegment as aseg
from PIL import Image, ImageFont, ImageDraw
import json

file_name = '1. Greetings'

def vocabsol():
    txt_file = f'_Originals_/{file_name}.txt'                                                # Path of original En word list
    lesson_title = txt_file[12: 24]
    src_lang = 'en'
    dest_lang = 'fi'


    #INPUT: list of En words from _Originals_ folder in txt file
    #OUTPUT: En words as list called orig_wds
    with open(txt_file) as f:
        txt = f.read()
    new_txt1 = txt.replace('\n', ',')
    orig_wds = new_txt1.split(',')


    #INPUT: orig_wds in En as list
    #OUTPUT: bi_dict as {index num: {En: translated_wds}
    bi_dict = {}
    for num, engl in enumerate(orig_wds):
        num += 1
        translation = Translator().translate([engl], src=src_lang, dest=dest_lang)
        for tr_wds in translation:
            translated_wds = tr_wds.text
            bi_dict[num] = {engl: translated_wds}


    #INPUT: bi_dict
    #OUTPUT: mp3 files in venv folder
    silence = aseg.silent(duration=2000)
    intermission = aseg.silent(duration=1200)
    #TTS for individual words in both languages(bi_dict), saved to mp3 in venv
    for ind, lil_d in bi_dict.items():
        for k, v in lil_d.items():
            out_en_slow = gTTS(text=k, lang=src_lang, slow=True)
            out_en_slow.save(f'{ind}_en_slow.mp3')
            out_en_fast = gTTS(text=k, lang=src_lang, slow=False)
            out_en_fast.save(f'{ind}_en_fast.mp3')
            out_translated_slow = gTTS(text=v, lang=dest_lang, slow=True)
            out_translated_slow.save(f'{ind}_translated_slow.mp3')
            out_translated_fast = gTTS(text=v, lang=dest_lang, slow=False)
            out_translated_fast.save(f'{ind}_translated_fast.mp3')
    #loads saved tts mp3 to memory to merge files
            translated_fast = aseg.from_mp3(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{ind}_translated_fast.mp3')
            translated_slow = aseg.from_mp3(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{ind}_translated_slow.mp3')
            en_fast = aseg.from_mp3(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{ind}_en_fast.mp3')
            en_slow = aseg.from_mp3(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{ind}_en_slow.mp3')
    #merges audio files with silent breaks and saves in folder naming source and dest lang
            translated2eng = translated_fast + silence + en_fast + intermission
            eng2translated = en_fast + silence + translated_slow + translated_fast + intermission
            translated2eng.export(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{dest_lang}_2_{src_lang}/{lesson_title}_{ind}_Translated2English.mp3', format='mp3')
            eng2translated.export(f'C:/Users/Les/PycharmProjects/Estonian_Vocab_1000/{src_lang}_2_{dest_lang}/{lesson_title}_{ind}_English2Translated.mp3', format='mp3')


    #INPUT: bi_dict
    #OUTPUT: images with En and translated words in venv
    for n, dikt in bi_dict.items():
        for s, t in dikt.items():
            im = Image.open('Background.png')
            font = ImageFont.truetype('consola.ttf', 69)
            d = ImageDraw.Draw(im)
            txteng = s
            txttranslated = t
    #fills source language
            d.text((370,269), text=txteng, font=font, fill=(240,240,230))
            im.save(f'{src_lang}_2_{dest_lang}/{n}-1_1.png')
    #fills both source and destiantion language
            d.text((370,269), text=txteng, font=font, fill=(240,240,230))
            d.text((370,369), text=txttranslated, font=font, fill=(240, 240, 230))
            im.save(f'{src_lang}_2_{dest_lang}/{n}-1_2.png')

            im = Image.open('Background.png')
            font = ImageFont.truetype('consola.ttf', 69)
            d = ImageDraw.Draw(im)
            txteng = s
            txttranslated = t
    #fills destinataion language
            d.text((370,269), text=txttranslated, font=font, fill=(240,240,230))
            im.save(f'{dest_lang}_2_{src_lang}/{n}-1_1.png')
    #fills both destination and source language
            d.text((370,269), text=txttranslated, font=font, fill=(240,240,230))
            d.text((370,369), text=txteng, font=font, fill=(240, 240, 230))
            im.save(f'{dest_lang}_2_{src_lang}/{n}-1_2.png')
    #title translation
            src_title = 'Lesson ' + lesson_title
            src_subtitle = 'English to Finnish'
            src_subtitle2 = "Finnish to English"
            title_trans = Translator().translate(src_title, src=src_lang, dest=dest_lang)
            dest_title = title_trans.text
    #Title1:
            im = Image.open('Background.png')
            font = ImageFont.truetype('consola.ttf', 69)
            d = ImageDraw.Draw(im)
            d.text((370, 269), text=src_title, font=font, fill=(240, 240, 230))
            d.text((370, 369), text=dest_title, font=font, fill=(240, 240, 230))
            im.save(f'{src_lang}_2_{dest_lang}/__00TITLE.png')
    #Title1:
            im = Image.open('Background.png')
            font = ImageFont.truetype('consola.ttf', 69)
            d = ImageDraw.Draw(im)
            d.text((370, 269), text=dest_title, font=font, fill=(240, 240, 230))
            d.text((370, 369), text=src_title, font=font, fill=(240, 240, 230))
            im.save(f'{dest_lang}_2_{src_lang}/__00TITLE.png')


def fixwds():
    pass


vocabsol()