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
button_slash, button_bsp, button_clear = st.columns(3)
if button_slash.button("/", key="slash", use_container_width=True):
    append_character("/", "Slash.png" )
# if button_question.button("?", key="question", use_container_width=True):  //button_question
#     append_character("?", "Question.png")
if button_bsp.button("backspace", key='bsp', use_container_width=True):
    drop_character()
if button_clear.button("clear all", key="clear_all", use_container_width=True):
    clear_list()

button_A, button_EI, button_OU, button_doubleslash = st.columns(4)
if button_A.button("A", key='A', use_container_width=True):
    append_character("A", "A.png")
if button_EI.button("E/I", key='E', use_container_width=True):
    append_character("E", "E.png")
if button_OU.button("O/U", key='O',use_container_width=True):
    append_character("O", "O.png")
if button_doubleslash.button("//", key="doubleslash", use_container_width=True):
    append_character("//", "DoubleSlash.png")

button_BA, button_BEI, button_BOU, button_B = st.columns(4) 
if button_BA.button("BA", key='BA', use_container_width=True):
    append_character("BA", "BA.png")
if button_BEI.button("BE/BI", key='BE', use_container_width=True):
    append_character("BE", "BeBi.png")
# if button_BI.button("BI", key='BI', use_container_width=True): // button_BI,
#     append_character("BI", "BeBi.png") 
if button_BOU.button("BO/BU", key='BO', use_container_width=True):
    append_character("BO", "BoBu.png")
# if button_BU.button("BU", key='BU', use_container_width=True):  button_BU,
#     append_character("BU", "BoBu.png")
if button_B.button("B", key='B', use_container_width=True):
    append_character("B", "B.png")


button_KA, button_KEI,  button_KOU,  button_K = st.columns(4) 
if button_KA.button("KA", key='KA', use_container_width=True):
    append_character("KA", "KA.png" )
if button_KEI.button("KE/KI", key='KE', use_container_width=True):
    append_character("KE", "KeKi.png")
# if button_KI.button("KI", key='KI', use_container_width=True): //button_KI,
#     append_character("KI", "KeKi.png")
if button_KOU.button("KO/KU", key='KO', use_container_width=True):
    append_character("KO", "KoKu.png")
# if button_KU.button("KU", key='KU', use_container_width=True): //button_KU,
#     append_character("KU", "KoKu.png")
if button_K.button("K", key='K', use_container_width=True):
    append_character("K", "K.png")

button_DA, button_DEI, button_DOU, button_D = st.columns(4) 
if button_DA.button("DA", key='DA', use_container_width=True):
    append_character("DA", "DA.png" )
if button_DEI.button("DE/DI", key='DE', use_container_width=True):
    append_character("DE", "DeDi.png")
# if button_DI.button("DI", key='DI', use_container_width=True): //button_DI, 
#     append_character("DI", "DeDi.png")
if button_DOU.button("DO/DU", key='DO', use_container_width=True):
    append_character("DO", "DoDu.png")
# if button_DU.button("DU", key='DU', use_container_width=True): //button_DU,
#     append_character("DU", "DoDu.png")
if button_D.button("D", key='D', use_container_width=True):
    append_character("D", "D.png" )

button_GA, button_GEI, button_GOU, button_G = st.columns(4)
if button_GA.button("GA", key='GA', use_container_width=True):
    append_character("GA", "GA.png")
if button_GEI.button("GE/GI", key='GE', use_container_width=True):
    append_character("GE", "GeGi.png")
# if button_GI.button("GI", key='GI', use_container_width=True): //button_GI,
#     append_character("GI", "GeGi.png")  
if button_GOU.button("GO/GU", key='GO', use_container_width=True):
    append_character("GO", "GoGu.png")
# if button_GU.button("GU", key='GU', use_container_width=True): //button_GU, 
#     append_character("GU", "GoGu.png")
if button_G.button("G", key='G', use_container_width=True):
    append_character("G", "G.png")

button_HA, button_HEI, button_HOU, button_H = st.columns(4)
if button_HA.button("HA", key='HA', use_container_width=True):
    append_character("HA", "HA.png" )
if button_HEI.button("HE/HI", key='HE', use_container_width=True):
    append_character("HE", "HeHi.png")   
# if button_HI.button("HI", key='HI', use_container_width=True): //button_HI,
#     append_character("HI", "HeHi.png")
if button_HOU.button("HO/HU", key='HO', use_container_width=True):
    append_character("HO", "HoHu.png")
# if button_HU.button("HU", key='HU', use_container_width=True): //button_HU,
#     append_character("HU", "HoHu.png")
if button_H.button("H", key='H', use_container_width=True):
    append_character("H", "H.png")

button_LA, button_LEI, button_LOU, button_L = st.columns(4)
if button_LA.button("LA", key='LA', use_container_width=True):
    append_character("LA", "LA.png")
if button_LEI.button("LE/LI", key='LE', use_container_width=True):
    append_character("LE", "LeLi.png") 
# if button_LI.button("LI", key='LI', use_container_width=True): //button_LI,
#     append_character("LI", "LeLi.png") 
if button_LOU.button("LO/LU", key='LO', use_container_width=True):
    append_character("LO", "LoLu.png")
# if button_LU.button("LU", key='LU', use_container_width=True): //button_LU,
#     append_character("LU", "LoLu.png")
if button_L.button("L", key='L', use_container_width=True):
    append_character("L", "L.png")

button_MA, button_MEI, button_MOU, button_M = st.columns(4)
if button_MA.button("MA", key="MA", use_container_width=True):
    append_character("MA", "MA.png")
if button_MEI.button("ME/MI", key="ME", use_container_width=True):
    append_character("ME", "MeMi.png")
# if button_MI.button("MI", key="MI", use_container_width=True): //button_MI,
#     append_character("MI", "MeMi.png") 
if button_MOU.button("MO/MU", key="MO", use_container_width=True):
    append_character("MO", "MoMu.png")
# if button_MU.button("MU", key="MU", use_container_width=True): //button_MU,
#     append_character("MU", "MoMu.png")
if button_M.button("M", key="M", use_container_width=True):
    append_character("M", "M.png")

button_NA, button_NEI, button_NOU, button_N = st.columns(4)
if button_NA.button("NA", key="NA", use_container_width=True):
    append_character("NA", "NA.png" )
if button_NEI.button("NE/NI", key="NE", use_container_width=True):
    append_character("NE", "NeNi.png")
# if button_NI.button("NI", key="NI", use_container_width=True): //button_NI,
#     append_character("NI", "NeNi.png")
if button_NOU.button("NO/NU", key="NO", use_container_width=True):
    append_character("NO", "NoNu.png")
# if button_NU.button("NU", key="NU", use_container_width=True): //button_NU,
#     append_character("NU", "NoNu.png")
if button_N.button("N", key="N", use_container_width=True):
    append_character("N", "N.png")

button_NGA, button_NGEI, button_NGOU, button_NG = st.columns(4)
if button_NGA.button("NGA", key="NGA", use_container_width=True):
    append_character("NGA", "NGA.png")
if button_NGEI.button("NGE/NGI", key="NGE", use_container_width=True):
    append_character("NGE", "NGeNGi.png")   
# if button_NGI.button("NGI", key="NGI", use_container_width=True): //button_NGI, 
#     append_character("NGI", "NGeNGi.png")
if button_NGOU.button("NGO/NGU", key="NGO", use_container_width=True):
    append_character("NGO", "NGoNGu.png")
# if button_NGU.button("NGU", key="NGU", use_container_width=True): //button_NGU, 
#     append_character("NGU", "NGoNGu.png")
if button_NG.button("NG", key="NG", use_container_width=True):
    append_character("NG", "NG.png")

button_PA, button_PEI, button_POU, button_P = st.columns(4)
if button_PA.button("PA", key="PA", use_container_width=True):
    append_character("PA", "PA.png")
if button_PEI.button("PE/PI", key="PE", use_container_width=True):
    append_character("PE", "PePi.png")
# if button_PI.button("PI", key="PI", use_container_width=True): //button_PI,
#     append_character("PI", "PePi.png") 
if button_POU.button("PO/PU", key="PO", use_container_width=True):
    append_character("PO", "PoPu.png")
# if button_PU.button("PU", key="PU", use_container_width=True): //button_PU,
#     append_character("PU", "PoPu.png")
if button_P.button("P", key="P", use_container_width=True):
    append_character("P", "P.png")

button_RA, button_REI, button_ROU, button_R = st.columns(4)
if button_RA.button("RA", key="RA", use_container_width=True):
    append_character("RA", "RA.png" )
if button_REI.button("RE/RI", key="RE", use_container_width=True):
    append_character("RE", "ReRi.png")
# if button_RI.button("RI", key="RI", use_container_width=True): //button_RI,
#     append_character("RI", "ReRi.png")
if button_ROU.button("RO/RU", key="RO", use_container_width=True):
    append_character("RO", "RoRu.png")
# if button_RU.button("RU", key="RU", use_container_width=True): //button_RU,
#     append_character("RU", "RoRu.png")
if button_R.button("R", key="R", use_container_width=True):
    append_character("R", "R.png")

button_SA, button_SEI, button_SOU, button_S = st.columns(4)
if button_SA.button("SA", key="SA", use_container_width=True):
    append_character("SA", "SA.png")
if button_SEI.button("SE/SI", key="SE", use_container_width=True):
    append_character("SE", "SeSi.png")
# if button_SI.button("SI", key="SI", use_container_width=True): //button_SI,
#     append_character("SI", "SeSi.png")
if button_SOU.button("SO/SU", key="SO", use_container_width=True):
    append_character("SO", "SoSu.png")
# if button_SU.button("SU", key="SU", use_container_width=True): //button_SU,
#     append_character("SU", "SoSu.png")
if button_S.button("S", key="S", use_container_width=True):
    append_character("S", "S.png")

button_TA, button_TEI, button_TOU,  button_T = st.columns(4)
if button_TA.button("TA", key="TA", use_container_width=True):
    append_character("TA", "TA.png" )
if button_TEI.button("TE/TI", key="TE", use_container_width=True):
    append_character("TE", "TeTi.png")
# if button_TI.button("TI", key="TI", use_container_width=True): //button_TI,
#     append_character("TI", "TeTi.png")
if button_TOU.button("TO/TU", key="TO", use_container_width=True):
    append_character("TO", "ToTu.png")
# if button_TU.button("TU", key="TU", use_container_width=True): //button_TU,
#     append_character("TU", "ToTu.png")
if button_T.button("T", key="T", use_container_width=True):
    append_character("T", "T.png")

button_WA, button_WEI, button_WOU, button_W = st.columns(4)
if button_WA.button("WA", key="WA", use_container_width=True):
    append_character("WA", "WA.png")
if button_WEI.button("WE/WI", key="WE", use_container_width=True):
    append_character("WE", "WeWi.png")
# if button_WI.button("WI", key="WI", use_container_width=True): //button_WI, 
#     append_character("WI", "WeWi.png") 
if button_WOU.button("WO/WU", key="WO", use_container_width=True):
    append_character("WO", "WoWu.png")
# if button_WU.button("WU", key="WU", use_container_width=True): //button_WU, 
#     append_character("WU", "WoWu.png")
if button_W.button("W", key="W", use_container_width=True):
    append_character("W", "W.png")

button_YA, button_YEI, button_YOU,  button_Y = st.columns(4)
if button_YA.button("YA", key="YA", use_container_width=True):
    append_character("YA", "YA.png" )
if button_YEI.button("YE/YI", key="YE", use_container_width=True):
    append_character("YE", "YeYi.png")
# if button_YI.button("YI", key="YI", use_container_width=True): //button_YI, 
#     append_character("YI", "YeYi.png")
if button_YOU.button("YO/YU", key="YO", use_container_width=True):
    append_character("YO", "YoYu.png")
# if button_YU.button("YU", key="YU", use_container_width=True): //button_YU,
#     append_character("YU", "YoYu.png")
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