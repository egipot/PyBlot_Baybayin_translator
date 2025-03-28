import streamlit as st
import os

## Access the parent directory
parent_dir = os.path.dirname(os.path.dirname(__file__))
print(parent_dir)  # Outputs the directory one level up


# Define Page settings  
st.set_page_config(page_title="PyBlot's Baybayin Translator", 
            page_icon=':flag-ph:',
            layout='wide', initial_sidebar_state='auto')
st.title("Baybayin sample translations:")
st.text('\n')

#st.subheader('Here are the most common Tagalog words/phrases that you may encounter:')

# Function to translate all the word samples: 
def translate(wordsample):
    wordsample_translated = []
    for syllable in wordsample: 
        syllable_file = syllable + '.png'
        syllable_file = os.path.join(parent_dir, 'images', syllable_file)
        wordsample_translated.append(syllable_file)
    #print(wordsample1_translated)
    st.image(wordsample_translated, use_container_width=False, width=40)

st.text('\n')

# Sample 1
st.markdown('''**:blue[Salamat]** - this is the Tagalog translation of :green[Thank You].''')
st.markdown('''**:blue[ ---  Sa  ---  la  ---  ma  ---  t  ---]** == ''')
wordsample1 = ['SA', 'LA', 'MA', 'T']
translate(wordsample1)
st.text('\n')

# Sample 2
st.markdown('''**:blue[Magandang Umaga]** is the same as :green[Good Morning].''')
st.markdown('''**:blue[ --- Ma  ----  ga  ---  n  ---  da  ---  ng  --- ___  ---   U  ---  ma  ---  ga  ---]** == ''')
wordsample2 = ['MA', 'GA', 'N', 'DA', 'NG', 'space', 'U', 'MA', 'GA']
translate(wordsample2)
st.text('\n')

# Sample 3
st.markdown('''**:blue[Kumusta?]** - also means :green[How are you?].''')
st.markdown('''**:blue[ --- Ku  ----  mu  ---  s  ---  ta  --- ]** == ''')
wordsample3 = ['KOKU', 'MOMU', 'S', 'TA']
translate(wordsample3)
st.text('\n')

# Sample 4
st.markdown('''**:blue[Ingat lagi]** - the direct translation is :green[Take care always].''')
st.markdown('''**:blue[ ---  I  ----  nga  ---  t  ---  ___  ---  La  ---  gi  ---]** == ''')
wordsample4 = ['I', 'NGA', 'T', 'space', 'LA', 'GeGI']
translate(wordsample4)
st.text('\n')

st.markdown('''Notice that the consonant-only syllable (i.e. sound that is pronounced in combination of the previous syllable \
             and is not pronounced with a vowel after), 
            is still represented as a separate character. Such as the "p" in the word "ulap" (cloud). \
            This makes it easier to learn and translate Baybayin.''')
st.markdown('''In old documentations about pre-collonial Baybayin, such syllables are elimited in writing, even if pronounced and important in conveying the meaning. \
            Our ancestors already know the words from verbal learning, and writing such syllables was considered unnecessary. \
            This made it difficult for the foreigners to decode Baybayin. ''')
