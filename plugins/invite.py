import hikari
import lightbulb

plugin = lightbulb.Plugin('invite')

@plugin.command()
@lightbulb.command("invite", "sends you an invite for me!")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Lucian", description="Invite me to your server!", color= 0xC1C806)
    embed.add_field("Invite", "[link](https://discord.com/api/oauth2/authorize?client_id=994548521271316530&permissions=1634712677623&scope=bot%20applications.commands)")
    embed.set_footer(f"Requested by {ctx.user}")
    await ctx.respond(embed)  # or respond(embed=embed)
    
def load(bot):
    bot.add_plugin(plugin)