class basic_chart:
  
    def __init__(self, ticker, period, interval):
        import yfinance as yf
        
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.data = yf.download(
            self.ticker,
            period=self.period,
            interval=self.interval,
            group_by="ticker"
        ).dropna()

    def show(self):
        import pandas as pd
        import plotly.graph_objects as go
        
        # Fix: use self.data instead of data
        if isinstance(self.data.columns, pd.MultiIndex):
            self.data.columns = self.data.columns.droplevel(0)

        fig = go.Figure(data=[go.Candlestick(
            x=self.data.index,
            open=self.data['Open'],
            high=self.data['High'],
            low=self.data['Low'],
            close=self.data['Close']
        )])

        fig.update_layout(
            title=f"{self.ticker} Candlestick Chart ({self.period})",
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            xaxis_rangeslider_visible=False
        )

        fig.show()
        return fig   # return the figure object instead of None


a=basic_chart(ticker="BTC-USD", period="100d", interval="1d")

print(a.show())