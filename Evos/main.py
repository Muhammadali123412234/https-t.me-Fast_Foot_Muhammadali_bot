from telebot import TeleBot, types

bot = TeleBot("8101053684:AAHUXU90q6OQbMelZzQjkIKK0NA5v2rnzDo")

# Savatdagi mahsulotlar
cart = {}

# Setlar
set_images = {
    "COMBO+": "COMBO+.jpg",
    "Kids Combo": "Kids Combo.jpg",
    "Fit Combo": "FitCombo.jpg",
    "Iftar kofte": "Iftar kofte.jpg",
    "Iftar strips": "Iftar strips.jpg",
    "Donar boks mol": "Donar boks  mol.jpg",
    "Donar boks tovuq": "Donar boks tovuq.jpg"
}

set_prices = {
    "COMBO+": 25000,
    "Kids Combo": 20000,
    "Fit Combo": 30000,
    "Iftar kofte": 35000,
    "Iftar strips": 30000,
    "Donar boks mol": 15000,
    "Donar boks tovuq": 18000
}

# Lavash mahsulotlari
lavash_images = {
    "Lavash tovuq go'shtli": "Lavash tovuq go'sht.jpg",
    "Lavash tovuq go'shtli pishloqli": "Lavash cheese tovuq go'sht Standart.jpg",
    "Lavash mol go'shtli": "Mol goʼshtidan qalampir lavash.jpg",
    "Lavash mol go'shtli pishloqli": "Mol goʼshtidan pishloqli lavash Standard.jpg",
    "Lavash qalampir tovuq go'shtli": "Tovuq goʼshtli qalampir lavash.jpg"
}

lavash_prices = {
    "Lavash tovuq go'shtli": 28000,
    "Lavash tovuq go'shtli pishloqli": 32000,
    "Lavash mol go'shtli": 30000,
    "Lavash mol go'shtli pishloqli": 34000,
    "Lavash qalampir tovuq go'shtli": 30000
}

# Burger mahsulotlari
burger_images = {
    "Gamburger": "Gamburger.jpg",
    "Chizburger": "Cheese burger.jpg",
    "Double burger": "Double burger.jpg",
    "Double chizburger": "Double cheese.jpg"
}

burger_prices = {
    "Gamburger": 22000,
    "Chizburger": 24000,
    "Double burger": 32000,
    "Double chizburger": 34000
}

# Shaurma mahsulotlari
shaurma_images = {
    "Shaurma mol go'shtli": "Shaurma mol go'sht.jpg",
    "Shaurma tovuq go'shtli": "Shaurma tovuq go'sht.jpg",
    "Shaurma qalampir mol go'shtli": "Shaurma qalampir mol go'sht.jpg",
    "Shaurma qalampir tovuq go'shtli": "Shaurma qalampir tovuq go'sht.jpg"
}

shaurma_prices = {
    "Shaurma mol go'shtli": 28000,
    "Shaurma tovuq go'shtli": 26000,
    "Shaurma qalampir mol go'shtli": 30000,
    "Shaurma qalampir tovuq go'shtli": 28000
}

# Asosiy menyu
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🍴 Menyu"),
        types.KeyboardButton("📋 Mening buyurtmalarim"),
        types.KeyboardButton("📥 Savat"),
        types.KeyboardButton("📞 Aloqa"),
        types.KeyboardButton("🔙 Ortga")
    )
    return markup

# Yangi foydalanuvchini kutish
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(
        "📞 Avval telefon raqamingizni yuboring yoki +998XX XXXXXXX ko'rinishida yozing.",
        request_contact=True
    )
    markup.add(button)
    bot.send_message(message.chat.id, "Iltimos, telefon raqamingizni yuboring:", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    phone_number = message.contact.phone_number
    bot.send_message(message.chat.id, f"✅ Raqamingiz qabul qilindi: {phone_number}", reply_markup=get_main_menu())

# Menyu ko'rsatish
@bot.message_handler(func=lambda message: message.text == "🍴 Menyu")
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("Setlar"),
        types.KeyboardButton("Lavashlar"),
        types.KeyboardButton("Shaurmalar"),
        types.KeyboardButton("Burgerlar"),
        types.KeyboardButton("🔙 Ortga")
    )
    bot.send_message(message.chat.id, "Menyuni tanlang:", reply_markup=markup)

# Setlar ro'yxatini ko'rsatish
@bot.message_handler(func=lambda message: message.text == "Setlar")
def show_sets_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for set_name in set_images.keys():
        markup.add(types.KeyboardButton(set_name))
    markup.add(types.KeyboardButton("🔙 Ortga"))
    bot.send_message(message.chat.id, "Setlardan birini tanlang:", reply_markup=markup)

# Lavashlar ro'yxatini ko'rsatish
@bot.message_handler(func=lambda message: message.text == "Lavashlar")
def show_lavash_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for lavash_name in lavash_images.keys():
        markup.add(types.KeyboardButton(lavash_name))
    markup.add(types.KeyboardButton("🔙 Ortga"))
    bot.send_message(message.chat.id, "Lavashlardan birini tanlang:", reply_markup=markup)

# Burgerlar ro'yxatini ko'rsatish
@bot.message_handler(func=lambda message: message.text == "Burgerlar")
def show_burger_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for burger_name in burger_images.keys():
        markup.add(types.KeyboardButton(burger_name))
    markup.add(types.KeyboardButton("🔙 Ortga"))
    bot.send_message(message.chat.id, "Burgerlardan birini tanlang:", reply_markup=markup)

# Shaurmalar ro'yxatini ko'rsatish
@bot.message_handler(func=lambda message: message.text == "Shaurmalar")
def show_shaurma_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for shaurma_name in shaurma_images.keys():
        markup.add(types.KeyboardButton(shaurma_name))
    markup.add(types.KeyboardButton("🔙 Ortga"))
    bot.send_message(message.chat.id, "Shaurmalardan birini tanlang:", reply_markup=markup)

# Mahsulot tasvirini va narxini ko'rsatish
@bot.message_handler(func=lambda message: message.text in {**set_images, **lavash_images, **burger_images, **shaurma_images})
def send_product_image(message):
    product_name = message.text
    
    # Determine which category the product belongs to
    if product_name in set_images:
        image_name = set_images[product_name]
        price = set_prices[product_name]
    elif product_name in lavash_images:
        image_name = lavash_images[product_name]
        price = lavash_prices[product_name]
    elif product_name in burger_images:
        image_name = burger_images[product_name]
        price = burger_prices[product_name]
    elif product_name in shaurma_images:
        image_name = shaurma_images[product_name]
        price = shaurma_prices[product_name]
    
    file_path = f"Rasmlar/{image_name}"
    
    try:
        with open(file_path, 'rb') as photo:
            # Create inline keyboard for quantity adjustment
            markup = types.InlineKeyboardMarkup()
            row = [
                types.InlineKeyboardButton("-", callback_data=f"minus_{product_name}"),
                types.InlineKeyboardButton("1", callback_data="quantity"),
                types.InlineKeyboardButton("+", callback_data=f"plus_{product_name}")
            ]
            markup.row(*row)
            markup.add(types.InlineKeyboardButton("🛒 Savatga qo'shish", callback_data=f"add_{product_name}"))
            
            bot.send_photo(
                message.chat.id, 
                photo, 
                caption=f"Narxi: {price:,} so'm",
                reply_markup=markup
            )
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Rasm topilmadi.")

# Buyurtmalarni ko'rsatish
@bot.message_handler(func=lambda message: message.text == "📋 Mening buyurtmalarim")
def show_orders(message):
    if not cart:
        bot.send_message(message.chat.id, "📝 Sizda hozircha buyurtmalar yo'q.")
        return

    total_price = 0
    order_text = "📋 Sizning buyurtmalaringiz:\n\n"
    
    for item, qty in cart.items():
        # Determine price based on product category
        if item in set_prices:
            price = set_prices[item]
        elif item in lavash_prices:
            price = lavash_prices[item]
        elif item in burger_prices:
            price = burger_prices[item]
        elif item in shaurma_prices:
            price = shaurma_prices[item]
            
        item_total = price * qty
        total_price += item_total
        order_text += f"• {item}: {qty} dona - {item_total:,} so'm\n"
    
    order_text += f"\n💰 Jami summa: {total_price:,} so'm"
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("✅ Buyurtmani tasdiqlash"),
        types.KeyboardButton("❌ Buyurtmani bekor qilish"),
        types.KeyboardButton("🔙 Ortga")
    )
    
    bot.send_message(message.chat.id, order_text, reply_markup=markup)

# Buyurtmani tasdiqlash
@bot.message_handler(func=lambda message: message.text == "✅ Buyurtmani tasdiqlash")
def confirm_order(message):
    if not cart:
        bot.send_message(message.chat.id, "❌ Savatda mahsulot yo'q!")
        return

    total_price = 0
    order_text = "✅ Buyurtma tasdiqlandi!\n\n📋 Buyurtma tarkibi:\n\n"
    
    for item, qty in cart.items():
        # Determine price based on product category
        if item in set_prices:
            price = set_prices[item]
        elif item in lavash_prices:
            price = lavash_prices[item]
        elif item in burger_prices:
            price = burger_prices[item]
        elif item in shaurma_prices:
            price = shaurma_prices[item]
            
        item_total = price * qty
        total_price += item_total
        order_text += f"• {item}: {qty} dona - {item_total:,} so'm\n"
    
    order_text += f"\n💰 Jami summa: {total_price:,} so'm"
    
    # Clear the cart after order confirmation
    cart.clear()
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🍴 Menyu"),
        types.KeyboardButton("🔙 Ortga")
    )
    
    bot.send_message(message.chat.id, order_text, reply_markup=markup)

# Buyurtmani bekor qilish
@bot.message_handler(func=lambda message: message.text == "❌ Buyurtmani bekor qilish")
def cancel_order(message):
    if not cart:
        bot.send_message(message.chat.id, "❌ Savatda mahsulot yo'q!")
        return

    # Clear the cart
    cart.clear()
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🍴 Menyu"),
        types.KeyboardButton("🔙 Ortga")
    )
    
    bot.send_message(message.chat.id, "❌ Buyurtma bekor qilindi!", reply_markup=markup)

# Asosiy menyuga qaytish
@bot.message_handler(func=lambda message: message.text == "🔙 Ortga")
def back_to_main_menu(message):
    bot.send_message(message.chat.id, "Asosiy menyuga qaytdik:", reply_markup=get_main_menu())

# Callback query handler for inline buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data.startswith("minus_") or call.data.startswith("plus_"):
        product_name = call.data.split("_")[1]
        current_quantity = int(call.message.reply_markup.keyboard[0][1].text)
        
        if call.data.startswith("minus_") and current_quantity > 1:
            current_quantity -= 1
        elif call.data.startswith("plus_"):
            current_quantity += 1
        
        # Update the quantity button
        markup = types.InlineKeyboardMarkup()
        row = [
            types.InlineKeyboardButton("-", callback_data=f"minus_{product_name}"),
            types.InlineKeyboardButton(str(current_quantity), callback_data="quantity"),
            types.InlineKeyboardButton("+", callback_data=f"plus_{product_name}")
        ]
        markup.row(*row)
        markup.add(types.InlineKeyboardButton("🛒 Savatga qo'shish", callback_data=f"add_{product_name}"))
        
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )
    
    elif call.data.startswith("add_"):
        product_name = call.data.split("_")[1]
        quantity = int(call.message.reply_markup.keyboard[0][1].text)
        
        # Determine price based on product category
        if product_name in set_prices:
            price = set_prices[product_name]
        elif product_name in lavash_prices:
            price = lavash_prices[product_name]
        elif product_name in burger_prices:
            price = burger_prices[product_name]
        elif product_name in shaurma_prices:
            price = shaurma_prices[product_name]
        
        # Add to cart
        cart[product_name] = quantity
        
        # Send confirmation message
        total = price * quantity
        bot.answer_callback_query(
            call.id,
            text=f"✅ {quantity} dona {product_name} savatga qo'shildi",
            show_alert=True
        )
        
        # Show updated cart
        show_cart(call.message)

# Savatni ko'rsatish
@bot.message_handler(func=lambda message: message.text == "📥 Savat")
def show_cart(message):
    if not cart:
        bot.send_message(message.chat.id, "Savatda hech narsa yo'q.")
    else:
        cart_summary = "\n".join([f"{item}: {qty} dona" for item, qty in cart.items()])
        bot.send_message(message.chat.id, f"Savatdagi mahsulotlar:\n{cart_summary}")

if __name__ == "__main__":
    bot.polling()
