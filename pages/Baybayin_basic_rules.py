import streamlit as st
import os


## Access the parent directory
parent_dir = os.path.dirname(os.path.dirname(__file__))
#print(parent_dir)  # Outputs the directory one level up


# Function to translate all the word samples: 
def translate(wordsample):
    wordsample_translated = []
    for syllable in wordsample: 
        if len(syllable) > 2:
            syllable_caption = syllable[:2].upper() + ' or ' + syllable[2:].upper()
        else:
            syllable_caption = syllable
        syllable_file = syllable + '.png'
        syllable_file = os.path.join(parent_dir, 'images', syllable_file)
        wordsample_translated.append(syllable_file)
    #print(wordsample1_translated)
    st.image(wordsample_translated, use_container_width=False, width=80, caption = syllable_caption)


st.title("Understanding Baybayin alphabet")

st.text('\n')

st.subheader('Pronunciation and definition:')
st.markdown(''':blue-background[Baybayin *[bay-ba-yin, with accent/stress on the second syllable **-ba-**]* is an ancient writing system in the pre-colonial times in the Philippines.] ''')
st.markdown(''' Baybayin *[bay-ba-yin, with accent/stress on the last syllable **-yin**]*  means to spell or to pronounce per syllable. 
            This is based on the root word "baybay", which can refer to an enumeration or iteration ''')

st.markdown('''This same word can also refer to the shoreline, as the same root word "baybay" can also refer to an edge or boundary.''')
st.markdown('''The Philippines has more than 170 dialects, and it some of the most widely used ones have different variations of baybayin writing.
             Thus, making it difficult to standardize the learning and re-integration to the study curriculum. ''')

st.subheader('Rules in speaking Filipino (Tagalog dialect):')
st.markdown(' - A character is a combination of a consonant and vowel sound. For example - BA, BE, BI, BO, BU. ')
st.markdown(' - The base character is a combination of a consonant and a vowel -A sound. ')
st.markdown(' - A dicritical mark called "kudlit" on top of a base character changes the vowel sound to either -E or -I. ')
st.markdown(' - A dicritical mark called "kudlit" at the bottom of a base character changes the vowel sound to either -O or -U. ')
st.markdown(''' - Originally, the stand-alone consonants are not written, even if pronounced and important in conveying the meaning. 
            But during translation to Spanish (Latin alphabet), a priest transcribed these stand-alone consonants with a cross at the bottom of the base character (virama).''')


ch0, ch1, ch2, ch3, ch4, ch5 = st.columns(6)
with ch0:
    st.write('')
with ch1:
    rulesample1 = ['BA']
    translate(rulesample1)
with ch2:
    rulesample2 = ['BeBi']
    translate(rulesample2)
with ch3:
    rulesample3 = ['BoBu']
    translate(rulesample3)
with ch4:
    rulesample4 = ['B']
    translate(rulesample4)
with ch5:
    st.write('')



st.subheader('Rules in writing:')
st.markdown('  - Each character represents a sound, mostly in syllables.')
st.markdown('  - Pre-colonial Baybayin, does not have spaces in between words.')
st.markdown('  - Pre-colonial Baybayin, only have two punctuation marks : "/" for comma or a pause and "//" for period or full-stop of a sentence.')
st.markdown('  - Pre-colonial Baybayin, there are no numbers.') 
st.markdown('  - Pre-colonial Baybayin, there is difference between upper and lower keys.') 
st.markdown('''  - Direction of writing is from left-to-right in horizontal medium, while bottom-to-top in vertical medium such as in a bamboo. 
            Imagine writing in a bamboo trunk left-to-right, then rotate it to 90-degrees counter-clockwise to be in vertical orientation. ''')
st.markdown(''' - In ancient Tagalog, DA and RA have the same characters and meaning. In current Tagalog, there are **few** cases that this is still true, but may have slight variations. 
            For instance, "dadating == darating" (will arrive), "din == rin" (also), "narito == nandito" (something is here).  ''')
st.markdown('''  - From the original writing rules, the sounds that does not accompany a vowel. For example, in the word "araw" (sun), 
            the second syllable "-raw" is written only with the "ra" character, omitting the "w". However, the Filipino natives know that the transcribed "a - ra"  represents "araw". ''')

ch6, ch7, ch8, ch9, ch10 = st.columns(5, border=False)
with ch6:
    st.write('')
with ch7:
    rulesample4 = ['A']
    translate(rulesample4)
with ch8:
    rulesample5 = ['RA']
    translate(rulesample5)
with ch9:
    rulesample6 = ['W']
    translate(rulesample6)
    st.caption ('^This stand-alone consonant is not written in pre-colonial Baybayin')
with ch10:
    st.write('')

st.subheader('In this Baybayin translator: ')
st.markdown('''To make the usage and learning easier, I decided to : ''')
st.markdown('  - use the consonant-only representation (x at the bottom of base character) ')
st.markdown('  - separate the characters for D and R to show differences, because there are more cases when these two characters cannot be used interchangeably.')
st.markdown('  - allow the use of spaces between words to make it readable.')
st.markdown('  - allow the use of question mark to show better context and differentiate a statement to a question.')
st.markdown('  - show separate buttons for syllables with -E and -I.')
st.markdown('  - show separate buttons for syllables with -O and -U.')

st.text('This app is best viewed in landscape mode and light theme (The result is not visible in dark theme).')
st.text('The Baybayin characters used in this tool is my own and copywrited under (c)KalatasArt.  ')

st.text('\n')
st.text('\n')
st.markdown('''***:gray[References:]***''') 
st.markdown('''*:gray[ --- https://en.wikibooks.org/wiki/Learn_Baybayin/Reading_and_Writing    ]*''')
st.markdown('''*:gray[ --- https://en.wikipedia.org/wiki/Baybayin    ]*''')
st.markdown('''*:gray[ --- https://www.gutenberg.org/files/16119/16119-h/16119-h.htm    ]*''')   
st.markdown('''*:gray[ --- https://theficklefeet.com/how-to-write-baybayin/  ]*''')
st.markdown('''*:gray[ --- https://tagalog.pinoydictionary.com/search?q=baybay  ]*''')
st.markdown('''*:gray[ --- https://philpad.com/list-of-languages-in-the-philippines-living-dialects/ ]*''')