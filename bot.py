import asyncio

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot running...")

    async def run():
        await app.run_polling()

    asyncio.run(run())

if __name__ == "__main__":
    main()
