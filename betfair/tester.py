from betfair import dbReader

quotes = dbReader.handle.get_quotes(1.129426476, 'Arsenal')

print quotes