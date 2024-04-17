function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];

}

function retorna_total_faq(url){  
    fetch(url, {
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total de faq').innerHTML = data.id
    })

}

function renderiza_produtos_mais_vendidos(url) {
    fetch(url, {
        method: 'GET',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('produtos_mais_vendidos').getContext('2d');
        
        var cores_faturamento_mensal = gera_cor(qtd=50); 
        
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels, 
                datasets: [{
                    label: 'categories',
                    backgroundColor: cores_faturamento_mensal,
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[1],
                    borderColor: cores_faturamento_mensal[160],
                    borderWidth: 1
                }]
            }
        });
    });
}