import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")

with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作","家庭", "家庭","朋友"])

#建立三個不等寬的欄位：左欄放輸入(1)、中欄放看板(2)、右欄放設定(1.2)

col_left, col_center, col_right = st.columns([1, 2, 1.2], gap="large")

with col_left: 
    with st.container(border=True):     
        st.write("行程描述") 

    title = st.text_input("行程主旨",placeholder="請填寫會議名稱...")

    meeting_time = st.time_input("選擇時間")    

    txt = st.text_input("時間：09:00")
    @dialog("新增完成")
    def showAdd():        
        st.write(f"新增行程{txt} 成功")
    showAdd() 
    st.button("按鈕放左邊")
    
with col_center: 
    st.write("###  看板區")
    st.info("主要行程訊息放中間")
    
with col_right: 
    st.write("###  行程檢視")
    tab1 , tab2 , =st.tabs(["本月行程" , "已封存的行程"])

with tab1:    
    with st.container(border=ture):
        st.write("本月行程")
with tab2:    
    with st.container(border=ture):
        st.write("已封存的行程")

st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")        
st.button("按鈕 A")
st.write("")   #塞入一哥空白間距
st.button("按鈕 B")
        





with st.expander("查看進階提醒參數設定"):
    st.write("這裡是發信伺服器的底層設定...")
