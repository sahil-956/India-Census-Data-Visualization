import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
final_df=pd.read_csv('India.csv')
list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title('Visualise Data')
state_choice=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[5:]))

plot=st.sidebar.button('Plot Graph')
if plot:
    st.text('size represents primary parameter')
    st.text('color represents secondary paramenter')
    if state_choice=='Overall India':
        #plot for india
        fig=px.scatter_mapbox(final_df,lat='Latitude',lon='Longitude',size=primary,
                              color=secondary,color_continuous_scale="Viridis",zoom=4, mapbox_style='carto-positron',
                              height=700,width=700,hover_name='State')
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for state
        state_df=final_df[final_df['State']==state_choice]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary,
                                color=secondary, color_continuous_scale="Viridis", zoom=4,
                                mapbox_style='carto-positron',
                                height=700, width=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)