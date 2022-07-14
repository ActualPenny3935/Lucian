import hikari
import lightbulb

plugin = lightbulb.Plugin('recomendations')

@plugin.command()
@lightbulb.command("recomendations", "gives you our recomendations." )
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.context) -> None:
    embed = hikari.Embed(title="Our recomendations", description="We recomend that you take a look at the commands that have **permmision** locks with `/permmisions`.", color= 0xC1C806)
    embed.add_field("Suggest", "We recomend that you you set your `suggestions` channel to were only staff and the bot can send messages in it.\nTo recive the suggestion message you need to set the suggestion channel with `/set_suggestions_channel`")
    embed.add_field("Permmisions", "We recomend that you check out what commands have permmisions are required on what commands with `/permmisions`.")
    embed.set_footer(f"Requested by {ctx.user}")
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
