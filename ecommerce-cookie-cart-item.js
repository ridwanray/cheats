17: {quantity: 1}
18: {quantity: 1}
20: {quantity: 5}
21: {quantity: 1}
23: {quantity: 2}
26: {quantity: 1}
28: {quantity: 1}
31: {quantity: 1}
33: {quantity: 1}
57: {quantity: 1}
	
	
	
	for (const property in cart) {
     total= total + cart[property]['quantity'];
  console.log(cart[property]['quantity']);
}