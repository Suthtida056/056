import streamlit as st

#ตั้งค่าหน้าเว็บไซต์
st.set_page_config(
    page_title = "ระบบจองตั๋วคอนเสิร์ต",
    page_icon = "⛟"
)

#กำหนดราคาตั๋ว
prices = {
    "Standard":100,
    "VIP":250,
    "Premium":400
}

#การแสดงหัวข้อเว็บไซต์
st.title("⛟ระบบจองตํ่วคอนเสิร์ต")
st.write("DIGITAL BOOKING")

st.divider()

#แสดงประเภทตั๋ว
st.subheader("ประเภทตั๋ว")
col1, col2, col3 = st.columns(3)
with col1:
  st.info("Stadard")
  st.write("100")
with col1:
  st.info("VIP")
  st.write("250")
with col1:
  st.info("Premium")
  st.write("400")
st.divider()

#แบบฟอร์มสั่งซื้อ
st.Subheader("แบบฟอร์มสั่งซื้อ")
name = st.text_input("ชื่อผู้ซื้อ")
ticket = st.selectbox(
    "เลือกประเภทตั๋ว"
    ["Stadard","VIP","Premium" ]
)

quantity = st.nuber_input(
    "จำนวนตั๋ว",
    min_value=1,
    max_value=10,
    value=1,
)

#คำนวณราคา
price = prices[ticket]
total = price*quantity

st.write("ราคาต่อตั๋ว:",price,"บาท")
st.write("จำนวน:",price,"ใบ")
st.Subheader(f"ยอดรวม{total:,}บาท")

st.dicider()

#ยืนยันการสั่งซื้อ
if st.button("ยืนยันการสั่งซื้อ"):
  if name == "":
    st.error("กรุณากรอกชื่อผู้ซื้อ")
  else:
    st.success("สั่งซื้อตั๋วเรียบร้อยแล้ว")

    st.Subheader("สรุปคำสั่งซื้อ")
    st.write("ชื้อผู้ซื้อ:",name)
    st.write("ประเทตั๋ว:",ticket)
    st.write("จำนวน:",quantity,"ใบ")
    st.write("ราคาต่อตั๋ว:",price,"บาท")

    st.success(f"ยอดชำระ{total:,}บาท")
st.caption("DIGITAL BOOKINZG")
