data = [9, 5, 3, 23, 65, 87]
a = data.some((value,index,data)=>{
		value < 4;
}

)
 console.log(a)
 if(a == false){
	console.log('it says none of the items is less than 4')
}