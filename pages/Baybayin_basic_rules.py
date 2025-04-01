import streamlit as st
import os


## Access the parent directory
parent_dir = os.path.dirname(os.path.dirname(__file__))
print(parent_dir)  # Outputs the directory one level up


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
st.markdown(' - A character is a combination of a consonant and vowel sound, such as BA, BE, BI, BO, BU, ... ')
st.markdown(' - The base character is a combination of a consonant and a vowel -A sound. ')
st.markdown(' - A dicritical mark called "kudlit" on top of a base character changes the vowel sound to either -E or -I. ')
st.markdown(' - A dicritical mark called "kudlit" at the bottom of a base character changes the vowel sound to either -O or -U. ')
st.markdown(''' - Originally, the stand-alone consonants are not written. 
            But during translation, a Spanish priest transcribed these stand-alone consonants with a cross at the bottom of the base character. ''')
st.markdown(''' - In ancient Tagalog, DA and RA have the same characters and meaning. In current Tagalog, there are **few** cases that this is still true, but may have slight variations. 
            For instance, "dadating == darating" (will arrive), "din == rin" (also), "narito == nandito" (something is here).  ''')

#container1 = st.container(height = 225, border=True)
# with st.container (height = 225, border=True, key='container1'):
#     file1 = os.path.join(parent_dir, 'images', 'BA.PNG')
#     col1a, col1b = st.columns([1,15], gap='small', vertical_alignment='center' )
#     with col1a:
#         st.image(file1, use_container_width=False, width=40)
#     with col1b:
#         st.write(' = BA')

#     file2 = os.path.join(parent_dir, 'images', 'BeBi.PNG')
#     col2a, col2b = st.columns([1,15], gap='small', vertical_alignment='center' )
#     with col2a:
#         st.image(file2, use_container_width=False, width=40)
#     with col2b:
#         st.write(' = BE / BI')

#     file3 = os.path.join(parent_dir, 'images', 'BoBu.PNG')
#     col3a, col3b = st.columns([1,15], gap='small', vertical_alignment='center' )
#     with col3a:
#         st.image(file3, use_container_width=False, width=40)
#     with col3b:
#         st.write(' = BO / BU')

#     file4 = os.path.join(parent_dir, 'images', 'B.PNG')
#     col4a, col4b = st.columns([1,15], gap='small', vertical_alignment='center' )
#     with col4a:
#         st.image(file4, use_container_width=False, width=40)
#     with col4b:
#         st.write(' = B')


st.subheader('Rules in writing:')
st.markdown('  - Each character represents a sound, mostly in syllables.')
st.markdown('  - Pre-colonial Baybayin, does not have spaces in between words.')
st.markdown('  - Pre-colonial Baybayin, only have two punctuation marks : "/" for comma or a pause and "//" for period or full-stop of a sentence.')
st.markdown('  - Pre-colonial Baybayin, there are no numbers.') 
st.markdown('  - Pre-colonial Baybayin, there is difference between upper and lower keys.') 
st.markdown('''  - Direction of writing is from left-to-right in horizontal medium, while bottom-to-top in vertical medium such as in a bamboo. 
            Imagine writing in a bamboo trunk left-to-right, then rotate it to 90-degrees counter-clockwise to be in vertical orientation. ''')

st.markdown('''  - From the original writing rules, the sounds that does not accompany a vowel. For example, in the word "araw" (sun), 
            the second syllable "-raw" is written only with the "ra" character, omitting the "w". However, the Filipino natives know that the transcribed "a - ra"  represents "araw". ''')


# with st.container (height = 130, border=True, key='container2'):
#     files1 = [os.path.join(parent_dir, 'images', 'A.PNG'), os.path.join(parent_dir, 'images', 'RA.PNG'), os.path.join(parent_dir, 'images', 'W.PNG') ]
#     col11a, col11b, col11c, col11d = st.columns([1, 1, 1, 10], vertical_alignment='center' )
#     with col11a:
#         st.image(files1[0], use_container_width=False, width=40)
#     with col11b:
#         st.image(files1[1], use_container_width=False, width=40)    
#     with col11c:
#         st.image(files1[2], use_container_width=False, width=40)   
#     with col11d:
#         st.write(' == ARAW in Modern Baybayin translation')
 
#     col22a, col22b, col22c = st.columns([1, 1, 10], vertical_alignment='center' )
#     with col22a:
#         st.image(files1[0], use_container_width=False, width=40)
#     with col22b:
#         st.image(files1[1], use_container_width=False, width=40)    
#     # with col11c:
#     #     st.image(files1[2], use_container_width=False, width=40)   
#     with col22c:
#         st.write(' == ARAW in original Baybayin (pre-colonial version)')


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


st.image('example1_screenshot.png', caption='example 1')
