import hikari
import lightbulb

plugin = lightbulb.Plugin('builder')

@plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("footer", "the footer of the embed.", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("image", "the image of the embed.(link)", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("thumbnail", "the thumbnail of the embed.(link)", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("field_content", "content of the field.", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("field_name", "name of the field.", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("embed_color", "HEX COLOR", required=False, type=hikari.OptionType.STRING)
@lightbulb.option("user", "optional... user to DM this to", required=False, type=hikari.OptionType.USER)
@lightbulb.option("description", "the description of the embed", required=True, type=hikari.OptionType.STRING)
@lightbulb.option("title", "the title of the embed.", required=True, type=hikari.OptionType.STRING)   
@lightbulb.command("builder", "lets you build an embed")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    channel_id = ctx.channel_id
    embed = hikari.Embed(title=f"{ctx.options.title}", description=f"{ctx.options.description}")
    if str(ctx.options.embed_color) != "None":
        embed.color = (f"{ctx.options.embed_color}")
    if str(ctx.options.field_name) != "None" and str(ctx.options.field_content) != "None":
        embed.add_field(f"{ctx.options.field_name}", f"{ctx.options.field_content}")
    if str(ctx.options.set_thumbnail) != "None":
        embed.set_thumbnail(f"{ctx.options.thumbnail}")
    if str(ctx.options.image) != "None":
        embed.set_image(f"{ctx.options.image}")
    if str(ctx.options.footer) != "None":
        embed.set_footer(f"{ctx.options.footer}")
    if str(ctx.options.user) != "None":
        this_dm_channel = await plugin.rest.create_dm_channel(ctx.options.user)
        await plugin.rest.create_message(this_dm_channel,embed)
    else:
        await plugin.rest.create_message(channel_id,embed)
    await ctx.respond("Your message has been created!", flags=hikari.MessageFlag.EPHEMERAL)

def load(bot):
    bot.add_plugin(plugin)