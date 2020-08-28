storeemail = "annaeemherbal@gmail.com"
		emailsubject = str(buyername ) + "  Placed An Order From Annaeem Store"
		for i in (items):
			a = ("Item Name:",(i.product.name), "--" "Quantity:", i.quantity, "Item Price(each):", i.product.price, "Total Price:", i.get_total, '\\n')

		print("-------------------------------------------------------------------")
		print(a)
		print("Total Item(s):", cartItems, "--" ,"Total Price:", order.get_cart_total)
		send_mail(emailsubject, 'this is the django test body', storeemail, [buyermail], fail_silently=False)