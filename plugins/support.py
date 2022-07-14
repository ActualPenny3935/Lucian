import hikari
import lightbulb

plugin = lightbulb.Plugin('support')

@plugin.command()
@lightbulb.command("support", "Get an invite to the support server!")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Support server", description="Here is the link to my support server\nSupport response time may varry from 1-48 hours.", color= 0xC1C806)
    embed.add_field("Invite", "[link](https://discord.gg/Z4kXXz8Y7T)")
    embed.set_footer(f"Requested by {ctx.user}")
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
