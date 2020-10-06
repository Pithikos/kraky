import asyncio
import pytest

from kraky import KrakyApiClient, KrakyWsClient


kraky_api_client = KrakyApiClient()
kraky_ws_client = KrakyWsClient()


class TestKrakyApiClient:

    @pytest.mark.asyncio
    async def test_get_last_price(self):
        result = await kraky_api_client.get_last_price("xbtusd")
        assert isinstance(result, float)

    @pytest.mark.asyncio
    async def test_get_ohlc_data(self):
        result = await kraky_api_client.get_ohlc_data("xbtusd", 1)
        assert "last" in result

    @pytest.mark.asyncio
    async def test_get_recent_trades(self):
        result = await kraky_api_client.get_recent_trades("xbtusd")
        assert "last" in result
