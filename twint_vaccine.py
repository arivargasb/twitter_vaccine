import twint

# Configure
c = twint.Config()
c.Search = "vaccin"
c.Lang = "en"
c.Geo = "37.68636195427385,-97.34987062254712,2000km" 
# c.Limit = 300
c.Output = "./vaccine_us_0720to0121.csv"
# c.Store_json = True
c.Store_csv = True
c.Since= '2020-07-01'
c.Until = '2021-01-05'

# Run
twint.run.Search(c)