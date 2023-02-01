import openai
import python_telegram_bot

# OpenAI API credentials
openai.api_key="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"
# Telegram Bot API credentials
token = "6060124504:AAHX5CPW4EwSLw1RU3QK5bJPyuheAU8Ym2k"

async def botman(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"I'm Botman. Watcha need?")

async def yo(update, context):
    # Get the user's message
    message = update.message.text.split(" ", 1)[1]
    print(message)
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{message}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    await update.message.reply_text(f'Response: {response}')

async def botchelangelo(update, context):
    # Get the user's message
    message = update.message.text.split(" ", 1)[1]
    print(message)
    # Use OpenAI to generate an image
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=f"{message}"
    )

    image_url = response.url

    await update.message.reply_photo(photo=image_url, caption=f"Image for '{message}'")

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("botman", botman))
app.add_handler(CommandHandler("yo", yo))
app.add_handler(CommandHandler("botchelangelo", botchelangelo))
app.run_polling()
