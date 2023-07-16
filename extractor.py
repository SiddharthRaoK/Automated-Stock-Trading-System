import yfinance as yf


def get_data(cmp_index):  # USING THE API TO LOAD THE DATA
    index = yf.Ticker(cmp_index)
    data = index.info
    return data


def company_data(index):  # NEEDED DATA IS LOADED FOR THE DETAILS
    data = get_data(index)
    info = [
        data['address1'],
        data['city'],
        data['state'],
        data['zip'],
        data['country'],
        data['phone'],
        data['website'],
        data['industry'],
        data['industryDisp'],
        data['sector'],
        data['longBusinessSummary']
    ]
    return info


def company_stock_values(index):  # PRICES ARE LOADED FOR THE 3 MONTH TIME PERIOD FOR LATER COMPARISON
    index = yf.Ticker(index)
    data = index.history(period="3mo")
    return data
