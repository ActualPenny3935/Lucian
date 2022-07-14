import hikari
import lightbulb

plugin = lightbulb.Plugin('user-info')

@plugin.command()
@lightbulb.command("user-info", "gets info on a user.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context)-> None:
    target = ctx.user
    embed = hikari.Embed(title="User information", description=f"Displaying information for {ctx.user.mention}", color= 0xC1C806)
    embed.set_footer(f"Requested by {ctx.user}")
    embed.set_thumbnail(ctx.user.avatar_url)
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
