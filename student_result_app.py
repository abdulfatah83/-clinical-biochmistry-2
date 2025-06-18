
import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="منظومة الكيمياء الطبية 2 | د. عبدالفتاح البكوش", 
                   page_icon="🧪", layout="centered")

@st.cache_data
def load_data():
    df = pd.read_excel("قائمة_الطلبة_ML661_ربيع 2025.xlsx", skiprows=12)
    df = df[["رقم القيد", "الاسم", "الاعمال"]]
    df = df.dropna(subset=["رقم القيد"])
    df["رقم القيد"] = df["رقم القيد"].astype(str).str.strip()
    return df

if "page" not in st.session_state:
    st.session_state.page = "home"
if "student_id" not in st.session_state:
    st.session_state.student_id = ""

def main_page():
    st.markdown("""
        <div style="background: linear-gradient(90deg, #2980B9, #6DD5FA); border-radius:18px; padding:32px 18px; box-shadow:0 2px 8px #8882;">
            <h1 style='text-align: center; color: #fff; font-size:2.8rem;'>منظومة الكيمياء الطبية 2</h1>
            <h3 style='text-align: center; color: #fff;'>للأستاذ عبدالفتاح البكوش</h3>
        </div>
        <br>
        <p style='text-align:center; font-size: 1.1rem;'>عزيزي الطالب، يرجى إدخال رقم القيد الخاص بك للبحث عن نتيجتك في أعمال السنة.</p>
    """, unsafe_allow_html=True)

    student_id = st.text_input("🔎 رقم القيد:", placeholder="أدخل رقم القيد هنا...", key="input_id")
    btn_search = st.button("دخول", use_container_width=True, type="primary")

    if btn_search:
        if not student_id.strip():
            st.warning("يرجى إدخال رقم القيد.")
        else:
            st.session_state.student_id = student_id.strip()
            st.session_state.page = "result"

def result_page():
    data = load_data()
    student_id = st.session_state.student_id
    result = data[data["رقم القيد"] == student_id]

    st.markdown("""
        <div style="background: linear-gradient(90deg, #2980B9, #6DD5FA); border-radius:16px; padding:20px 12px; box-shadow:0 2px 6px #8882;">
            <h2 style='text-align: center; color: #fff;'>منظومة الكيمياء الطبية 2</h2>
            <h4 style='text-align: center; color: #fff;'>الأستاذ عبدالفتاح البكوش</h4>
        </div>
        <br>
    """, unsafe_allow_html=True)

    if not result.empty:
        st.success("تم العثور على الطالب!")
        st.markdown(f"""
        <div style='background: #f7fbff; border-radius:14px; padding:28px; box-shadow:0 2px 4px #bbb6; border:1.5px solid #58a;'>
            <h3 style='color:#195;'>👤 الاسم الثلاثي:</h3>
            <p style='font-size:1.5rem; margin-bottom:10px; color:#246;'>{result.iloc[0]['الاسم']}</p>
            <h4 style='color:#195;'>🆔 رقم القيد:</h4>
            <p style='font-size:1.3rem; color:#246;'>{result.iloc[0]['رقم القيد']}</p>
            <h4 style='color:#195;'>📊 درجة النصفي:</h4>
            <p style='font-size:1.3rem; color:#246;'>{result.iloc[0]['الاعمال']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("رقم القيد غير موجود. الرجاء التأكد من صحة الرقم.")

    if st.button("رجوع للصفحة الرئيسية", use_container_width=True):
        st.session_state.page = "home"
        st.session_state.student_id = ""

if st.session_state.page == "home":
    main_page()
elif st.session_state.page == "result":
    result_page()
