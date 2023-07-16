import streamlit as st
from streamlit_lottie import st_lottie

from extractor import *

if 'state' not in st.session_state:  # THIS IS DONE TO AVOID THE RESET SCENARIO WHEN RESETS OCCUR
    st.session_state['state'] = {
        'submit_state':False
    }

with st.sidebar:  # STORING USER DATA TO HOLD TIMESTAMPS OF USAGE
    st.header("Enter User Details:")
    name = st.text_input("User name")
    reg_id = st.text_input("User id")
    submit_state = st.button("Submit")
    if submit_state:
        st.session_state['state']['submit_state'] = True  # SETTING A SESSION STATE SO THAT A RESET DOESN'T OCCUR

if st.session_state['state']['submit_state']:
    column1, column2 = st.columns(2)
    with column1:  # BOT INTRO
        st.header("SHARE_MARKET_BUD")
        st.write("Hello, I am your Stock Market Buddy, here to assist you with all things related to the stock market.")
        confidence = st.slider("How confident are you with the share Market", min_value=0, max_value=10)

        option = st.selectbox("What would you like to do?",
                              ("View Share Details", "View Company Details", "Buy/Sell Shares"))

        if option == "View Share Details":  # CHOICE THAT THE USER NEEDS
            cmp_index = st.text_input("Enter the index of the share")
            if st.button("View Details"):
                share_data = company_stock_values(cmp_index)  # LOADING IN VALUES USING EXTRACTOR
                st.write("Share Details:")
                st.write(share_data)

                if len(share_data) > 0:  # CHECK IF DATA IS LOADED
                    current_price = share_data['Close'][-1]
                    price_last_week = share_data['Close'][0]
                    if current_price > price_last_week:  # PRICES ARE COMPARED
                        st.write("OLD PRICE :", price_last_week)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_last_week - current_price)
                        st.write("The price has increased since a week ago.")
                    elif current_price < price_last_week:
                        st.write("OLD PRICE :", price_last_week)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_last_week - current_price)
                        st.write("The price has decreased since a week ago.")
                    else:
                        st.write("OLD PRICE :", price_last_week)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_last_week - current_price)
                        st.write("The price has not changed since a week ago.")
                else:
                    st.write("No data available for the share.")  # DATA MISSING

        elif option == "View Company Details":  # COMPANY DETAILS ARE SHOWN TO THE USER
            cmp_index = st.text_input("Enter the index of the company")
            if st.button("View Details"):
                company_info = company_data(cmp_index)
                st.write("Company Details:")
                st.write(company_info)

        elif option == "Buy/Sell Shares":
            cmp_index = st.text_input("Enter the index of the share")
            if st.button("Check Price"):
                share_data = company_stock_values(cmp_index)  # COMPANY DATA IS LOADED AS PER THE INDEX PROVIDED
                if len(share_data) > 0 and len(share_data['Close']) > 11:
                    prices = share_data['Close']
                    price_10_days_ago = prices[-11]
                    current_price = prices[-1]
                    if current_price > price_10_days_ago:
                        st.write("OLD PRICE :", price_10_days_ago)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_10_days_ago - current_price)
                        st.write("You should consider selling the share.")
                    elif current_price < price_10_days_ago:
                        st.write("OLD PRICE :", price_10_days_ago)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_10_days_ago - current_price)
                        st.write("You should consider buying the share.")
                    else:
                        st.write("OLD PRICE :", price_10_days_ago)
                        st.write("NEW PRICE :", current_price)
                        st.write("SHARE PRICE DIFF (OLD - CURRENT) :", price_10_days_ago - current_price)
                        st.write("I'd say let's hold on to the shares for now.....the market did not change a lot")
                else:
                    st.write("Insufficient data available to perform price comparison.")  # LACK OF DATA

    with column2:
        st_lottie("https://assets2.lottiefiles.com/packages/lf20_ab0pxvgc.json")  # LOTTIE
