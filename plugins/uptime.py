import hikari
import lightbulb
import datetime

plugin = lightbulb.Plugin('uptime')

@plugin.command()
@lightbulb.command("uptime", "Gets how long the bot has been online for.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    uptime = round(ctx.app.d.uptime.timestamp())
    full_dt = f"<t:{uptime}:F>"
    relative_dt = f"<t:{uptime}:R>"
    embed = hikari.Embed(title="Up time", description=f"Time: {full_dt} {relative_dt}")
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
