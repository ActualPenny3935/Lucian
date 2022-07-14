import hikari
import lightbulb

plugin = lightbulb.Plugin('license')

@plugin.command()
@lightbulb.command("license", "link to Lucian's lisance")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="lisances", description="We have to lisances The creative commons legal  code and MIT", color=0xC1C806)
    embed.add_field("lisance", "Link to our [lisance](https://docs.google.com/document/d/1nlwZUr41zwB9w5PEs4Q45XLtSMfSkTYtIYR86dGIdj0/edit?usp=sharing)")
    embed.set_footer(f"Requested by {ctx.user}")
    embed.set_thumbnail(ctx.user.avatar_url)
    
    await ctx.respond(embed)
    
def load(bot):
    bot.add_plugin(plugin)
