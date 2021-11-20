import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


#df = pd.read_csv("final_TBBT.csv")

st.title("THE BIG BANG THEORY")
st.header("Who is your favourite character?")
st.header("Let's see what data has to say...")

filter = ["Series 01",
          "Series 02",
          "Series 03",
          "Series 04",
          "Series 05",
          "Series 06",
          "Series 07",
          "Series 08",
          "Series 09",
          "Series 10",
          "Overall"]

selected_filter = st.selectbox("Choose any series number or overall",sorted(filter))

def create_df(selected_filter):
    df = pd.read_csv("new_TBBT.csv")
    if selected_filter != 'Overall':
        df = df[df['series_num'] == selected_filter]
    return df


if st.button("Show Analysis"):
    df_got = create_df(selected_filter)
    df_new = df_got.groupby('person_scene').agg(
        {'series_num': 'count', 'num_lines': 'sum', 'num_words': 'sum'}).sort_values(['series_num'],
                                                                                     ascending=False).reset_index().head(10)
    df_new_lines = df_got.groupby('person_scene').agg(
        {'series_num': 'count', 'num_lines': 'sum', 'num_words': 'sum'}).sort_values(['num_lines'],
                                                                                     ascending=False).reset_index().head(10)
    df_new_words = df_got.groupby('person_scene').agg(
        {'series_num': 'count', 'num_lines': 'sum', 'num_words': 'sum'}).sort_values(['num_words'],
                                                                                     ascending=False).reset_index().head(10)
    st.header("Who got the screen appearances more:")
    col1,col2 = st.columns(2)
    with col1:
        st.header("In {}".format(selected_filter))
        fig,ax = plt.subplots()
        ax.barh(df_new['person_scene'],df_new['series_num'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col2:
        fig,ax = plt.subplots()
        ax.pie(df_new['series_num'].head(7),labels=df_new['person_scene'].head(7),autopct="%0.2f")
        st.pyplot(fig)

    st.header("Who got the lines more:")
    col3,col4 = st.columns(2)
    with col3:
        st.header("In {}".format(selected_filter))
        fig,ax = plt.subplots()
        ax.barh(df_new_lines['person_scene'], df_new_lines['num_lines'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    with col4:
        fig, ax = plt.subplots()
        ax.pie(df_new_lines['num_lines'].head(7), labels=df_new_lines['person_scene'].head(7), autopct="%0.2f")
        st.pyplot(fig)

    st.header("Who got the words more:")
    col5,col6 = st.columns(2)
    with col5:
        st.header("In {}".format(selected_filter))
        fig, ax = plt.subplots()
        ax.barh(df_new_words['person_scene'], df_new_words['num_words'], color='blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col6:
        fig, ax = plt.subplots()
        ax.pie(df_new_words['num_words'].head(7), labels=df_new_words['person_scene'].head(7), autopct="%0.2f")
        st.pyplot(fig)



    st.header("Data has its own fav characters....who is yours...")
    st.header("Happy Learning")





