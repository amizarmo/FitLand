import streamlit as st
import pandas as pd
import plotly.express as px

tab1, tab2, tab3 = st.tabs(['Introduction',
                            'Dense Neural Net',
                            'Recurrent Neural Net'])

with tab1:
    st.title('Fitness Lanscape Exploration')
    st.write(
    """
    embedding from a dense neural network are mapped to the real fitness values.
    this network was trained on the PAX3 TF fitness landscape.
    you can chosse different TFs fitness landscapes to observe in the same embedding
    """
    )

with tab2:
    df = pd.read_csv('ANN_2l_PAX3.csv', index_col=0)
    #df.melt(id_vars=['PAX3','PAX4','HOXB7','HOXC4','KLF1','GFI1B','BCL6'])

    tfs = st.multiselect('what TFs to show for ANN embedding',
                        ['PAX3','PAX4','HOXB7','HOXC4','KLF1','GFI1B','BCL6'],
                        'PAX3')

    temp = df[['x','y']+tfs]

    df2 = temp.melt(id_vars=['x','y'])

    fig = px.scatter_3d(df2, x='x', y='y', z='value', color='variable',)
    fig.update_traces(marker={'size': 1})
    st.plotly_chart(fig)

with tab3:
    df = pd.read_csv('RNN_1l_PAX3.csv', index_col=0)
    #df.melt(id_vars=['PAX3','PAX4','HOXB7','HOXC4','KLF1','GFI1B','BCL6'])

    tfs = st.multiselect('what TFs to show for RNN embedding',
                        ['PAX3','PAX4','HOXB7','HOXC4','KLF1','GFI1B','BCL6'],
                        'PAX3')

    temp = df[['x','y']+tfs]

    df2 = temp.melt(id_vars=['x','y'])

    fig = px.scatter_3d(df2, x='x', y='y', z='value', color='variable',)
    fig.update_traces(marker={'size': 1})
    st.plotly_chart(fig)