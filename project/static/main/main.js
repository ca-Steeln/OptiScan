
let numKeys = document.getElementById('id_num_keys');
let mainForm = document.getElementById('main-form');
let radioCusSearch = document.getElementById('id_custom_search');
let templateInputs = document.getElementsByTagName('input');
let sumbitFormBtn = document.getElementById('form-button');

    // events listener -----------------------------------
document.addEventListener('input', (e)=>{
    if (e.target === numKeys){
        radioCusSearch.checked = true;
    }
})

document.addEventListener('change', (e)=>{
    if (radioCusSearch.checked){
        numKeys.focus()

    }


})

