import telebot

# Token ەکەی خۆت لە نێوان گووتەکان دابنێ
TOKEN =  8621854686:AAElDSplwb0pBpZwDMo6jE2FjmiIo5EEthY
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "بەخێربێیت! 📊\nبۆ حیسابکردنی Lot Size، ئەم زانیارییانەم بۆ بنێرە:\n"
      "Balance StopLossPips\n\n"
      "نموونە: 1000 20",
  )


@bot.message_handler(func=lambda message: True)
def calculate_position(message):
  try:
    data = message.text.split()
    balance = float(data[0])
    sl_pips = float(data[1])

    # 0.5% & 1.0% Risk calculation
    risk_05 = balance * 0.005
    risk_10 = balance * 0.010

    lot_05 = risk_05 / (sl_pips * 10)
    lot_10 = risk_10 / (sl_pips * 10)

    response = (
        f"💵 **Balance:** ${balance}\n"
        f"🎯 **Stop Loss:** {sl_pips} Pips\n\n"
        f"🟢 **Risk 0.5%:**\n"
        f"- Risk Amount: ${risk_05:.2f}\n"
        f"- Lot Size: {lot_05:.2f}\n\n"
        f"🟠 **Risk 1.0%:**\n"
        f"- Risk Amount: ${risk_10:.2f}\n"
        f"- Lot Size: {lot_10:.2f}"
    )

    bot.reply_to(message, response, parse_mode="Markdown")
  except Exception:
    bot.reply_to(
      message, "تکایە بە شێوازێکی دروست بنووسە.\nنموونە: `1000 20`", parse_mode="Markdown"
    )


bot.polling()
