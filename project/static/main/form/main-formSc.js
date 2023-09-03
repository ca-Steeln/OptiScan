
var contentMatches = document.querySelector('#id-content-matches p');
document.addEventListener('click', (e)=>{

    if(e.target.parentElement.hasAttribute('options')){
        if(e.target.hasAttribute('print')){

            printContent(contentMatches);

            function printContent(content) {
                let printWindow = window.open("", "", 'height=500, width=500');
                printWindow.document.write('</head><body>');
                printWindow.document.write(content.innerHTML);
                printWindow.document.write('</body></html>');
                printWindow.document.close();
                printWindow.print();
            }
        }

        else if(e.target.hasAttribute('copy')){
            navigator.clipboard.writeText(contentMatches.innerText)
            console.log(contentMatches.innerText)
        }
    }

})