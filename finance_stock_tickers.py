import os
from datetime import datetime, timedelta
from os import system, name
import pandas as pd
from numpy import integer
import yfinance as yahooFinance
import matplotlib.pyplot as plt

from python_port_apis.date_time_util_functions import current_time_now


class StockTicker:
    def __init__(self, incvsfile, outputfile, out_type):
        self.filename = incvsfile
        self.data = pd.read_csv(self.filename)
        self.outfile = outputfile + '.' + out_type
        self.out_text = outputfile + '.' + 'txt';
        self.out_dbg_text = outputfile + '_dbg.' + 'txt';
        self.div_end = 3;  # 3% divend
        self.div_years = 5;
        self.ipo_years = 10;
        self.stk_beta = 1.5;
        self.market_cap = 1000000;
        self.stk_sector_dict = {}
        self.stk_industry_dict = {}
        self.stk_symbol_dict = {}
        self.stk_ipo_year_data_dict = {}
        self.stk_country_data_dict = {}
        self.stk_corp_data_dict = {}
        self.stk_cap_data_dict = {}
        self.stock_symbol_selected = {}
        self.stock_no_ipo_candidate = {}
        self.stock_new_ipo_candidate = {}

    def print_data(self):
        print(self.data)

    def print_stock_selected_dict(self):
        print("top selected stocks:", len(self.stock_symbol_selected))
        print(self.stock_symbol_selected)
        print("new IPO stocks:", len(self.stock_new_ipo_candidate))
        print(self.stock_new_ipo_candidate)
        print("Missing IPO info stocks:", len(self.stock_no_ipo_candidate))
        print(self.stock_no_ipo_candidate)

    def build_stk_dict(self, dataframe, store_dict):
        data_list = dataframe.to_records(index=True, column_dtypes=dict, index_dtypes=None)
        for data_item in range(0, len(data_list)):
            data_str = data_list[data_item]
            store_dict[data_str[0]] = data_str[1]

    def mod_stk_select_param(self, div_end, div_years, ipo_years, market_cap):
        self.div_end = div_end;  # 3% divend
        self.div_years = div_years;
        self.ipo_years = ipo_years;
        self.market_cap = market_cap;

    def stk_all_info_table(self):
        sector_data = self.data.loc[:, ['Sector']]
        df = pd.DataFrame(data=sector_data)
        self.build_stk_dict(df, self.stk_sector_dict)

        industry_data = self.data.loc[:, ['Industry']]
        df = pd.DataFrame(data=industry_data)
        self.build_stk_dict(df, self.stk_industry_dict)

        stk_ipo_year_data = self.data.loc[:, ['IPO Year']]
        df = pd.DataFrame(data=stk_ipo_year_data)
        self.build_stk_dict(df, self.stk_ipo_year_data_dict)

        stk_market_cap_data = self.data.loc[:, ['Market Cap']]
        df = pd.DataFrame(data=stk_market_cap_data)
        self.build_stk_dict(df, self.stk_cap_data_dict)

        stk_country_data = self.data.loc[:, ['Country']]
        df = pd.DataFrame(data=stk_country_data)
        self.build_stk_dict(df, self.stk_country_data_dict)

    def process_stock_csv(self):
        out_data = self.data.loc[:, ['Symbol', 'Name', 'Sector', 'Industry', 'Country', 'Market Cap', 'IPO Year']]
        out_file_name = self.out_text
        d_dir = os.path.dirname(out_file_name)
        if not os.path.isdir(d_dir):
            os.mkdir(os.path.dirname(out_file_name))
        with open(out_file_name, 'w', encoding="utf8") as fulltext:
            df = pd.DataFrame(data=out_data)
            df.to_csv(out_file_name, na_rep='(missing)')
        fulltext.close()

    def stk_ticker_build_dict(self):
        # stk_table_list = df.
        sym_data = self.data.loc[:, ['Symbol']]
        df = pd.DataFrame(data=sym_data)
        print("Total stock in NASDAQ:", len(df) - 1)
        self.build_stk_dict(df, self.stk_symbol_dict)

    # show options expirations
    def stock_rt_option_show(self, yf_ticker_sym):
        opt_expiration_list = yf_ticker_sym.option()
        print(opt_expiration_list)

    # show sustainability
    def stock_sustainability(self, yf_ticker_sym):
        stock_sustainability = yf_ticker_sym.sustainability
        print(stock_sustainability)

    def stock_finance_status(self, yf_ticker_sym):
        # show cashflow
        cash_gen_flow = yf_ticker_sym.cashflow
        cash_qt_flow = yf_ticker_sym.quarterly_cashflow
        print("Overall Cash FLOW")
        print(cash_gen_flow)
        print("Quarterly Cash Flow")
        print(cash_qt_flow)
        # show major holders
        major_holders = yf_ticker_sym.major_holders
        # show institutional holders
        institution_holders = yf_ticker_sym.institutional_holders
        print(major_holders)
        print(institution_holders)
        # show earnings
        print(yf_ticker_sym.earnings)
        print(yf_ticker_sym.quarterly_earnings)

    def stock_event_calender(self, yf_ticker_sym):
        # show next event (earnings, etc)
        stk_event_sch = yf_ticker_sym.calendar
        print(stk_event_sch)

    # get option chain for specific expiration
    def stock_rt_option_selected(self, expiration_date, yf_ticker_sym):
        opt = yf_ticker_sym.option_chain(expiration_date)
        print(opt)

                                                                          # evaluate the growth and dividend healthy index
    def stock_growth_dividend_eval(self, yf_ticker_sym, cut_off_date):
        stk_dividend = yf_ticker_sym.dividends
        finance_info = yf_ticker_sym.info
        stk_earning_growth = finance_info["earningsGrowth"]
        dividend_pay_ratio = finance_info["payoutRatio"]
        if dividend_pay_ratio is None:
            dividend_pay_ratio = 10
        dividends_date = stk_dividend.index
        cur_dividend = 0
        last_dividend = 0
        dividend_points = 10
        for dividend_index in range(0, len(stk_dividend)):
            if dividends_date[dividend_index] >= cut_off_date:
                if stk_dividend[dividend_index] < cur_dividend:
                    dividend_points -= 1
                cur_dividend = stk_dividend[dividend_index]
                last_dividend = stk_dividend[dividend_index]
        hist_price = finance_info["currentPrice"]
        if hist_price == 0:
            hist_price = finance_info["regularMarketPrice"]
        if hist_price == 0:
            hist_price = finance_info["twoHundredDayAverage"]
        if hist_price != 0 and dividend_pay_ratio != 0:
            return float(dividend_points)/dividend_pay_ratio, last_dividend/hist_price
        else:
            return dividend_points, 0

        # data = yf.download('QCOM', '2020-01-01', '2021-10-15')
        # Plot the close prices
        # data["Adj Close"].plot()
        # plt.show()
        # evaluate the growth and dividend healthy index

    def stock_long_short_eval(self, yf_ticker_sym, cut_off_date):
        stk_dividend = yf_ticker_sym.dividends
        finance_info = yf_ticker_sym.info
        dividend_pay_ratio = finance_info["payoutRatio"]
        if dividend_pay_ratio is None:
            dividend_pay_ratio = 10
        dividends_date = stk_dividend.index
        cur_dividend = 0
        last_dividend = 0
        dividend_points = 10
        for dividend_index in range(0, len(stk_dividend)):
            if dividends_date[dividend_index] >= cut_off_date:
                if stk_dividend[dividend_index] < cur_dividend:
                    dividend_points -= 1
                cur_dividend = stk_dividend[dividend_index]
                last_dividend = stk_dividend[dividend_index]
        hist_price = finance_info["currentPrice"]
        if hist_price == 0:
            hist_price = finance_info["regularMarketPrice"]
        if hist_price == 0:
            hist_price = finance_info["twoHundredDayAverage"]
        if hist_price != 0 and dividend_pay_ratio != 0:
            return float(dividend_points) / dividend_pay_ratio, last_dividend / hist_price
        else:
            return dividend_points, 0

        # data = yf.download('QCOM', '2020-01-01', '2021-10-15')
        # Plot the close prices
        # data["Adj Close"].plot()
        # plt.show()
    def stock_static_selected_dict(self):
        self.stk_all_info_table()
        self.stk_ticker_build_dict()
        for sym_item in self.stk_symbol_dict:
            var_str = self.stk_country_data_dict.get(sym_item)
            if var_str == "China":
                continue
            var_str = self.stk_sector_dict.get(sym_item)
            if var_str == '':
                continue
            var_str = self.stk_industry_dict.get(sym_item)
            if var_str == '':
                continue
            var_str = self.stk_ipo_year_data_dict.get(sym_item)
            try:
                ipo_year_int = int(var_str)
            except ValueError:
                self.stock_no_ipo_candidate[self.stk_symbol_dict.get(sym_item)] = sym_item
                continue
            if (2022 - ipo_year_int) < self.ipo_years:
                self.stock_new_ipo_candidate[self.stk_symbol_dict.get(sym_item)] = sym_item
                continue
            var_str = self.stk_cap_data_dict.get(sym_item)
            if var_str == '':
                continue
            if (int(var_str) / 10000) < self.market_cap:
                continue
            self.stock_symbol_selected[self.stk_symbol_dict.get(sym_item)] = sym_item

        # self.print_stock_selected_dict()

    def stock_semi_static_selected(self):
        ticker_count = 0
        for stock_sym in self.stock_symbol_selected:
            #print(type(stock_sym), stock_sym)
            ticker_count += 1
        for stock_sym in self.stock_no_ipo_candidate:
            #print(type(stock_sym), stock_sym)
            ticker_count += 1
            #print(stock_sym_info.dividends)
        print("Total tick get ", ticker_count)

    def stock_selected_quality(self, tick_str, stock_sym_info):
        time_date = current_time_now().date() - timedelta(days=(10 * 365))
        date_only = '{0:%Y-%m-%d}'.format(time_date)
        dividend_index, dividend_rate = self.stock_growth_dividend_eval(stock_sym_info, pd.Timestamp(time_date))
        dividend_rate = round(dividend_rate * 400, 2)
        dividend_index = round(dividend_index, 2)
        if dividend_index > 10 and dividend_rate > 2.5:
            print("{}, stock quality:{}, annual dividend: {}{}".format(tick_str, dividend_index, dividend_rate, "%"))
            return True
        else:
            print("{}, stock quality:{}, annual dividend: {}{}".format(tick_str, dividend_index, dividend_rate, "%"))
            return False

    def stock_qualified_selected(self):
        for stock_sym in self.stock_symbol_selected:
            stock_sym_info = yahooFinance.Ticker(stock_sym)
            stock_sym_content = stock_sym_info.info
            # self.stock_sustainability(stock_sym_info)
            if self.stock_selected_quality(stock_sym, stock_sym_info):
                company_name = stock_sym_content['shortName']
                sector_str = stock_sym_content['sector']
                industry_str = stock_sym_content['industry']
                web_site_str = stock_sym_content['website']
                print("Stock:{}, company:{}, sector:{}, industry:{}, web site:{}".format(stock_sym, company_name, sector_str, industry_str, web_site_str))

    def stock_single_selected(self):
        stock_sym = "TXN"
        stock_sym_info = yahooFinance.Ticker(stock_sym)
        stock_sym_content = stock_sym_info.info
        print(stock_sym_content)
        self.stock_sustainability(stock_sym_info)
        company_name = stock_sym_content['shortName']
        sector_str = stock_sym_content['sector']
        industry_str = stock_sym_content['industry']
        web_site_str = stock_sym_content['website']
        self.stock_selected_quality(stock_sym, stock_sym_info)
        print("Stock:{}, company:{}, sector:{}, industry:{}, web site:{}".format(stock_sym, company_name, sector_str, industry_str, web_site_str))
