import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="Mother's Spice | Gujarati Heritage",page_icon="🥭",layout="wide")
st.markdown("""<style>.stApp{background:#FFF8EE} h1,h2,h3{color:#8D402B!important} .hero{background:#8D402B;color:#fff;padding:3rem;border-radius:24px}.hero h1{color:#fff!important}.tile{background:white;border:1px solid #EAD9C9;border-radius:18px;padding:24px;margin:12px 0} .stApp p,.stApp label,.stApp .stCaption{color:#302720} section[data-testid="stSidebar"] p,section[data-testid="stSidebar"] label,section[data-testid="stSidebar"] h1,section[data-testid="stSidebar"] span{color:#FFFFFF!important} .tile h2,.tile h3,.tile p{color:#302720!important} .hero p{color:#FFFFFF!important} .hero h1{color:#FFFFFF!important} .stButton button,.stLinkButton a{font-weight:600} </style>""",unsafe_allow_html=True)
PRODUCTS = [
("🌿","Traditional Methi Masala","Classic fragrant Gujarati fenugreek spice blend"),
("🥭","Raw Mango & Gunda Pickle","Tangy, spicy raw mango and gunda"),
("🍯","Sweet Raw Mango Pickle (Galyu Athanu)","Sweet and tangy mango pickle"),
("🌶️","Tindora & Mango Pickle","Ivy gourd and mango with traditional spices"),
("🥭","Chhundo","Gujarati sweet-spiced grated mango preserve"),
]
WHATSAPP="https://wa.me/919426725111"
EMAIL="parthiv1971@gmail.com"
def chat(msg):
    st.link_button("💬 Send on WhatsApp",WHATSAPP+"?text="+quote(msg))
with st.sidebar:
    st.title("🌿 Mother's Spice")
    page=st.radio("Explore",["Home","Products","Mango Community","Our Story","Contact & Orders","WhatsApp"])
    st.caption("A Mother's Love in Every Bite")
    st.link_button("Chat with Parthiv",WHATSAPP)
if page=="Home":
    st.markdown('<div class="hero"><h1>Every Jar Tells a Story.</h1><p>Made with a mother’s blessings. Crafted with love. Rooted in Gujarati tradition.</p><p>🥭 India’s flavours. Australia’s table.</p></div>',unsafe_allow_html=True)
    st.header("From our kitchen to your home")
    st.write("Mother’s Spice is the heartfelt vision of Parthiv Shah, inspired by his mother’s cherished recipes.")
    cols=st.columns(3)
    for i,(icon,name,desc) in enumerate(PRODUCTS[:3]):
        with cols[i]:st.markdown(f'<div class="tile"><h2>{icon}</h2><h3>{name}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
elif page=="Products":
    st.title("🥭 Our Products")
    for icon,name,desc in PRODUCTS:
        st.markdown(f'<div class="tile"><h2>{icon} {name}</h2><p>{desc}</p></div>',unsafe_allow_html=True)
    st.info("Prices, allergens, ingredients, jar weights and availability will be confirmed before sales.")
elif page=="Mango Community":
    st.title("🥭 One Mango, Two Homelands")
    st.write("Connecting India and Australia through mangoes, growers, family recipes and community stories.")
    st.markdown('<div class="tile" style="text-align:center;font-size:2rem">🇮🇳 India ━━━ 🥭 ━━━ Australia 🇦🇺</div>',unsafe_allow_html=True)
    a,b=st.columns(2)
    with a:
        st.subheader("🇮🇳 India")
        st.write("Kesar, Alphonso, Totapuri and the Gujarati traditions of chhundo and athanu.")
    with b:
        st.subheader("🇦🇺 Australia")
        st.write("Kensington Pride, R2E2, local growers, mango seasons and home kitchens.")
    st.caption("Illustrative cultural connection, not an import or trade route. A detailed illustrated map is planned.")
    with st.form("story"):
        name=st.text_input("Your name (optional)")
        story=st.text_area("Share a mango memory")
        submitted=st.form_submit_button("Preview story")
    if submitted:
        st.success("Preview only — stories are not stored or posted.")
        st.write(story)
elif page=="Our Story":
    st.title("❤️ The Mother’s Spice Story")
    st.write("For Parthiv Shah, cooking is more than ingredients: it is love, memory and a priceless legacy passed down by his mother.")
    st.write("Her treasured recipes, wisdom and blessings inspire each pickle and spice blend — authentic Gujarati flavours to share across generations.")
    st.markdown("> Made with a Mother’s Blessings, Crafted with Love, Rooted in Tradition.")
elif page=="Contact & Orders":
    st.title("✉️ Contact & Orders")
    st.write("Founder: **Parthiv Shah**")
    st.write("📞 +91 94267 25111 | ✉️ "+EMAIL)
    st.caption("Enquiries only. Orders and payments are not processed on this website.")
    with st.form("enquiry"):
        name=st.text_input("Your name *")
        email=st.text_input("Email (optional)")
        phone=st.text_input("Phone (optional)")
        product=st.selectbox("Product", [p[1] for p in PRODUCTS])
        quantity=st.number_input("Quantity (jars)",min_value=1,value=1)
        message=st.text_area("Message")
        consent=st.checkbox("I agree to share my enquiry via WhatsApp or email.")
        submit=st.form_submit_button("Prepare enquiry")
    if submit:
        if not name.strip() or not consent: st.warning("Please enter your name and confirm consent.")
        else:
            body=f"Hello Parthiv, I would like to enquire about Mother's Spice.\nName: {name}\nEmail: {email}\nPhone: {phone}\nProduct: {product}\nQuantity: {quantity}\nMessage: {message}"
            st.success("Your message is ready. Choose how to send it.")
            chat(body)
            st.link_button("✉️ Send via email","mailto:"+EMAIL+"?subject="+quote("Mother's Spice enquiry")+"&body="+quote(body))
            st.caption("Nothing is stored or sent until you complete the message in your chosen app.")
else:
    st.title("💬 WhatsApp Mother’s Spice")
    st.write("Chat directly with founder Parthiv Shah.")
    for title,msg in [
        ("🥭 View catalogue","Namaste Parthiv, please share the Mother's Spice catalogue and jar sizes."),
        ("💰 Prices & availability","Namaste Parthiv, could you share prices and product availability?"),
        ("🎁 Gift and bulk orders","Namaste Parthiv, I would like to enquire about gifting and bulk orders."),
        ("🌏 Mango community","Namaste Parthiv, tell me more about the India–Australia mango community.")
    ]:
        st.link_button(title, WHATSAPP+"?text="+quote(msg))
st.divider()
st.caption("© Mother’s Spice · Parthiv Shah · Gujarati heritage, shared with love")
