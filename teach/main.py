import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(discord.__version__)
    
@bot.slash_command(guild_ids=[841315183808741397])
async def calc(ctx):
    class die(discord.ui.View):
        def __init__(self):
            super().__init__()
            
        @discord.ui.button(label=1, row=0)
        async def b1_callback(self, button, interaction):
            if int(interaction.message.content):
                await interaction.response.edit_message(content=interaction.message.content+"1")
            else:
                await interaction.response.edit_message(content=1)
            
        @discord.ui.button(label=2, row=0)
        async def b2_callback(self, button, interaction):
            await interaction.response.edit_message(content=2 if not int(None) else interaction.message.content+"2")
            
        @discord.ui.button(label=3, row=0)
        async def b3_callback(self, button, interaction):
            await interaction.response.edit_message(content=2 if not int(None) else interaction.message.content+"2")
            
        @discord.ui.button(label=4, row=1)
        async def b4_callback(self, button, interaction):
            await interaction.response.edit_message(content=2 if not int(None) else interaction.message.content+"2")
            
        @discord.ui.button(label=5, row=1)
        async def b5_callback(self, button, interaction):
            await interaction.response.edit_message(content=2 if not int(None) else interaction.message.content+"2")
            
        @discord.ui.button(label=6, row=1)
        async def b6_callback(self, button, interaction):
            await interaction.response.edit_message(content=6)
            
        @discord.ui.button(label=7, row=2)
        async def b7_callback(self, button, interaction):
            await interaction.response.edit_message(content=7)
            
        @discord.ui.button(label=8, row=2)
        async def b8_callback(self, button, interaction):
            await interaction.response.edit_message(content=8)
            
        @discord.ui.button(label=9, row=2)
        async def b9_callback(self, button, interaction):
            await interaction.response.edit_message(content=9)
            
        @discord.ui.button(label=00, row=3)
        async def b10_callback(self, button, interaction):
            await interaction.response.edit_message(content=00)
            
        @discord.ui.button(label=0, row=3)
        async def b11_callback(self, button, interaction):
            await interaction.response.edit_message(content=0)
            
        @discord.ui.button(label="=", row=3)
        async def b12_callback(self, button, interaction):
            ans = eval(interaction.message.content)
            await interaction.response.edit_message(content=ans)
            
    await ctx.respond(".", view=die())
    
bot.run("OTMwNDMyMTI2ODEyMzIzODgw.Yd1ycQ.l_xdUzFwESqVF5ETz9s1X2nQNds")