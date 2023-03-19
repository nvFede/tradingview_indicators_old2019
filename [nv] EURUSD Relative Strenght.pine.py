study(title='[nv] EURUSD Distance Comparative Strenght Index', overlay=false)

fast_ema_input = input(defval=21, title = 'Fast Line', type=integer)
slow_ema_input = input(defval=26, title = 'Slow Line', type=integer)

EURUSD = security('EURUSD', period, close)
EURGBP = security('EURGBP', period, close)
EURAUD = security('EURAUD', period, close)
EURJPY = security('EURJPY', period, close)
EURCHF = security('EURCHF', period, close)
EURCAD = security('EURCAD', period, close)
EURNZD = security('EURNZD', period, close)

USDEUR = security('USDEUR', period, close)
USDGBP = security('USDGBP', period, close)
USDAUD = security('USDAUD', period, close)
USDJPY = security('USDJPY', period, close)
USDCHF = security('USDCHF', period, close)
USDCAD = security('USDCAD', period, close)
USDNZD = security('USDNZD', period, close)


EURUSD_EMA_FAST = ema(EURUSD, fast_ema_input)
EURGBP_EMA_FAST = ema(EURGBP, fast_ema_input)
EURAUD_EMA_FAST = ema(EURAUD, fast_ema_input)
EURJPY_EMA_FAST = ema(EURJPY, fast_ema_input)
EURCHF_EMA_FAST = ema(EURCHF, fast_ema_input)
EURCAD_EMA_FAST = ema(EURCAD, fast_ema_input)
EURNZD_EMA_FAST = ema(EURNZD, fast_ema_input)

USDEUR_EMA_FAST = ema(USDEUR, fast_ema_input)
USDGBP_EMA_FAST = ema(USDGBP, fast_ema_input)
USDAUD_EMA_FAST = ema(USDAUD, fast_ema_input)
USDJPY_EMA_FAST = ema(USDJPY, fast_ema_input)
USDCHF_EMA_FAST = ema(USDCHF, fast_ema_input)
USDCAD_EMA_FAST = ema(USDCAD, fast_ema_input)
USDNZD_EMA_FAST = ema(USDNZD, fast_ema_input)




EUR_close = ( EURUSD+ EURGBP+ EURAUD+ EURJPY+ EURCHF+ EURCAD+ EURNZD ) / 7
EUR_fast_ema = ( EURUSD_EMA_FAST + EURGBP_EMA_FAST + EURAUD_EMA_FAST + EURJPY_EMA_FAST + EURCHF_EMA_FAST + EURCAD_EMA_FAST + EURNZD_EMA_FAST ) / 7
EUR_distance = sma(EUR_close - EUR_fast_ema,5)

USD_close = ( USDEUR+ USDGBP+ USDAUD+ USDJPY+ USDCHF+ USDCAD+ USDNZD ) / 7
USD_fast_ema = ( USDEUR_EMA_FAST + USDGBP_EMA_FAST + USDAUD_EMA_FAST + USDJPY_EMA_FAST + USDCHF_EMA_FAST + USDCAD_EMA_FAST + USDNZD_EMA_FAST ) / 7
USD_distance = sma(USD_close - USD_fast_ema, 5)

plot_EUR = plot (EUR_distance, linewidth=2, title='Euro', color=red )
plot_USD = plot (USD_distance, linewidth=2, title='Dollar', color=green )

