import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot token from Railway Environment Variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")


# ================================
# /start command
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = "Assalamualaikum Sir 👋\n\nWhat do you want to know about me? 😄"

    keyboard = [
        [InlineKeyboardButton("👤 My Name", callback_data="name")],
        [InlineKeyboardButton("😸 About Me", callback_data="about")],
        [InlineKeyboardButton("📚 My Interests", callback_data="interests")],
        [InlineKeyboardButton("⚙️ What I Do", callback_data="do")],
        [InlineKeyboardButton("🧠 My Skills", callback_data="skills")],
        [InlineKeyboardButton("🎯 My Goal", callback_data="goal")],
        [InlineKeyboardButton("🎮 In Game Info", callback_data="game")],
        [InlineKeyboardButton("❤️ About My Love", callback_data="love")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)


# ================================
# Button handler
# ================================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # Different responses for each button
    if data == "name":
        text = (
            "👤 *My Name*\n\n"
            "Md Saafi Rahman 👀😣\n\n"
            "Nickname:\n"
            "NYT SAAFi / Saa'Fe.. 🌚"
        )

    elif data == "about":
        text = (
            "😸 *About Me*\n\n"
            "I'm a teenager who loves learning new things\n"
            "and exploring technology or gaming... 🤕"
        )

    elif data == "interests":
        text = (
            "📚 *My Interests*\n\n"
            "• Learning & Study 📚\n"
            "• Coding 🤖\n"
            "• Telegram Bot Development\n"
            "• Image Editing\n"
            "• Technology & Tools"
        )

    elif data == "do":
        text = (
            "⚙️ *What I Do*\n\n"
            "• Build Telegram Bots using Python\n"
            "• Work with Termux\n"
            "• Explore new tools\n"
            "• Create new tools\n"
            "• Experiment with automation tools"
        )

    elif data == "skills":
        text = (
            "🧠 *My Skills*\n\n"
            "• Basic Python\n"
            "• Telegram Bot Development\n"
            "• Editing Video / Photo\n"
            "• Basic troubleshooting"
        )

    elif data == "goal":
        text = (
            "🎯 *My Goal*\n\n"
            "Enough...\n"
            "I just want to choose my dreams."
        )

    elif data == "game":
        text = (
            "🎮 *In Game Info*\n\n"
            "In Game Name:\n"
            "NYTㅤＳꫝꜰᎥ\n\n"
            "UID:\n"
            "7799479251"
        )

    elif data == "love":
        text = (
            "❤️ *About My Love*\n\n"
            "Status: Single 😂\n"
            "Or One Side Lover (5 years) 😣❤️‍🩹\n\n"
            "Her name first & last letter:\n"
            "A\n\n"
            "Her name digits:\n"
            "4"
        )

    else:
        text = "Unknown option."

    # Edit message when button clicked
    await query.edit_message_text(text=text, parse_mode="Markdown")


# ================================
# Main function
# ================================
def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Button clicks
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")

    app.run_polling()


# ================================
# Run the bot
# ================================
if __name__ == "__main__":
    main()