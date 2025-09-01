import streamlit as st

st.title("💖 Khushi Special 💖")

# Session states
if "reasons" not in st.session_state:
    st.session_state.reasons = [
        "Maan jaoo na 💕",
        "Itta bura maanta hu ky ki maan nhi skti? 😔",
        "Achha chalo rasmalayi khate hain 🍮",
        "Achha chalo tumhari favourite jagah me chalte hain 🏞️",
        "Itna kyu bhaav kha rahi ho, khana hi hai to mere sath chalo 🍽️",
        "Itna kyu muh bna rahi ho, muh tedha ho gya to accha nhi lagega 😅",
        "Thoda sa bhi daya nhi aa rahi kya mujhpe 😢"
    ]
    st.session_state.reason_index = 0
    st.session_state.no_count = 0
    st.session_state.lyrics_stage = 0
    st.session_state.final_msg_shown = False

lyrics_blocks = [
    """🎶 Tu hi meri shab hai  
    Subah hai, tu hi din hai mera  
    Tu hi mera rab hai  
    Tu dua mein shamil hai 🎶""",
    
    """🎶 Tum jo aaye zindagi mein baat ban gayi  
    Ishq mazhab, ishq meri zaat ban gayi 🎶""",
    
    """🎶 Main tenu samjhawan ki  
    Na tere bina lagda jee  
    Tu ki jaane pyaar mera  
    Main karaan intezar tera 🎶"""
]

yes_message = """Sarangeeee 💖  
Meri baahon ko teri saanson ki jo aadatein lagi hai,  
aisi jee leta hoon ab main thoda aur...  
Meri dil ki rait pe, aankhon ki jo padhe parchhai teri... ✨"""

# Greeting
st.write("Hello Khushi 👋, kaise ho?")
user_reply = st.text_input("gusse mei mt likhna:")

if user_reply:
    reply = user_reply.lower()  # converts input to lowercase for consistent checking

    if "hello" in reply:
        st.write("Gussa ho kya? 😅")
    elif reply == "yes":
        st.success(yes_message)
        st.session_state.no_count = 0
        st.session_state.reason_index = 0
        st.session_state.lyrics_stage = 0
        st.session_state.final_msg_shown = False
    elif reply == "no":
        st.session_state.no_count += 1
        
        # 14th no special message
        if st.session_state.no_count >= 14:
            st.error("😢 Bacchhe ki jaan leni hai to ek baar mei le lo, yu ruth ke kyu thoda thoda maar rahi hoo...")
        
        # Show reasons first
        elif st.session_state.reason_index < len(st.session_state.reasons):
            st.warning(st.session_state.reasons[st.session_state.reason_index])
            st.session_state.reason_index += 1
        
        # Show lyrics after reasons
        elif st.session_state.lyrics_stage < len(lyrics_blocks):
            st.session_state.lyrics_stage += 1
            lines = "\n\n".join(lyrics_blocks[:st.session_state.lyrics_stage])
            st.info(lines)
        
        # Show final friendly message after all reasons & lyrics
        else:
            if not st.session_state.final_msg_shown:
                st.success("Haan maloom hai, galti meri hai, maan jaoo n 😅 itna kyun gussa kar rahi ho…")
                st.session_state.final_msg_shown = True
            else:
                st.write("Bas ab thoda khush ho jao 😄")
    else:
        st.write("Bas tumse baat karke hi accha lagta hai 💕")
