const country = document.querySelector(".country")
const year = document.querySelector(".year")
const month = document.querySelector(".month")
const products = document.querySelector(".products")
const hero_button = document.querySelector(".hero-btn")
const prediction_button = document.querySelector(".pred_btn")
const result_box = document.querySelector(".result");


prediction_button.addEventListener('click', function(){
    console.log("Button:", prediction_button);

    console.log("Button clicked");
    const data = {
        COUNTRY:country.value,
        YEAR:Number(year.value),
        MONTH:Number(month.value),
        PRODUCT:products.value,
        
    }
    console.log(data)
    fetch("http://127.0.0.1:8000/predict",{
        method: "POST",
        headers: {
            "Content-type":"application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if(!response.ok){
            return response.json().then(error =>{
                throw new Error(error.detail[0].msg)
            })
        }
        return response.json()
    }).then(result => {
        result_box.textContent = result.predicted_value;
    }).catch(error => {
        console.log("ERROR:", error);
        result_box.textContent = error.message;
    })
})

hero_button.addEventListener('click', function(e){
    hero_button.scrollIntoView({
        behavior:"smooth"
    })
})