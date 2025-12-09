
import streamlit as st
from PIL import Image
import urllib.parse
import time

# -------------------------
# THEME COLORS (Gold/Brown)
# -------------------------
primary_color = "#E36618"      # Rich Gold for headings
background_color = "#E78309"   # Golden Brown background
accent_color = "#3412E1"        # Bright gold accents / borders
text_color = "#012940"          # Dark brown for text

# WhatsApp number 
WHATSAPP_NUMBER = st.secrets["WHATSAPP_NUMBER"]


# -------------------------
# CSS: Floating Icons + Aesthetic Background + Animations
# -------------------------
style = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=PT+Sans:wght@400;700&display=swap');

    html, body, [class*="css"] {{
        background: linear-gradient(135deg, {background_color} 0%, "#3412E1"  100%);
        font-family: 'PT Sans', sans-serif;
        overflow-x: hidden;
    }}

    h1, h2, h3 {{
        font-family: 'Playfair Display', serif;
        color: {primary_color} !important;
        text-align: center;
    }}

    p {{
        font-size: 18px;
        line-height: 1.6;
        color: {text_color};
    }}

    .card {{
        background: rgba(255, 255, 255, 0.85);
        padding: 22px;
        border-radius: 20px;
        border: 1.5px solid {accent_color};
        margin-top: 20px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.07);
        backdrop-filter: blur(4px);
        animation: fadeIn 1s ease-in-out;
    }}

    /* Floating Icons */
    .float-icon {{
        position: fixed;
        width: 60px;
        opacity: 0.23;
        animation: float 9s infinite ease-in-out;
        z-index: 0;
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-35px) rotate(12deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}

    #icon1 {{ top: 10%; left: 5%; animation-duration: 10s; }}
    #icon2 {{ top: 60%; left: 85%; animation-duration: 12s; }}
    #icon3 {{ top: 80%; left: 10%; animation-duration: 14s; }}
    #icon4 {{ top: 30%; left: 75%; animation-duration: 11s; }}

    @keyframes fadeIn {{
        from {{opacity: 0;}}
        to {{opacity: 1;}}
    }}
</style>
"""
def inject_global_css():
    st.markdown(f"""
    <style>
    /* Birthday Section */
    .birthday-title {{
        font-size: 80px;
        text-align: center;
        font-weight: 800;
        color: {primary_color};
    }}

    .birthday-text {{
        font-size: 60px;
        text-align: center;
        color: {text_color};
        margin-bottom: 16px;
        line-height: 50px;
    }}

    .blessing-card {{
        margin-top: 25px;
        padding: 25px;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.09);
        border: 1px solid rgba(255,255,255,0.25);
        backdrop-filter: blur(6px);
        box-shadow: 0px 6px 14px rgba(0,0,0,0.35);
        animation: fadeIn 1s ease;
    }}

    .blessing-title {{
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        color: {accent_color};
    }}

    .blessing-text {{
        text-align: center;
        font-style: italic;
        font-size: 36px;
        color: {text_color};
        line-height: 36px;
    }}

    /* Christmas Section */
    .christmas-card {{
        margin-top: 40px;
        padding: 30px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(8px);
        box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
        animation: fadeIn 1.4s ease;
    }}

    .christmas-title {{
        text-align: center;
        font-size: 50px;
        font-weight: 700;
        color: {accent_color};
    }}

    .christmas-text {{
        text-align: center;
        font-size: 48px;
        line-height: 48px;
        color: {text_color};
    }}

    .christmas-subtitle {{
        margin-top: 20px;
        color: {primary_color};
        font-size: 48px;
        font-weight: 700;
    }}

    .event-details {{
        font-size: 44px;
        color: {text_color};
    }}

    </style>
    """, unsafe_allow_html=True)


# -------------------------
# FLOATING ICON IMAGES
# -------------------------
icon_bday = "https://cdn-icons-png.flaticon.com/512/3469/3469334.png"
icon_tree = "https://cdn-icons-png.flaticon.com/512/1864/1864583.png"
icon_gift = "https://cdn-icons-png.flaticon.com/512/2541/2541988.png"
icon_star = "https://cdn-icons-png.flaticon.com/512/1828/1828884.png"


# -------------------------
# BIRTHDAY HERO SECTION
# -------------------------
def birthday_section():
    st.markdown("""
        <h1 class="birthday-title"> A Very Special Day</h1>

        <p class="birthday-text">
            Happy Birthday, Babai! Today is not just another day but it's a celebration of <b>you</b>.
        </p>

        <p class="birthday-text">
            May your life be filled with joy, strength, and beautiful moments.
        </p>

        <div class="blessing-card">
            <h3 class="blessing-title">✨ Bible Blessing ✨</h3>
            <p class="blessing-text">
                “The Lord bless you and keep you;<br>
                the Lord make His face shine upon you<br>
                and be gracious to you.”<br>
                — <b>Numbers 6:24–25</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

# -------------------------
# CHRISTMAS SECTION
# -------------------------
def christmas_section():
    st.markdown("""
    <div class="christmas-card">
        <h2 class="christmas-title">🎄 Christmas Surprise 🎁</h2>
        <p class="christmas-text">As we celebrate your special day, we would love for you to join us and share the joy of Christmas together</p>
        <h3 class="christmas-subtitle">📅 Event Details</h3>
        <p class="event-details"><b>Date:</b> December 25th, 2025 at 7:00 PM</p>
        <p class="event-details"><b>Location:</b> Our Home — Guntur</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("✨ View Invitation Card"):
        st.image("Green and White Christmas Invitation.png", width='stretch')

# -------------------------
# FOOTER
# -------------------------
def footer():
    st.markdown("""
        <p style="
            text-align:center; 
            font-size:24px; 
            color:#E36618 ; 
            margin-top:40px; 
            font-weight:700;
        ">Made with ❤️ for Babai</p>
    """, unsafe_allow_html=True)

# -------------------------
# UNIQUE RSVP SECTION
# -------------------------
def arrival_section():
    st.subheader("✨one quick question✨")
    st.write("Can you please tell us quickly about your arrival? ❤️")

    # radio choice
    choice = st.radio("Your Response:", ["we'll be there! 🎉", "Unable to come 😔"], index=0, key="arrival_choice")

    # button - handle click
    if st.button("Send Confirmation ❤️", key="send_confirmation"):
        st.success("Thank you Babai! Redirecting to WhatsApp...")

        # build WhatsApp link using the selected choice (choice is defined here)
        wa_message = f"My arrival update: {choice}"
        wa_url = f"https://api.whatsapp.com/send?phone={urllib.parse.quote(WHATSAPP_NUMBER)}&text={urllib.parse.quote(wa_message)}"

        # open WhatsApp in a new tab using JS (works from inside Streamlit iframe in most browsers)
        st.markdown(
            f"""
            <script>
                window.open('{wa_url}', '_blank');
            </script>
            """,
            unsafe_allow_html=True,
        )

        # fallback clickable link in case popups are blocked
        st.markdown(
            f"<p style='margin-top:10px'><a href='{wa_url}' target='_blank' style='font-size:18px; color:{primary_color};'>Click here if WhatsApp didn’t open automatically</a></p>",
            unsafe_allow_html=True,
        )

# -------------------------
# MAIN APP
# -------------------------
def main():
    st.set_page_config(page_title="Happiest Birthday GB Babai", layout="wide")
    st.markdown(style, unsafe_allow_html=True)
    inject_global_css()

    # Floating icons
    st.markdown(f"""
        <img id="icon1" class="float-icon" src="{icon_bday}">
        <img id="icon2" class="float-icon" src="{icon_tree}">
        <img id="icon3" class="float-icon" src="{icon_gift}">
        <img id="icon4" class="float-icon" src="{icon_star}">
    """, unsafe_allow_html=True)

    st.title("✨ Happiest Birthday GB Babai!✨")

    birthday_section()
    christmas_section()
    arrival_section()
    footer()


if __name__ == "__main__":
    main()
