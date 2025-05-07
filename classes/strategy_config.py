import toml

class StrategyConfig:
    
    def __init__(self, config_file):
        
        self.config = self.load_config(config_file)
        
        # Set default values for certain parameters
        self.trade_params = {
            'capital': self.config.get('trade', {}).get('capital', 10000),
            'risk': self.config.get('trade', {}).get('risk', 1),
            'reward': self.config.get('trade', {}).get('reward', 3),
            'parallel_trades': self.config.get('trade', {}).get('parallel_trades', 1),
            'trade_delay': self.config.get('trade', {}).get('trade_delay', 0)
        }
        
        self.symbol_params = {
            'name': self.config.get('symbol', {}).get('name', 'BTCUSDT'),
            'timeframe': self.config.get('symbol', {}).get('timeframe', '1m'),
            'start_date': self.config.get('symbol', {}).get('start_date', '2020-01-01'),
            'end_date': self.config.get('symbol', {}).get('end_date', '2100-01-01')
        }
        
        self.indicators = self.config.get('indicators.1m', {})
    
    def load_config(self, config_file):
        return toml.load(config_file)
    
    def get_trade_params(self):
        return self.trade_params
    
    def get_symbol_params(self):
        return self.symbol_params
    
    def get_indicators(self):
        return self.indicators