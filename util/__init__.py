from .bot import Bot
from .handlers import Handlers
from .checks import Checks

async def setup(bot):
    await bot.add_cog(Util(bot))
