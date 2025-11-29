# Import the necessary libraries
import streamlit as st
from PIL import Image
import os


# Define Page settings  
st.set_page_config(page_title="PyBlot's Baybayin Translator", 
            page_icon=':flag-ph:',
            layout='wide', initial_sidebar_state='auto')
st.title("PyBlot's Baybayin Translator")
st.markdown("Translate a Filipino (Tagalog) expression by selecting per syllable. Then click on the Submit button to show the equivalent Baybayin characters.")
st.markdown("""*:gray[This app is best viewed in landscape mode and using light theme.]*""")


# Store the input syllable(s) into a list.
# And list its equivalent Baybayin character (image .PNG) 
if 'char_list' not in st.session_state:
    st.session_state.char_list = []
    st.session_state.image_list = []


#Functions
def append_character(newchar, image_file):
    st.session_state.char_list.append(newchar)
    short_path = os.path.join("images2", image_file)  # Using relative path
    st.session_state.image_list.append(short_path)
    #print(short_path)
    
def drop_character():
    st.session_state.char_list = st.session_state.char_list[:-1]
    st.session_state.image_list = st.session_state.image_list[:-1]

def clear_list():
    st.session_state.char_list = []
    st.session_state.image_list = []


# Display all possible syllables (with Latin labels) as keyboard-like buttons  
# keyboard line 1 (vowels, terminating characters, backspace, clear all)
button_A, button_E, button_I, button_O, button_U = st.columns(5)
if button_A.button("A", key='A', use_container_width=True):
    append_character("A", "A.png")
if button_E.button("E", key='E', use_container_width=True):
    append_character("E", "E.png")
if button_I.button("I", key='I',use_container_width=True):
    append_character("I", "I.png")
if button_O.button("O", key='O',use_container_width=True):
    append_character("O", "O.png")
if button_U.button("U", key='U',use_container_width=True):
    append_character("U", "U.png")

button_slash,  button_doubleslash, button_question, button_bsp, button_clear = st.columns(5)
if button_slash.button("/", key="slash", use_container_width=True):
    append_character("/", "Slash.png" )
if button_doubleslash.button("//", key="doubleslash", use_container_width=True):
    append_character("//", "DoubleSlash.png")
if button_question.button("?", key="question", use_container_width=True):
    append_character("?", "Question.png")
# if button_space.button("space", key="space", use_container_width=True):
#     append_character(" ", "Space.png")
if button_bsp.button("backspace", key='bsp', use_container_width=True):
    drop_character()
if button_clear.button("clear all", key="clear_all", use_container_width=True):
    clear_list()

button_BA, button_BE, button_BI, button_BO, button_BU = st.columns(5) 
if button_BA.button("BA", key='BA', use_container_width=True):
    append_character("BA", "BA.png")
if button_BE.button("BE", key='BE', use_container_width=True):
    append_character("BE", "BeBi.png")
if button_BI.button("BI", key='BI', use_container_width=True):
    append_character("BI", "BeBi.png") 
if button_BO.button("BO", key='BO', use_container_width=True):
    append_character("BO", "BoBu.png")
if button_BU.button("BU", key='BU', use_container_width=True):
    append_character("BU", "BoBu.png")

# keyboard line 2 (consonants ending with -A)
# button_BA, button_KA, button_DA, button_GA, button_HA, button_LA, button_MA, button_NA, button_NGA, button_PA, button_RA, button_SA, button_TA, button_WA, button_YA = st.columns(15) 
# if button_BA.button("BA", key='BA', use_container_width=True):
#     append_character("BA", "BA.png")
# if button_KA.button("KA", key='KA', use_container_width=True):
#     append_character("KA", "KA.png" )
# if button_DA.button("DA", key='DA', use_container_width=True):
#     append_character("DA", "DA.png" )
# if button_GA.button("GA", key='GA', use_container_width=True):
#     append_character("GA", "GA.png")
# if button_HA.button("HA", key='HA', use_container_width=True):
#     append_character("HA", "HA.png" )
# if button_LA.button("LA", key='LA', use_container_width=True):
#     append_character("LA", "LA.png")
# if button_MA.button("MA", key="MA", use_container_width=True):
#     append_character("MA", "MA.png")
# if button_NA.button("NA", key="NA", use_container_width=True):
#     append_character("NA", "NA.png" )
# if button_PA.button("PA", key="PA", use_container_width=True):
#     append_character("PA", "PA.png")
# if button_RA.button("RA", key="RA", use_container_width=True):
#     append_character("RA", "RA.png" )
# if button_SA.button("SA", key="SA", use_container_width=True):
#     append_character("SA", "SA.png")
# if button_TA.button("TA", key="TA", use_container_width=True):
#     append_character("TA", "TA.png" )
# if button_WA.button("WA", key="WA", use_container_width=True):
#     append_character("WA", "WA.png")
# if button_YA.button("YA", key="YA", use_container_width=True):
#     append_character("YA", "YA.png" )
# if button_NGA.button("NGA", key="NGA", use_container_width=True):
#     append_character("NGA", "NGA.png")

# # keyboard line 3 (consonants ending with -E)
# button_BE, button_KE, button_DE, button_GE, button_HE, button_LE, button_ME, button_NE, button_NGE, button_PE, button_RE, button_SE, button_TE, button_WE, button_YE = st.columns(15) 
# if button_BE.button("BE", key='BE', use_container_width=True):
#     append_character("BE", "BeBi.png")
# if button_KE.button("KE", key='KE', use_container_width=True):
#     append_character("KE", "KeKi.png")
# if button_DE.button("DE", key='DE', use_container_width=True):
#     append_character("DE", "DeDi.png")
# if button_GE.button("GE", key='GE', use_container_width=True):
#     append_character("GE", "GeGi.png")
# if button_HE.button("HE", key='HE', use_container_width=True):
#     append_character("HE", "HeHi.png")
# if button_LE.button("LE", key='LE', use_container_width=True):
#     append_character("LE", "LeLi.png")   
# if button_ME.button("ME", key="ME", use_container_width=True):
#     append_character("ME", "MeMi.png")
# if button_NE.button("NE", key="NE", use_container_width=True):
#     append_character("NE", "NeNi.png")
# if button_NGE.button("NGE", key="NGE", use_container_width=True):
#     append_character("NGE", "NGeNGi.png")
# if button_PE.button("PE", key="PE", use_container_width=True):
#     append_character("PE", "PePi.png")
# if button_RE.button("RE", key="RE", use_container_width=True):
#     append_character("RE", "ReRi.png")
# if button_SE.button("SE", key="SE", use_container_width=True):
#     append_character("SE", "SeSi.png")
# if button_TE.button("TE", key="TE", use_container_width=True):
#     append_character("TE", "TeTi.png")
# if button_WE.button("WE", key="WE", use_container_width=True):
#     append_character("WE", "WeWi.png")
# if button_YE.button("YE", key="YE", use_container_width=True):
#     append_character("YE", "YeYi.png")
    
# # keyboard line 4 (consonants ending with -I)
# button_BI, button_KI, button_DI, button_GI, button_HI, button_LI, button_MI, button_NI, button_NGI, button_PI, button_RI, button_SI, button_TI, button_WI, button_YI = st.columns(15) 
# if button_BI.button("BI", key='BI', use_container_width=True):
#     append_character("BI", "BeBi.png")   
# if button_KI.button("KI", key='KI', use_container_width=True):
#     append_character("KI", "KeKi.png")
# if button_DI.button("DI", key='DI', use_container_width=True):
#     append_character("DI", "DeDi.png")
# if button_GI.button("GI", key='GI', use_container_width=True):
#     append_character("GI", "GeGi.png")   
# if button_HI.button("HI", key='HI', use_container_width=True):
#     append_character("HI", "HeHi.png")
# if button_LI.button("LI", key='LI', use_container_width=True):
#     append_character("LI", "LeLi.png")   
# if button_MI.button("MI", key="MI", use_container_width=True):
#     append_character("MI", "MeMi.png")  
# if button_NI.button("NI", key="NI", use_container_width=True):
#     append_character("NI", "NeNi.png")
# if button_NGI.button("NGI", key="NGI", use_container_width=True):
#     append_character("NGI", "NGeNGi.png") 
# if button_PI.button("PI", key="PI", use_container_width=True):
#     append_character("PI", "PePi.png") 
# if button_RI.button("RI", key="RI", use_container_width=True):
#     append_character("RI", "ReRi.png")
# if button_SI.button("SI", key="SI", use_container_width=True):
#     append_character("SI", "SeSi.png")   
# if button_TI.button("TI", key="TI", use_container_width=True):
#     append_character("TI", "TeTi.png")
# if button_WI.button("WI", key="WI", use_container_width=True):
#     append_character("WI", "WeWi.png")  
# if button_YI.button("YI", key="YI", use_container_width=True):
#     append_character("YI", "YeYi.png")

# # keyboard line 5 (consonants ending with -O)
# button_BO, button_KO, button_DO, button_GO, button_HO, button_LO, button_MO, button_NO, button_NGO, button_PO, button_RO, button_SO, button_TO, button_WO, button_YO = st.columns(15) 
# if button_BO.button("BO", key='BO', use_container_width=True):
#     append_character("BO", "BoBu.png")
# if button_KO.button("KO", key='KO', use_container_width=True):
#     append_character("KO", "KoKu.png")
# if button_DO.button("DO", key='DO', use_container_width=True):
#     append_character("DO", "DoDu.png")
# if button_GO.button("GO", key='GO', use_container_width=True):
#     append_character("GO", "GoGu.png")
# if button_HO.button("HO", key='HO', use_container_width=True):
#     append_character("HO", "HoHu.png")
# if button_LO.button("LO", key='LO', use_container_width=True):
#     append_character("LO", "LoLu.png")
# if button_MO.button("MO", key="MO", use_container_width=True):
#     append_character("MO", "MoMu.png")
# if button_NO.button("NO", key="NO", use_container_width=True):
#     append_character("NO", "NoNu.png")
# if button_NGO.button("NGO", key="NGO", use_container_width=True):
#     append_character("NGO", "NGoNGu.png")
# if button_PO.button("PO", key="PO", use_container_width=True):
#     append_character("PO", "PoPu.png")
# if button_RO.button("RO", key="RO", use_container_width=True):
#     append_character("RO", "RoRu.png")
# if button_SO.button("SO", key="SO", use_container_width=True):
#     append_character("SO", "SoSu.png")
# if button_TO.button("TO", key="TO", use_container_width=True):
#     append_character("TO", "ToTu.png")
# if button_WO.button("WO", key="WO", use_container_width=True):
#     append_character("WO", "WoWu.png")
# if button_YO.button("YO", key="YO", use_container_width=True):
#     append_character("YO", "YoYu.png")

# # keyboard line 6 (consonants ending with -U)
# button_BU, button_KU, button_DU, button_GU, button_HU, button_LU, button_MU, button_NU, button_NGU, button_PU, button_RU, button_SU, button_TU, button_WU, button_YU = st.columns(15) 
# if button_BU.button("BU", key='BU', use_container_width=True):
#     append_character("BU", "BoBu.png")
# if button_KU.button("KU", key='KU', use_container_width=True):
#     append_character("KU", "KoKu.png")
# if button_DU.button("DU", key='DU', use_container_width=True):
#     append_character("DU", "DoDu.png")
# if button_GU.button("GU", key='GU', use_container_width=True):
#     append_character("GU", "GoGu.png")
# if button_HU.button("HU", key='HU', use_container_width=True):
#     append_character("HU", "HoHu.png")
# if button_LU.button("LU", key='LU', use_container_width=True):
#     append_character("LU", "LoLu.png")
# if button_MU.button("MU", key="MU", use_container_width=True):
#     append_character("MU", "MoMu.png")
# if button_NU.button("NU", key="NU", use_container_width=True):
#     append_character("NU", "NoNu.png")
# if button_NGU.button("NGU", key="NGU", use_container_width=True):
#     append_character("NGU", "NGoNGu.png")
# if button_PU.button("PU", key="PU", use_container_width=True):
#     append_character("PU", "PoPu.png")
# if button_RU.button("RU", key="RU", use_container_width=True):
#     append_character("RU", "RoRu.png")
# if button_SU.button("SU", key="SU", use_container_width=True):
#     append_character("SU", "SoSu.png")
# if button_TU.button("TU", key="TU", use_container_width=True):
#     append_character("TU", "ToTu.png")
# if button_WU.button("WU", key="WU", use_container_width=True):
#     append_character("WU", "WoWu.png")
# if button_YU.button("YU", key="YU", use_container_width=True):
#     append_character("YU", "YoYu.png")

# keyboard line 7 (consonant-only)
button_B, button_K, button_D, button_G, button_H = st.columns(5)  
if button_B.button("B", key='B', use_container_width=True):
    append_character("B", "B.png")
if button_K.button("K", key='K', use_container_width=True):
    append_character("K", "K.png")
if button_D.button("D", key='D', use_container_width=True):
    append_character("D", "D.png" )
if button_G.button("G", key='G', use_container_width=True):
    append_character("G", "G.png")
if button_H.button("H", key='H', use_container_width=True):
    append_character("H", "H.png")

button_L, button_M, button_N, button_NG, button_P = st.columns(5) 
if button_L.button("L", key='L', use_container_width=True):
    append_character("L", "L.png")
if button_M.button("M", key="M", use_container_width=True):
    append_character("M", "M.png")
if button_N.button("N", key="N", use_container_width=True):
    append_character("N", "N.png")
if button_NG.button("NG", key="NG", use_container_width=True):
    append_character("NG", "NG.png")
if button_P.button("P", key="P", use_container_width=True):
    append_character("P", "P.png")

button_R, button_S, button_T, button_W, button_Y = st.columns(5) 
if button_R.button("R", key="R", use_container_width=True):
    append_character("R", "R.png")
if button_S.button("S", key="S", use_container_width=True):
    append_character("S", "S.png")
if button_T.button("T", key="T", use_container_width=True):
    append_character("T", "T.png")
if button_W.button("W", key="W", use_container_width=True):
    append_character("W", "W.png")
if button_Y.button("Y", key="Y", use_container_width=True):
    append_character("Y", "Y.png")


# keyboard line 8 (space-only)
if st.button("space", key="space", use_container_width=True):
    append_character(" ", "Space.png")

# removed to separate space from line1
# button_space = st.columns() -> previously 11th in line1
# if button_space.button("space", key="space", use_container_width=True):
#     append_character(" ", "Space.png")


# Display the list
#st.write("Current Char_List:", st.session_state.char_list)
#st.write("Current Image_List:", st.session_state.image_list)
#st.write("Length of the List:",len(st.session_state.char_list))
#for x in st.session_state.char_list
st.markdown(f'''{"Tagalog expression to translate: " + " - ".join(st.session_state.char_list)}''')

# Submit button to finalize the list
if st.button("Submit", key="btn_submit"):
    #st.write("Finalized List:", st.session_state.image_list)
    cols = st.columns(len(st.session_state.image_list), vertical_alignment='center')
    for col, img in zip(cols, st.session_state.image_list):
        col.image(img, use_container_width=True)




st.markdown("""*:gray[The result of this translator is a list of images for illustration purposes. If there is a need to provide the text version, you may email me (kalatasart@gmail.com) for OpenType and TrueType font files.]*""")