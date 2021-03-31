# A single source of truth for constant variables related to the exchange
class Constants:
    """
    API Documentation Links:
    https://api-docs.coinzoom.com/
    https://api-markets.coinzoom.com/
    """
    EXCHANGE_NAME = "coinzoom"
    REST_URL = "https://api.coinzoom.com/api/v1/public"
    # REST_URL = "https://api.stage.coinzoom.com/api/v1/public"
    WS_PRIVATE_URL = "wss://api.coinzoom.com/api/v1/public/market/data/stream"
    # WS_PRIVATE_URL = "wss://api.stage.coinzoom.com/api/v1/public/market/data/stream"
    WS_PUBLIC_URL = "wss://api.coinzoom.com/api/v1/public/market/data/stream"
    # WS_PUBLIC_URL = "wss://api.stage.coinzoom.com/api/v1/public/market/data/stream"

    HBOT_BROKER_ID = "CZ_API_HBOT"

    ENDPOINT = {
        # Public Endpoints
        "TICKER": "marketwatch/ticker",
        "SYMBOL": "instruments",
        "ORDER_BOOK": "marketwatch/orderbook/{trading_pair}/150/2",
        "ORDER_CREATE": "orders/new",
        "ORDER_DELETE": "orders/cancel",
        "ORDER_STATUS": "orders/list",
        "USER_ORDERS": "orders/list",
        "USER_BALANCES": "ledger/list",
    }

    WS_SUB = {
        "TRADES": "TradeSummaryRequest",
        "ORDERS": "OrderBookRequest",
        "USER_ORDERS_TRADES": "OrderUpdateRequest",

    }

    WS_METHODS = {
        "ORDERS_SNAPSHOT": "ob",
        "ORDERS_UPDATE": "oi",
        "TRADES_UPDATE": "ts",
        "USER_BALANCE": "getTradingBalance",
        "USER_ORDERS": "OrderResponse",
        "USER_ORDERS_CANCEL": "OrderCancelResponse",
    }

    # Timeouts
    MESSAGE_TIMEOUT = 30.0
    PING_TIMEOUT = 10.0
    API_CALL_TIMEOUT = 10.0
    API_MAX_RETRIES = 4

    # Intervals
    # Only used when nothing is received from WS
    SHORT_POLL_INTERVAL = 5.0
    # CoinZoom poll interval can't be too long since we don't get balances via websockets
    LONG_POLL_INTERVAL = 8.0
    # One minute should be fine for order status since we get these via WS
    UPDATE_ORDER_STATUS_INTERVAL = 60.0
    # 10 minute interval to update trading rules, these would likely never change whilst running.
    INTERVAL_TRADING_RULES = 600
