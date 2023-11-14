import streamlit as st
import pandas as pd
import numpy as np

# 添加标题
st.title('我的 Streamlit 应用')

# 添加文本
st.write('这是一个简单的 Streamlit 应用。')

# 添加图表
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 添加地图
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# 添加交互式小部件
if st.checkbox('显示DataFrame'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.write(chart_data)

