
import hikari
import lightbulb
import datetime
import os
import json



bot = lightbulb.BotApp(
    token='TOKEN',
    prefix='.',
    default_enabled_guilds=(992671415419547649))

embed = hikari.Embed()

bot.load_extensions_from('./plugins')

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
 print('Bot has started!')
 bot.d.uptime = datetime.datetime.now(datetime.timezone.utc)
 
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"ERROR: Something went wrong during invocation of command `{event.context.command.name}`.",flags=hikari.MessageFlag.EPHEMERAL)
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception
    print(f"{event.context.author} -- {exception}")
    #await event.context.app.rest.create_message(,content=f"{event.context.author} -- {exception}")

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("ERROR: You are not the owner of this bot.",flags=hikari.MessageFlag.EPHEMERAL)
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"ERROR: This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.",flags=hikari.MessageFlag.EPHEMERAL)
    elif isinstance(exception, lightbulb.MissingRequiredPermission):
        await event.context.respond(f"ERROR: You are missing one or more permissions required in order to run the `{event.context.command.name}` command.",flags=hikari.MessageFlag.EPHEMERAL)
    elif isinstance(exception, lightbulb.MissingRequiredRole):
        await event.context.respond(f"ERROR: You are missing one or more roles required in order to run the `{event.context.command.name}` command.",flags=hikari.MessageFlag.EPHEMERAL)
    else:
        #raise exception
        await event.context.respond("There was an error! If you believe this is a mistake, please inform the server admin",flags=hikari.MessageFlag.EPHEMERAL)
        print(f"Told {event.context.author} to tell you if the error was a mistake...")
 
@bot.command
@lightbulb.command("developer", "test group",aliases=["dev", "maker"])
@lightbulb.implements(lightbulb.SlashCommand)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond(" My developer is `ActualPenny3935#2305`")
    
@bot.command()
@lightbulb.command('joined Date' , 'see when this member joined.')
@lightbulb.implements(lightbulb.UserCommand)
async def cmd_context_joined_date(ctx: lightbulb.UserContext) -> None:
    member = ctx.options.target
    await ctx.respond(f"**{member.display_name}** joined at <t:{member.joined_at.timestamp():.0f}:f>")
    
@bot.command()
@lightbulb.command('word Count' , 'view the word count for this message.')
@lightbulb.implements(lightbulb.MessageCommand)
async def cmd_context_word_count(ctx: lightbulb.MessageContext) -> None:
    message = ctx.options.target
    words = len(message.content.split(" "))
    await ctx.respond(f"Message: {message.content}\nWord count: {words:,}")





@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.option("reason", "Reason for kicking the member", required=False, type=str)
@lightbulb.option("user", "user to kick", type=hikari.User)
@lightbulb.command('kick', 'kicks a member!')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx):
    embed = hikari.Embed(title="Kicked:exclamation:", description=f"{ctx.options.user.mention} has been **__kicked__** by {ctx.user.mention}", color=0xFFA500)
    embed.add_field(name="Reson", value=f"`{ctx.options.reason or 'No reason provided'}`.")
    await ctx.bot.rest.kick_user(ctx.guild_id, ctx.options.user.id)
    await ctx.respond(embed)

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num2 + ctx.options.num1)

@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("reason", "Reason for unbanning that user",)
@lightbulb.option("user_id", 'id of the to be unbanned user', type=hikari.User)
@lightbulb.command('unban', 'unban a user')
@lightbulb.implements(lightbulb.SlashCommand)
async def unban(ctx):
   await ctx.bot.rest.unban_user(ctx.guild_id, ctx.options.user_id.id)
   await ctx.respond(f"{ctx.user.mention} unbanned {ctx.options.user_id.mention}.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")
   
@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("user", "what user you want to timeout", required=True, type=hikari.User)
@lightbulb.option("minutes", "how long you would like the member to be timeouted for in Minutes", required=True, type=int)
@lightbulb.command("timeout", "timeouts a user")
@lightbulb.implements(lightbulb.SlashCommand)
async def timeout(ctx: lightbulb.Context):
    targettime = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=ctx.options.minutes)
    Member = ctx.options.user
    embed = hikari.Embed(title="Timeout!:mute: ", description=f"{ctx.options.user.mention} has been __**muted**__ by {ctx.user.mention} for `{ctx.options.minutes}` minutes.",color= 0xFFA500)
    await Member.edit(communication_disabled_until=targettime)
    await ctx.respond(embed)

    
@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("reason", "Reason for taking that role", required=False, type=str)
@lightbulb.option("user", "person that will have the role taken",type=hikari.User)
@lightbulb.option("role", "role to be taken away", type=hikari.Role)
@lightbulb.command("takerole", 'take someones role')
@lightbulb.implements(lightbulb.SlashCommand)
async def takerole(ctx):
    embed = hikari.Embed(title="Role taken", description=f"{ctx.options.user.mention}'s has been __taken__ by {ctx.user.mention}", color=0xFFA500)
    embed.add_field(name="Reson", value=f"`{ctx.options.reason or 'No reason provided'}`.")
    await ctx.bot.rest.remove_role_from_member(user=ctx.options.user, guild=ctx.guild_id, role=ctx.options.role)
    await ctx.respond(embed)
    
@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('subtract', 'Subtract two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def subtract (ctx):
    await ctx.respond(ctx.options.num1 - ctx.options.num2)
    
@bot.command
@lightbulb.command('ping', 'Gets ping of the bot!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    embed = hikari.Embed(title="Pong!", description=f"Ping:`{ctx.app.heartbeat_latency * 1000:.0f}ms`", color= 0xC1C806)
    await ctx.respond(embed)

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('multiply', 'Multiply two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def multiply (ctx):
    await ctx.respond(ctx.options.num2 * ctx.options.num1)
@bot.command
@lightbulb.option("reason", "Reason for the role", required=False)
@lightbulb.option("user", "person that will get the role",type=hikari.User)
@lightbulb.option("role", "role to be given", type=hikari.Role)
@lightbulb.command("giverole", 'Give somebody a role)')
@lightbulb.implements(lightbulb.SlashCommand)
async def giverole(ctx):
        await ctx.bot.rest.add_role_to_member(user=ctx.options.user, guild=ctx.guild_id, role=ctx.options.role)
        await ctx.respond(f"{ctx.user.mention} gave {ctx.options.user.mention} the {ctx.options.role.mention} role.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('divide', 'divide two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def divide (ctx):
    await ctx.respond(ctx.options.num1 / ctx.options.num2)

@bot.command
@lightbulb.option("reason", "Reason for the ban",required=False)
@lightbulb.option("user", "user to ban",type=hikari.User)
@lightbulb.command('ban', 'bans a member!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx):
    await ctx.bot.rest.ban_user(ctx.guild_id, ctx.options.user.id)
    await ctx.respond(f"{ctx.user.mention} banned {ctx.options.user.mention}.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")

@bot.command()
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
        this_dm_channel = await bot.rest.create_dm_channel(ctx.options.user)
        await bot.rest.create_message(this_dm_channel,embed)
    else:
        await bot.rest.create_message(channel_id,embed)
    await ctx.respond("Your message has been created!", flags=hikari.MessageFlag.EPHEMERAL)
    








server_suggestions_channel_dict = {}
if os.path.isfile("server_suggestions_channel_dict.json"):
    with open("server_suggestions_channel_dict.json", "r") as f:
        server_suggestions_channel_dict = json.load(f)



bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="for /help :)",
        type=hikari.ActivityType.WATCHING,))
