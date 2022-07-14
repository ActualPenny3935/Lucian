import hikari
import lightbulb

plugin = lightbulb.Plugin('help')

@plugin.command()
@lightbulb.command("help", "Help")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Help!", description="""If you would like more information we recomend that you join the [support server](https://discord.gg/Z4kXXz8Y7T)
                         and we can help you with questions or concerncs.
                         
                         Note: We highly recomend that you look at `/recommendations` as this can help optimize the bot in the server and help the bot 
                         work best with what you would wan't.""", color= 0xC1C806)
    embed.add_field("Staff", "/kick\n/ban\n/unban\n/timeout\n/snipe", inline=True)
    embed.add_field("Usefull", "/support\n/bug\n/invite\n/ping\n/uptime", inline=True)
    embed.add_field("Setup", "/recomendations\n/permissions\n")
    embed.set_footer(f"Requested by {ctx.user}")
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
