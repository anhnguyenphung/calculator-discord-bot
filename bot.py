import os
from dotenv import load_dotenv
from discord.ext import commands
import math
import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='abs', help='Calculate the absolute value of a number')
async def cal_abs(ctx, a):
    response = str(abs(float(a)))
    await ctx.send(response)


@bot.command(name='add', help='Calculate the sum of two numbers')
async def cal_sum(ctx, a, b):
    response = str(float(a) + float(b))
    await ctx.send(response)


@bot.command(name='minus', help='Calculate the difference of two numbers')
async def cal_diff(ctx, a, b):
    response = str(float(a) - float(b))
    await ctx.send(response)


@bot.command(name='multiply', help='Calculate the multiplication of two numbers')
async def cal_product(ctx, a, b):
    response = str((float(a) * float(b)))
    await ctx.send(response)


@bot.command(name='divide', help='Calculate the quotient of two numbers')
async def cal_div(ctx, a, b):
    response = "Can not divide by zero"
    if float(b) != 0:
        response = str((float(a) / float(b)))
    await ctx.send(response)


@bot.command(name='factorial', help='Calculate the factorial of a number')
async def factorial(ctx, a):
    response = 1
    for i in range(1, int(a)+1):
        response *= i
    await ctx.send(str(response))


@bot.command(name='square-root', help='Calculate square root of a number')
async def square_root(ctx, a):
    response = str(math.sqrt(float(a)))
    await ctx.send(str(response))


@bot.command(name='power', help='Calculate the power with base and exponent')
async def power(ctx, a, b):
    response = str(math.pow(float(a), float(b)))
    await ctx.send(response)


@bot.command(name='avg', help='Calculate the average of two numbers')
async def avg(ctx, a, b):
    response = str((float(a) + float(b))/2)
    await ctx.send(response)

keep_alive.keep_alive()

bot.run(TOKEN)