function retorna_total_faq(url){  
    fetch(url, {
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total de faq').innerHTML = data.id
    })

}

function get_category_counts(url) {
    fetch(url, {
        method: 'GET',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('get_category_counts').getContext('2d');
        Chart.defaults.font.size = 20
        
        var cores_faturamento_mensal = ['rgb(255, 99, 132)', 'rgb(55, 99, 132)', 'rgb(255, 199, 132)'];
                 
        const myChart = new Chart(ctx, {
            type: 'pie',
            
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Quantidade',
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal
                    
                }]
            }
        });
    });
}

function get_location_counts(url) {
    fetch(url, {
        method: 'GET',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('get_location_counts').getContext('2d');
        Chart.defaults.font.size = 20
        var cores_faturamento_mensal = ['rgb(255, 99, 132)', 'rgb(55, 99, 132)', 'rgb(255, 199, 132)'];
                 
        const myChart = new Chart(ctx, {
            type: 'polarArea',
            
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Local',
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal
                    
                }]
            }
        });
    });
}