function handleErrors(response) {
    if (response.status !== 200) {
        //throw Error(response.statusText);
        console.log("cones herer")
    }
    return response;
}



fetch('/enquiry', {
  method: 'POST',
  body: formData
}).then(handleErrors)
.then(function(response){
        console.log(response.status);
        return response.json() 
}).then(data => {

  document.getElementById("output-message").innerText = "Great! Your enquiry has been sent."
  document.getElementById("output-message").classList.add("alert","alert-success","alert-dismissible","fade","show");
  setTimeout(function(){ 
  document.getElementById("output-message").style.display = "none";
  document.getElementById("title").value = "";
  document.getElementById("quantity").value = "";
  document.getElementById("phone").value = "";
  document.getElementById("email").value = "";


   }, 4000);
  setTimeout(function(){ 
  document.getElementById("output-message").style.display = "";
  //document.getElementById("output-message").classList.remove("alert","alert-success","alert-dismissible","fade","show");
   }, 1000);

 
 
 
})
.catch(error => {
  //
  console.error('Error:', error);
  document.getElementById("output-message").innerText = "Sorry! There was an error submitting your enquiry.";
  document.getElementById("output-message").classList.add("alert","alert-danger","alert-dismissible","fade","show");
  setTimeout(function(){ 
  document.getElementById("output-message").style.display = "none";
   }, 4000);
  setTimeout(function(){ 
  document.getElementById("output-message").style.display = "";
  //document.getElementById("output-message").classList.remove("alert","alert-danger","alert-dismissible","fade","show");
   }, 1000);

});

});
